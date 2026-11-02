#
# spec file for package texturecraft
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


Name:           texturecraft
Version:        0.2.0
Release:        0
Summary:        Paint PBR textures directly on 3D meshes
# Legal-Review-Notice: scope is the two shipped targets (texturecraft,
# texturecraft-cli); apps/texturecraft-web (wasm) and xtask are not built.
# Upstream code and the zebra app icon (assets/app-icon/LICENSE.txt) are
# MIT OR Apache-2.0. The desktop binary additionally embeds the Phosphor
# icon font (MIT, vendor/egui-phosphor; upstream ships no notice for it, so
# its licence text is Source2, the LICENSE of phosphor-icons/web v2.1.1,
# whose fonts are byte-identical to the embedded ones) and, via eframe
# default_fonts (epaint_default_fonts), Ubuntu Light (Ubuntu-font-1.0), Hack
# (MIT, with Bitstream Vera glyphs under Bitstream-Vera) and egui-icons, a
# five-glyph subset of emoji-icon-font (MIT); monochrome_emoji_fonts is off,
# so Noto Emoji is not embedded. LGPL-2.1-or-later:
# winit links the bindings wayland-protocols-plasma (declared MIT) generates
# from KDE's blur.xml protocol (LGPL-2.1-or-later); the source ships in the
# src.rpm. Unicode-3.0 comes from the ICU crates and the CLDR-derived
# craft-i18n data; BSD-3-Clause from exr and lebe; ISC from libloading;
# Zlib from foldhash. self_cell 1.3.0 declares Apache-2.0 OR GPL-2.0-only;
# the build takes the Apache-2.0 option, so no GPL obligation is incurred.
# moxcms and pxfm (BSD-3-Clause OR Apache-2.0) are taken under Apache-2.0;
# crates offering Unlicense, 0BSD, Zlib, BSD-2-Clause or LLVM-exception
# beside MIT/Apache-2.0 are taken under their MIT/Apache-2.0 options.
# texturecraft-cli links no font, icon, ICU or windowing crate, hence its
# narrower tag (its Unicode-3.0 is unicode-ident, via naga). No ArtCraft
# brand asset is shipped or embedded: docs/brand (trademarked, not open
# source) is excluded from the tarball via the tar_scm exclude.
# CRAFT_FONTS_DIR stays unset, so no craft-fonts faces are embedded. The
# vendor-tree copyleft audit is recorded in the .changes entry of each
# re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND Bitstream-Vera AND ISC AND LGPL-2.1-or-later AND MIT AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/texturecraft
Source0:        %{name}-%{version}.tar.zst
# Vendored with cargo_vendor filter=true (crates no Linux target uses are
# emptied) into vendor-texturecraft/, as upstream's own vendor/ holds the
# patched egui-phosphor path dependency. Nothing in the dependency graph
# carries a prebuilt object for Linux (no ring, aws-lc or wasm tooling), so
# no strip is needed; check again after every re-vendor. The prebuilt files
# left are test fixtures:
# Source-Binary-Exception: vendor-texturecraft.tar.zst:vendor-texturecraft/libloading-*/tests/*.dll -- test-data: fixtures loaded only by libloading's own cfg(windows) tests, never built or run here
Source1:        vendor-texturecraft.tar.zst
# MIT licence of the Phosphor icon font egui-phosphor embeds: its
# Phosphor.ttf and Phosphor-Fill.ttf are byte-identical to those of
# phosphor-icons/web v2.1.1, the earliest release that ships them.
Source2:        https://raw.githubusercontent.com/phosphor-icons/web/v2.1.1/LICENSE#/LICENSE-phosphor.txt
# PATCH-FIX-OPENSUSE texturecraft-control-token-0600.patch -- write the
# --control token owner-only (0600), like the CLI does.
Patch0:         texturecraft-control-token-0600.patch
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
# Floor follows the workspace rust-version (1.95).
BuildRequires:  cargo >= 1.95
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
# Owns the hicolor icon directories for the filelist checker.
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
# wgpu's Vulkan backend dlopens libvulkan (ash); its GLES fallback libEGL.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
# winit dlopens Xlib-xcb to hand the Xlib display to x11rb (x11-dl).
Requires:       libX11-xcb.so.1()(64bit)
# winit's X11 backend dlopens Xlib (x11-dl).
Requires:       libX11.so.6()(64bit)
# winit dlopens Xcursor for X11 cursor themes (x11-dl).
Requires:       libXcursor.so.1()(64bit)
# winit dlopens XInput2 for X11 pointer and tablet input (x11-dl).
Requires:       libXi.so.6()(64bit)
# rfd's XDG portal backend dlopens libdbus for the open/save dialogs.
Requires:       libdbus-1.so.3()(64bit)
# winit's Wayland backend dlopens libwayland-client (wayland-sys).
Requires:       libwayland-client.so.0()(64bit)
# x11rb dlopens libxcb for the X11 protocol (dl-libxcb).
Requires:       libxcb.so.1()(64bit)
# winit dlopens xkbcommon-x11 for X11 keymaps (xkbcommon-dl).
Requires:       libxkbcommon-x11.so.0()(64bit)
# winit dlopens xkbcommon for keyboard layouts (xkbcommon-dl).
Requires:       libxkbcommon.so.0()(64bit)
# wgpu's GLES fallback on Wayland dlopens libwayland-egl.
Recommends:     libwayland-egl.so.1()(64bit)
# The headless CLI scripts the same engine and serves it to MCP agents.
Recommends:     texturecraft-cli
# Open/save dialogs go through the XDG file chooser portal (rfd xdg-portal).
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
TextureCraft is an open-source, native 3D texture painter: texture sets,
layers, masks, fills, filters, smart materials and effects painted
straight onto the model, with familiar menus, shortcuts and panels.

