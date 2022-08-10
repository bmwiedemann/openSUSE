#
# spec file
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


%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "soup2"
%define nsuffix -soup2
%define shlib   libgeocode-glib0
%define typelib typelib-1_0-GeocodeGlib-1_0
%else
%define shlib   libgeocode-glib-2-0
%define typelib typelib-1_0-GeocodeGlib-2_0

%endif

Name:           geocode-glib%{?nsuffix}
Version:        3.26.4
Release:        0
Summary:        Convenience library for the Yahoo! Place Finder APIs
License:        LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org/
Source0:        https://download.gnome.org/sources/geocode-glib/3.26/geocode-glib-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.34
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.99.2
%if "%{flavor}" == "soup2"
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
%else
BuildRequires:  pkgconfig(libsoup-3.0)
%endif

%description
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n %{shlib}
Summary:        Convenience library for the Yahoo! Place Finder APIs
# We require the icon set, which is shipped in the main package (in order
# to keep the library parallel installable, we require at least current version).
Group:          System/Libraries
# geocode-glib (without suffix) is built only once in the ""-flavor
Requires:       geocode-glib >= %{version}

%description -n %{shlib}
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package -n %{typelib}
Summary:        Introspection bindings for geocode-glib
Group:          System/Libraries

%description -n %{typelib}
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
Requires:       %{shlib} = %{version}
Requires:       %{typelib} = %{version}

%description devel
The geocode-glib library is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

This package contains development files needed to develop with the
geocode-glib library.

%prep
%setup -q -n geocode-glib-%{version}

%build
# FIXME Please investigate if we should package installed-tests
%meson \
	-Denable-gtk-doc=true \
	-Denable-installed-tests=false \
%if "%{flavor}" == "soup2"
	-Dsoup2=true \
%else
	-Dsoup2=false \
%endif
	%{nil}
%meson_build

%install
%meson_install
# we package the icons as part of the ""-flavor package
%if "%{flavor}" != ""
rm -rf %{buildroot}%{_datadir}/icons/hicolor
%endif

%ldconfig_scriptlets -n %{shlib}

%if "%{flavor}" == ""
%files
%{_datadir}/icons/hicolor/
%endif

%files -n %{shlib}
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n %{typelib}
%{_libdir}/girepository-1.0/GeocodeGlib-*.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/geocode-glib*/
%{_datadir}/gir-1.0/*.gir
%{_includedir}/geocode-glib-*/
%{_libdir}/pkgconfig/geocode-glib-*.pc
%{_libdir}/*.so

%changelog
