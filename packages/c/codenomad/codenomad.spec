#
# spec file for package codenomad
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

# The internal node dependency generator would slurp the vendored
# package.json files and emit bogus npm(...) Provides/Requires;
# everything the app needs at runtime is staged below.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
Name:           codenomad
Version:        1.0.1
Release:        0
Summary:        AI coding command center (Tauri desktop)
# Upstream is MIT. Derived over the shipped trees, not the build roots.
# Rust side: normal deps of -p codenomad-tauri for the Linux targets
# (offline cargo tree over the locked vendor closure, 380 crates):
# MPL-2.0 links at runtime via tauri -- tauri-utils -- kuchikiki --
# cssparser/selectors; CDLA-Permissive-2.0 links via reqwest --
# hyper-rustls -- webpki-roots; Unicode-3.0 via the ICU crates.
# Zlib, Unlicense, CC0-1.0 and BSD-2-Clause survive as offered
# alternatives of linked crates (miniz_oxide, memchr et al, dunce,
# zerocopy). npm side: the staged server is a production
# (omit-dev) install of the server workspace, 296 packages: MIT,
# ISC, Apache-2.0, BSD-3-Clause (node-forge takes the BSD choice),
# BlueOak-1.0.0, the tauri dual MIT/Apache pair, 0BSD. The sharp
# libvips shims (LGPL-3.0-or-later) and the caniuse/spdx/argparse/
# WTFPL/AFL bits are dev-only and never staged, so they are out.
# Re-derive both trees on every bump.
License:        MIT AND Apache-2.0 AND ISC AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC0-1.0 AND 0BSD AND MPL-2.0 AND Unicode-3.0 AND Zlib AND Unlicense AND CDLA-Permissive-2.0
URL:            https://github.com/NeuralNomadsAI/CodeNomad
Source0:        %{name}-%{version}.tar.gz
# Rust vendor tree. Produced with the OBS cargo_vendor backend against
# packages/tauri-app with update=false (respect upstream Cargo.lock),
# tag=crates (upstream already ships vendor/ with the tao +
# tauri-plugin-updater forks selected via [patch.crates-io]) and
# filter=true (drop crates only needed on non-Linux targets):
# /usr/lib/obs/service/cargo_vendor --src CodeNomad-1.0.1/packages/tauri-app --outdir vendor-out --compression zst --tag crates --update false --filter true
# The filter leaves two Windows-only prebuilt sets inside Linux crates:
# aws-lc-sys builder/prebuilt-nasm/*.obj (copied only for windows-x86_64,
# see use_prebuilt_nasm in builder/main.rs) and ring
# pregenerated/*-nasm.o plus *-win32n.o (windows asm targets only, see
# ASM_TARGETS in build.rs). Both deleted here with .cargo-checksum.json
# repair; Linux builds aws-lc-sys and ring from C and .S sources
# (verified by compiling both crates offline). Cargo.lock is untouched.
# Source-Binary-Exception: vendor-crates.tar.zst:vendor-crates/libloading-0.7.4/tests/*.dll -- test-data: Windows-only dlopen fixtures for the cfg(windows) test, never touched on Linux
# Source-Binary-Exception: vendor-crates.tar.zst:vendor-crates/wry-0.54.4/examples/custom_protocol/wasm.wasm -- test-data: demo asset fetched only by the custom-protocol example page, never built or shipped
# Source-Binary-Exception: vendor-crates.tar.zst:vendor-crates/flate2-1.1.9/tests/corrupt-gz-file.bin -- test-data: gzip corpus the gunzip test reads to assert InvalidInput, never executed
# Source-Binary-Exception: rollup-vendor.tar.zst:rollup-vendor/vendor/libloading-0.8.9/tests/*.dll -- test-data: Windows-only dlopen fixtures for the cfg(windows) functions test, never touched on Linux
# Source-Binary-Exception: go-x-sys-c0bba94a.tar.gz:x-sys/windows/testdata/ev-signed-file.exe -- test-data: Authenticode test fixture documented by x/sys's own testdata README, never executed
Source1:        vendor-crates.tar.zst
# npm lockfile for the node_modules service (Source10). Upstream's
# lockfileVersion-3 file cannot be fed verbatim: the service aborts on
# the 5 workspace "link" entries and the 8 "packages/*" workspace keys.
# This file drops the links and workspace definitions but re-keys the 3
# nested workspace deps (packages/<ws>/node_modules/...) as
# node_modules/__ws-<ws>__/... so their tarballs still land in the
# obscpio (e.g. electron-app's app-builder-bin 4.2.0 beside the top
# 4.0.0). Regenerate with the same transform, then manualrun.
# The registry tarballs ship prebuilt binaries for every platform
# upstream supports. At repack time the binaries nothing on Linux
# loads were deleted: all non-Linux platform files
# (esbuild, rollup, sharp, libvips, tauri-cli, fsevents, iconv),
# the 7zip/app-builder electron-packaging helpers, the playwright
# screenshot codec, and wasm blobs whose bytes travel inlined in a
# sibling js file (undici llhttp, source-map mappings, shiki onig).
# Kept is nothing: every prebuilt binary the Linux build or the
# staged app loads is now built from source instead (the build section:
# esbuild via Sources 20-22, rollup NAPI via Sources 23-24).
# The sharp .node and libvips .so files are deleted too: Patch5
# drops the PWA pwaAssets icon generation, the only sharp
# consumer, so sharp never loads at build or runtime.
# package-lock.json integrity values and node_modules.sums were
# regenerated for exactly those 108 tarballs (97 filtered, shiki
# onig.wasm, 4 sharp/libvips, 4 esbuild, 2 rollup); the entry set
# is unchanged, so offline resolution is unaffected.
Source10:       package-lock.json
Source11:       node_modules.spec.inc
# Checksums for the registry tarballs in node_modules.obscpio (service output).
Source12:       node_modules.sums
# From-source esbuild. Upstream publishes no source tarballs, so these
# are repacked from the Go module proxy (release tags v0.21.5/v0.25.12
# plus the single pinned dependency both trees need):
#   esbuild v0.21.5 (git fc37c2fa): h1:oShm8TT5QUhf6vM7teg0nmd14eHu64dPmVluC2f4DMg=
#   esbuild v0.25.12 (git 208f5399): h1:7kIg7aG2++vhheW5YCzut1q1AjehYVQU752NcMuGVsw=
#   x/sys c0bba94a (2022-07-15): h1:0A+M6Uqn+Eje4kHMK80dtF3JCXC4ykBgQG4Fe06QRhQ=
# (re-verify with `go mod download -json` against the proxy/sumdb).
# Repack: unzip the module zips, rename to the bare top dirs. The build
# compiles both trees offline (GOPROXY=off, replace to the shipped
# x/sys) and installs the binaries where the esbuild loaders probe;
# the 4 prebuilt platform binaries were deleted at repack (sums +
# lock integrity regenerated, entry set unchanged).
Source20:       esbuild-0.21.5.tar.gz
Source21:       esbuild-0.25.12.tar.gz
Source22:       go-x-sys-c0bba94a.tar.gz
# From-source rollup NAPI. Source23 is the upstream release tag
# v4.52.5 workspace (rust/ holds the napi bindings crate), Source24
# the `cargo vendor` output for its locked Cargo.lock (196 crates).
# The build compiles bindings_napi offline (vendor source replacement,
# system toolchain) and installs the binding where the rollup
# loader probes; both prebuilt .node files were deleted at repack
# (sums + lock integrity regenerated, entry set unchanged).
Source23:       rollup-4.52.5.tar.gz
Source24:       rollup-vendor.tar.zst
# PATCH-FIX-OPENSUSE codenomad-system-node.patch: use system Node.js.
Patch0:         %{name}-system-node.patch
# PATCH-FIX-OPENSUSE codenomad-no-opencode-download.patch: no runtime npm.
Patch1:         %{name}-no-opencode-download.patch
# PATCH-FIX-OPENSUSE codenomad-offline-server-staging.patch: staging install.
Patch2:         %{name}-offline-server-staging.patch
# PATCH-FIX-OPENSUSE codenomad-no-ui-update.patch: no UI self-update.
Patch3:         %{name}-no-ui-update.patch
# PATCH-FIX-OPENSUSE codenomad-wayland-default.patch: native Wayland.
Patch4:         %{name}-wayland-default.patch
# PATCH-FIX-OPENSUSE codenomad-no-pwa-assets.patch: no PWA icon gen.
Patch5:         %{name}-no-pwa-assets.patch
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  go
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  nodejs24
BuildRequires:  npm
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rust >= 1.85
BuildRequires:  zsh
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Requires:       nodejs24 >= 24.20
Requires:       opencode >= 2.1.2
# The server shells out to git for repo features (clone, worktrees,
# rev-parse) and runs directory-only without it.
Recommends:     git-core
ExclusiveArch:  x86_64 aarch64
%include %{_sourcedir}/node_modules.spec.inc

