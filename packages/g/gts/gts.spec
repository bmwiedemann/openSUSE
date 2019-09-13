#
# spec file for package gts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define libname libgts-0_7-5
%define snapshot_date 121130
Name:           gts
Version:        0.7.6_p20%{snapshot_date}
Release:        0
Summary:        GNU Triangulated Surface Library (GTS)
License:        LGPL-2.0+
Group:          Development/Libraries/C and C++
Source0:        http://%{name}.sourceforge.net/tarballs/%{name}-snapshot-%{snapshot_date}.tar.gz
Url:            http://gts.sourceforge.net/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libnetpbm-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{libname} = %{version}

%description
GTS stands for the GNU Triangulated Surface Library. It is an Open
Source Free Software Library intended to provide a set of useful
functions to deal with 3D surfaces meshed with interconnected
triangles.

A brief summary of its main features:

  * Simple object-oriented structure giving easy access to topological
    properties.
  * 2D dynamic Delaunay and constrained Delaunay triangulations.
  * Robust geometric predicates (orientation, in circle) using fast
    adaptive floating point arithmetic (adapted from the fine work of
    Jonathan R.  Shewchuk).
  * Robust set operations on surfaces (union, intersection, difference).
  * Surface refinement and coarsening (multiresolution models).
  * Dynamic view-independent continuous level-of-detail.
  * Preliminary support for view-dependent level-of-detail.
  * Bounding-boxes trees and Kd-trees for efficient point location and
    collision/intersection detection.
  * Graph operations: traversal, graph partitioning. 
  * Metric operations (area, volume, curvature ...). 
  * Triangle strips generation for fast rendering. 


%package -n     %{libname}
Summary:        GTS Runtime Library
Group:          System/Libraries

%description -n %{libname}
This package provides the GTS runtime library.


%package devel
Summary:        Development files and documentation for GTS
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Requires:       gcc
Requires:       gcc-c++
Requires:       glib2-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that use GTS.

%prep
%setup -q -n %{name}-snapshot-%{snapshot_date}
%{?suse_update_config:%{suse_update_config -f}}

%build
%configure \
	--disable-static

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/*.la

# Seems to fail randomly
#%%check
#chmod +x test/*/*.sh
#make check

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/delaunay
%{_bindir}/gts2dxf
%{_bindir}/gts2oogl
%{_bindir}/gts2stl
%{_bindir}/gtscheck
%{_bindir}/gts-config
%{_bindir}/gtscompare
%{_bindir}/gtstemplate
%{_bindir}/stl2gts
%{_bindir}/transform
%{_bindir}/gts2xyz
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgts-0.7.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/gts.h
%{_includedir}/gtsconfig.h
%{_bindir}/happrox
%{_libdir}/libgts.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
