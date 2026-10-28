#
# spec file for package gridcraft
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


Name:           gridcraft
Version:        0.12.1
Release:        0
Summary:        Native spreadsheet with XLSX support, formulas and charts
# Legal-Review-Notice: scope is the two shipped targets (gridcraft, gridcraft-cli).
# Upstream code is MIT OR Apache-2.0; the binaries additionally embed: OFL-1.1
# and Ubuntu-font-1.0 fonts via eframe default_fonts (epaint_default_fonts) and
# Unicode-3.0 code via unicode-ident. self_cell 1.3.0 declares
# Apache-2.0 OR GPL-2.0-only; the build takes the Apache-2.0 option, so no GPL
# obligation is incurred. adler2's 0BSD option is not taken (MIT/Apache-2.0
# elected). docs/brand (trademarked, not open source) is excluded from the
# tarball via the tar_scm exclude and is never installed. CRAFT_FONTS_DIR stays
# unset, so no OFL craft-fonts are embedded. vendor-tree copyleft audit is
# recorded in the .changes entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Unlicense AND Zlib
URL:            https://github.com/storytold/gridcraft
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
Recommends:     gridcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
GridCraft is an open-source, native spreadsheet. It opens and saves .xlsx
workbooks and CSV/TSV files, evaluates hundreds of worksheet functions, and
formats, sorts, filters and charts your data.

This package provides the desktop application; the companion gridcraft-cli
subpackage provides the headless converter, evaluator and command server.

%package -n gridcraft-cli
Summary:        Headless GridCraft converter, evaluator and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Unlicense AND Zlib

%description -n gridcraft-cli
Headless GridCraft command line: inspect, convert, evaluate, script and
serve MCP without a window.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream has no `cargo install` story; package.sh builds these two workspace
# members by hand (apps/gridcraft-web is wasm and is never built here).
# CRAFT_FONTS_DIR stays unset: the build then uses the bundled eframe
# default fonts plus the system fallback.
%{cargo_build} --locked -p gridcraft -p gridcraft-cli

%install
install -Dm0755 target/release/gridcraft %{buildroot}%{_bindir}/gridcraft
install -Dm0755 target/release/gridcraft-cli %{buildroot}%{_bindir}/gridcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.gridcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.gridcraft.desktop
install -Dm0644 packaging/linux/ai.storyteller.gridcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.gridcraft.xml
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.12.1, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.gridcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.gridcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.gridcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.gridcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.gridcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Headless CLI integration tests (in-memory workbooks and temp dirs, no
# window, GPU or network) covering the shipped engine via its CLI.
%{cargo_test} --locked -p gridcraft-cli
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/gridcraft --version
%{buildroot}%{_bindir}/gridcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.gridcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.gridcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license assets/app-icon/LICENSE.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/gridcraft
%{_datadir}/applications/ai.storyteller.gridcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.gridcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.gridcraft.xml

%files -n gridcraft-cli
%{_bindir}/gridcraft-cli

%changelog
