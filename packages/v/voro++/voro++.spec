#
# spec file for package voro++
#
# Copyright (c) 2014-2017 Christoph Junghans
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           voro++
Version:        0.4.6
Release:        0
Summary:        Voronoi tessellation library
Group:          Productivity/Scientific/Math
License:        BSD-3-Clause
URL:            http://math.lbl.gov/voro++/
Source0:        http://math.lbl.gov/voro++/download/dir/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM voro++-cmake.patch, sent upstream 21.3.14
Patch0:         voro++-cmake.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Voro++ is a software library for carrying out three-dimensional computations
of the Voronoi tessellation. A distinguishing feature of the Voro++ library
is that it carries out cell-based calculations, computing the Voronoi cell for
each particle individually. It is particularly well-suited for applications that
rely on cell-based statistics, where features of Voronoi cells (e.g. volume,
centroid, number of faces) can be used to analyze a system of particles.

%package -n libvoro++0
Summary:        Voronoi tessellation library
Group:          System/Libraries

%description -n libvoro++0
Voro++ is a software library for carrying out three-dimensional computations
of the Voronoi tessellation. A distinguishing feature of the Voro++ library
is that it carries out cell-based calculations, computing the Voronoi cell for
each particle individually. It is particularly well-suited for applications that
rely on cell-based statistics, where features of Voronoi cells (e.g. volume,
centroid, number of faces) can be used to analyze a system of particles.

This package contains the voro++ library.

%package devel
Summary:    Development headers and libraries for voro++
Group:      Development/Libraries/C and C++
Requires:   libvoro++0 = %{version}-%{release}

%description devel
Voro++ is a software library for carrying out three-dimensional computations
of the Voronoi tessellation. A distinguishing feature of the Voro++ library
is that it carries out cell-based calculations, computing the Voronoi cell for
each particle individually. It is particularly well-suited for applications that
rely on cell-based statistics, where features of Voronoi cells (e.g. volume,
centroid, number of faces) can be used to analyze a system of particles.

This package contains development headers and libraries for voro++.

%prep
%setup -q
%patch0 -p0

%build
%{cmake} -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_SKIP_RPATH=1 \
 -DLIB=%{_lib} ..
make %{?_smp_mflags}

%install
%cmake_install

%post -n libvoro++0 -p /sbin/ldconfig
%postun -n libvoro++0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_mandir}/man1/*
%{_bindir}/*

%files -n libvoro++0
%defattr(-,root,root,-)
%doc LICENSE NEWS README
%{_libdir}/libvoro++.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/voro++/
%{_libdir}/libvoro++*.so

%changelog
