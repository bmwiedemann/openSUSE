#
# spec file for package soundcraft
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


Name:           soundcraft
Version:        0.13.1
Release:        0
Summary:        Native digital audio workstation with multitrack editing and mixing
# Legal-Review-Notice: scope is the two shipped targets (soundcraft, soundcraft-cli)
# built --package soundcraft --package soundcraft-cli (never the default workspace,
# which also contains the wasm-only soundcraft-web). Upstream code is MIT OR Apache-2.0;
# the binaries additionally embed: MPL-2.0 symphonia audio decoders; Unicode-3.0 code via
# the ICU crates (and unicode-ident); Ubuntu-font-1.0/OFL-1.1 egui default fonts
# (Ubuntu-Light, Noto Emoji; Hack is MIT, covered by the MIT option); ISC libloading;
# Zlib foldhash; BSD-3-Clause encoding_rs. self_cell 1.3.0 declares Apache-2.0 OR
# GPL-2.0-only; the build takes the Apache-2.0 option, so no GPL obligation is incurred.
# docs/brand (trademarked, not open source, see NOTICE) is excluded from the tarball via
# the tar_scm exclude and is never installed. v0.6.1 adds one git dependency,
# craft-ui 0.1.0 (rev 5c874d5, MIT OR Apache-2.0), linked into the soundcraft GUI
# via soundcraft-ui-egui; cargo_vendor vendors it, so nothing is fetched at build
# time. Upstream ships no vendor/ directory, hence cargo_vendor runs with
# update=true. Vendor-tree copyleft audit is recorded in the
# .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/soundcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  c_compiler
BuildRequires:  cargo >= 1.90
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
# Own /usr/share/icons/hicolor for the filelist checker: the runtime
# Requires alone does not satisfy it.
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
# cpal 0.16 links ALSA unconditionally on Linux (non-optional
# target dependency; cargo tree on the shipped targets resolves
# alsa 0.9.1 + alsa-sys 0.3.1). clap-host/vst3-host only dlopen
# plugins (clap-sys, libloading, no link-time system dep) and au-host
# carries no system dependency on Linux.
BuildRequires:  pkgconfig(alsa)
# eframe/wgpu GPU compositor: Vulkan preferred, EGL fallback.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
Requires:       hicolor-icon-theme
# libasound is linked at build time via alsa-sys, so the soname
# dependency is automatic; this commented Requires only documents the
# audio-system dependency proven by cargo tree above.
# Requires:      libasound.so.2()(64bit)
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
Recommends:     soundcraft-cli
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
SoundCraft is an open-source, native digital audio workstation. Record, edit
and mix multitrack audio and MIDI in Edit and Mix windows, with built-in EQ,
dynamics, reverb, delay, modulation and instruments, CLAP/VST3 plugin hosting,
and WAV/AIFF/FLAC/MP3/MIDI import.

This package provides the desktop application; the companion soundcraft-cli
subpackage provides headless editing, conversion, bounce and a command server.

%package -n soundcraft-cli
Summary:        Headless SoundCraft editor, converter and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n soundcraft-cli
Headless SoundCraft: edit sessions, convert and inspect audio, bounce mixes
and serve commands over stdio with an opt-in MCP server for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream's default workspace also contains the wasm-only soundcraft-web and
# the xtask helper; ship only the two native binaries.
%{cargo_build} --locked --package soundcraft --package soundcraft-cli

%install
install -Dm0755 target/release/soundcraft %{buildroot}%{_bindir}/soundcraft
install -Dm0755 target/release/soundcraft-cli %{buildroot}%{_bindir}/soundcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.soundcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.soundcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.soundcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.soundcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.13.1, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.soundcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.soundcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.soundcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Unit tests for the engine and its library crates (synthetic sessions and
# signals only: no soundcard, no network). The GUI (soundcraft, ui-egui) needs
# a display/GPU and soundcraft-web targets wasm, so neither is tested here.
%{cargo_test} --locked -p soundcraft-audio-io -p soundcraft-dsp -p soundcraft-midi -p soundcraft-time -p soundcraft-model -p soundcraft-mix -p soundcraft-automation -p soundcraft-engine -p soundcraft-playback -p soundcraft-clap-host -p soundcraft-vst3-host -p soundcraft-au-host
# Both binaries exit before any window, GPU or audio-device init on --version.
%{buildroot}%{_bindir}/soundcraft --version
%{buildroot}%{_bindir}/soundcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.soundcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/soundcraft
%{_datadir}/applications/ai.storyteller.soundcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.soundcraft.xml

%files -n soundcraft-cli
%{_bindir}/soundcraft-cli

%changelog
