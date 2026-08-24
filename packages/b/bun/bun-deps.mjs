// List every URL Bun's build downloads, one per line, as:
//
//     <kind>\t<name>\t<url>
//
// The list is not hardcoded: it is obtained by importing Bun's own dependency
// definitions (scripts/build/deps/index.ts) and calling each dependency's
// source() function, so a version bump automatically picks up added, removed
// and re-pinned dependencies. Run from the root of an unpacked Bun source
// tree with Node.js >= 24:
//
//     node --experimental-strip-types bun-deps.mjs
//
// Dependencies that are not downloaded - SQLite (an amalgamation committed to
// Bun's own tree) and, unless --webkit=prebuilt is passed, WebKit - are
// reported with their kind and no URL.

const { allDeps } = await import(new URL("./scripts/build/deps/index.ts", import.meta.url).href);

// WebKit is the one dependency whose URL depends on how it is built: as a
// prebuilt engine it is downloaded, from source it is a separate tarball.
const webkitMode = process.argv.includes("--webkit=prebuilt") ? "prebuilt" : "local";

// source() takes the resolved build configuration. Only the few fields below
// affect which URL a dependency resolves to; the rest of the configuration
// describes the compiler and is irrelevant here. Resolving it properly would
// drag in the whole toolchain probe, which requires a full build environment.
const { NODEJS_VERSION } = await import(
  new URL("./scripts/build/deps/nodejs-headers.ts", import.meta.url).href
);
const { WEBKIT_VERSION } = await import(new URL("./scripts/build/deps/webkit.ts", import.meta.url).href);

const arm64 = process.arch === "arm64";
const cfg = {
  nodejsVersion: NODEJS_VERSION,
  webkitVersion: WEBKIT_VERSION,
  cacheDir: "/nonexistent/cache",
  vendorDir: "/nonexistent/vendor",
  // --local-deps redirections. Empty here, but the field has to exist:
  // depSourceDir() indexes it unconditionally (scripts/build/source.ts).
  localDeps: {},
  webkit: webkitMode,
  os: "linux",
  linux: true,
  darwin: false,
  windows: false,
  freebsd: false,
  arm64,
  x64: !arm64,
  abi: "gnu",
  asan: false,
  lto: false,
  debug: false,
  release: true,
  baseline: false,
};

let failed = 0;
for (const dep of allDeps) {
  let src;
  try {
    src = dep.source(cfg);
  } catch (error) {
    process.stderr.write(`bun-deps: ${dep.name}: ${error.message}\n`);
    failed++;
    continue;
  }
  if (src.kind === "github-archive") {
    process.stdout.write(`archive\t${dep.name}\thttps://github.com/${src.repo}/archive/${src.commit}.tar.gz\n`);
  } else if (src.kind === "prebuilt") {
    process.stdout.write(`prebuilt\t${dep.name}\t${src.url}\n`);
  } else {
    process.stdout.write(`${src.kind}\t${dep.name}\t-\n`);
  }
}
process.exit(failed === 0 ? 0 : 1);
