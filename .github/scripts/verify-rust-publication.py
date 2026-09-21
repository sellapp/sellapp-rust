"""Verify and upload retained Rust crate bytes without building or running package code.

The upload wire format is the official Cargo registry Publish API:
https://doc.rust-lang.org/cargo/reference/registry-web-api.html#publish
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import tarfile
import tomllib
import urllib.error
import urllib.request

REPOSITORY = "sellapp/sellapp-rust"
PACKAGE = "sellapp-sdk"
MAX_PACKAGE_BYTES = 50 * 1024 * 1024
REGISTRY = "https://crates.io"
USER_AGENT = "SellApp-Rust-Publication/1 (support@sell.app)"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def validate_manifest(raw, expected_hash, source, ownership, sdk_commit, tag):
    require(
        bool(re.fullmatch(r"[a-f0-9]{64}", expected_hash)),
        "Expected a SHA-256 manifest digest",
    )
    require(
        len(raw) <= 65536 and sha256(raw) == expected_hash,
        "Publication manifest hash differs",
    )
    manifest = json.loads(raw)
    version = manifest.get("version", "")
    require(
        bool(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version)) and tag == "v" + version,
        "Release tag/version differs",
    )
    require(
        manifest.get("schemaVersion") == 1 and manifest.get("repository") == REPOSITORY,
        "Unexpected publication repository/schema",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{40}", sdk_commit))
        and manifest.get("sdkCommit") == sdk_commit,
        "SDK commit differs from workflow checkout",
    )
    require(
        ownership.get("repository") == REPOSITORY
        and ownership.get("language") == "rust",
        "Unexpected source ownership",
    )
    require(
        source.get("sdkVersion") == version and source.get("language") == "rust",
        "Generated SDK language/version differs",
    )
    require(
        source.get("generatorDirty") is False,
        "Source was generated from a dirty checkout",
    )
    require(
        manifest.get("sourceSha")
        == source.get("generatorCommit")
        == ownership.get("sourceSha"),
        "Generator source identity differs",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{40}", manifest.get("sourceSha", ""))),
        "Invalid generator source identity",
    )
    require(
        manifest.get("specSha256")
        == source.get("specSha256")
        == ownership.get("specSha256"),
        "Specification identity differs",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{64}", manifest.get("specSha256", ""))),
        "Invalid specification digest",
    )
    require(manifest.get("packageName") == PACKAGE, "Unexpected crate name")
    files = manifest.get("files", [])
    expected = {f"{PACKAGE}-{version}.crate"}
    require(
        len(files) == 1 and {f.get("name") for f in files} == expected,
        "Expected exactly the versioned Rust crate",
    )
    for item in files:
        require(
            bool(re.fullmatch(r"[a-f0-9]{64}", item.get("sha256", ""))),
            "Invalid package digest",
        )
        require(
            type(item.get("size")) is int and 0 < item["size"] <= MAX_PACKAGE_BYTES,
            "Invalid package size",
        )
    return manifest



def validate_package(data, item, version):
    require(len(data) == item["size"] and sha256(data) == item["sha256"],
            "Package bytes differ from validated manifest")
    prefix = f"{PACKAGE}-{version}/"
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        total = 0
        for entry in archive:
            require(entry.isfile() and entry.name.startswith(prefix),
                    "Package entries must be regular files under the versioned root")
            name = entry.name[len(prefix):]
            require(name and "\\" not in name and ":" not in name
                    and all(part not in ("", ".", "..") for part in name.split("/"))
                    and not any(ord(c) < 32 for c in name), "Unsafe package entry")
            require(name not in files, "Duplicated package entry")
            total += entry.size
            require(0 <= entry.size <= MAX_PACKAGE_BYTES and total <= 100 * 1024 * 1024,
                    "Oversized unpacked crate")
            files[name] = archive.extractfile(entry).read()
    require({"Cargo.toml", "src/lib.rs", "README.md", "LICENSE.txt", "NOTICE.txt"}
            <= files.keys(), "Missing crate metadata, source or documentation")
    require(len(files["Cargo.toml"]) <= 65536, "Oversized Cargo metadata")
    cargo = tomllib.loads(files["Cargo.toml"].decode())
    info = cargo["package"]
    require(info["name"] == PACKAGE and info["version"] == version,
            "Crate name/version differs")
    require(info.get("license") == "MIT" and info.get("readme") == "README.md",
            "Crate readme/license differs")
    require(info.get("repository") == "https://github.com/" + REPOSITORY,
            "Crate repository differs")
    require(cargo.get("lib", {}).get("name") == "sellapp",
            "Expected the stable sellapp library import")
    require(files["README.md"].startswith(b"# SellApp Rust SDK"), "Unexpected crate README")
    return cargo, files


def publication_metadata(cargo, files):
    """Construct registry metadata solely from the reviewed packaged Cargo.toml."""
    package = cargo["package"]
    dependencies = []

    def collect(table, target=None):
        for section, kind in (("dependencies", "normal"), ("dev-dependencies", "dev"),
                              ("build-dependencies", "build")):
            for name, declaration in sorted(table.get(section, {}).items()):
                if isinstance(declaration, str):
                    declaration = {"version": declaration}
                require(isinstance(declaration, dict)
                        and isinstance(declaration.get("version"), str),
                        "Dependency must have a registry version")
                require(not ({"git", "path", "registry", "registry-index", "workspace"}
                             & declaration.keys()), "Non-default registry dependency")
                dependencies.append({
                    "name": declaration.get("package", name),
                    "version_req": declaration["version"],
                    "features": declaration.get("features", []),
                    "optional": declaration.get("optional", False),
                    "default_features": declaration.get("default-features", True),
                    "target": target,
                    "kind": kind,
                    "registry": None,
                    "explicit_name_in_toml": name if declaration.get("package") else None,
                })

    collect(cargo)
    for target, table in sorted(cargo.get("target", {}).items()):
        collect(table, target)
    require(isinstance(package.get("description"), str) and package["description"].strip(),
            "Missing crate description")
    return {
        "name": package["name"],
        "vers": package["version"],
        "deps": dependencies,
        "features": cargo.get("features", {}),
        "authors": package.get("authors", []),
        "description": package["description"],
        "documentation": package.get("documentation"),
        "homepage": package.get("homepage"),
        "readme": files["README.md"].decode(),
        "readme_file": "README.md",
        "keywords": package.get("keywords", []),
        "categories": package.get("categories", []),
        "license": package["license"],
        "license_file": None,
        "repository": package["repository"],
        "badges": {},
        "links": package.get("links"),
        "rust_version": package.get("rust-version"),
    }


def publication_body(metadata, crate):
    raw = json.dumps(metadata, ensure_ascii=False, separators=(",", ":")).encode()
    require(len(raw) <= MAX_PACKAGE_BYTES, "Oversized publication metadata")
    return struct.pack("<I", len(raw)) + raw + struct.pack("<I", len(crate)) + crate


class NoRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def publish_retained(manifest, data, metadata):
    """No retries: an uncertain result requires checking registry acceptance first."""
    opener = urllib.request.build_opener(NoRedirects)
    version_url = f"{REGISTRY}/api/v1/crates/{PACKAGE}/{manifest['version']}"
    try:
        with opener.open(urllib.request.Request(version_url, headers={
                "User-Agent": USER_AGENT, "Accept": "application/json"}), timeout=30):
            raise ValueError("Crate version already exists; verify it instead of re-uploading")
    except urllib.error.HTTPError as error:
        require(error.code == 404, "Registry availability check failed; no upload attempted")
    body = publication_body(metadata, data)
    token = os.environ.get("CARGO_REGISTRY_TOKEN", "")
    require(token and token.strip() == token and "\r" not in token and "\n" not in token,
            "CARGO_REGISTRY_TOKEN must contain the publishing credential")
    request = urllib.request.Request(REGISTRY + "/api/v1/crates/new", data=body, method="PUT",
                                     headers={"Authorization": token, "User-Agent": USER_AGENT,
                                              "Content-Type": "application/octet-stream",
                                              "Accept": "application/json"})
    try:
        with opener.open(request, timeout=120) as response:
            raw = response.read(1024 * 1024 + 1)
            require(len(raw) <= 1024 * 1024, "Oversized registry response")
            acknowledgment = json.loads(raw)
            require(not acknowledgment.get("errors"), "Registry rejected publication")
    except urllib.error.HTTPError as error:
        raise ValueError(f"Registry upload returned HTTP {error.code}; check acceptance before retrying") from None
    except (TimeoutError, urllib.error.URLError):
        raise ValueError("Registry upload result is uncertain; check acceptance before retrying") from None
    receipt = {
        "packageName": PACKAGE, "version": manifest["version"],
        "sha256": sha256(data), "accepted": True,
        "warnings": acknowledgment.get("warnings", {}),
    }
    Path("publication-acknowledgment.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("crates.io accepted " + PACKAGE + " " + manifest["version"])


def github(resource, binary=False):
    command = ["gh", "api", "--hostname", "github.com", resource]
    if binary:
        command.extend(["--header", "Accept: application/octet-stream"])
    result = subprocess.run(command, capture_output=True, timeout=120)
    require(result.returncode == 0, "GitHub asset/metadata read failed")
    return result.stdout if binary else json.loads(result.stdout)


def checkout_commit(local):
    if local:
        result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
        commit = result.stdout.strip()
        status = subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"],
                                capture_output=True, text=True, check=True)
        require(not status.stdout, "Local SDK checkout has tracked changes")
        return commit
    require(os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
            and os.environ.get("GITHUB_REF") == "refs/heads/main",
            "Run this workflow from the official repository main branch")
    return os.environ.get("GITHUB_SHA", "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--local", action="store_true",
                        help="Verify a clean local checkout of the delivered SDK commit")
    parser.add_argument("--publish-retained", action="store_true",
                        help="Upload the already verified dist artifact; no build is performed")
    args = parser.parse_args()
    require(bool(re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", args.tag)), "Expected release tag vX.Y.Z")
    commit = checkout_commit(args.local)
    prefix = "repos/" + REPOSITORY
    release = github(prefix + "/releases/tags/" + args.tag)
    require(release.get("tag_name") == args.tag, "GitHub release tag differs")
    ref = github(prefix + "/git/ref/tags/" + args.tag)["object"]
    for _ in range(3):
        if ref.get("type") == "commit":
            break
        require(ref.get("type") == "tag" and bool(re.fullmatch(r"[a-f0-9]{40}", ref.get("sha", ""))),
                "Unexpected Git tag object")
        ref = github(prefix + "/git/tags/" + ref["sha"])["object"]
    require(ref.get("type") == "commit" and ref.get("sha") == commit,
            "Release tag differs from workflow checkout")
    assets = release.get("assets", [])

    def download(name, maximum):
        matches = [asset for asset in assets if asset.get("name") == name]
        require(len(matches) == 1, "Missing or duplicated release asset: " + name)
        asset = matches[0]
        require(type(asset.get("id")) is int and type(asset.get("size")) is int
                and 0 < asset["size"] <= maximum, "Invalid release asset size/identity")
        data = github(prefix + "/releases/assets/" + str(asset["id"]), binary=True)
        require(len(data) == asset["size"], "Downloaded release asset size differs")
        return data

    raw = (Path("dist/publication-manifest.json").read_bytes() if args.publish_retained
           else download("publication-manifest.json", 65536))
    manifest = validate_manifest(raw, args.sha256,
                                 json.loads(Path("generation-manifest.json").read_text()),
                                 json.loads(Path(".sellapp-sdk-sync.json").read_text()),
                                 commit, args.tag)
    item = manifest["files"][0]
    data = (Path("dist", item["name"]).read_bytes() if args.publish_retained
            else download(item["name"], MAX_PACKAGE_BYTES))
    cargo, files = validate_package(data, item, manifest["version"])
    metadata = publication_metadata(cargo, files)
    if args.publish_retained:
        require(github(prefix).get("private") is False, "Publish only from the public SDK repository")
        publish_retained(manifest, data, metadata)
    else:
        require(not Path("dist").exists(), "Output directory already exists")
        Path("dist").mkdir()
        Path("dist", item["name"]).write_bytes(data)
        Path("dist/publication-manifest.json").write_bytes(raw)
        print("Verified retained crate for " + args.tag + " at " + commit)


if __name__ == "__main__":
    main()
