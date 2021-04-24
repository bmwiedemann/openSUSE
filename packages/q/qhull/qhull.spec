#
# spec file for package qhull
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


%define libname libqhull_r8_0
%define srcyear 2020
%define srcver  8.0.2
Name:           qhull
Version:        2020.2
Release:        0
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
License:        Qhull
Group:          Development/Libraries/C and C++
URL:            http://www.qhull.org
Source0:        http://www.qhull.org/download/qhull-%{srcyear}-src-%{srcver}.tgz
# PATCH-FIX-OPENSUSE
Patch1:         0002-Remove-tools-from-CMake-exported-targets.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram. The source code runs in 2D
and higher dimensions. Qhull implements the Quickhull algorithm for computing
the convex hull. It handles roundoff errors from floating point arithmetic. It
computes volumes, surface areas, and approximations to the convex hull.

Qhull does not support constrained Delaunay triangulations, triangulation of
non-convex surfaces, mesh generation of non-convex objects, or medium-sized
inputs in 9-D and higher.

%package -n %{libname}
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
Group:          System/Libraries

%description -n %{libname}
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram. The source code runs in 2D
and higher dimensions. Qhull implements the Quickhull algorithm for computing
the convex hull. It handles roundoff errors from floating point arithmetic. It
computes volumes, surface areas, and approximations to the convex hull.

Qhull does not support constrained Delaunay triangulations, triangulation of
non-convex surfaces, mesh generation of non-convex objects, or medium-sized
inputs in 9-D and higher.

%package -n qhull_r-devel
Summary:        Development and documentation files for qhull
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       qhull-devel = %{version}
Obsoletes:      qhull-devel < %{version}

%description -n qhull_r-devel
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files for the Qhull libraries.

%package -n qhullcpp-devel-static
Summary:        Development and documentation files for qhull - C++ interface
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n qhullcpp-devel-static
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files and static lib for Qhull's C++ interface.

%prep
%setup -q
%patch1 -p1

%build
# Needed for static lib libqhullcpp.a
export CXXFLAGS+=" -ffat-lto-objects"

%cmake \
        -DDOC_INSTALL_DIR="%{_docdir}/%{name}" \
        -DINCLUDE_INSTALL_DIR="%{_includedir}" \
        -DLIB_INSTALL_DIR="%{_lib}" \
        -DBIN_INSTALL_DIR="%{_bindir}" \
        -DMAN_INSTALL_DIR="%{_mandir}/man1/"
%cmake_build qhullcpp

%install
%cmake_install
# Fixup wrong location
%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/cmake %{buildroot}%{_libdir}/
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}/
%endif
rm %{buildroot}%{_docdir}/%{name}/COPYING.txt

# Manually install cpp lib since it isn't installed by make install
find ./ -name "libqhullcpp.a" -print -exec install -m0644 {} %{buildroot}%{_libdir}/ \;

# We don't install static libs for qhull, so don't install the corresponding pkgconfig files either
rm %{buildroot}%{_libdir}/pkgconfig/qhullstatic*.pc

# Remove deprecated qhull headers
rm -fr %{buildroot}%{_includedir}/libqhull

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING.txt
%{_docdir}/%{name}/
%{_bindir}/qconvex
%{_bindir}/qdelaunay
%{_bindir}/qhalf
%{_bindir}/qhull
%{_bindir}/qvoronoi
%{_bindir}/rbox
%{_mandir}/man1/*

%files -n %{libname}
%license COPYING.txt
%{_libdir}/libqhull_r.so.*

%files -n qhull_r-devel
%{_includedir}/libqhull_r/
%{_libdir}/libqhull_r.so
%{_libdir}/cmake/Qhull
%{_libdir}/pkgconfig/qhull_r.pc

%files -n qhullcpp-devel-static
%{_includedir}/libqhullcpp/
%{_libdir}/libqhullcpp.a
%{_libdir}/pkgconfig/qhullcpp.pc

%changelog
