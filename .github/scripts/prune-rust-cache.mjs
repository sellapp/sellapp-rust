import { execFileSync } from 'node:child_process';
import { existsSync, readdirSync, realpathSync, rmSync } from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

function inside(parent, child) {
  const relative = path.relative(parent, child);
  return relative !== '' && !relative.startsWith(`..${path.sep}`) && relative !== '..' && !path.isAbsolute(relative);
}

export function pruneRustCache({
  source = process.cwd(),
  target = process.env.CARGO_TARGET_DIR,
  runnerTemp = process.env.RUNNER_TEMP,
} = {}) {
  if (!target || !runnerTemp) throw new Error('CARGO_TARGET_DIR and RUNNER_TEMP are required');
  const sourceRoot = realpathSync(source);
  const targetRoot = realpathSync(target);
  const temporaryRoot = realpathSync(runnerTemp);
  if (!inside(temporaryRoot, targetRoot)) throw new Error('Refusing to prune a Rust target outside RUNNER_TEMP');
  const metadata = JSON.parse(
    execFileSync(
      'cargo',
      ['metadata', '--no-deps', '--format-version', '1', '--manifest-path', path.join(sourceRoot, 'Cargo.toml')],
      { encoding: 'utf8' },
    ),
  );
  const rootPackage = metadata.packages.find(
    (candidate) => path.resolve(candidate.manifest_path) === path.join(sourceRoot, 'Cargo.toml'),
  );
  if (!rootPackage) throw new Error('Cargo metadata did not contain the Rust SDK package');
  const packagePrefix = rootPackage.name;
  const targetPrefixes = new Set(rootPackage.targets.map((entry) => entry.name.replaceAll('-', '_')));
  const removed = [];
  const remove = (entry) => {
    if (!existsSync(entry)) return;
    rmSync(entry, { recursive: true, force: true });
    removed.push(path.relative(targetRoot, entry));
  };
  remove(path.join(targetRoot, 'package'));
  for (const profile of ['debug', 'release']) {
    const directory = path.join(targetRoot, profile);
    const packageHashes = new Set();
    remove(path.join(directory, 'incremental'));
    for (const entry of list(path.join(directory, '.fingerprint'))) {
      if (entry.startsWith(`${packagePrefix}-`)) {
        packageHashes.add(entry.slice(packagePrefix.length + 1));
        remove(path.join(directory, '.fingerprint', entry));
      }
    }
    for (const entry of list(path.join(directory, 'deps'))) {
      if (
        [...targetPrefixes].some((prefix) =>
          [...packageHashes].some(
            (hash) => entry.startsWith(`${prefix}-${hash}`) || entry.startsWith(`lib${prefix}-${hash}`),
          ),
        )
      )
        remove(path.join(directory, 'deps', entry));
    }
    for (const name of targetPrefixes) {
      remove(path.join(directory, name));
      remove(path.join(directory, `${name}.d`));
      remove(path.join(directory, `lib${name}.rlib`));
      remove(path.join(directory, `lib${name}.rmeta`));
    }
    for (const entry of list(path.join(directory, 'examples'))) {
      if (
        [...targetPrefixes].some(
          (prefix) =>
            entry === prefix ||
            entry === `${prefix}.d` ||
            [...packageHashes].some((hash) => entry.startsWith(`${prefix}-${hash}`)),
        )
      )
        remove(path.join(directory, 'examples', entry));
    }
  }
  return removed.sort();
}

function list(directory) {
  try {
    return readdirSync(directory);
  } catch {
    return [];
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const removed = pruneRustCache({ source: process.argv[2] ?? process.cwd() });
  console.log(`Removed ${removed.length} crate-owned Rust cache entries`);
}
