#
# spec file for package gom
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


Name:           gom
Version:        0.3.3
Release:        0
Summary:        GObject Data Mapper
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://git.gnome.org/browse/gom/
Source:         http://download.gnome.org/sources/gom/0.3/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.38.1
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.7

%description
This is a DataMapper for GObject.

%package -n libgom-1_0-0
Summary:        GObject Data Mapper
Group:          System/Libraries
Obsoletes:      gom-lang

%description -n libgom-1_0-0
This is a DataMapper for GObject.

%package -n typelib-1_0-Gom-1_0
Summary:        Introspection bindings for the GObject Data Mapper
Group:          System/Libraries

%description -n typelib-1_0-Gom-1_0
This is a DataMapper for GObject.

This package provides the GObject Introspection bindings for gom.

%package -n python3-gom
Summary:        Python3 binding for the GObject Dara Mapper
Group:          Development/Languages/Python
Supplements:    packageand(python3:typelib-1_0-Gom-1_0)

%description -n python3-gom
This is a DataMapper for GObject.

With this package you can glue gom to python3.

%package devel
Summary:        Development files for the GObject Data Mapper
Group:          Development/Libraries/GNOME
Requires:       libgom-1_0-0 = %{version}
Requires:       python3-gom = %{version}
Requires:       typelib-1_0-Gom-1_0 = %{version}

%description  devel
This is a DataMapper for GObject.

%prep
%setup -q

%build
%meson
%meson_build

%check
# Temp disable tests while we figure out why it times out on x86_64
#meson_test

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgom-1_0-0 -p /sbin/ldconfig
%postun -n libgom-1_0-0 -p /sbin/ldconfig

%files -n libgom-1_0-0
%license COPYING
%doc README
%{_libdir}/libgom-1.0.so.*

%files -n typelib-1_0-Gom-1_0
%{_libdir}/girepository-1.0/Gom-1.0.typelib

%files -n python3-gom
%{python3_sitearch}/gi/overrides/Gom.py

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gom-1.0/
%{_datadir}/gir-1.0/*.gir

%changelog