%description
CodeNomad desktop client (Tauri flavor): a web UI for AI coding
agents with a bundled Node server. This build uses the system
Node.js and the system opencode package. The upstream self-updater
is disabled (unsigned builds ship without updater config) and the
in-app OpenCode npm installer is neutered; updates flow via RPM.

%prep
%autosetup -p1 -a1 -n CodeNomad-%{version}

%build
%limit_build -m 2000
# npm closure first (fully offline via the local registry).
rm -rf node_modules
local-npm-registry %{_sourcedir} install --include=dev --include=optional --ignore-scripts
# esbuild from source (the 4 prebuilt platform binaries were deleted
# at repack). Both release trees build offline with the system
# toolchain; the binaries land where each loader probes (root
# 0.25.12, vite-nested 0.21.5) before prebuild, which execs
# --version and checks it against package.json.
esarch=x64
%ifarch aarch64
esarch=arm64
%endif
tar xzf %{SOURCE20} && tar xzf %{SOURCE21} && tar xzf %{SOURCE22}
export GOPROXY=off CGO_ENABLED=0 GOTOOLCHAIN=local GOFLAGS=-mod=mod GOCACHE=$PWD/.gocache GOPATH=$PWD/.gopath
top=$PWD
for esver in 0.21.5 0.25.12; do
  (cd esbuild-$esver && go mod edit -replace golang.org/x/sys=$top/x-sys && go build -ldflags="-s -w" -o $top/esbuild-bin-$esver ./cmd/esbuild)
