#
# spec file for package openidea
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

%define rolldown_version 1.2.14
%define lightningcss_version 1.33.0
# Full DWARF pushed upstream's fat-LTO link past 37 GB: line tables only, as zed
%global build_rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=1 -C strip=none
Name:           openidea
Version:        0.1.38
Release:        0
Summary:        IntelliJ IDEA-style IDE with a Rust core
# Legal-Review-Notice: upstream is Apache-2.0; the rest is derived from what the
# binary carries, not from upstream's THIRD_PARTY_LICENSES.md.
#  * Rust: 697 crates linked on Linux (no proc-macros), MIT or Apache-2.0 arm taken
#  * Wasmtime, Cranelift: Apache-2.0 WITH LLVM-exception
#  * odpic-sys, oracle (Oracle data sources): UPL-1.0 OR Apache-2.0,
#    distributed under the Apache-2.0 arm
#  * spellbook, nucleo-matcher, option-ext, cssparser 0.37.0 and
#    macros, dtoa-short, selectors 0.38.0: MPL-2.0
#  * webpki-roots: CDLA-Permissive-2.0; notify: CC0-1.0; ICU crates: Unicode-3.0
#  * foldhash, zlib-rs: Zlib
#  * ring, aws-lc, rustls-webpki, dalek and others: ISC, BSD-3-Clause
#  * Vite bundle (npm packages, per its source maps): MIT, ISC; d3: BSD-3-Clause
#  * chevrotain, dompurify (Apache-2.0 arm): Apache-2.0; elkjs (mermaid ELK): EPL-2.0
#  * Inter and JetBrains Mono fonts in the bundle: OFL-1.1
#  * IntelliJ icons and diff code: Apache-2.0, some MIT; cspell-dicts, themes: MIT
#  * en_US Hunspell dictionary (SCOWL, Ispell): BSD-3-Clause AND MIT, as aspell-en
#  * Not shipped, removed from sources: prebuilt Lombok, JDT LS extensions, sample plugins
#  * Not shipped: dev-only npm tools; rolldown (MIT), lightningcss (MPL-2.0): build only
#  * MPL-2.0 and EPL-2.0 sources ship in the source package
License:        Apache-2.0 AND MIT AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND EPL-2.0 AND ISC AND MPL-2.0 AND OFL-1.1 AND Unicode-3.0 AND Zlib
URL:            https://github.com/l0ng-ai/openidea
# Tag repacked without prebuilt jars, fixture/official plugin.wasm and
# p0-probe full/min.wasm (their .wasm.sources provenance files stay)
Source0:        %{name}-%{version}.tar.zst
# All vendor trees: cargo_vendor update=false filter=true, minus prebuilt files and
# their .cargo-checksum.json entries. Here: aws-lc-sys, ring Windows nasm objects, binary
# fixtures of libloading, wit-parser, wry, async-compression; wit-component's libdl.so
# emptied: only its dylib Linker reads it, which wasmtime bindgen never calls
Source1:        vendor.tar.zst
# rolldown NAPI binding, built from source; its vendor tree lacks mimalloc's Windows bin/
# and libloading's, pnp's binary test fixtures; napi-build's wasi_heap_sync_exports.o emptied
Source2:        https://github.com/rolldown/rolldown/archive/refs/tags/v%{rolldown_version}.tar.gz#/rolldown-%{rolldown_version}.tar.gz
Source3:        rolldown-vendor.tar.zst
# lightningcss NAPI binding, built from source; napi-build 1.x's Windows src/libs emptied
Source4:        https://github.com/parcel-bundler/lightningcss/archive/refs/tags/v%{lightningcss_version}.tar.gz#/lightningcss-%{lightningcss_version}.tar.gz
Source5:        lightningcss-vendor.tar.zst
Source6:        %{name}.desktop
# Generated: npm install --package-lock-only --ignore-scripts on Patch3's package.json,
# against a registry serving only pnpm-lock.yaml's tarballs (no platform binaries);
# its 8 optional peers added as peer entries so the build's registry serves them
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
# PATCH-FIX-OPENSUSE openidea-no-self-update.patch -- updates come from RPM
Patch0:         openidea-no-self-update.patch
# PATCH-FIX-OPENSUSE openidea-no-server-download.patch -- no prebuilt remote server
Patch1:         openidea-no-server-download.patch
# PATCH-FIX-OPENSUSE openidea-no-prebuilt-jars.patch -- drop the embedded prebuilt jars
Patch2:         openidea-no-prebuilt-jars.patch
# PATCH-FIX-OPENSUSE openidea-npm-build-deps.patch -- vendor only build and test tools
Patch3:         openidea-npm-build-deps.patch
# PATCH-FIX-OPENSUSE openidea-rlib-only.patch -- skip the unused mobile library types
Patch4:         openidea-rlib-only.patch
# PATCH-FIX-OPENSUSE openidea-no-tool-installs.patch -- tools come from the distribution
Patch5:         openidea-no-tool-installs.patch
# PATCH-FIX-OPENSUSE openidea-no-jdk-downloads.patch -- JDKs come from the distribution
Patch6:         openidea-no-jdk-downloads.patch
# PATCH-FIX-OPENSUSE openidea-no-agent-installs.patch -- no ACP Registry or npx agents
Patch7:         openidea-no-agent-installs.patch
# PATCH-FIX-OPENSUSE openidea-no-coverage-installs.patch -- no coverage/profiler installs
Patch8:         openidea-no-coverage-installs.patch
BuildRequires:  cargo-packaging
BuildRequires:  cmake
# The ide-agent and ide-tools tests run git and curl.
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  local-npm-registry
BuildRequires:  memory-constraints
BuildRequires:  nodejs >= 22.12
BuildRequires:  npm
BuildRequires:  pkgconfig
# rolldown's oxc crates need Rust 1.97.
BuildRequires:  rust >= 1.97
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(x11)
# dlopened by tao (x11-dl); GTK pulls them in today, named so they stay
Requires:       libX11.so.6()(64bit)
Requires:       libXi.so.6()(64bit)
# The VCS features run the git command line.
Recommends:     git-core
# Uploaded to remote development hosts.
Suggests:       %{name}-server
# C, C++ and Objective-C code insight (clangd).
Suggests:       clang
# Go code insight (gopls) and debugging (dlv).
Suggests:       delve
Suggests:       gopls
# C, C++ and Swift debugging (lldb-dap).
Suggests:       lldb
# Lua code insight.
Suggests:       lua-language-server
# CMake code insight.
Suggests:       neocmakelsp
# Python code insight (pyright, ty) and debugging (debugpy).
Suggests:       python3-debugpy
Suggests:       python3-pyright
Suggests:       python3-ty
# TOML code insight.
Suggests:       taplo
# LaTeX code insight.
Suggests:       texlab
# Zig code insight.
Suggests:       zls
ExclusiveArch:  %{rust_tier1_arches}
%include %{_sourcedir}/node_modules.spec.inc

