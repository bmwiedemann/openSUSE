#
# spec file for package photocraft
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


Name:           photocraft
Version:        0.14.0
Release:        0
Summary:        Native image editor with layers, masks, type and PSD support
# Legal-Review-Notice: scope is the two shipped targets (photocraft, photocraft-cli)
# built with --features heif. Upstream code is MIT OR Apache-2.0; the binaries
# additionally embed: OFL-1.1 fonts (assets/fonts) and, via eframe default_fonts,
# the Ubuntu Light font under Ubuntu-font-1.0 (epaint_default_fonts); ISC Lucide
# icons (assets/icons); the CC-BY-3.0 Magnetic-Lasso glyph
# (assets/icons/lasso-magnetic.svg, attribution in ATTRIBUTION.md shipped as
# documentation); the CC0-1.0 synthetic ICC profile (crates/cms/profiles); IJG-licensed
# code via jpeg-encoder; Unicode-3.0 code via the ICU crates; and the SCOWL word
# list (assets/dict, custom permissive license without SPDX id, text shipped as
# a license file). MIT-licensed embeds (Feather-derived icons, Solarized palette) are
# covered by the MIT option. self_cell 1.3.0 declares Apache-2.0 OR GPL-2.0-only;
# the build takes the Apache-2.0 option, so no GPL obligation is incurred.
# docs/brand (trademarked, not open source) is excluded from the tarball via the
# tar_scm exclude and is never installed. The heif feature pulls in only the
# pure-Rust heic-rs crate (forbid(unsafe_code), no C, no system library);
# vendor-tree copyleft audit is recorded in the .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-3.0 AND CC0-1.0 AND IJG AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/photocraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
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
Recommends:     mesa-vulkan-drivers
Recommends:     photocraft-cli
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
PhotoCraft is an open-source, native image editor with layers, masks,
adjustment layers, layer styles, type and brushes. It opens, edits and
saves layered PSD and PSB files and 8/16/32-bit documents, composited on
the GPU.

This package provides the desktop application; the companion photocraft-cli
subpackage provides the headless converter, batch runner and command server.

%package -n photocraft-cli
Summary:        Headless PhotoCraft converter, batch runner and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-3.0 AND CC0-1.0 AND IJG AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n photocraft-cli
Headless PhotoCraft: convert and inspect documents, run engine commands,
apply batch action lists and droplets, and serve commands over stdio/TCP
with an opt-in MCP server for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream has no `cargo install` story; package.sh builds these two workspace
# members by hand. heif matches the official builds (pure-Rust heic-rs, no
# system library). CRAFT_FONTS_DIR stays unset: the build then uses the
# bundled Inter/JetBrains Mono plus the system CJK fallback.
%{cargo_build} --locked -p photocraft -p photocraft-cli --features heif

%install
install -Dm0755 target/release/photocraft %{buildroot}%{_bindir}/photocraft
install -Dm0755 target/release/photocraft-cli %{buildroot}%{_bindir}/photocraft-cli
install -Dm0644 packaging/linux/ai.storyteller.photocraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.photocraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.photocraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.photocraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.14.0, 2026-10-23): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-23/g" packaging/linux/ai.storyteller.photocraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.photocraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.photocraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.photocraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.photocraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Codec unit tests (synthetic data only, no corpus or network) with the same
# feature set as the shipped binaries.
%{cargo_test} --locked -p photocraft-codecs --features heif
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/photocraft --version
%{buildroot}%{_bindir}/photocraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.photocraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.photocraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license assets/dict/LICENSE-SCOWL.txt
%license assets/fonts/OFL-Inter.txt
%license assets/fonts/OFL-JetBrainsMono.txt
%license assets/icons/LICENSE-lucide.txt
%license assets/icons/LICENSE-noun-magnetic-lasso.txt
%license assets/icons/LICENSE-symmetry-axes.txt
%license crates/ui-egui/src/LICENSE-solarized.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/photocraft
%{_datadir}/applications/ai.storyteller.photocraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.photocraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.photocraft.xml

%files -n photocraft-cli
%{_bindir}/photocraft-cli

%changelog
