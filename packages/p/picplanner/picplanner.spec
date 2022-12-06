#
# spec file for package picplanner
#
# Copyright (c) 2022 SUSE LLC
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


Name:           picplanner
Version:        0.3.2
Release:        0
Summary:        A GTK application for photographers using GNU Linux or especially Linux phones
License:        GPL-3.0-or-later
URL:            https://gitlab.com/Zwarf/%{name}
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4) >= 4.1.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(shumate-1.0) >= 1.0.0.beta

%description
A GTK application for photographers using GNU Linux or especially
Linux phones. It can be used to calculate the position of the Sun,
Moon and Milky Way in order to plan the position and time for an
photograph.

%lang_package

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc CHANGELOG README.md
%{_bindir}/picplanner
%{_datadir}/applications/de.zwarf.picplanner.desktop
%{_datadir}/glib-2.0/schemas/de.zwarf.picplanner.gschema.xml
%{_datadir}/icons/azimuth-symbolic.svg
%{_datadir}/icons/elevation-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/de.zwarf.picplanner.svg
%{_datadir}/icons/hicolor/symbolic/apps/de.zwarf.picplanner-symbolic.svg
%{_datadir}/icons/map-symbolic.svg
%{_datadir}/icons/milky-way-color.svg
%{_datadir}/icons/milky-way-symbolic.svg
%{_datadir}/icons/moon-full.svg
%{_datadir}/icons/moon-new.svg
%{_datadir}/icons/moon-waning.svg
%{_datadir}/icons/moon-waxing.svg
%{_datadir}/icons/pin.svg
%{_datadir}/icons/sun.svg
%{_datadir}/metainfo/de.zwarf.picplanner.metainfo.xml

%files lang -f %{name}.lang

%changelog
