#
# spec file for package geocode-glib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           geocode-glib
Version:        3.26.1
Release:        0
Summary:        Convenience library for the Yahoo! Place Finder APIs
License:        LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org/
Source0:        https://download.gnome.org/sources/geocode-glib/3.26/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.34
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.99.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42

%description
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n libgeocode-glib0
Summary:        Convenience library for the Yahoo! Place Finder APIs
# We require the icon set, which is shipped in the main package (in order
# to keep the library parallel installable, we require at least current version).
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libgeocode-glib0
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n typelib-1_0-GeocodeGlib-1_0
Summary:        Introspection bindings for geocode-glib
Group:          System/Libraries

%description -n typelib-1_0-GeocodeGlib-1_0
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

This package provides the GObject Introspection bindings for the
geocode-glib library.

%package devel
Summary:        Development files for geocode-glib, a library for the Yahoo Place Finder APIs
Group:          Development/Libraries/C and C++
Requires:       libgeocode-glib0 = %{version}
Requires:       typelib-1_0-GeocodeGlib-1_0 = %{version}

%description devel
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

This package contains development files needed to develop with the
geocode-glib library.

%prep
%setup -q

%build
# FIXME Please investigate if we should package installed-tests
%meson \
	-Denable-gtk-doc=true \
	-Denable-installed-tests=false \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgeocode-glib0 -p /sbin/ldconfig
%postun -n libgeocode-glib0 -p /sbin/ldconfig

%files
%{_datadir}/icons/gnome/

%files -n libgeocode-glib0
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-GeocodeGlib-1_0
%{_libdir}/girepository-1.0/GeocodeGlib-1.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/geocode-glib/
%{_datadir}/gir-1.0/*.gir
%{_includedir}/geocode-glib-1.0/
%{_libdir}/pkgconfig/geocode-glib-1.0.pc
%{_libdir}/*.so

%changelog
