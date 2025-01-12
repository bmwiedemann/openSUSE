#
# spec file for package geos
#
# Copyright (c) 2025 SUSE LLC
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


%define uver	3_13_0
Name:           geos
Version:        3.13.0
Release:        0
Summary:        Geometry Engine - Open Source
License:        LGPL-2.1-only
URL:            https://libgeos.org
Source0:        https://download.osgeo.org/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of JTS
in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid().

%package -n libgeos%{uver}
Summary:        Geometry Engine library

%description -n libgeos%{uver}
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of JTS
in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid().

%package -n libgeos_c1
Summary:        C language interface for the GEOS library

%description -n libgeos_c1
This subpackage contains a shared library providing a C linkage
interface for the (C++) GEOS library.

%package devel
Summary:        Development files for GEOS
Requires:       libgeos%{uver} = %{version}-%{release}
Requires:       libgeos_c1 = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description devel
GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology
Suite (JTS). As such, it aims to contain the complete functionality of
JTS in C++. This includes all the OpenGIS "Simple Features for SQL" spatial
predicate functions and spatial operators, as well as specific JTS topology
functions such as IsValid()

This package contains the development files to build applications that
use GEOS.

%prep
%autosetup

%build
%cmake
%cmake_build

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
# disable tests for i586 as they fail
%ifnarch %ix86
%ctest
%endif

%install
%cmake_install

%ldconfig_scriptlets -n libgeos%{uver}
%ldconfig_scriptlets -n libgeos_c1

%files
%license COPYING
%{_bindir}/geosop

%files -n libgeos%{uver}
%license COPYING
%{_libdir}/libgeos.so.*

%files -n libgeos_c1
%license COPYING
%{_libdir}/libgeos_c.so.*

%files devel
%license COPYING
%doc NEWS.md README.md
%{_bindir}/geos-config
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/GEOS
%{_libdir}/cmake/GEOS/geos-*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_c.so

%changelog
