#
# spec file for package qhull
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sonum   7
%define srcyear 2015
%define srcver  7.2.0
%define libver  7_2_0
Name:           qhull
Version:        2015.2
Release:        0
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
License:        Qhull
Group:          Development/Libraries/C and C++
Url:            http://www.qhull.org
Source0:        http://www.qhull.org/download/qhull-%{srcyear}-src-%{srcver}.tgz
BuildRequires:  cmake
BuildRequires:  gcc-c++
Requires:       libqhull%{sonum}-%{libver} = %{version}

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

%package -n libqhull%{sonum}-%{libver}
Summary:        Computing convex hulls, Delaunay triangulations and Voronoi diagrams
Group:          System/Libraries

%description -n libqhull%{sonum}-%{libver}
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
Requires:       qhull = %{version}

%description devel
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files for the Qhull libraries.

%prep
%setup -q

%build
%cmake \
        -DDOC_INSTALL_DIR="%{_docdir}/%{name}" \
        -DINCLUDE_INSTALL_DIR="%{_includedir}" \
        -DLIB_INSTALL_DIR"=%{_libdir}" \
        -DBIN_INSTALL_DIR="%{_bindir}" \
        -DMAN_INSTALL_DIR="%{_mandir}/man1/"
%make_jobs

%install
%cmake_install
rm %{buildroot}%{_libdir}/*.a

%post -n libqhull%{sonum}-%{libver} -p /sbin/ldconfig
%postun -n libqhull%{sonum}-%{libver} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc Announce.txt COPYING.txt README.txt REGISTER.txt
%{_docdir}/%{name}/
%{_bindir}/qconvex
%{_bindir}/qdelaunay
%{_bindir}/qhalf
%{_bindir}/qhull
%{_bindir}/qvoronoi
%{_bindir}/rbox
%{_mandir}/man1/*

%files -n libqhull%{sonum}-%{libver}
%defattr(-,root,root)
%doc COPYING.txt
%{_libdir}/libqhull.so.%{sonum}
%{_libdir}/libqhull.so.%{srcver}
%{_libdir}/libqhull_p.so.%{sonum}
%{_libdir}/libqhull_p.so.%{srcver}
%{_libdir}/libqhull_r.so.%{sonum}
%{_libdir}/libqhull_r.so.%{srcver}

%files devel
%defattr(-,root,root)
%doc COPYING.txt
%{_includedir}/libqhull/
%{_includedir}/libqhull_r/
%{_includedir}/libqhullcpp/
%{_libdir}/libqhull.so
%{_libdir}/libqhull_p.so
%{_libdir}/libqhull_r.so

%changelog
