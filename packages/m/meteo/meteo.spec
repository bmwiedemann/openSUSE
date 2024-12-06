#
# spec file for package meteo
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid com.gitlab.bitseater.meteo
Name:           meteo
Version:        0.9.9.3
Release:        0
Summary:        Program to show the weather forecast of the next hours and days
License:        GPL-3.0-or-later
URL:            https://gitlab.com/bitseater/meteo
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) > 2.54.1
BuildRequires:  pkgconfig(webkit2gtk-4.0)

%description
A program which displays current weather, with information about temperature,
pressure, wind speed and direction, as well as sunrise and sunset times.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/icons/hicolor/scalable/status/%{appid}-*.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_mandir}/man?/%{appid}.?%{?ext_man}
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,192x192@2,192x192@2/apps,24x24@2,24x24@2/apps,256x256@2,256x256@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