done
install -D -m0755 esbuild-bin-0.25.12 node_modules/@esbuild/linux-$esarch/bin/esbuild
install -D -m0755 esbuild-bin-0.21.5 node_modules/vite/node_modules/@esbuild/linux-$esarch/bin/esbuild
rm -rf esbuild-0.21.5 esbuild-0.25.12 x-sys esbuild-bin-0.21.5 esbuild-bin-0.25.12 .gocache .gopath
# rollup NAPI from source (both prebuilt .node files were deleted at
# repack). The crate builds offline from the tag workspace against
# the locked vendor; the binding lands where the rollup loader
# probes before prebuild, which requires it unconditionally.
roarch=x64
%ifarch aarch64
roarch=arm64
%endif
tar xzf %{SOURCE23} && tar --zstd -xf %{SOURCE24}
mkdir -p rollup-4.52.5/rust/vendor rollup-4.52.5/rust/.cargo
cp -a rollup-vendor/vendor/. rollup-4.52.5/rust/vendor/
printf '[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' > rollup-4.52.5/rust/.cargo/config.toml
export CARGO_NET_OFFLINE=true CARGO_HOME=$PWD/.cargo-home
(cd rollup-4.52.5/rust && cargo build --release --locked --offline -p bindings_napi)
install -D -m0755 rollup-4.52.5/rust/target/release/libbindings_napi.so node_modules/@rollup/rollup-linux-$roarch-gnu/rollup.linux-$roarch-gnu.node
rm -rf rollup-4.52.5 rollup-vendor .cargo-home
# Build UI + server and stage src-tauri/resources (server,
# ui-loading). The bundled-Node download is patched out; the Rust
# side falls back to /usr/bin/node. This runs under the registry as
# well: prebuild's server staging does its own nested production npm
# install, which must resolve from the same local tarballs (without
# it the build phones registry.npmjs.org and dies EAI_AGAIN).
local-npm-registry %{_sourcedir} run prebuild --workspace @codenomad/tauri-app
# Rust backend. Only the desktop crate ships; the windows/macos test
# members stay out. Braced macro form is mandatory (see craft suite).
pushd packages/tauri-app
%{cargo_build} -p codenomad-tauri
popd

