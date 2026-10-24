# Building the git-bug Web UI for openSUSE

## Status

The spec builds and embeds the Web UI by default on x86-64. Other
architectures retain the CLI-only build until they are tested. Use
`--without webui` for the CLI-only variant or `--with webui` to explicitly test
the frontend on another architecture (after adding its Node-API platform
suffix to the spec's `napi_triple`).

`_service` generates the npm container and source include, and fetches and
vendors the Rust sources of the native npm addons. The RPM compiles Rolldown,
Tailwind CSS oxide and Lightning CSS from those sources. No prebuilt machine
code from npm enters the build; the spec fails if npm installs any ELF file.
Both the Web UI-enabled and CLI-only RPM builds have passed locally with
external networking disabled.

The JavaScript inside the npm tarballs is still upstream's published,
bundled output. Rebuilding the JavaScript toolchain from TypeScript sources is
out of scope.

| Plan step | Status |
|---|---|
| 1. Separate downloading and npm resolution | Complete |
| 2. Implement converter | Complete |
| 3. Use service's multi-lock input | Complete and tested with installed service |
| 4. Test conversion | Complete; 37 unit tests across preparation, native addons and notice collection |
| 5. Generate genuine npm lock | Generated; provenance checked and fresh-cache installation passed. Exact peer-graph equivalence is not claimed. |
| 6. Integrate service/submission workflow | Implemented with manual services, a legacy cpio container and generated source includes |
| 7. Factory tools and native dependencies | Complete: native addons compiled from Rust sources; esbuild is not used by the build |
| 8. Reduce dependencies | Build inventory reduced to the 860 sources npm installs; development dependencies not yet pruned |
| 9. Update spec and source patches | Spec integration complete; no upstream source patch required |
| 10. Offline checks and packaging review | Both local RPM variants passed; packaged Web UI binary passed smoke tests. Clean OBS build and full license review pending |
| 11. Maintenance documentation | Service regeneration, RPM build, and fallback documented |

## Three different artifacts

- `node-sources-full.json` is the reviewed complete download inventory: the
  upstream pnpm inventory with the downstream security replacements. Lock
  generation resolves against it.
- `node-sources.json` is the reduced build inventory written by
  `prepare-webui-lock.py` and consumed by `obs-service-node_modules`. It
  contains the sources npm selected, minus optional platform-specific packages.
- `package-lock.json` must be produced and validated by npm. It records the
  actual installation tree and peer resolution.

The two inventories describe tarball URLs and checksums, not an installation
layout. Never pass them to npm as `package-lock.json`.

The upstream `webui/pnpm-lock.yaml` remains the authority for the initial source
inventory. Generating an npm lock must not silently fetch newer versions from
an external registry.

## Converter

Requirements: Python 3.8 or newer and PyYAML, available in openSUSE as the
appropriate `python3*-PyYAML` package for the interpreter. Tests use the standard
library. The optional installed-service integration test also uses that
service's own dependencies.

Run from the packaging directory, with the release unpacked separately:

```sh
python3 pnpm-to-obs.py \
    --input /path/to/git-bug-0.11.0/webui/pnpm-lock.yaml \
    --output node-sources-upstream.json

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
    test_pnpm_to_obs.py test_prepare_webui_lock.py test_collect_webui_licenses.py \
    test_native_addons.py
```

The converter writes the plain upstream inventory. The submitted
`node-sources-full.json` is that inventory plus the reviewed security
replacements described below, so do not overwrite it with converter output.

The converter supports pnpm lockfile version 9. It keeps all package versions
and platform variants, including optional native bindings. It preserves explicit
HTTPS tarball URLs and derives standard npm registry URLs for integrity-only
registry records. It does not read npm registry configuration or contact the
network.

The output uses the installed service's support for a mapping of npm-v3-shaped
objects. Each object contains one package identity. Peer-specific records with
the same source collapse into one download. Different versions remain distinct.

The converter rejects missing or malformed hashes, unsupported lock versions,
local/workspace/Git resolutions, patched dependencies, duplicate YAML keys,
conflicting source records, and service tarball filename collisions. Unsupported
inputs need explicit implementation, not an automatic fallback to current npm
registry contents.

### Download and verify

Lock generation needs every tarball of the complete inventory. The submitted
container holds only the reduced build inventory, so download the complete one
with the service directly:

```sh
/usr/lib/obs/service/node_modules \
    --input node-sources-full.json \
    --node-dir /path/to/downloaded-tarballs \
    --download
```

Verification is required. The installed service can log a download error without
returning a failing exit status. `prepare-webui-lock.py` checks that every
tarball of the inventory it resolves against exists and matches its recorded
integrity hashes before starting npm. For the plain upstream inventory,
`pnpm-to-obs.py --verify-dir` performs the same check.

These downloads are source preparation. They must not happen during rpmbuild.

The configured manual service entry is:

```xml
<service name="node_modules" mode="manual">
  <param name="input">node-sources.json</param>
  <param name="legacy-container">true</param>
  <param name="cpio">node_modules.obscpio</param>
  <param name="output">node_modules.spec.inc</param>
  <param name="source-offset">10000</param>
</service>
```

After regenerating `node-sources.json`, update the submitted sources with:

```sh
osc service manualrun node_modules
```

Submit both `node_modules.obscpio` and `node_modules.spec.inc` along with the
manifest, npm lock, scripts, spec, and service definition. The cpio container
holds 860 tarballs and occupies about 61 MiB, down from 809 MiB for the
complete inventory. `.gitignore` explicitly allows this file; the existing Git
LFS attributes cover it.

OBS/osc expands the container into individual source tarballs before RPM runs.
The generated include declares them as sources numbered from 10000. The RPM
build uses these regular files from the source directory. Do not replace them
with symlinks in a local test: the registry helper skips symlink directory entries.

For a plain `rpmbuild` invocation outside OSC, first extract the container in
your RPM source directory:

```sh
cd /path/to/rpm/SOURCES
cpio -idm < /path/to/package/node_modules.obscpio
```

Generating the installation lock is a maintainer operation that uses the
complete download from the previous section; the spec only consumes the
submitted lock.

## Downstream security updates

The submitted inventory replaces upstream fast-uri 3.1.7 with 3.1.9 and
qs 6.16.0 with 6.16.1. The npm manifest pins these replacements through
overrides. All other source records are unchanged.

To regenerate the lock with these reviewed replacements, add
`--security-inventory /absolute/path/to/node-sources-full.json` to the
`prepare-webui-lock.py` command below. Without this option, the helper
reproduces the upstream inventory and does not retain the downstream security
fixes. The helper rejects changes to unrelated source records and verifies
tarball hashes before resolution. It refuses `node-sources.json` here, because
it overwrites that file with the reduced build inventory.

Picomatch 2.3.2 and 4.0.7 remain vendored. CVE-2026-112366 is unresolved:
the advisory identifies versions through 4.0.7 as affected, and npm has no
newer release. See https://github.com/advisories/GHSA-fc5q-39xc-vjpf.
Neither follow-redirects nor webpack-dev-server appears in the source inventory
or npm installation lock.

## Generate the genuine npm lock

`prepare-webui-lock.py` automates this stage. It uses an empty temporary cache,
pins direct dependencies to their upstream importer versions, translates the
reviewed pnpm override to npm, and starts `local-npm-registry` with the verified
tarballs. It disables scripts and auditing and runs in a new Linux user/network
namespace with only loopback enabled. It requires `unshare` and permission to
create unprivileged user namespaces.

```sh
python3 prepare-webui-lock.py \
    --webui /path/to/git-bug-0.11.0/webui \
    --tarballs /path/to/downloaded-tarballs \
    --security-inventory "$PWD/node-sources-full.json" \
    --output-dir .
```

The outputs are:

- `webui-package.json`, the npm-compatible manifest with pinned direct versions.
- `package-lock.json`, a genuine npm-generated installation lock.
- `node-sources.json`, the reduced build inventory for the `node_modules`
  service.
- `webui-lock-report.json`, the selected source count, unused source identities,
  native addon overrides and excluded platform packages.

The RPM compiles one module per native addon (see below), so npm must install a
single copy of each. If the first resolution yields several versions of an
addon, the helper overrides it to the highest locked version and resolves
again. Currently `@tailwindcss/node` pins Lightning CSS 1.32.0 while Vite uses
1.33.0; the override unifies both on 1.33.0 and changes no other lock entry.

The build inventory keeps every source npm selected, except identities whose
every lock entry is an optional package restricted by `os`, `cpu` or `libc`.
npm skips such packages when the registry lacks them. Required packages that
only list supported platforms, such as `systeminformation`, stay.

The helper verifies the complete tarball inventory before starting npm. It
rejects selected sources or integrity hashes absent from the pnpm inventory.
For dependencies bundled inside another npm tarball, it checks their manifests
inside the already verified parent archive. The current tree has six such
bundled entries, including versions not listed separately in the pnpm lock.

The override translation is deliberately specific to this release. If upstream
changes its overrides, the helper fails and requires review rather than guessing
how pnpm-specific selectors map to npm.

There is an important limitation in Factory's `local-npm-registry` 1.1.0:
its normal wrapper appends `--no-package-lock` to the npm command. Do not assume
that `local-npm-registry ... install --package-lock-only` will generate a lock.
The preparation tool uses the helper's `--debug` server mode and invokes npm
separately with its explicit localhost registry URL.

It passes `--omit-lockfile-registry-resolved`, so npm writes a portable lock
without temporary localhost URLs. The integrity hashes and installation tree
remain locked. The normal helper successfully installs this lock with `ci`,
despite appending `--no-package-lock`.

Use `--legacy-peer-deps` consistently. Strict resolution repeatedly reported
incompatible upstream TypeScript peer requirements and was stopped after three
minutes. Legacy resolution completed in four seconds. This choice does not
prove that npm reproduces pnpm's peer graph.

Any generated lock must be checked for:

- All selected package versions belonging to the verified source inventory.
- Peer-resolution changes relative to pnpm snapshots.
- Locally generated registry URLs that must not survive into a portable lock.
- Successful installation with a new empty cache and a fresh local registry.
- Native modules loaded by the build all belonging to addons listed in
  `native-addons.py`. Any other module would be missing from the build
  inventory, and its npm loader fails the build.

### Validated baseline

The full inventory contains 1,167 verified tarballs, about 811 MiB on disk. npm
selected 1,041 distinct source identities for 1,089 installation entries, of
which six are bundled entries. On x86-64, `ci` installed 907 packages.

With the generated files copied into `webui/` as `package.json` and
`package-lock.json`, the tested installation command was equivalent to:

```sh
local-npm-registry /path/to/downloaded-tarballs ci \
    --ignore-scripts --legacy-peer-deps --no-audit --no-fund --maxsockets=2
```

The test used a fresh cache and a network namespace without external interfaces.
The local registry helper was the upstream 1.1.0 release referenced by Factory's
spec, unpacked in `/tmp`, rather than a system-installed RPM. The preparation
tool accepts `--registry-helper node /absolute/path/to/dist/index.js` for this
case. The final package should use Factory's `local-npm-registry` RPM.

An earlier baseline pointed `ESBUILD_BINARY_PATH` at Factory's esbuild 0.28.2.
Tracing the Vite 8 build later showed that it never runs esbuild: Rolldown
bundles and Lightning CSS processes styles. The spec no longer uses esbuild.
Vite transformed 3,546 modules and generated `webui/dist`, including
compressed assets and Inter webfonts.

The generated assets were embedded with Go 1.26.8 using the supplied vendor
archive, `GOTOOLCHAIN=local`, `GOPROXY=off`, `GOSUMDB=off`, and
`GOFLAGS='-mod=vendor -buildmode=pie'`. Both the build and
`go test -tags webui ./webui` passed with external networking disabled.

Run the standalone smoke test against a built executable:

```sh
python3 test-webui.py /path/to/git-bug
```

It creates a temporary Git repository, starts a read-only server on localhost,
and checks HTML, a client-side route, gzip handling, referenced JS/CSS assets,
webfonts, and a GraphQL query. The baseline passed checks for 11 referenced
assets and seven fonts. This is an HTTP smoke test, not a browser interaction
test.

A trial using `file:` tarball URLs instead of the local registry caused an
OOM kill; a heap-limited retry did not complete within two minutes. That
transport is not used by the generated lock or recommended build commands.

## Native addons built from source

The Vite build loads three Node-API modules, verified with `strace`:
Rolldown's binding, Tailwind CSS oxide and Lightning CSS. npm normally
installs them as prebuilt binaries in optional platform packages. Those
packages are not in the build inventory. The RPM compiles the modules from the
upstream Rust workspaces instead and installs them where the npm loaders look
first, next to the loading package:

| npm package | Upstream | Cargo package | Installed module |
|---|---|---|---|
| `rolldown` | rolldown/rolldown | `rolldown_binding` | `rolldown/dist/rolldown-binding.<triple>.node` |
| `@tailwindcss/oxide` | tailwindlabs/tailwindcss | `tailwind-oxide` | `@tailwindcss/oxide/tailwindcss-oxide.<triple>.node` |
| `lightningcss` | parcel-bundler/lightningcss | `lightningcss_node` | `lightningcss/lightningcss.<triple>.node` |

`native-addons.py` holds this table. It reads the addon versions from
`package-lock.json`, regenerates the marked region of `_service`, and writes
`native-addons.spec.inc` with the source tags and the `%{native_addons}` list
used by the spec. Each addon gets three manual services: `tar_scm` checks out
tag `v<version>`, `recompress` makes `<name>-<version>.tar.zst`, and
`cargo_vendor` writes `vendor-<name>.tar.zst`. `cargo_vendor` drops non-Linux
crates (`filter`) and audits the lockfile. Its filter mode cannot
enforce the lockfile, but the RPM builds with `--locked` against upstream's
`Cargo.lock`, so any drift fails the build. For this release the vendored
lockfiles are byte-identical to upstream's.

`cargo_vendor` keeps `update=false` on purpose, and the openSUSE source
validator warns about it. The compiled modules only run during the RPM build to
generate the Web UI assets and are not packaged, so keeping the dependency set
upstream tested matters more here than semver updates of crates. Crate updates
come with new upstream releases of the addons. The generated `_service` region
carries a comment explaining this for reviewers.

The RPM build:

- Unpacks only the crates directory of each vendor tarball, keeping upstream's
  `Cargo.lock` and `.cargo/config.toml` (Lightning CSS sets link flags there).
- Checks that each source tree's `package.json` has the locked npm name and
  version.
- Runs `cargo build --release --offline --locked -p <crate>` with the vendored
  source replacement given on the command line. It uses plain cargo because
  `%cargo_build` sets `RUSTFLAGS`, which overrides the project rustflags, and
  forces full debuginfo. The modules only run during the build and are not
  packaged.
- Fails if npm installed any ELF file, then installs the compiled modules.

The locally built modules produced a `webui/dist` byte-identical to the one
produced with upstream's prebuilt binaries. In the local RPM build (3 jobs)
the Rust builds of Rolldown, oxide and Lightning CSS took 7, 1 and 5 minutes.
With 12 jobs they peaked at 1.7, 0.5 and 2.0 GB of memory.
`_constraints` requests 4 GB of memory and 10 GB of disk on x86_64.

Build requirements: Rust 1.98 or newer (the newest toolchain pinned upstream),
cargo, CMake, GCC and G++ for mimalloc, make for jemalloc, and zstd. `tar_scm`
keeps its Git clones in `rolldown/`, `tailwindcss/` and `lightningcss/`;
`.gitignore` excludes them.

## Updating the Web UI sources

From the packaging directory, with the release unpacked separately:

```sh
/usr/lib/obs/service/node_modules --input node-sources-full.json \
    --node-dir /path/to/downloaded-tarballs --download
python3 prepare-webui-lock.py \
    --webui /path/to/git-bug-<version>/webui \
    --tarballs /path/to/downloaded-tarballs \
    --security-inventory "$PWD/node-sources-full.json" --output-dir .
python3 native-addons.py
osc service manualrun
```

`native-addons.py` lists Rust source tarballs left over from previous versions;
remove them. `osc service manualrun` also reruns `go_modules`, which rewrites
`vendor.tar.gz` even when its contents are unchanged.

## RPM integration and validation

The spec now:

- Requires Go 1.26 or newer, matching `go.mod`, instead of the contradictory
  Go 1.24 and 1.25 requirements.
- Uses Factory Node 24, npm 24, the local registry helper, Python for checks,
  and the Rust toolchain only when Web UI support is enabled.
- Compiles the native npm addons from source, as described above.
- Copies the npm-compatible manifest and lock into `webui/`, installs through
  the loopback registry with lifecycle scripts disabled, and runs the Vite build.
- Uses the vendored Go dependencies and disables Go toolchain/module downloads.
- Embeds the generated assets with `go build -tags webui`.
- Collects available production dependency notices and installs them as license
  files. The License expression conservatively covers the production dependency
  inventory, including dependencies that tree shaking may remove.
- Runs handler tests and the HTTP smoke test without suppressing failures. The
  broader bridge suite remains excluded because it needs external services.

`collect-webui-licenses.py` checks license identifiers against the spec's declared
set and records the copied notices in `webui-licenses/index.json`. It reports
missing upstream notice files rather than inventing copyright notices. The
current archives for `@wry/context` and `@wry/trie` omit top-level license text;
their metadata and READMEs are retained. These omissions still need review.

The latest local validation ran the actual spec with `rpmbuild -bb --nodeps`,
inside a network namespace with only loopback enabled, for both the default
x86-64 variant and `--without webui`. Dependency checks were bypassed because
`golang-packaging` was not installed. This is a full local RPM build, not a
clean OBS buildroot validation.

Both runs produced the main RPM and completion subpackages. The Web UI build
installed exactly the three compiled modules. Its handler tests and the HTTP
smoke test passed, and the main RPM has no Node.js or npm runtime dependency.
The builds emitted an empty debugsource file-list warning, which remains to be
reviewed separately.

Other architectures and the complete frontend license audit remain open.

## Remaining implementation stages

1. Review npm/pnpm graph differences beyond the verified source inventory;
   retain the explicit peer-resolution policy.
2. Prune development dependencies, regenerate the npm lock, and reduce the
   build inventory further.
3. Enable the UI on other architectures: add their `napi_triple` and test the
   Rust builds there.
4. Complete the license/notice audit, including the two missing upstream license
   texts noted above.
5. Run a clean OBS build with dependency resolution enabled and review the
   debugsource warning.

Use Quilt for upstream source patches, registering files before editing them.
The packaging directory itself currently has no Quilt series.
