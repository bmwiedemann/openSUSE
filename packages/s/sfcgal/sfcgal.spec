#
# spec file for package sfcgal
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Ioda-Net Sàrl, Charmoille, Switzerland. Bruno Friedmann (tigerfoot)
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


%define source_name SFCGAL
%define _libname    libSFCGAL1
%define _soversion  1
# while upstream https://gitlab.com/Oslandia/SFCGAL/-/issues/259
# and https://gitlab.com/Oslandia/SFCGAL/-/issues/258 are pending.
# this force postgis ix86 to be build without sfcgal.
ExcludeArch:    %{ix86}
%ifarch %{ix86} x86_64
%define withosgd 1
BuildRequires:  pkgconfig(openscenegraph)
%else
# openscenegraph not available for
# s390x ppc64le ppc64 aarch64 armv7l
# dummy
%define withosgd 0
%endif
Name:           sfcgal
Version:        1.5.1
Release:        0
Summary:        C++ wrapper library around CGAL
License:        LGPL-2.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://sfcgal.gitlab.io/SFCGAL/
Source0:        https://gitlab.com/sfcgal/SFCGAL/-/archive/v%{version}/SFCGAL-v%{version}.tar.bz2
# PATCH-FIX-UPSTREAM build with boost 1.85
Patch1:         boost1_85.diff
BuildRequires:  cmake
BuildRequires:  gmp-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_chrono-devel >= 1.70
BuildRequires:  libboost_filesystem-devel >= 1.70
BuildRequires:  libboost_headers-devel >= 1.70
BuildRequires:  libboost_program_options-devel >= 1.70
BuildRequires:  libboost_serialization-devel >= 1.70
BuildRequires:  libboost_system-devel >= 1.70
BuildRequires:  libboost_test-devel >= 1.70
BuildRequires:  libboost_thread-devel >= 1.70
BuildRequires:  libboost_timer-devel >= 1.70
BuildRequires:  libcgal-devel >= 5.6
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-clang
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libecpg) >= 10
BuildRequires:  pkgconfig(libecpg_compat) >= 10
BuildRequires:  pkgconfig(libpgtypes) >= 10
BuildRequires:  pkgconfig(libpq) >= 10
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(zlib)

%description
This package contains tools & sample data to test %{_libname}.

%package -n %{_libname}
Summary:        Libraries SFCGAL applications
Group:          Development/Libraries/C and C++
Provides:       libsfcgal%{_soversion}

%description -n %{_libname}
This library  support ISO 19107:2013, OGC Simple Features Access 1.2 for 3D operations.
It provides standard compliant geometry types and operations, that can
be accessed from its C or C++ APIs. PostGIS uses the C API, to expose some
SFCGAL's functions in spatial databases (cf. PostGIS manual).

Geometry coordinates have an exact rational number representation and can
be either 2D or 3D. Among supported geometry types are :

 Points
 LineStrings
 Polygons
 TriangulatedSurfaces
 PolyhedralSurfaces
 GeometryCollections
 Solids

Supported operations include :

 WKT reading and writing with exact rational number representation for coordinates
 Intersection operations and predicates
 Convex hull computation
 Tessellation
 Extrusion
 Area and distance computation
 Minkovski sums
 Contour offsets
 Straight skeleton generations

%package devel
Summary:        Development files and tools for SFCGAL applications
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}

%description devel
Content headers & files to envelopment files for %{_libname}

%prep
%setup -q -n %{source_name}-v%{version}
%patch -P1 -p1

%build
%limit_build -m 6400
tmpflags="%{optflags} -fPIC -fPIE"
echo "${tmpflags}"
# Desactivate lto (check with upstream)
%define _lto_cflags %{nil}
tmpflags="${tmpflags/-flto=auto}"
%ifarch ppc64 ppc64le
# bypass bug 927268 for PowerPC if clang is used above in place of gcc
tmpflags="${tmpflags/-fstack-protector}"
tmpflags="${tmpflags/-strong}"
%endif
#Remove -fstack-clash-protection added on 42.3 for unknown reason
tmpflags="${tmpflags/-fstack-clash-protection}"

%cmake \
  -DCMAKE_USER_MAKE_RULES_OVERRIDE=OFF \
  -DCMAKE_C_FLAGS="${tmpflags} -Doverride=" \
  -DCMAKE_CXX_FLAGS="${tmpflags} -Doverride=" \
  -DCMAKE_CXX_FLAGS_RELEASE="${tmpflags} -Doverride=" \
  -DCMAKE_BUILD_TYPE="Release" \
  -DCMAKE_GMP_ENABLE_CXX=ON \
  -DSFCGAL_CHECK_VALIDITY=TRUE \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
%if %{withosgd}
  -DSFCGAL_WITH_OSG=ON \
%else
  -DSFCGAL_WITH_OSG=OFF \
%endif
  -DSFCGAL_BUILD_EXAMPLES=ON \
  -DSFCGAL_BUILD_TESTS=ON

%cmake_build

%install
%cmake_install

# Work fine only on x86
%ifarch i586 x86_64
%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/unit-test-SFCGAL ||:
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/standalone-regress-test-SFCGAL ||:
%endif

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%files -n %{_libname}
%license LICENSE
%doc README.md AUTHORS NEWS
%{_libdir}/libSFCGAL.so.%{version}
%{_libdir}/libSFCGAL.so.%{_soversion}
%if %{withosgd}
%{_libdir}/libSFCGAL-osg.so.%{version}
%{_libdir}/libSFCGAL-osg.so.%{_soversion}
%endif

%files
%license LICENSE
%doc README.md AUTHORS NEWS
%{_bindir}/example-CGAL-*
%{_bindir}/example-SFCGAL-*
%{_bindir}/unit-test-SFCGAL
%{_bindir}/standalone-regress-test-SFCGAL
%{_bindir}/test-regress-convex_hull
%{_bindir}/test-regress-polygon_triangulator

%files devel
%license LICENSE
%doc README.md AUTHORS NEWS
%{_libdir}/libSFCGAL.so
%if %{withosgd}
%{_libdir}/libSFCGAL-osg.so
%endif
%{_libdir}/pkgconfig/sfcgal.pc
%{_includedir}/SFCGAL
%{_bindir}/sfcgal-config

%changelog
