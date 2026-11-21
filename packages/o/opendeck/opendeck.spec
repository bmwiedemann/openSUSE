#
# spec file for package opendeck
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
# the app needs no system node modules at all.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
# Tauri link needs the release line tables only (cf. openidea).
%global build_rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=1 -C strip=none
Name:           opendeck
Version:        2.14.2
Release:        0
Summary:        Use stream controllers like the Elgato Stream Deck
# Legal-Review-Notice: upstream is GPL-3.0-or-later; the rest is derived
# from what the binaries carry, not from any upstream list.
#  * Rust (461+132 linked crates, no proc-macros): MIT or Apache-2.0 arm
#    taken; MPL-2.0 via tauri/kuchikiki/cssparser, option-ext, dtoa-short
#  * elgato-streamdeck; CDLA-Permissive-2.0, Unicode-3.0, Zlib, Unlicense,
#    CC0-1.0, ISC, BSD-2/3-Clause, BSL-1.0, 0BSD, LLVM-exception as offered
#  * aws-lc-sys adds AND OpenSSL for BoringSSL lineage (same tree as the
#    accepted openidea/codenomad vendors): covered by its ISC arm.
#  * psp, streamdeck-strip-render declare no license field; their vendored
#    LICENSE files are Apache-2.0 and MIT. Re-derive on every bump.
#  * npm bundle (vite output, embedded): MIT, ISC, Apache-2.0 (dompurify
#    takes the Apache arm); build-only tools never ship. Fonts: OFL-1.1,
#  * except Tinos and Open Sans (Apache-2.0).
License:        GPL-3.0-or-later AND Apache-2.0 AND MIT AND ISC AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CDLA-Permissive-2.0 AND MPL-2.0 AND Unicode-3.0 AND Unlicense AND Zlib AND Apache-2.0 WITH LLVM-exception AND 0BSD AND OFL-1.1
URL:            https://github.com/nekename/OpenDeck
Source0:        https://github.com/nekename/OpenDeck/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Rust vendor tree of src-tauri (cargo_vendor update=false filter=true,
# Cargo.lock untouched): git pins vendored, stale config.guess/sub synced
# and Windows-only objects stripped, checksums repaired.
Source1:        vendor.tar.zst
# Rust vendor tree of the bundled starterpack plugin
# (plugins/com.amansprojects.starterpack.sdPlugin), same service flags;
# its enigo git pin is vendored.
Source2:        plugin-vendor.tar.zst
# Source-Binary-Exception: vendor.tar.zst:vendor/libloading-0.7.4/tests/*.dll -- test-data: Windows-only dlopen fixtures for the cfg(windows) test, never touched on Linux
# Source-Binary-Exception: vendor.tar.zst:vendor/flate2-1.1.9/tests/corrupt-gz-file.bin -- test-data: gzip corpus the gunzip test reads to assert InvalidInput, never executed
# Source-Binary-Exception: vendor.tar.zst:vendor/wry-0.57.0/examples/custom_protocol/wasm.wasm -- test-data: demo asset fetched only by the custom-protocol example page, never built or shipped
# Source-Binary-Exception: rollup-vendor.tar.zst:vendor/libloading-0.9.0/tests/*.dll -- test-data: Windows-only dlopen fixtures for the cfg(windows) functions test, never touched on Linux
# Source-Binary-Exception: rollup-vendor.tar.zst:vendor/libmimalloc-sys2-0.1.52/c_src/mimalloc3/bin/* -- other-platform: Windows redirect DLLs, import libs and minject tool; Linux builds mimalloc from the C sources
# Source-Binary-Exception: rollup-vendor.tar.zst:vendor/psm-0.1.29/src/arch/wasm32.o -- other-platform: stack-switching stub for wasm32 targets; Linux assembles the .S sources
# Source-Binary-Exception: lightningcss-vendor.tar.zst:vendor/napi-build-1.2.1/src/libs/* -- other-platform: Windows node import libraries; Linux links nothing at build time
# Source-Binary-Exception: go-x-sys-c0bba94a.tar.gz:x-sys/windows/testdata/ev-signed-file.exe -- test-data: Authenticode test fixture documented by x/sys's own testdata README, never executed
# From-source esbuild 0.21.5, repacked from the Go module proxy (hashes
# in the report); the build compiles it offline with the system toolchain.
# The 23 prebuilt platform binaries were deleted at repack.
Source3:        esbuild-0.21.5.tar.gz
Source4:        go-x-sys-c0bba94a.tar.gz
# From-source rollup 4.57.1 NAPI (tag workspace, 207-crate locked vendor);
# the binding lands where the rollup loader probes. Prebuilt .node files
# were deleted at repack.
Source5:        https://github.com/rollup/rollup/archive/refs/tags/v4.57.1.tar.gz#/rollup-4.57.1.tar.gz
Source6:        rollup-vendor.tar.zst
# From-source lightningcss 1.31.1 NAPI (commit archive, no tag; 201-crate
# vendor). Single version for the closure: Patch2 pins the nested 1.30.2.
Source7:        https://github.com/parcel-bundler/lightningcss/archive/6993d9f1d3cd69030c5976cd8860361b7679f68d.tar.gz#/lightningcss-1.31.1.tar.gz
Source8:        lightningcss-vendor.tar.zst
# From-source tailwindcss oxide 4.1.18 NAPI. Source9 is the upstream
# release tag, Source10 the `cargo vendor` output for its locked root
# Cargo.lock (90 crates, napi crate tailwind-oxide in crates/node).
Source9:        https://github.com/tailwindlabs/tailwindcss/archive/refs/tags/v4.1.18.tar.gz#/tailwindcss-4.1.18.tar.gz
Source10:       oxide-vendor.tar.zst
# npm tree for the node_modules service: exact upstream-tested versions,
# dev-only tools dropped; every binary nothing on Linux loads deleted at
# repack, the 4 helpers compiled from source instead (see below).
Source11:       package-lock.json
Source12:       node_modules.spec.inc
# Checksums for the registry tarballs in node_modules.obscpio.
Source13:       node_modules.sums
Source14:       %{name}.desktop
Source15:       OFL-1.1.txt
# Metainfo written for this package: upstream's file fails validation
# (remote screenshots, short captions), so it is not used.
Source16:       %{name}.metainfo.xml
# PATCH-FIX-OPENSUSE opendeck-disable-telemetry.patch -- telemetry is
# opt-in: default off, first-run dialog no longer claims collection
Patch0:         %{name}-disable-telemetry.patch
# PATCH-FIX-OPENSUSE opendeck-no-deno-build.patch -- Deno is x86_64-only
# in Factory: replicate build.ts natively (stage assets, cargo install)
Patch1:         %{name}-no-deno-build.patch
# PATCH-FIX-OPENSUSE opendeck-npm-build-deps.patch -- pin the exact
# upstream-tested versions (single lightningcss), drop dev-only tools
# (tauri CLI, prettier, svelte-check), keep build and runtime deps
Patch2:         %{name}-npm-build-deps.patch
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  go
BuildRequires:  local-npm-registry
BuildRequires:  memory-constraints
BuildRequires:  nodejs24
BuildRequires:  npm
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.85
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(xkbcommon)
# Windows plugins run through Wine; Node.js plugins need Node.
Recommends:     nodejs
Recommends:     wine
ExclusiveArch:  %{rust_tier1_arches}
%include %{_sourcedir}/node_modules.spec.inc