%install
# NOTE: the cargo build macro forces CARGO_TARGET_DIR to the top source
# dir on current toolchains, so the binary lands in ./target/release
# even though the build runs in packages/tauri-app. Older toolchains
# (16.x/15.x) leave the default, which is under packages/tauri-app.
binary=target/release/codenomad-tauri
test -f "$binary" || binary=packages/tauri-app/target/release/codenomad-tauri
install -D -m0755 "$binary" %{buildroot}%{_bindir}/codenomad
# Server + loading UI under prefix/lib, NOT libdir: the backend only
# looks up ../lib/CodeNomad and ../lib/codenomad relative to the
# binary, which never matches lib64. These are arch-independent data.
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/resources
cp -a packages/tauri-app/src-tauri/resources/server %{buildroot}%{_prefix}/lib/%{name}/resources/server
cp -a packages/tauri-app/src-tauri/resources/ui-loading %{buildroot}%{_prefix}/lib/%{name}/resources/ui-loading
# The staged trees never need source maps or upstream's own test files
# at runtime (vite emits maps for both bundles; thousands of files).
# Sweep the staged copy only, so the build and the tests below still
# see pristine sources. Empty non-code files (placeholders, fixtures)
# go too; empty loadable modules stay, a missing one would fail imports.
find %{buildroot}%{_prefix}/lib/%{name}/resources -name '*.map' -delete
find %{buildroot}%{_prefix}/lib/%{name}/resources -name '*.test.js*' -delete
find %{buildroot}%{_prefix}/lib/%{name}/resources -type f -size 0 ! -name '*.js' ! -name '*.cjs' ! -name '*.mjs' ! -name '*.node' ! -name '*.wasm' -delete
# The linter rejects env interpreters; the system Node lives at the
# fixed path either way, so pin the first line where it names node.
# Same for the vendored python helpers. Husky git hooks never run
# from an installed payload, so drop those directories whole.
grep -rl '^#!%{_bindir}/env node$' %{buildroot}%{_prefix}/lib/%{name}/resources | xargs -r sed -i '1s|^#!%{_bindir}/env node$|#!%{_bindir}/node|'
grep -rl '^#!%{_bindir}/env python3$' %{buildroot}%{_prefix}/lib/%{name}/resources | xargs -r sed -i '1s|^#!%{_bindir}/env python3$|#!%{_bindir}/python3|'
find %{buildroot}%{_prefix}/lib/%{name}/resources -type d -name '.husky' -prune -exec rm -rf {} +
# Desktop entry + icons (declared in tauri.conf.json for deb/rpm).
# Upstream's file points at the wrong binary name, hides itself and
# has no category; fix all three for a visible menu entry. The window
# class carries the application ID so Wayland groups the window with
# its desktop entry (the Tauri identifier already matches the file).
install -D -m0644 packages/tauri-app/src-tauri/icons/linux/ai.neuralnomads.codenomad.client.desktop %{buildroot}%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
sed -i -e 's/^Exec=.*/Exec=codenomad/' -e '/^NoDisplay=/d' -e 's/^Categories=.*$/Categories=Development;IDE;/' -e 's/^StartupWMClass=.*/StartupWMClass=ai.neuralnomads.codenomad.client/' %{buildroot}%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
for s in 32 48 64 128 256 512; do
  install -D -m0644 packages/tauri-app/src-tauri/icons/linux/${s}x${s}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/codenomad-tauri.png
done

%check
# Upstream CI runs the crate tests headless; the workspace default
# member limits them to the shipped crate, mirrored here. One shell
# regression needs a real zsh and the probe tests need system Node.
# The cargo test run shares the build's top target dir, so only
# the test harness itself still compiles here.
pushd packages/tauri-app
export CODENOMAD_TEST_NODE=%{_bindir}/node
%{cargo_test} -p codenomad-tauri --locked --release -- --test-threads=4
popd
# The staged resources ship no source maps or upstream test files.
test "$(find %{buildroot}%{_prefix}/lib/%{name}/resources \( -name '*.map' -o -name '*.test.js*' \) | wc -l)" = 0

%files
%license LICENSE
%doc README.md
%{_bindir}/codenomad
%{_prefix}/lib/%{name}/
%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
%{_datadir}/icons/hicolor/*/apps/codenomad-tauri.png

%changelog