It opens glTF/GLB, FBX, COLLADA, USD (USDA/USDC/USDZ), Alembic, OBJ, PLY
and STL meshes, paints base colour, roughness, metallic, normal and
height together, bakes mesh maps, path traces previews and exports
texture sets as PNG, EXR, TGA, JPEG or TIFF with engine presets.

This package provides the desktop application; the companion
texturecraft-cli subpackage provides the headless command line, MCP
server and JSON-lines server.

%package -n texturecraft-cli
Summary:        Headless TextureCraft command line and MCP server
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND ISC AND MIT AND Unicode-3.0 AND Zlib
# render dlopens Vulkan or EGL through wgpu; no other subcommand needs a GPU.
Recommends:     (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))

%description -n texturecraft-cli
Headless TextureCraft: inspect projects, run and batch engine commands,
bake mesh maps, export texture sets and render previews from the command
line, plus an opt-in MCP server over stdio for AI agents and a JSON-lines
server on stdio or a token-protected loopback port. It needs no window.

%prep
%autosetup -a1 -p1
cp %{SOURCE2} .
# The crate ships UFL.txt executable; it is installed as a licence text.
chmod a-x vendor-texturecraft/epaint_default_fonts-*/fonts/*.txt

%build
%limit_build -m 2000
# Upstream has no cargo install story; packaging/linux/package.sh builds
# these two workspace members by hand (apps/texturecraft-web is wasm and
# xtask a developer tool; neither is built here). CRAFT_FONTS_DIR stays
# unset: the build then embeds only the Phosphor icon font and the eframe
# default fonts.
%cargo_build -- --locked -p texturecraft -p texturecraft-cli

%install
install -Dm0755 target/release/texturecraft %{buildroot}%{_bindir}/texturecraft
install -Dm0755 target/release/texturecraft-cli %{buildroot}%{_bindir}/texturecraft-cli
install -Dm0644 packaging/linux/ai.storyteller.texturecraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.texturecraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.texturecraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.texturecraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.2.0, 2026-11-01): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the percent-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-11-01/g" packaging/linux/ai.storyteller.texturecraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.texturecraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.texturecraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.texturecraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.texturecraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Engine unit tests (synthetic data only, no corpus, network or GPU), plus
# the automation crate behind the CLI's MCP and JSON-lines servers: its
# workspace-root confinement and agent-task tests run headless, over
# loopback only, and skip the one render step when there is no GPU.
%cargo_test -- --locked -p texturecraft-core -p texturecraft-texel -p texturecraft-geom -p texturecraft-compose -p texturecraft-bake -p texturecraft-formats -p texturecraft-paint -p texturecraft-engine -p texturecraft-automation
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/texturecraft --version
%{buildroot}%{_bindir}/texturecraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.texturecraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.texturecraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
# Licences of the eframe default fonts and the Phosphor icon font
# embedded in the binary.
%license vendor-texturecraft/epaint_default_fonts-*/fonts/Hack-Regular.txt
%license vendor-texturecraft/epaint_default_fonts-*/fonts/UFL.txt
%license vendor-texturecraft/epaint_default_fonts-*/fonts/egui-icons.txt
%license vendor-texturecraft/epaint_default_fonts-*/fonts/emoji-icon-font-mit-license.txt
%license LICENSE-phosphor.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/texturecraft
%{_datadir}/applications/ai.storyteller.texturecraft.desktop
%{_datadir}/icons/hicolor/*/apps/ai.storyteller.texturecraft.*
%{_datadir}/metainfo/ai.storyteller.texturecraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.texturecraft.xml

%files -n texturecraft-cli
%license LICENSE-APACHE
%license LICENSE-MIT
# The protocol reference the CLI's help points to.
%doc docs/control-protocol.md
%{_bindir}/texturecraft-cli

%changelog
