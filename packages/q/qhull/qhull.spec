#
# spec file for package qhull
#
# Copyright (c) 2020 SUSE LLC
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

%package devel
Summary:        Development and documentation files for qhull
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files for the Qhull libraries.

%prep
%setup -q
%patch1 -p1

%build
%cmake \
        -DDOC_INSTALL_DIR="%{_docdir}/%{name}" \
        -DINCLUDE_INSTALL_DIR="%{_includedir}" \
        -DLIB_INSTALL_DIR="%{_lib}" \
        -DBIN_INSTALL_DIR="%{_bindir}" \
        -DMAN_INSTALL_DIR="%{_mandir}/man1/"
%cmake_build

%install
%cmake_install
# Fixup wrong location
%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/cmake %{buildroot}%{_libdir}/
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}/
%endif
rm %{buildroot}%{_docdir}/%{name}/COPYING.txt

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

%files devel
%{_includedir}/libqhull/
%{_includedir}/libqhull_r/
%{_includedir}/libqhullcpp/
%{_libdir}/libqhull_r.so
%{_libdir}/cmake/Qhull
%{_libdir}/pkgconfig/qhull*pc

%changelog
