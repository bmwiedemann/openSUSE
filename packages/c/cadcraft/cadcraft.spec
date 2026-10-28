#
# spec file for package cadcraft
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           cadcraft
Version:        0.13.0
Release:        0
Summary:        Open-source CAD and drafting application
# Legal-Review-Notice: scope is the two shipped targets (cadcraft, cadcraft-cli).
# Upstream code is MIT OR Apache-2.0; the binaries additionally embed: MPL-2.0
# acadrust 0.6.5 (DWG reading/writing, used unmodified behind the byte-level
# cadcraft-dwg bridge, non-wasm targets only — see NOTICE); OFL-1.1 and
# Ubuntu-font-1.0 fonts via epaint_default_fonts (eframe default_fonts);
# Unicode-3.0 code via the ICU crates; ISC libloading; BSD-2-Clause arrayref;
# BSD-3-Clause tiny-skia; Zlib foldhash. self_cell 1.3.0 declares
# Apache-2.0 OR GPL-2.0-only; the build takes the Apache-2.0 option, so no GPL
# obligation is incurred. No Autodesk/Adobe/Avid material ships: icons, fonts,
# hatch patterns and linetypes are drawn or defined in code (ATTRIBUTION.md
# shipped as documentation). docs/brand (trademarked, not open source) is
# excluded from the tarball via the tar_scm exclude and is never installed.
# Two rev-pinned git dependencies (craft-ui and craft-docpath from
# storytold/craft-libs, MIT OR Apache-2.0, like upstream code), vendored
# with the rest, so the vendor tree still covers every dependency and
# nothing is fetched at build time;
# vendor-tree copyleft audit is recorded in the .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/cadcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
# Floor follows the highest rust-version in the built crates
# (cadcraft-ui-egui and craft-ui declare 1.95).
BuildRequires:  cargo >= 1.95
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
# Own /usr/share/icons/hicolor for the filelist checker: the runtime
# Requires alone does not satisfy it.
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
# eframe/wgpu GPU compositor: Vulkan preferred, EGL fallback.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
Requires:       hicolor-icon-theme
# X11/Wayland client libs for the desktop GUI only;
# the headless -cli subpackage needs none of these.
Requires:       libX11-xcb.so.1()(64bit)
Requires:       libX11.so.6()(64bit)
Requires:       libXcursor.so.1()(64bit)
Requires:       libXi.so.6()(64bit)
Requires:       libwayland-client.so.0()(64bit)
Requires:       libxcb.so.1()(64bit)
Requires:       libxkbcommon-x11.so.0()(64bit)
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     cadcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
CADCraft is an open-source computer-aided design and drafting application
with a command line, object snaps, layers, dimensions, hatches and blocks.
It opens and saves DXF and DWG drawings, exports SVG and PNG, and can be
driven by AI agents over MCP.

This package provides the desktop application; the companion cadcraft-cli
subpackage provides the headless converter, exporter and command server.

%package -n cadcraft-cli
Summary:        Headless CADCraft converter, exporter and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n cadcraft-cli
Headless CADCraft: inspect and convert drawings, export images, run engine
commands and scripts, and serve commands over stdio/TCP with an MCP server
for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# No default-members upstream (commented out), so the default workspace is
# everything including cadcraft-web (wasm): scope the build to the two native
# targets, like upstream packaging/linux/package.sh does.
%{cargo_build} --locked --package cadcraft --package cadcraft-cli

%install
install -Dm0755 target/release/cadcraft %{buildroot}%{_bindir}/cadcraft
install -Dm0755 target/release/cadcraft-cli %{buildroot}%{_bindir}/cadcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.cadcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.cadcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.cadcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.cadcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.13.0, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.cadcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.cadcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.cadcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.cadcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.cadcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Full workspace unit and integration tests, as upstream CI runs them. All
# headless: engine/crate tests are pure computation on synthetic drawings,
# and the ui-egui tests drive CadApp in-process with egui::Context::default()
# (no eframe window). cadcraft-web carries no tests and its wasm-only
# deps are cfg-gated, so it builds natively.
# 0.7.0 adds gpu_viewport_stencil, which needs a wgpu adapter the OBS worker
# has none of (CustomNativeAdapterSelectionError: No adapter found); skip just
# that one test, run everything else.
%{cargo_test} --locked --workspace -- --skip clipped_viewport_contents_draw_only_inside_their_outline
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/cadcraft --version
%{buildroot}%{_bindir}/cadcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.cadcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.cadcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/cadcraft
%{_datadir}/applications/ai.storyteller.cadcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.cadcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.cadcraft.xml

%files -n cadcraft-cli
%{_bindir}/cadcraft-cli

%changelog
