#
# spec file for package openvdb
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020 LISA GmbH, Bingen, Germany.
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


%define libname libopenvdb7_1

Name:           openvdb
Version:        7.1.0
Release:        0
Summary:        Sparse volume data structure and tools
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.openvdb.org
Source:         https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  glu-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libglfw-devel
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  pkgconfig(IlmBase)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(jemalloc)

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

%description	devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%package tools
Summary:        OpenVDB command line tools
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description	tools
This package contains the command line utilites that come with the OpenVDB
library: vdb_lod, vdb_print, vdb_render, vdb_view

%prep
%setup -q

# fix 64bit library path
%if "%{_lib}" == "lib64"
sed -i 's/lib$/lib64/g' openvdb/CMakeLists.txt
%endif

%build
# -DCMAKE_NO_SYSTEM_FROM_IMPORTED:BOOL=TRUE is needed,
# will bail out with: stdlib.h not found otherwise
%cmake \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC " \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC " \
    -DCMAKE_NO_SYSTEM_FROM_IMPORTED:BOOL=TRUE \
    -DOPENVDB_BUILD_VDB_PRINT=ON \
    -DOPENVDB_BUILD_VDB_LOD=ON \
    -DOPENVDB_BUILD_VDB_RENDER=ON \
    -DOPENVDB_BUILD_VDB_VIEW=ON \
    -DOPENVDB_BUILD_PYTHON_MODULE=OFF \
    -DOPENVDB_ENABLE_RPATH=OFF \
    -DUSE_EXR=ON

make %{?_smp_mflags}

%install
%cmake_install
# remove static lib
rm %{buildroot}%{_libdir}/libopenvdb.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/OpenVDB
%{_libdir}/*.so

%files tools
%license LICENSE
%{_bindir}/vdb_lod
%{_bindir}/vdb_print
%{_bindir}/vdb_render
%{_bindir}/vdb_view

%changelog
