#
# spec file for package figcraft
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


Name:           figcraft
Version:        0.11.2
Release:        0
Summary:        Design and prototype user interfaces
# Legal-Review-Notice: scope is the two shipped targets (figcraft, figcraft-cli).
# Upstream code is MIT OR Apache-2.0; the binaries additionally embed, via
# eframe default_fonts, Hack and the emoji icon font (MIT), Noto Emoji under
# OFL-1.1 (epaint_default_fonts) and the Ubuntu Light font under
# Ubuntu-font-1.0 (epaint_default_fonts). MPL-2.0 comes from
# imbl/imbl-sized-chunks (workspace dependency); CDLA-Permissive-2.0 from
# webpki-roots (TLS roots); Unicode-3.0 from the ICU crates. self_cell 1.3.0
# declares Apache-2.0 OR GPL-2.0-only; the build takes the Apache-2.0 option,
# so no GPL obligation is incurred. Crates offering Unlicense, BSL-1.0, 0BSD
# or LLVM-exception beside MIT/Apache-2.0 are taken under their MIT/Apache-2.0
# options. docs/brand (trademarked, not open source) is excluded from the
# tarball via the tar_scm exclude and is never installed. CRAFT_FONTS_DIR stays
# unset: no craft-fonts OFL faces are embedded, the app uses egui's bundled
# fonts plus the system fonts it scans at startup. The vendor-tree copyleft
# audit is recorded in the .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/figcraft
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
Recommends:     figcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
FigCraft is an open-source, native interface design and prototyping tool.
Lay out screens on an infinite canvas with frames, auto layout and
constraints, build reusable components and variants, and link screens
into clickable prototypes.

This package provides the desktop application; the companion figcraft-cli
subpackage provides the headless converter, renderer and command server.

%package -n figcraft-cli
Summary:        Headless FigCraft converter, renderer and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n figcraft-cli
Headless FigCraft: inspect and convert documents, render exports, run
scripted engine commands, and serve commands with an opt-in MCP server
for agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream has no `cargo install` story; package.sh builds these two workspace
# members by hand. CRAFT_FONTS_DIR stays unset: the build then uses egui's
# bundled fonts plus the system fonts the app scans at startup.
%{cargo_build} --locked -p figcraft -p figcraft-cli

%install
install -Dm0755 target/release/figcraft %{buildroot}%{_bindir}/figcraft
install -Dm0755 target/release/figcraft-cli %{buildroot}%{_bindir}/figcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.figcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.figcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.figcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.figcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.11.2, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.figcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.figcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.figcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.figcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.figcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Engine unit tests (synthetic data only, no corpus or network).
%{cargo_test} --locked -p figcraft-geom -p figcraft-doc
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/figcraft --version
%{buildroot}%{_bindir}/figcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.figcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.figcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/figcraft
%{_datadir}/applications/ai.storyteller.figcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.figcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.figcraft.xml

%files -n figcraft-cli
%{_bindir}/figcraft-cli

%changelog
