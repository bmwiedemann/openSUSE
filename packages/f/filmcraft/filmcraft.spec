#
# spec file for package filmcraft
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


Name:           filmcraft
Version:        0.12.0
Release:        0
Summary:        Timeline video editor written in pure Rust
# Legal-Review-Notice: scope is the two shipped binaries (filmcraft in
# the main package, filmcraft-cli in the -cli subpackage) built with
# default features. Upstream code is
# MIT OR Apache-2.0; both binaries additionally embed: MPL-2.0 audio
# decoders via symphonia 0.5.5 (MP3/FLAC/ALAC/Vorbis/AAC interim,
# used unmodified; vendor.tar.zst ships in the src.rpm); OFL-1.1
# fonts embedded via include_bytes (assets/fonts: Inter, JetBrains
# Mono, Noto Serif, via filmcraft-text for export burn-in, so in both
# binaries) and via eframe default_fonts (Ubuntu-font-1.0, desktop
# binary only, but kept on both tags per policy);
# ISC libloading (VA-API dlopen); Unicode-3.0 via unicode-ident;
# Zlib via miniz_oxide/bytemuck. self_cell 1.3.0 declares
# Apache-2.0 OR GPL-2.0-only; the build takes the Apache-2.0 option,
# so no GPL obligation is incurred. docs/brand (trademarked, not open
# source) is excluded from the tarball via the tar_scm exclude and is
# never installed; brand.rs is patched to the open-source app tile.
# The whisper feature (candle/ureq) stays off; VA-API (filmcraft-platform)
# dlopens libva at runtime, so no libva BuildRequires; FFmpeg appears
# only as an external test oracle, never linked.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/filmcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE filmcraft-no-brand-assets.patch -- replace trademarked
# ArtCraft marks (docs/brand/, NOT open source) embedded via include_bytes!
# with the open-source FilmCraft tile; permanent downstream carry, not
# upstreamable (upstream ships the marks intentionally).
Patch0:         filmcraft-no-brand-assets.patch
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
BuildRequires:  cargo >= 1.95
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
# cpal links ALSA on Linux; Vulkan/EGL/X11/Wayland are dlopened at runtime.
BuildRequires:  pkgconfig(alsa)
# eframe/wgpu needs Vulkan or EGL at runtime; mesa provides Vulkan in a VM.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
# Desktop runtime: hicolor base dirs own the installed icon tree.
Requires:       hicolor-icon-theme
# eframe/winit with x11+wayland features needs the X11/Wayland client
# libs and xkbcommon at runtime; the headless -cli subpackage below
# ships none of these.
Requires:       libX11-xcb.so.1()(64bit)
Requires:       libX11.so.6()(64bit)
Requires:       libXcursor.so.1()(64bit)
Requires:       libXi.so.6()(64bit)
Requires:       libwayland-client.so.0()(64bit)
Requires:       libxcb.so.1()(64bit)
Requires:       libxkbcommon-x11.so.0()(64bit)
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     filmcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
FilmCraft is an open-source, clean-room timeline video editor built in
pure Rust: edit video, color and sound with its own H.264/HEVC/ProRes/
AAC/VP9/Opus/AV1 codecs and export. This package provides the desktop
application; the companion filmcraft-cli subpackage provides the
headless exporter and command runner.

%package -n filmcraft-cli
Summary:        Headless FilmCraft exporter and command runner
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n filmcraft-cli
Headless FilmCraft exporter and command runner: export sequences,
inspect projects and run engine commands from scripts and CI without
the desktop.

%prep
%autosetup -a1 -p1
# Trademarked ArtCraft marks must never ship: belt-and-braces removal even
# though tar_scm already excludes docs/brand from the tarball.
rm -rf docs/brand

%build
%limit_build -m 2000
# Upstream has no `cargo install` story; package.sh builds these two workspace
# members by hand. Default features: whisper (candle) stays off and
# CRAFT_FONTS_DIR stays unset (bundled Inter/JetBrains Mono/Noto Serif plus
# the system CJK fallback). Cargo.lock is committed upstream.
%{cargo_build} --locked -p filmcraft -p filmcraft-cli

%install
install -Dm0755 target/release/filmcraft %{buildroot}%{_bindir}/filmcraft
install -Dm0755 target/release/filmcraft-cli %{buildroot}%{_bindir}/filmcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.filmcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.filmcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.filmcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.filmcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.12.0, 2026-10-23): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner would brace
# the date-format placeholders as RPM macros, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-23/g" packaging/linux/ai.storyteller.filmcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.filmcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.filmcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.filmcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.filmcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 NOTICE %{buildroot}%{_docdir}/%{name}/
install -m 0644 ATTRIBUTION.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 LICENSE-MIT LICENSE-APACHE %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/fonts/OFL-*.txt %{buildroot}%{_docdir}/%{name}/
install -d -m 0755 %{buildroot}%{_docdir}/filmcraft-cli
ln -s ../filmcraft/README.md %{buildroot}%{_docdir}/filmcraft-cli/README.md
ln -s ../filmcraft/NOTICE %{buildroot}%{_docdir}/filmcraft-cli/NOTICE
ln -s ../filmcraft/ATTRIBUTION.md %{buildroot}%{_docdir}/filmcraft-cli/ATTRIBUTION.md

%check
# Codec unit tests (synthetic vectors only, no corpus or network) with the
# same feature set as the shipped binaries; FFmpeg oracle tests skip when
# no ffmpeg binary is present, so no ffmpeg BuildRequires.
%{cargo_test} --locked -p filmcraft-codecs
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/filmcraft --version
%{buildroot}%{_bindir}/filmcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.filmcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.filmcraft.metainfo.xml

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE-APACHE
%license %{_docdir}/%{name}/LICENSE-MIT
%license %{_docdir}/%{name}/OFL-Inter.txt
%license %{_docdir}/%{name}/OFL-JetBrainsMono.txt
%license %{_docdir}/%{name}/OFL-NotoSerif.txt
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/NOTICE
%doc %{_docdir}/%{name}/ATTRIBUTION.md
%{_bindir}/filmcraft
%{_datadir}/applications/ai.storyteller.filmcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.filmcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.filmcraft.xml

%files -n filmcraft-cli
%{_bindir}/filmcraft-cli
%dir %{_docdir}/filmcraft-cli
%{_docdir}/filmcraft-cli/*

%changelog
