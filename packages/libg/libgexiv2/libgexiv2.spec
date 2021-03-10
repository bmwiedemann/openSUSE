#
# spec file for package libgexiv2
#
# Copyright (c) 2021 SUSE LLC
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


%define tarname gexiv2
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
%bcond_without python3
Name:           libgexiv2
Version:        0.12.2
Release:        0
Summary:        A GObject-based Exiv2 wrapper
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://ftp.gnome.org/pub/gnome/sources/gexiv2/0.12/%{tarname}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gobject}
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  libtool
BuildRequires:  meson >= 0.48
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(exiv2) >= 0.26
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n libgexiv2-2
Summary:        A GObject-based Exiv2 wrapper
Group:          System/Libraries

%description -n libgexiv2-2
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n typelib-1_0-GExiv2-0_10
Summary:        A GObject-based Exiv2 wrapper - Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GExiv2-0_10
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides the GObject Introspection bindings for the
libgexiv2 library.

%package devel
Summary:        A GObject-based Exiv2 wrapper -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libgexiv2-2 = %{version}

%description devel
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n python-gexiv2
Summary:        A GObject-based Exiv2 wrapper
Group:          Development/Libraries/Python
Requires:       python-gobject

%description -n python-gexiv2
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides the Python 2 bindings for the libgexiv2 library.

%package -n python3-gexiv2
Summary:        A GObject-based Exiv2 wrapper
Group:          Development/Libraries/Python
Requires:       python3-gobject

%description -n python3-gexiv2
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides the Python 3 bindings for the libgexiv2 library.

%prep
%autosetup -n %{tarname}-%{version} -p1

%build
%meson \
	-Dintrospection=true \
	%{nil}
%meson_build

%install
%meson_install

%post -n libgexiv2-2 -p /sbin/ldconfig
%postun -n libgexiv2-2 -p /sbin/ldconfig

%files -n libgexiv2-2
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_libdir}/libgexiv2.so.*

%files -n typelib-1_0-GExiv2-0_10
%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

%files devel
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%{_includedir}/gexiv2/
%{_libdir}/libgexiv2.so
%{_libdir}/pkgconfig/gexiv2.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2.vapi
%{_datadir}/vala/vapi/gexiv2.deps

%if %{with python2}
%files -n python-gexiv2
%{python_sitearch}/*
%endif

%if %{with python3}
%files -n python3-gexiv2
%{python3_sitearch}/*
%endif

%changelog
