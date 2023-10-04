#
# spec file for package eyedropper
#
# Copyright (c) 2023 SUSE LLC
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

%define lname com.github.finefindus.eyedropper
%define _ver  v0.7.0-beta
%define vbeta 0.7.0.beta
Name:           eyedropper
Version:        0.7.0~beta
Release:        0
Summary:        Pick and format colors
License:        GPL-3.0-or-later
URL:            https://github.com/FineFindus/eyedropper
Source:         %{url}/releases/download/%{_ver}/%{name}-%{vbeta}.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  desktop-file-utils

%description
An application to pick and format colors.

Features:
- Pick a Color
- Enter a color in Hex-Format
- Parse RGB/RGBA/ARGB Hex-Colors
- View colors in formats
- Customize which formats appear as well as their order
- Generate a palette of different shades

%lang_package

%prep
%autosetup -n %{name}-%{vbeta}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/%{lname}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{lname}.gschema.xml
%{_datadir}/dbus-1/services/%{lname}.SearchProvider.service
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{lname}.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/%{lname}*.svg
%{_datadir}/metainfo/%{lname}.metainfo.xml

%files lang -f %{name}.lang

%changelog

