#
# spec file for package openvdb
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024 LISA GmbH, Bingen, Germany.
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


%bcond_without nanovdb

%define libname libopenvdb10_1
%if 0%{suse_version} <= 1500
# force a recent gcc version on 15.X, default would be gcc7 which is too old
%define gcc_major 10
%endif

Name:           openvdb
Version:        10.1.0
Release:        0
Summary:        Sparse volume data structure and tools
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.openvdb.org
Source:         https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         openvdb-boost-static-assert-include.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc%{?gcc_major}-c++ >= 9.3.1
BuildRequires:  libboost_iostreams-devel-impl >= 1.70
BuildRequires:  libboost_system-devel-impl >= 1.70
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel >= 2020.3
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jemalloc)
# 32-bit: linker errors
ExcludeArch:    %ix86 %arm32

%description
OpenVDB is a C++ library comprising a hierarchical data structure and
a large suite of tools for the efficient storage and manipulation of
sparse volumetric data discretized on three-dimensional grids.

%package -n %{libname}
Summary:        Sparse volume data structure library
Group:          System/Libraries

%description -n %{libname}
OpenVDB is a C++ library comprising a hierarchical data structure and
a large suite of tools for the efficient storage and manipulation of
sparse volumetric data discretized on three-dimensional grids.

%package devel
Summary:        Development files for openvdb
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libboost_headers-devel-impl

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%package tools
Summary:        OpenVDB command line tools
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description tools
This package contains the command line utilites that come with the OpenVDB
library: vdb_lod, vdb_print, vdb_render, vdb_view

%prep
%setup -q
%autopatch -p1

%build
%limit_build -m 3072
# -DCMAKE_NO_SYSTEM_FROM_IMPORTED:BOOL=TRUE is needed,
# will bail out with: stdlib.h not found otherwise
%cmake \
    -DCMAKE_CXX_STANDARD=17 \
%{?gcc_major:-DCMAKE_C_COMPILER=gcc-%{gcc_major} -DCMAKE_CXX_COMPILER=g++-%{gcc_major}} \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC " \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC " \
    -DCMAKE_NO_SYSTEM_FROM_IMPORTED:BOOL=TRUE \
    -DOPENVDB_CORE_STATIC:BOOL=OFF \
%if %{with nanovdb}
    -DUSE_NANOVDB=ON \
%endif
    -DOPENVDB_BUILD_VDB_PRINT=ON \
    -DOPENVDB_BUILD_VDB_LOD=ON \
    -DOPENVDB_BUILD_VDB_VIEW=ON \
    -DOPENVDB_BUILD_VDB_RENDER=ON \
    -DOPENVDB_BUILD_PYTHON_MODULE=OFF \
    -DOPENVDB_ENABLE_RPATH=OFF

%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}
%if %{with nanovdb}
%{_includedir}/nanovdb
%endif
%{_libdir}/cmake/OpenVDB
%{_libdir}/*.so

%files tools
%license LICENSE
%{_bindir}/vdb_lod
%{_bindir}/vdb_print
%{_bindir}/vdb_view
%{_bindir}/vdb_render
%if %{with nanovdb}
%{_bindir}/nanovdb_print
%{_bindir}/nanovdb_validate
%endif

%changelog
