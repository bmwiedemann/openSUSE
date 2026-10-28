#
# spec file for package deckcraft
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


Name:           deckcraft
Version:        0.11.1
Release:        0
Summary:        Native presentation app with slides, shows and an agent API
# Legal-Review-Notice: scope is the two shipped targets (deckcraft, deckcraft-cli)
# built with --package deckcraft --package deckcraft-cli (never the default workspace:
# a deckcraft-web member exists). Upstream code is MIT OR Apache-2.0; the binaries
# additionally embed: the epaint_default_fonts TTFs (Hack-Regular under MIT,
# emoji-icon-font under MIT, NotoEmoji-Regular under OFL-1.1, Ubuntu-Light under
# Ubuntu-font-1.0); MPL-2.0 symphonia audio decoding (used unmodified; upstream
# NOTICE names its source); Unicode-3.0 code via the ICU crates and unicode-ident.
# self_cell 1.3.0 declares Apache-2.0 OR GPL-2.0-only; the build takes the
# Apache-2.0 option, so no GPL obligation is incurred. The in-house H.264, HEVC,
# VP9 and AV1 decoders (crates/h264, hevc, vp9, av1, ported from FilmCraft per the
# workspace Cargo comment) implement patented algorithms; upstream ships them under
# MIT OR Apache-2.0 with no patent grant stated, so legal comfort for the codec
# patents is still open. docs/brand (trademarked, not open source) is excluded
# from the tarball via the tar_scm exclude and is never installed. CRAFT_FONTS_DIR
# stays unset: the fonts build step then embeds nothing and the package carries no
# craft-fonts OFL texts. cargo_vendor runs with update=true (no vendor/ upstream)
# and the vendor-tree copyleft audit is recorded in the .changes entry.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/deckcraft
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
BuildRequires:  pkgconfig
# cpal slide-show sound links libasound (README: alsa-lib-devel on Fedora).
BuildRequires:  pkgconfig(alsa)
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
Recommends:     deckcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
DeckCraft is an open-source, native presentation app: themes, layouts,
shapes, pictures, tables, charts, transitions and animations. It opens and
saves PowerPoint (.pptx) files and presents them full screen with a
presenter view. Every action is also a command that the command line and
AI agents (through MCP) can drive.

This package provides the desktop application; the companion deckcraft-cli
subpackage provides the headless renderer, converter and command server.

%package -n deckcraft-cli
Summary:        Headless DeckCraft renderer, converter and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n deckcraft-cli
Headless DeckCraft: render and convert decks, run engine commands, inspect
documents, and serve commands over stdio with an MCP server for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream's package.sh builds these two workspace members by hand (the default
# workspace also builds deckcraft-web, which is not shipped). CRAFT_FONTS_DIR
# stays unset: the fonts build step then embeds nothing and falls back to
# system fonts.
%{cargo_build} --locked -p deckcraft -p deckcraft-cli

%install
install -Dm0755 target/release/deckcraft %{buildroot}%{_bindir}/deckcraft
install -Dm0755 target/release/deckcraft-cli %{buildroot}%{_bindir}/deckcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.deckcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.deckcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.deckcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.deckcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.11.1, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.deckcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.deckcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.deckcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.deckcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.deckcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Media codec unit tests (committed fixtures only, no network) covering the
# in-house H.264/HEVC/VP9/AV1 decoders and the symphonia audio path.
%{cargo_test} --locked -p deckcraft-media
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/deckcraft --version
%{buildroot}%{_bindir}/deckcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.deckcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.deckcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/deckcraft
%{_datadir}/applications/ai.storyteller.deckcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.deckcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.deckcraft.xml

%files -n deckcraft-cli
%{_bindir}/deckcraft-cli

%changelog
