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
# Upstream is MIT. The Rust vendor closure links MPL-2.0 crates
# (cssparser/selectors) and the npm closure ships BlueOak/CC-BY/WTFPL
# bits; see Legal-Review-Notice for the derivation.
# Legal-Review-Notice: preliminary union for 1.0.1 staging. Rust side
# scanned over vendor-crates/ Cargo.toml license fields (621 crates,
# MPL-2.0 via cssparser-0.29/0.36/0.37 + selectors, Unicode-3.0,
# Zlib, Unlicense; CDLA-Permissive-2.0 present in tree, scoping to
# -p codenomad-tauri via cargo tree pending first green build).
# npm side scanned over the 1320 registry entries in
# package-lock.json (MIT 952, ISC 147, Apache-2.0 95, BlueOak 57,
# BSD-3/2, CC-BY-3.0/4.0, CC0-1.0, 0BSD, Python-2.0, WTFPL, AFL-2.1
# OR BSD-3-Clause, MPL-2.0; LGPL-3.0-or-later only in sharp-libvips
# platform shims, kept here until the staged server closure proves
# them unshipped). Re-derive both trees on every bump.
License:        MIT AND Apache-2.0 AND ISC AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0 AND 0BSD AND MPL-2.0 AND Unicode-3.0 AND Zlib AND Unlicense AND Python-2.0 AND WTFPL AND AFL-2.1 AND CDLA-Permissive-2.0 AND LGPL-3.0-or-later
URL:            https://github.com/NeuralNomadsAI/CodeNomad
Source0:        %{name}-%{version}.tar.gz
# Rust vendor tree. Produced with the OBS cargo_vendor backend against
# packages/tauri-app with update=false (respect upstream Cargo.lock)
# and tag=crates (upstream already ships vendor/ with the tao +
# tauri-plugin-updater forks selected via [patch.crates-io]):
# /usr/lib/obs/service/cargo_vendor --src CodeNomad-1.0.1/packages/tauri-app --outdir vendor-out --compression zst --tag crates --update false
Source1:        vendor-crates.tar.zst
# npm lockfile for the node_modules service (Source10). Upstream's
# lockfileVersion-3 file cannot be fed verbatim: the service aborts on
# the 5 workspace "link" entries and the 8 "packages/*" workspace keys.
# This file drops the links and workspace definitions but re-keys the 3
# nested workspace deps (packages/<ws>/node_modules/...) as
# node_modules/__ws-<ws>__/... so their tarballs still land in the
# obscpio (e.g. electron-app's app-builder-bin 4.2.0 beside the top
# 4.0.0). Regenerate with the same transform, then manualrun.
Source10:       package-lock.json
Source11:       node_modules.spec.inc
# Checksums for the registry tarballs in node_modules.obscpio (service output).
Source12:       node_modules.sums
# PATCH-FIX-OPENSUSE codenomad-system-node.patch: use system Node.js.
Patch0:         %{name}-system-node.patch
# PATCH-FIX-OPENSUSE codenomad-no-opencode-download.patch: no runtime npm.
Patch1:         %{name}-no-opencode-download.patch
# PATCH-FIX-OPENSUSE codenomad-offline-server-staging.patch: staging install.
Patch2:         %{name}-offline-server-staging.patch
# PATCH-FIX-OPENSUSE codenomad-no-ui-update.patch: no UI self-update.
Patch3:         %{name}-no-ui-update.patch
BuildRequires:  cargo-packaging
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  nodejs24
BuildRequires:  npm
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rust >= 1.85
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Requires:       nodejs24 >= 24.20
Requires:       opencode >= 2.1.2
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
# Desktop entry + icons (declared in tauri.conf.json for deb/rpm).
# Upstream's file points at the wrong binary name, hides itself and
# has no category; fix all three for a visible menu entry.
install -D -m0644 packages/tauri-app/src-tauri/icons/linux/ai.neuralnomads.codenomad.client.desktop %{buildroot}%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
sed -i -e 's/^Exec=.*/Exec=codenomad/' -e '/^NoDisplay=/d' -e 's/^Categories=.*$/Categories=Development;IDE;/' -e 's/^StartupWMClass=.*/StartupWMClass=codenomad/' %{buildroot}%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
for s in 32 48 64 128 256 512; do
  install -D -m0644 packages/tauri-app/src-tauri/icons/linux/${s}x${s}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/codenomad-tauri.png
done

%files
%license LICENSE
%doc README.md
%{_bindir}/codenomad
%{_prefix}/lib/%{name}/
%{_datadir}/applications/ai.neuralnomads.codenomad.client.desktop
%{_datadir}/icons/hicolor/*/apps/codenomad-tauri.png

%changelog