%description
OpenIDEA is an open-source IDE in the style of IntelliJ IDEA, built as a
Tauri desktop application with a Rust backend: editor, code insight
through language servers, debugger, Git, terminal, database and HTTP
clients for many languages.

This build downloads nothing to run: the in-app self-updater and the
installers of language servers, debuggers, coverage and profiling
tools, JDKs and agents are disabled. Tools are found on PATH as usual,
and for a missing one the IDE names the openSUSE package to install.

%package server
Summary:        Remote development server for OpenIDEA
# Legal-Review-Notice: derived as above, over the 548 crates linked into openidea-server.
#  * No GUI, Wasmtime or frontend: no Apache-2.0 WITH LLVM-exception, EPL-2.0, OFL-1.1
#  * MPL-2.0, CDLA-Permissive-2.0, CC0-1.0, Unicode-3.0, Zlib, ISC, BSD-3-Clause:
#    from the same crates as above
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND MPL-2.0 AND Unicode-3.0 AND Zlib

%description server
openidea-server is the OpenIDEA backend for remote development. When
OpenIDEA connects over SSH to a Linux host of the same architecture,
it uploads this server there and runs it; the server speaks to the IDE
over its standard input and output. The remote host needs libsqlite3
and a glibc at least as new as Tumbleweed's.

%prep
%autosetup -p1 -a1
# Its licence text has the same file name as upstream's own.
cp src/editor/core/cm/angular/LICENSE LICENSE-codemirror-lang-angular

