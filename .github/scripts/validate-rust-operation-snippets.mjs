import fs from 'node:fs/promises';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
const directory = path.resolve(process.argv[2]);
const target = path.join(directory, '.validation-snippets');
await fs.mkdir(path.join(target, 'src'), { recursive: true });
const snippets = (
  await Promise.all(
    ['operation-examples.json', 'operation-variants.json'].map(async (file) =>
      JSON.parse(await fs.readFile(path.join(directory, 'docs', file), 'utf8')),
    ),
  )
).flat();
await fs.writeFile(
  path.join(target, 'Cargo.toml'),
  `[package]
name = "sellapp-documentation-check"
version = "0.0.0"
edition = "2024"
[dependencies]
sellapp = { path = ${JSON.stringify(directory)} }
serde_json = "1"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
`,
);
await fs.writeFile(
  path.join(target, 'src/lib.rs'),
  snippets
    .map((snippet, index) => `#[allow(dead_code, unused_mut)]\nmod example${index} {\n${snippet.content}\n}`)
    .join('\n'),
);
const result = spawnSync('cargo', ['check', '--quiet'], {
  cwd: target,
  encoding: 'utf8',
  maxBuffer: 20 * 1024 * 1024,
  env: { ...process.env, CARGO_BUILD_JOBS: '1' },
});
if (result.status !== 0) {
  await fs.mkdir(path.resolve(import.meta.dirname, '../reports'), { recursive: true });
  await fs.writeFile(
    path.resolve(import.meta.dirname, '../reports/rust-snippet-errors.log'),
    result.stdout + result.stderr,
  );
  process.stderr.write((result.stdout + result.stderr).slice(-10000));
  process.exit(result.status ?? 1);
}
await fs.rm(target, { recursive: true });
console.log(`Compiled ${snippets.length} Rust operation examples.`);
