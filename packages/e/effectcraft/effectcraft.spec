#
# spec file for package effectcraft
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


Name:           effectcraft
Version:        0.17.0
Release:        0
Summary:        Motion graphics and VFX compositor
# Legal-Review-Notice: licence set re-derived from the vendored tree
# (cargo tree -p effectcraft -p effectcraft-cli -e normal, licence field
# of each vendor/<name>-<version>/Cargo.toml). Upstream code is
# MIT OR Apache-2.0; additionally linked: symphonia 0.5.5 (MPL-2.0, via
# filmcraft-codecs -> effectcraft-media -> effectcraft-host, in both
# binaries; MPL-2.0 section 3.2 source is the vendor.tar.zst in the
# src.rpm); BSD-2-Clause arrayref, BSD-3-Clause exr/lebe/tiny-skia(-path),
# ISC libloading, Zlib foldhash and Unicode-3.0 ICU code (all via the
# eframe/wgpu/image stack, choice of the dual/triple-licensed crates'
# MIT or Apache-2.0 option wherever offered); and embedded fonts
# (OFL-1.1: app assets/fonts plus egui's
# epaint_default_fonts; Ubuntu-font-1.0: epaint_default_fonts, pulled in
# by eframe's default_fonts feature). docs/brand/ (ArtCraft marks, NOT
# open source) is excluded from the tarball and its embedded PNG is
# replaced by effectcraft-no-brand-assets.patch, so no brand file ships.
# self_cell is dual Apache-2.0 OR GPL-2.0-only: the Apache-2.0 choice
# applies, no GPL obligation.
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/effectcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         effectcraft-no-brand-assets.patch
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(wayland-client)
# Icon theme scaffolding for the hicolor icons shipped below.
Requires:       hicolor-icon-theme
# Headless companion is optional at runtime but installed by default;
# keep it removable for minimal footprints.
Recommends:     effectcraft-cli
ExclusiveArch:  %{rust_tier1_arches}

%description
EffectCraft is an open-source motion graphics and visual effects
compositor: layers with keyframes and a graph editor, masks and shapes,
text animators, expressions, 3D cameras and lights, effects and a render
queue, with GPU compositing.

This package provides the desktop application; the companion
effectcraft-cli subpackage provides the headless renderer, batch
runner and command server.

%package -n effectcraft-cli
Summary:        Headless EffectCraft renderer, batch runner and command server
# Same licence set as the main package: symphonia MPL-2.0 is linked into
# both binaries (see Legal-Review-Notice above); kept per packaging policy
# (declare License on every subpackage).
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n effectcraft-cli
Headless EffectCraft renderer: batch-render compositions from scripts
and CI, plus a command server for agents, without the desktop GUI.

%prep
%autosetup -p1 -a1

%build
# Big workspace (eframe/wgpu/boa/wasmi/filmcraft): cap jobs by RAM.
%limit_build -m 2000
# Cargo.lock is committed upstream and the vendor tree matches it
# (cargo_vendor update=false); build locked and offline for reproducibility.
%{cargo_build} --locked -p effectcraft -p effectcraft-cli

%install
install -D -m 0755 target/release/effectcraft %{buildroot}%{_bindir}/effectcraft
install -D -m 0755 target/release/effectcraft-cli %{buildroot}%{_bindir}/effectcraft-cli
install -D -m 0644 packaging/linux/ai.storyteller.effectcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.effectcraft.desktop
# Upstream metainfo is a template; stamp the release version and date.
# Fixed release date (v0.17.0, 2026-10-25): a build-time date would differ
# on every rebuild. Upstream declares the app icon as type stock but it
# is a custom hicolor icon, so declare it as cached for validation.
mkdir -p %{buildroot}%{_datadir}/metainfo
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" \
  packaging/linux/ai.storyteller.effectcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.effectcraft.metainfo.xml
sed -i 's|<icon type="stock">ai.storyteller.effectcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.effectcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.effectcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
# Attribution sidecars are source-tree bookkeeping, not runtime files.
find %{buildroot}%{_datadir}/icons -name '*.attribution' -delete
# packaging/linux ships an empty mime stub; nothing to register, so skip it.

%check
# No cargo test: the GPU suite needs a GL device (llvmpipe is absent from
# the build root) and the full workspace suite doubles an already long
# build; upstream CI runs cargo test --workspace. Both binaries print
# their version before any window or GPU init, so smoke-test them here.
%{buildroot}%{_bindir}/effectcraft --version
%{buildroot}%{_bindir}/effectcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.effectcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.effectcraft.metainfo.xml

%files
%license LICENSE-MIT LICENSE-APACHE
%license assets/fonts/OFL-Inter.txt
%license assets/fonts/OFL-JetBrainsMono.txt
%license assets/fonts/OFL-NotoSerif.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/effectcraft
%{_datadir}/applications/ai.storyteller.effectcraft.desktop
%{_datadir}/metainfo/ai.storyteller.effectcraft.metainfo.xml
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor size dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*

%files -n effectcraft-cli
%license LICENSE-MIT LICENSE-APACHE
%license assets/fonts/OFL-Inter.txt
%license assets/fonts/OFL-JetBrainsMono.txt
%license assets/fonts/OFL-NotoSerif.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/effectcraft-cli

%changelog
