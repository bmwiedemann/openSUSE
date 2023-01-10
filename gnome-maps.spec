#
# spec file for package gnome-maps
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


Name:           gnome-maps
Version:        43.3
Release:        0
Summary:        Maps Application for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        https://download.gnome.org/sources/gnome-maps/43/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-maps-fix-dependency.patch -- Fix upstream dodo when setting dependency for libshumate
Patch0:         gnome-maps-fix-dependency.patch
# PATCH-FIX-UPSTREAM gnome-maps-icu72.patch mgorse@suse.com -- fix comparisons in time tests.
Patch1:         gnome-maps-icu72.patch

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
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0) >= 0.7.90
BuildRequires:  pkgconfig(shumate-1.0) >= 1.0.0
Recommends:     dbus(org.freedesktop.GeoClue2)
# gnome-maps 43 found a new way to specify typelib deps, which are not (yet) understood by gi-dep-scanner
Requires:       typelib(GtkClutter) = 1.0
Requires:       typelib(GeocodeGlib) = 1.0

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