%description
OpenDeck is a desktop application for using stream controller devices
like the Elgato Stream Deck, including support for plugins made for
the original Stream Deck SDK. The bundled starterpack plugin, udev
rules and URL-scheme handlers ship in the box, and telemetry stays
off unless enabled in the settings. Updates come from RPM: the in-app
update check is disabled.

%prep
%autosetup -p1 -n OpenDeck-%{version}
# Rust vendor trees, generated with update=false: Cargo.lock untouched.
tar --zstd -xf %{SOURCE1} -C src-tauri
tar --zstd -xf %{SOURCE2} -C plugins/com.amansprojects.starterpack.sdPlugin
# The exact pinned npm tree for the offline build (the registry itself
# is served from node_modules.obscpio by local-npm-registry).
cp %{SOURCE11} ./package-lock.json
# The OFL text for the embedded fonts, carried as a loose source.
cp %{SOURCE15} ./OFL-1.1.txt

%build
%limit_build -m 2000
# local-npm-registry runs under node and execs `npm`: bypass Leap's
# flapping libalternatives wrapper with a shim to versioned npm22/24.
# No-op where no versioned npm exists (Tumbleweed uses bare npm).
mkdir -p .npshim
for v in %{_bindir}/npm22 %{_bindir}/npm24; do
  if [ -x "$v" ]; then printf '#!/bin/sh\nexec %s "$@"\n' "$v" > .npshim/npm; chmod +x .npshim/npm; break; fi
