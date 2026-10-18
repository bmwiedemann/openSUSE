#
# spec file for package openvdb
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2026 LISA GmbH, Bingen, Germany.
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


%define libname libopenvdb13_1
%if 0%{?suse_version} <= 1500
# force a recent gcc version on 15.X, default would be gcc7 which is too old
%define gcc_major 14
%endif
%bcond_without nanovdb
# whines about LLVM apis
%bcond_with    openvdb_ax
# requires nanobind
%bcond_with    pyopenvdb
#
%bcond_without openvdb_tool
Name:           openvdb
Version:        13.1.0
Release:        0
Summary:        Sparse volume data structure and tools
License:        Apache-2.0
URL:            https://www.openvdb.org
Source:         https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-tool-building.patch
BuildRequires:  cmake >= 3.24
BuildRequires:  gcc%{?gcc_major}-c++ >= 11
BuildRequires:  libboost_iostreams-devel-impl >= 1.82
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Imath) >= 3.2
BuildRequires:  pkgconfig(OpenEXR) >= 3.2
BuildRequires:  pkgconfig(blosc) >= 1.17.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3) >= 3.3
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(log4cpp)
BuildRequires:  pkgconfig(tbb) >= 2020.3
# 32-bit: linker errors
ExcludeArch:    %{ix86} %{arm32}
%if %{with openvdb_ax}
BuildRequires:  cmake(LLVM) < 16
%endif
%if %{with pyopenvdb}
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(python3-embed)
%endif
%if %{with openvdb_tool}
BuildRequires:  cmake(Alembic) >= 1.8.8
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(tinfo)
%endif

%description
OpenVDB is a C++ library comprising a hierarchical data structure and
a large suite of tools for the efficient storage and manipulation of
sparse volumetric data discretized on three-dimensional grids.

%package -n %{libname}
Summary:        Sparse volume data structure library

%description -n %{libname}
OpenVDB is a C++ library comprising a hierarchical data structure and
a large suite of tools for the efficient storage and manipulation of
sparse volumetric data discretized on three-dimensional grids.

%package devel
Summary:        Development files for openvdb
Requires:       %{libname} = %{version}
Requires:       libboost_headers-devel-impl

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%package tools
Summary:        OpenVDB command line tools
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
    -DUSE_EXR=ON \
    -DUSE_PNG=ON \
%if %{with openvdb_ax}
    -DOPENVDB_BUILD_AX=ON \
    -DOPENVDB_BUILD_VDB_AX=ON \
%endif
    -DOPENVDB_BUILD_VDB_PRINT=ON \
    -DOPENVDB_BUILD_VDB_LOD=ON \
    -DOPENVDB_BUILD_VDB_VIEW=ON \
    -DOPENVDB_BUILD_VDB_RENDER=ON \
%if %{with openvdb_tool}
    -DOPENVDB_BUILD_VDB_TOOL=ON \
    -DOPENVDB_TOOL_USE_ABC:BOOL=ON \
    -DOPENVDB_TOOL_USE_JPG:BOOL=ON \
    -DOPENVDB_TOOL_USE_NANO:BOOL=OFF \
    -DOPENVDB_TOOL_USE_PNG:BOOL=ON \
%endif
%if %{with pyopenvdb}
    -DOPENVDB_BUILD_PYTHON_MODULE=ON \
%else
    -DOPENVDB_BUILD_PYTHON_MODULE=OFF \
%endif
    -DOPENVDB_ENABLE_RPATH=OFF

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

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
%{_bindir}/vdb_tool
%if %{with nanovdb}
%{_bindir}/nanovdb_print
%{_bindir}/nanovdb_validate
%endif

%changelog