%build
%limit_build -m 2000
napi_arch=x64
# rolldown's loader probes dist/ for its x64 binding, dist/shared/ for arm64
rolldown_dir=dist
%ifarch aarch64
napi_arch=arm64
rolldown_dir=dist/shared
%endif
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts --no-audit --no-fund
# Build-time helpers only: no LTO, so they build quickly.
export CARGO_HOME=$PWD/.cargo-home CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_LTO=false CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
tar xzf %{SOURCE2}
tar -C rolldown-%{rolldown_version} --zstd -xf %{SOURCE3} vendor
rm -f rolldown-%{rolldown_version}/rust-toolchain.toml
printf '\n[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' >> rolldown-%{rolldown_version}/.cargo/config.toml
(cd rolldown-%{rolldown_version} && cargo build %{?_smp_mflags} --release --locked --offline -p rolldown_binding)
install -D -m0755 rolldown-%{rolldown_version}/target/release/librolldown_binding.so node_modules/rolldown/$rolldown_dir/rolldown-binding.linux-$napi_arch-gnu.node
# Upstream's cargo config sets cross linkers and nodelete: replace it, pass nodelete
tar xzf %{SOURCE4}
tar -C lightningcss-%{lightningcss_version} --zstd -xf %{SOURCE5} vendor
rm -f lightningcss-%{lightningcss_version}/rust-toolchain.toml
printf '[source.crates-io]\nreplace-with = "vendored-sources"\n[source.vendored-sources]\ndirectory = "vendor"\n' > lightningcss-%{lightningcss_version}/.cargo/config.toml
(cd lightningcss-%{lightningcss_version} && RUSTFLAGS="-C link-args=-Wl,-z,nodelete" cargo build %{?_smp_mflags} --release --locked --offline -p lightningcss_node)
install -D -m0755 lightningcss-%{lightningcss_version}/target/release/liblightningcss_node.so node_modules/lightningcss/lightningcss.linux-$napi_arch-gnu.node
rm -rf rolldown-%{rolldown_version} lightningcss-%{lightningcss_version}
unset CARGO_PROFILE_RELEASE_LTO CARGO_PROFILE_RELEASE_CODEGEN_UNITS
# tauri-build embeds this bundle into the binary.
node node_modules/vite/bin/vite.js build
# The vendored grammars' old tree-sitter array.h has a strict-aliasing bug that corrupts
# the heap on aarch64 (gh#tree-sitter/tree-sitter-haskell#144, fixed in tree-sitter 0.26.4).
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1 CFLAGS=-fno-strict-aliasing
# custom-protocol serves the embedded bundle; the Tauri CLI sets it for release builds.
%cargo_build -- -p openidea --features tauri/custom-protocol
# Separate run so the two fat-LTO links never run at the same time.
%cargo_build -- -p ide-host --bin openidea-server

%install
install -D -m0755 target/release/openidea %{buildroot}%{_bindir}/openidea
install -D -m0755 target/release/openidea-server %{buildroot}%{_bindir}/openidea-server
install -D -m0644 %{SOURCE6} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m0644 src-tauri/icons/32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m0644 src-tauri/icons/128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -m0644 src-tauri/icons/128x128@2x.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -m0644 src-tauri/icons/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -D -m0644 src-tauri/icons/source/openidea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%check
# Workbench-importing tests outrun vitest's 5 s default on a loaded worker.
node node_modules/vitest/vitest.mjs run --testTimeout=60000
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1 CFLAGS=-fno-strict-aliasing
# These exercise the installers openidea-no-tool-installs.patch disables.
skip=
for t in dotnet_tool_install_into_tool_path elixir_ls_needs_elixir_and_lists_its_debugger \
         everything_missing_on_an_empty_system gem_install_wraps_stubs_with_gem_home \
         npm_install_uses_tools_prefix npm_typescript_is_pinned_and_shared \
         python_servers_name_uv_when_it_makes_the_virtualenv \
         release_install_end_to_end_without_network ruby_lsp_installs_into_the_project_ruby_not_a_private_gem_home \
         rust_analyzer_prefers_rustup_and_installs_component \
         rust_analyzer_selects_openvsx_without_rustup rustup_proxy_without_component_is_missing; do
  skip="$skip --skip tests::$t"
done
# Patched crates and editor core only: src-tauri's and ide-host's tests would rebuild the
# GUI stack and backend, and src-tauri's export_bindings rewrites src/bindings.ts.
# One thread: tests exec a script they just wrote, racing forks (ETXTBSY).
%cargo_test -- -p ide-core -p ide-text -p ide-language -p ide-syntax -p ide-search -p ide-spell -p ide-tools -p ide-sdk -p ide-agent -p ide-coverage -p ide-profiler -- --test-threads=1 $skip

%files
%license LICENSE NOTICE THIRD_PARTY_LICENSES.md LICENSE-codemirror-lang-angular
%license crates/ide-spell/src/dict/LICENSE-en_US crates/ide-spell/src/dict/LICENSE-cspell-dicts
%doc README.md
%{_bindir}/openidea
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files server
%license LICENSE NOTICE
%license crates/ide-spell/src/dict/LICENSE-en_US crates/ide-spell/src/dict/LICENSE-cspell-dicts
%{_bindir}/openidea-server

%changelog
