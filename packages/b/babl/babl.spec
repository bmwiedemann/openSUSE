#
# spec file for package babl
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


%define debug_package_requires libbabl-0_1-0 = %{version}-%{release}

Name:           babl
Version:        0.1.98
Release:        0
Summary:        Dynamic Pixel Format Translation Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gegl.org/babl/
Source0:        https://download.gimp.org/pub/babl/0.1/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(lcms2)
# None of these is needed for standard build:
#BuildRequires:  inkscape ruby w3m

%description
babl is a dynamic, any to any, pixel format translation library.

%package -n libbabl-0_1-0
Summary:        Dynamic Pixel Format Translation Library
Group:          System/Libraries

%description -n libbabl-0_1-0
babl is a dynamic, any to any, pixel format translation library.

It allows converting between different methods of storing pixels known
as pixel formats that have with different bitdepths and other data
representations, color models and component permutations.

A vocabulary to formulate new pixel formats from existing primitives is
provided as well as the framework to add new color models and data
types.

%package -n typelib-1_0-Babl-0_1
Summary:        Introspection bindings for babl
Group:          System/Libraries

%description -n typelib-1_0-Babl-0_1
babl is a dynamic, any to any, pixel format translation library.

This package provides the GObject Introspection bindings for babl.

%package devel
Summary:        Dynamic Pixel Format Translation Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libbabl-0_1-0 = %{version}
Requires:       typelib-1_0-Babl-0_1 = %{version}

%description devel
babl is a dynamic, any to any, pixel format translation library.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%post -n libbabl-0_1-0 -p /sbin/ldconfig
%postun -n libbabl-0_1-0 -p /sbin/ldconfig

%files -n libbabl-0_1-0
%license COPYING
%doc NEWS
%{_libdir}/*.so.*
%{_libdir}/babl-0.1/

%files -n typelib-1_0-Babl-0_1
%{_libdir}/girepository-1.0/Babl-0.1.typelib

%files devel
%doc AUTHORS TODO
%{_includedir}/babl-0.1/
%{_bindir}/babl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Babl-0.1.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/babl-0.1.deps
%{_datadir}/vala/vapi/babl-0.1.vapi

%changelog
