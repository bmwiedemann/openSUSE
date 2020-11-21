#
# spec file for package gnome-maps
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.36.4.1
Release:        0
Summary:        Maps Application for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        https://download.gnome.org/sources/gnome-maps/3.36/%{name}-%{version}.tar.xz

# Needed for typelib() Requires
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.40.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(champlain-0.12) >= 0.12.14
BuildRequires:  pkgconfig(folks) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.16.0
BuildRequires:  pkgconfig(geoclue-2.0) >= 0.12.99
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.15.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.50.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-0.7) >= 0.7.90
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

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -G "Maps Application" org.gnome.Maps DesktopUtility
# There is no devel file, so at this moment also no need to keep
rm %{buildroot}%{_datadir}/gnome-maps/gir-1.0/GnomeMaps-1.0.gir

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
%{_libdir}/%{name}/

%files lang -f %{name}.lang

%changelog
