#
# spec file for package lightcraft
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


Name:           lightcraft
Version:        0.13.0
Release:        0
Summary:        Photo library and raw developer
# Legal-Review-Notice: scope is the two shipped targets (lightcraft, lightcraft-cli)
# built with --features heif. Upstream code is MIT OR Apache-2.0, except the
# Apache-2.0-only crates lightcraft-segment (SAM 3 port) and lightcraft-fetch
# (model downloads); the binaries take the Apache-2.0 option there. The binaries
# additionally embed: OFL-1.1 Inter fonts (assets/fonts); via eframe default_fonts,
# the Ubuntu Light font under Ubuntu-font-1.0 (epaint_default_fonts); IJG-licensed
# code via jpeg-encoder; Unicode-3.0 code via the ICU crates; CC0-1.0 code via
# imgref (AVIF path); the Mozilla CA bundle via webpki-roots under
# CDLA-Permissive-2.0 (model downloads over HTTPS); plus MIT/BSD-2-Clause/
# BSD-3-Clause/ISC/Zlib permissive crates. self_cell 1.3.0 declares
# Apache-2.0 OR GPL-2.0-only; the build takes the Apache-2.0 option, so no GPL
# obligation is incurred. docs/brand (trademarked, not open source) is excluded
# from the tarball via the tar_scm exclude and is never installed. The heif
# feature pulls in only the pure-Rust heic-rs 0.1.4 crate (no C, no system
# library); HEVC patent comfort is still open -- this discloses the feature, it
# does not block it (distributor's call, same policy as PhotoCraft). SAM 3 /
# denoise model weights are never shipped; the rawnind-model feature (GPL-3.0
# checkpoint download offer) is not enabled. Vendor-tree copyleft audit is
# recorded in the .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND IJG AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/lightcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
BuildRequires:  cargo >= 1.90
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
# eframe/wgpu GUI runtime: Vulkan/EGL for compositing, X11/Wayland/xkbcommon
# for windowing; hicolor-icon-theme owns the installed icon dirs.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
Requires:       hicolor-icon-theme
Requires:       libX11-xcb.so.1()(64bit)
Requires:       libX11.so.6()(64bit)
Requires:       libXcursor.so.1()(64bit)
Requires:       libXi.so.6()(64bit)
Requires:       libwayland-client.so.0()(64bit)
Requires:       libxcb.so.1()(64bit)
Requires:       libxkbcommon-x11.so.0()(64bit)
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     lightcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
LightCraft is an open-source photo library and raw developer. Organise photos
and develop raw files non-destructively. This package provides the desktop
application; the companion lightcraft-cli subpackage provides the headless
renderer, command runner and opt-in MCP server.

%package -n lightcraft-cli
Summary:        Headless LightCraft command runner and MCP server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND IJG AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n lightcraft-cli
Headless LightCraft renderer and command runner: develop and export photos
from scripts and CI, plus an opt-in MCP server for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream has no `cargo install` story; package.sh builds these two workspace
# members by hand. heif matches the official builds (pure-Rust heic-rs, no
# system library). CRAFT_FONTS_DIR stays unset: the build then uses the
# bundled Inter plus the system CJK fallback.
%{cargo_build} --locked -p lightcraft -p lightcraft-cli --features heif

%install
install -Dm0755 target/release/lightcraft %{buildroot}%{_bindir}/lightcraft
install -Dm0755 target/release/lightcraft-cli %{buildroot}%{_bindir}/lightcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.lightcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.lightcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.lightcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.lightcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.13.0, 2026-10-23): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-23/g" packaging/linux/ai.storyteller.lightcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.lightcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.lightcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.lightcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.lightcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 README.md NOTICE LICENSE-MIT LICENSE-APACHE %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/fonts/OFL-*.txt %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/ATTRIBUTION.md %{buildroot}%{_docdir}/%{name}/
install -d -m 0755 %{buildroot}%{_docdir}/lightcraft-cli
ln -s ../lightcraft/README.md %{buildroot}%{_docdir}/lightcraft-cli/README.md
ln -s ../lightcraft/NOTICE %{buildroot}%{_docdir}/lightcraft-cli/NOTICE
ln -s ../lightcraft/ATTRIBUTION.md %{buildroot}%{_docdir}/lightcraft-cli/ATTRIBUTION.md

%check
# Codec unit tests (synthetic data only, no corpus or network) with the same
# feature set as the shipped binaries.
%{cargo_test} --locked -p lightcraft-codecs --features heif
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/lightcraft --version
%{buildroot}%{_bindir}/lightcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.lightcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.lightcraft.metainfo.xml

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE-APACHE
%license %{_docdir}/%{name}/LICENSE-MIT
%license %{_docdir}/%{name}/OFL-*.txt
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/NOTICE
%doc %{_docdir}/%{name}/ATTRIBUTION.md
%{_bindir}/lightcraft
%{_datadir}/applications/ai.storyteller.lightcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.lightcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.lightcraft.xml

%files -n lightcraft-cli
%{_bindir}/lightcraft-cli
%dir %{_docdir}/lightcraft-cli
%{_docdir}/lightcraft-cli/*

%changelog
