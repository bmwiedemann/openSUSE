#
# spec file for package osm-gps-map
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2014 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           osm-gps-map
Version:        1.2.0+38
Release:        0
Summary:        A Gtk+ Widget for Displaying OpenStreetMap tiles
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            http://nzjrs.github.io/osm-gps-map/
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(libsoup-3.0)

%description
A Gtk+ widget (and Python bindings) that when given GPS co-ordinates, draws a GPS track,
and points of interest on a moving map display. Downloads map data from a number of websites,
including openstreetmap.org.

The library has excellent performance and is currently used in a number of
Gtk+ and Maemo applications.

%package -n libosmgpsmap-1_0-1
Summary:        A Gtk+ Widget for Displaying OpenStreetMap tiles
Group:          System/Libraries

%description -n libosmgpsmap-1_0-1
A Gtk+ widget (and Python bindings) that when given GPS co-ordinates, draws a GPS track,
and points of interest on a moving map display. Downloads map data from a number of websites,
including openstreetmap.org.

The library has excellent performance and is currently used in a number of
Gtk+ and Maemo applications.

%package -n typelib-1_0-OsmGpsMap-1_0
Summary:        A Gtk+ Widget for Displaying OpenStreetMap tiles
Group:          System/Libraries

%description -n typelib-1_0-OsmGpsMap-1_0
A Gtk+ widget (and Python bindings) that when given GPS co-ordinates, draws a GPS track,
and points of interest on a moving map display. Downloads map data from a number of websites,
including openstreetmap.org.

The library has excellent performance and is currently used in a number of
Gtk+ and Maemo applications.

%package -n libosmgpsmap-devel
Summary:        A Gtk+ Widget for Displaying OpenStreetMap tiles - Development files
Group:          Development/Languages/C and C++
Requires:       libosmgpsmap-1_0-1 = %{version}
Requires:       typelib-1_0-OsmGpsMap-1_0 = %{version}

%description -n libosmgpsmap-devel
A Gtk+ widget (and Python bindings) that when given GPS co-ordinates, draws a GPS track,
and points of interest on a moving map display. Downloads map data from a number of websites,
including openstreetmap.org.

The library has excellent performance and is currently used in a number of
Gtk+ and Maemo applications.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-static \
    --enable-gtk-doc \
    %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# We package those files as %%doc, resulting in a different location
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%ldconfig_scriptlets -n libosmgpsmap-1_0-1

%files -n libosmgpsmap-1_0-1
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_libdir}/libosmgpsmap-1.0.so.*

%files -n typelib-1_0-OsmGpsMap-1_0
%{_libdir}/girepository-1.0/OsmGpsMap-1.0.typelib

%files -n libosmgpsmap-devel
%{_includedir}/osmgpsmap-1.0/
%{_datadir}/gir-1.0/OsmGpsMap-1.0.gir
%{_libdir}/libosmgpsmap-1.0.so
%{_libdir}/pkgconfig/osmgpsmap-1.0.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libosmgpsmap

%changelog
