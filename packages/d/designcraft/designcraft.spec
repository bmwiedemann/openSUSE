#
# spec file for package designcraft
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


Name:           designcraft
Version:        0.13.0
Release:        0
Summary:        Page layout and publishing workbench
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/designcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-cratesio.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     designcraft-cli
Recommends:     mesa-vulkan-drivers
Recommends:     xdg-desktop-portal
Recommends:     libX11.so.6()(64bit)
Recommends:     libXcursor.so.1()(64bit)
Recommends:     libXi.so.6()(64bit)
Recommends:     libXrandr.so.2()(64bit)
Recommends:     libwayland-client.so.0()(64bit)
ExclusiveArch:  %{rust_tier1_arches}

%description
Page layout and publishing workbench: lay out magazines, books and print
documents with a native Rust application.

This package provides the desktop application; the companion designcraft-cli
subpackage provides the headless command runner and opt-in MCP server.

%package -n designcraft-cli
Summary:        Headless DesignCraft command runner and MCP server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n designcraft-cli
Headless DesignCraft command runner: drive layouts, exports and conversions
from scripts and CI, plus an opt-in MCP server for agents.

%prep
%autosetup -a1
# Trademarked ArtCraft marks must never ship: belt-and-braces removal even
# though tar_scm already excludes docs/brand from the tarball.
rm -rf docs/brand
# Upstream metainfo declares the app icon as stock; it is a cached hicolor
# icon, otherwise appstream validation fails.
sed -i 's|<icon type="stock">ai.storyteller.designcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.designcraft.png</icon>|' packaging/linux/ai.storyteller.designcraft.metainfo.xml.in

%build
%limit_build -m 2000
# CRAFT_FONTS_DIR stays unset: use system fallback instead of embedding
# the OFL craft-fonts checkout. Cargo.lock is committed upstream.
# cargo_build already passes offline mode; only add locked flag.
%{cargo_build} --locked -p designcraft -p designcraft-cli

%install
install -D -m 0755 target/release/designcraft %{buildroot}%{_bindir}/designcraft
install -D -m 0755 target/release/designcraft-cli %{buildroot}%{_bindir}/designcraft-cli
install -D -m 0644 packaging/linux/ai.storyteller.designcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.designcraft.desktop
install -D -m 0644 packaging/linux/ai.storyteller.designcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.designcraft.xml
mkdir -p %{buildroot}%{_datadir}/metainfo
# Keep date command format literals unbraced so spec-cleaner leaves them alone.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/$(date -u +%Y-%m-%d)/g" packaging/linux/ai.storyteller.designcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.designcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 NOTICE %{buildroot}%{_docdir}/%{name}/
install -m 0644 LICENSE-MIT LICENSE-APACHE %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/fonts/OFL-*.txt %{buildroot}%{_docdir}/%{name}/
# Licence texts NOTICE points to for the hayro PDF backend and the Foxit
# fonts (BSD-3-Clause), CMYK profile (CC0-1.0) and Adobe CMaps it embeds.
cp -a licenses %{buildroot}%{_docdir}/%{name}/
install -d -m 0755 %{buildroot}%{_docdir}/designcraft-cli
ln -s ../designcraft/README.md %{buildroot}%{_docdir}/designcraft-cli/README.md
ln -s ../designcraft/NOTICE %{buildroot}%{_docdir}/designcraft-cli/NOTICE
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.designcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.designcraft.metainfo.xml
%{buildroot}%{_bindir}/designcraft-cli --version
%{buildroot}%{_bindir}/designcraft-cli commands | head -n 20
%{buildroot}%{_bindir}/designcraft --version || %{buildroot}%{_bindir}/designcraft --help | head -n 5

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE-APACHE
%license %{_docdir}/%{name}/LICENSE-MIT
%license %{_docdir}/%{name}/OFL-*.txt
%license %{_docdir}/%{name}/licenses
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/NOTICE
%{_bindir}/designcraft
%{_datadir}/applications/ai.storyteller.designcraft.desktop
%{_datadir}/metainfo/ai.storyteller.designcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.designcraft.xml
%{_datadir}/icons/hicolor/*

%files -n designcraft-cli
%{_bindir}/designcraft-cli
%dir %{_docdir}/designcraft-cli
%{_docdir}/designcraft-cli/*

%changelog
