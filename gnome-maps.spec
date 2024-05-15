#
# spec file for package gnome-maps
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


Name:           gnome-maps
Version:        46.11
Release:        0
Summary:        Maps Application for GNOME
License:        Apache-2.0 AND CC-BY-3.0 AND GPL-2.0-or-later AND BSD-3-Clause AND ISC AND MIT
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
# Needed for typelib() Requires
BuildRequires:  gobject-introspection
#
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.40.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(folks) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.16.0
BuildRequires:  pkgconfig(geoclue-2.0) >= 0.12.99
BuildRequires:  pkgconfig(geocode-glib-2.0) >= 3.15.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.69.2
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(gtk4) >= 3.22.0
# Needed for test run
BuildRequires:  pkgconfig(gweather4) >= 3.90.0
#
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0) >= 0.7.90
BuildRequires:  pkgconfig(shumate-1.0) >= 1.2.alpha
Recommends:     dbus(org.freedesktop.GeoClue2)

%description
Maps is a maps application for GNOME 3. It allows viewing street maps from
OpenStreetMaps and satellite imagery from Mapbox. You can also get directions
for your journeys, whether on foot, by bike, or by car.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
# There is no devel package, so at this moment also no need to keep gir and so files
rm %{buildroot}%{_datadir}/gnome-maps/gir-1.0/GnomeMaps-1.0.gir
rm %{buildroot}%{_libdir}/%{name}/libgnome-maps.so

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Maps.appdata.xml
%{_datadir}/applications/org.gnome.Maps.desktop
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Maps*
%{_datadir}/glib-2.0/schemas/org.gnome.Maps.gschema.xml
%{_libdir}/%{name}/libgnome-maps.so.0*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/GnomeMaps-1.0.typelib

%files lang -f %{name}.lang

%changelog
