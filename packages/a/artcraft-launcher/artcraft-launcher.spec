#
# spec file for package artcraft-launcher
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


Name:           artcraft-launcher
Version:        0.8.1
Release:        0
Summary:        Install, update and launch the Craft App Suite
# Legal-Review-Notice: scope is the one shipped target (artcraft-launcher,
# the desktop app; the wasm web app is never built). Upstream code is
# MIT OR Apache-2.0; the binary additionally embeds: OFL-1.1 fonts
# (assets/fonts, Inter/Archivo/GeistMono variable TTFs) and, via eframe
# default_fonts, the Ubuntu Light font under Ubuntu-font-1.0
# (epaint_default_fonts); the CC-BY-4.0 LinkedIn logo (Font Awesome,
# assets/social/linkedin.svg) and CC0-1.0 social icons (Simple Icons,
# assets/social) with their trademarked logos used only as links to
# ArtCraft's own accounts; MIT OR Apache-2.0 suite icons
# (assets/app-icons, copied unmodified from each Craft app's repo);
# MPL-2.0 code via option-ext 0.2.0 (linked through dirs 6 / dirs-sys 0.5,
# used for home/config/data dir lookup on Linux); Unicode-3.0 code via the
# ICU crates and unicode-ident; ISC code via ring, libloading,
# rustls-webpki and untrusted; BSD-2-Clause (arrayref, zerocopy) and
# BSD-3-Clause (moxcms, pxfm, tiny-skia, subtle) code; Zlib code via
# bytemuck, miniz_oxide, foldhash and the eframe/winit windowing stack;
# and Unlicense code via ksni 0.3.7 (the Linux tray-icon backend, which
# talks StatusNotifierItem D-Bus directly, so no GTK/libappindicator is
# needed). MIT-only crates (bytes, calloop, wayland-*, x11-*) are covered
# by the MIT option. self_cell 1.3.0 declares Apache-2.0 OR GPL-2.0-only;
# the build takes the Apache-2.0 option, so no GPL obligation is incurred.
# docs/brand (the ArtCraft name, logo and "A" mark, trademarked, NOT
# MIT/Apache per upstream AGENTS.md and docs/brand/LICENSE-brand.txt) is
# present in the source tarball unmodified because the build needs it:
# crates/ui-egui/src/icons.rs and apps/artcraft-launcher/src/tray.rs embed
# five of its files at compile time (include_image!/include_bytes!), so a
# tar_scm exclude breaks %build on every arch. Nothing from it is ever
# installed. The installed hicolor app icon is that same "A" mark rendered unmodified
# by upstream packaging/icons.sh for use as this app's own icon
# (assets/app-icon/LICENSE.txt permits it unmodified as part of this
# repository and ArtCraft Launcher); forks must remove it. No webpki-roots
# or webpki-root-certs crate is linked (native/Cargo.toml documents their
# CDLA license as the reason): TLS verifies against the OS trust store via
# rustls-platform-verifier. Vendor-tree copyleft audit is recorded in the
# .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Unlicense AND Zlib
URL:            https://github.com/storytold/craft-launcher
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM artcraft-launcher-pkcon-first.patch -- Linux install/update/remove through PackageKit when the distro carries the app (storytold/craft-launcher#256, open): pkcon-first with download-flow fallback, OCR-reviewed
Patch0:         artcraft-launcher-pkcon-first.patch
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
# X11/Wayland client libs for the desktop GUI (eframe/winit).
Requires:       libX11-xcb.so.1()(64bit)
Requires:       libX11.so.6()(64bit)
Requires:       libXcursor.so.1()(64bit)
Requires:       libXi.so.6()(64bit)
Requires:       libwayland-client.so.0()(64bit)
Requires:       libxcb.so.1()(64bit)
Requires:       libxkbcommon-x11.so.0()(64bit)
Requires:       libxkbcommon.so.0()(64bit)
# The PackageKit path needs PackageKit's console client; without it the
# launcher transparently uses its download flow, so this stays weak.
Recommends:     PackageKit
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
ArtCraft Launcher lists every app in the Craft App Suite (PhotoCraft,
LightCraft, FilmCraft, DesignCraft, VectorCraft, PdfCraft, EffectCraft,
WordCraft, DeckCraft, GridCraft, CADCraft and SoundCraft), installs the
right build for your computer, and keeps it up to date.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Build only the desktop app; the web app (apps/artcraft-launcher-web) is
# wasm-only and out of scope for this package.
%{cargo_build} --locked -p artcraft-launcher

%install
install -Dm0755 target/release/artcraft-launcher %{buildroot}%{_bindir}/artcraft-launcher
install -Dm0644 packaging/linux/ai.storyteller.artcraft-launcher.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.artcraft-launcher.desktop
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.8.1, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.artcraft-launcher.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.artcraft-launcher.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.artcraft-launcher</icon>|<icon type="cached" width="64" height="64">ai.storyteller.artcraft-launcher.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.artcraft-launcher.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Core unit tests (release/version/catalog parsing, synthetic data only,
# no network) for the shipped binary's logic.
%{cargo_test} --locked -p artcraft-launcher-core
# The binary exits before any window or GPU init on --version.
%{buildroot}%{_bindir}/artcraft-launcher --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.artcraft-launcher.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.artcraft-launcher.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license assets/fonts/OFL-Archivo.txt
%license assets/fonts/OFL-GeistMono.txt
%license assets/fonts/OFL-Inter.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/artcraft-launcher
%{_datadir}/applications/ai.storyteller.artcraft-launcher.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.artcraft-launcher.metainfo.xml

%changelog
