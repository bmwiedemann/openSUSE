#
# spec file for package sfcgal
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Ioda-Net Sàrl, Charmoille, Switzerland. Bruno Friedmann (tigerfoot)
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
%define _libname    libSFCGAL2
%define _soversion  2
%define withexamples 0
%ifarch %{ix86} x86_64
%define withosgd 1
%define withtest 1
BuildRequires:  pkgconfig(openscenegraph)
%else
# openscenegraph not available for
# s390x ppc64le ppc64 aarch64 armv7l
# dummy
%define withosgd 0
%define withtest 0
%endif
Name:           sfcgal
Version:        2.3.0
Release:        0
Summary:        C++ wrapper library around CGAL
License:        LGPL-2.0-or-later
URL:            https://sfcgal.gitlab.io/SFCGAL/
Source0:        https://gitlab.com/sfcgal/SFCGAL/-/archive/v%{version}/SFCGAL-v%{version}.tar.bz2
# PATCH-FIX-OPENSUSE sfcgal-fix-osg-namespace.patch - 2.3.0 opens 2 namespaces in OsgFactory
# but closes 3, so every -DSFCGAL_WITH_OSG=ON build fails. No upstream ref on purpose: the
# OSG backend was deleted upstream after 2.3.0, so there is no branch left to send it to.
Patch0:         sfcgal-fix-osg-namespace.patch
BuildRequires:  cmake
BuildRequires:  gmp-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_headers-devel >= 1.72
BuildRequires:  libboost_program_options-devel >= 1.72
BuildRequires:  libboost_serialization-devel >= 1.72
BuildRequires:  libboost_test-devel >= 1.72
BuildRequires:  libboost_thread-devel >= 1.72
BuildRequires:  libcgal-devel >= 5.6
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-clang
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libecpg) >= 10
BuildRequires:  pkgconfig(libecpg_compat) >= 10
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpgtypes) >= 10
BuildRequires:  pkgconfig(libpq) >= 10
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(nlohmann_json) >= 3.11
BuildRequires:  pkgconfig(zlib)
# while upstream https://gitlab.com/Oslandia/SFCGAL/-/issues/259
# and https://gitlab.com/Oslandia/SFCGAL/-/issues/258 are pending.
# this force postgis ix86 to be build without sfcgal.
ExcludeArch:    %{ix86}

%description
This package contains tools & sample data to test %{_libname}.

%package -n %{_libname}
Summary:        Libraries SFCGAL applications
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
Requires:       %{_libname} = %{version}
Requires:       pkgconfig(nlohmann_json) >= 3.11

%description devel
Content headers & files to envelopment files for %{_libname}

%prep
%autosetup -p1 -n %{source_name}-v%{version}

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
  -DSFCGAL_WITH_EIGEN=ON \
%if %{withosgd}
  -DSFCGAL_WITH_OSG=ON \
%else
  -DSFCGAL_WITH_OSG=OFF \
%endif
%if %{withexamples}
  -DSFCGAL_BUILD_EXAMPLES=ON \
%else
  -DSFCGAL_BUILD_EXAMPLES=OFF \
%endif
%if %{withtest}
  -DSFCGAL_BUILD_TESTS=ON
%else
  -DSFCGAL_BUILD_TESTS=OFF
%endif

%cmake_build

%install
%cmake_install

# Work fine only on x86
%ifarch i586 x86_64
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest ||:
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
%if %{withexamples}
%{_bindir}/example-CGAL-*
%{_bindir}/example-SFCGAL-*
%endif

%files devel
%license LICENSE
%doc README.md AUTHORS NEWS
%{_libdir}/libSFCGAL.so
%if %{withosgd}
%{_libdir}/libSFCGAL-osg.so
%endif
%{_libdir}/pkgconfig/sfcgal.pc
%{_libdir}/cmake/SFCGAL
%{_includedir}/SFCGAL
%{_bindir}/sfcgal-config

%changelog