done
export PATH=$PWD/.npshim:$PATH
# Native helper names per arch: esbuild's platform dirs use arm64 for
# aarch64, the napi bindings use the rust triple arch throughout.
goarch=x64
napi_arch=x64
%ifarch aarch64
goarch=arm64
napi_arch=arm64
%endif
%ifarch ppc64le
goarch=ppc64
napi_arch=ppc64
%endif
%ifarch s390x
goarch=s390x
napi_arch=s390x
%endif
%ifarch riscv64
goarch=riscv64
napi_arch=riscv64
%endif
local-npm-registry %{_sourcedir} install --include=dev --include=optional --ignore-scripts --no-audit --no-fund
# esbuild from source (all prebuilt platform binaries were deleted at
# repack). The tree builds offline with the system toolchain; the
# binary lands where the esbuild loader probes.
tar xzf %{SOURCE3} && tar xzf %{SOURCE4}
export GOPROXY=off CGO_ENABLED=0 GOTOOLCHAIN=local GOFLAGS=-mod=mod GOCACHE=$PWD/.gocache GOPATH=$PWD/.gopath
top=$PWD
(cd esbuild-0.21.5 && go mod edit -replace golang.org/x/sys=$top/x-sys && go build -ldflags="-s -w" -o $top/esbuild-bin ./cmd/esbuild)
install -D -m0755 esbuild-bin node_modules/@esbuild/linux-$goarch/bin/esbuild
rm -rf esbuild-0.21.5 x-sys esbuild-bin .gocache .gopath
# rollup NAPI from source (prebuilt .node files deleted at repack).
# bindings_napi builds offline from the tag workspace; the binding lands
# where the rollup loader probes.
tar xzf %{SOURCE5} && tar --zstd -xf %{SOURCE6} -C rollup-4.57.1/rust
rm -f rollup-4.57.1/rust-toolchain.toml rollup-4.57.1/rust/bindings_napi/.cargo/config.toml rollup-4.57.1/rust/bindings_wasm/.cargo/config.toml
mkdir -p rollup-4.57.1/rust/.cargo
printf '[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' > rollup-4.57.1/rust/.cargo/config.toml
export CARGO_NET_OFFLINE=true CARGO_HOME=$PWD/.cargo-home
(cd rollup-4.57.1/rust && cargo build --release --locked --offline -p bindings_napi)
install -D -m0755 rollup-4.57.1/rust/target/release/libbindings_napi.so node_modules/@rollup/rollup-linux-$napi_arch-gnu/rollup.linux-$napi_arch-gnu.node
rm -rf rollup-4.57.1
# lightningcss NAPI from source (prebuilt .node files deleted at repack).
# lightningcss_node builds offline from the 1.31.1 tree; RUSTFLAGS keeps
# the node's global constructors (cf. openidea).
tar xzf %{SOURCE7} && mv lightningcss-*/ lightningcss-1.31.1 && tar --zstd -xf %{SOURCE8} -C lightningcss-1.31.1
rm -f lightningcss-1.31.1/.cargo/config.toml
mkdir -p lightningcss-1.31.1/.cargo
printf '[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' > lightningcss-1.31.1/.cargo/config.toml
export RUSTFLAGS="-C link-args=-Wl,-z,nodelete"
(cd lightningcss-1.31.1 && cargo build --release --locked --offline -p lightningcss_node)
install -D -m0755 lightningcss-1.31.1/target/release/liblightningcss_node.so node_modules/lightningcss-linux-$napi_arch-gnu/lightningcss.linux-$napi_arch-gnu.node
unset RUSTFLAGS
rm -rf lightningcss-1.31.1
# tailwindcss oxide NAPI from source (every prebuilt .node file and the
# wasi .wasm blob were deleted at repack). The tailwind-oxide crate
# builds offline from the tag tree against the locked vendor.
tar xzf %{SOURCE9} && tar --zstd -xf %{SOURCE10} -C tailwindcss-4.1.18
rm -f tailwindcss-4.1.18/crates/node/.cargo/config.toml
mkdir -p tailwindcss-4.1.18/.cargo
printf '[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' > tailwindcss-4.1.18/.cargo/config.toml
(cd tailwindcss-4.1.18/crates/node && cargo build --release --locked --offline)
install -D -m0755 tailwindcss-4.1.18/target/release/libtailwind_oxide.so node_modules/@tailwindcss/oxide-linux-$napi_arch-gnu/tailwindcss-oxide.linux-$napi_arch-gnu.node
rm -rf tailwindcss-4.1.18 .cargo-home
unset CARGO_HOME
# Frontend bundle (this is what `deno task build` runs: package.json
# scripts are the tasks; Deno itself is never needed).
node node_modules/vite/bin/vite.js build
# Rust backend plus the bundled starterpack plugin (built by the
# patched build.rs straight from the plugin vendor tree, offline).
# The in-app update check is compiled out via this knob.
export OPENDECK_DISABLE_UPDATE_CHECK=1
pushd src-tauri
%cargo_build -- -p opendeck --features tauri/custom-protocol
popd

%install
# NOTE: %%cargo_build forces CARGO_TARGET_DIR to the top source dir, so
# the binary lands in ./target/release, while build.rs stages the plugin
# into src-tauri/target/plugins on every toolchain.
binary=target/release/opendeck
test -f "$binary" || binary=src-tauri/target/release/opendeck
install -D -m0755 "$binary" %{buildroot}%{_bindir}/opendeck
# Tauri resolves resources from %%{_prefix}/lib/OpenDeck next to the
# /usr/bin binary.
mkdir -p %{buildroot}%{_prefix}/lib/OpenDeck
cp -a src-tauri/target/plugins %{buildroot}%{_prefix}/lib/OpenDeck/plugins
# cargo install bookkeeping, not plugin payload.
rm -f %{buildroot}%{_prefix}/lib/OpenDeck/plugins/*/*/.crates.toml %{buildroot}%{_prefix}/lib/OpenDeck/plugins/*/*/.crates2.json
install -D -m0644 %{SOURCE14} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m0644 src-tauri/icons/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -D -m0644 %{SOURCE16} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
install -D -m0644 src-tauri/bundle/40-streamdeck.rules %{buildroot}%{_udevrulesdir}/40-streamdeck.rules

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE.md OFL-1.1.txt
%doc README.md
%{_bindir}/opendeck
%{_prefix}/lib/OpenDeck/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_udevrulesdir}/40-streamdeck.rules

%changelog
