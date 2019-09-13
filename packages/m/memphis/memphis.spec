#
# spec file for package memphis
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           memphis
Version:        0.2.3
Release:        0
Summary:        Map rendering library for OpenStreetMap
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://trac.openstreetmap.ch/trac/memphis/
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM memphis-link-gobject.patch vuntz@opensuse.org -- Fix linking issue, taken from Debian
Patch0:         memphis-link-gobject.patch
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
LibMemphis provides a GObject based API to render OpenStreetMap data on
a cairo surface. Libmemphis implements the 'Slippy Map Tilename'
specification, like Mapnik and Osmarender.

It supports zoom level 12 to 18, projected with the Mercator projection.

%package -n libmemphis-0_2-0
Summary:        Map rendering library for OpenStreetMap
Group:          System/Libraries

%description -n libmemphis-0_2-0
LibMemphis provides a GObject based API to render OpenStreetMap data on
a cairo surface. Libmemphis implements the 'Slippy Map Tilename'
specification, like Mapnik and Osmarender.

It supports zoom level 12 to 18, projected with the Mercator projection.

%package -n typelib-1_0-Memphis-0_2
Summary:        Introspection bindings for memphis, a map rendering library for OSM
Group:          System/Libraries

%description -n typelib-1_0-Memphis-0_2
LibMemphis provides a GObject based API to render OpenStreetMap data on
a cairo surface. Libmemphis implements the 'Slippy Map Tilename'
specification, like Mapnik and Osmarender.

This package provides the GObject Introspection bindings for the
memphis library.

%package devel
Summary:        Development files for memphis, a map rendering library for OSM
Group:          Development/Libraries/C and C++
Requires:       libmemphis-0_2-0 = %{version}
Requires:       typelib-1_0-Memphis-0_2 = %{version}

%description devel
LibMemphis provides a GObject based API to render OpenStreetMap data on
a cairo surface. Libmemphis implements the 'Slippy Map Tilename'
specification, like Mapnik and Osmarender.

It supports zoom level 12 to 18, projected with the Mercator projection.

%prep
%setup -q
%patch0 -p1

%build
# needed for patch0
autoreconf -fi
%configure \
    --disable-static \
    --enable-vala
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Those are demo files, they shouldn't get installed
rm %{buildroot}%{_bindir}/example
rm %{buildroot}%{_datadir}/memphis/default-rules.xml

%post -n libmemphis-0_2-0 -p /sbin/ldconfig
%postun -n libmemphis-0_2-0 -p /sbin/ldconfig

%files -n libmemphis-0_2-0
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libmemphis-0.2.so.*

%files -n typelib-1_0-Memphis-0_2
%{_libdir}/girepository-1.0/Memphis-0.2.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/libmemphis/
%{_includedir}/libmemphis-0.2/
%{_libdir}/libmemphis-0.2.so
%{_libdir}/pkgconfig/memphis-0.2.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/memphis-0.2.*

%changelog
