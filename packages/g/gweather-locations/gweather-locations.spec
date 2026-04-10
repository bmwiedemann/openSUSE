#
# spec file for package gweather-locations
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


Name:           gweather-locations
Version:        2026.2
Release:        0
Summary:        GWeather Locations Database
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gweather-locations
Source0:        %{name}-%{version}.tar.xz
Source99:       gweather-locations-rpmlintrc
BuildRequires:  meson python3-gobject
BuildSystem:    meson

%description
The GWeather locations database contains a list of locations used by GNOME components through the GWeather library.
The locations are structured in an XML file, which follows a provided schema file.
The XML source is "compiled" into a binary format for fast parsing and access.
Location names are translatable.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name}

%files
%license COPYING
%dir %{_libdir}/gweather-locations
%{_libdir}/gweather-locations/Locations.bin
%dir %{_datadir}/gweather-locations
%{_datadir}/gweather-locations/Locations.xml
%{_datadir}/gweather-locations/locations.dtd
%{_datadir}/pkgconfig/gweather-locations.pc

%files lang -f %{name}.lang

%changelog

