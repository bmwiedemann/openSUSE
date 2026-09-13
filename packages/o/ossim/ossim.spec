#
# spec file for package ossim
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015 Angelos Tzotsos <tzotsos@opensuse.org>.
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


%define so_ver 2
Name:           ossim
Version:        2.12.1
Release:        0
Summary:        Open Source Software Image Map (OSSIM)
License:        LGPL-3.0-only
URL:            https://trac.osgeo.org/ossim/
Source0:        https://github.com/ossimlabs/ossim/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE ossim-link-system-tiff.patch mpluskal@suse.com -- link the system libtiff via TIFF_LIBRARIES (set by CMake's own FindTIFF, used after dropping the bundled finders)
Patch0:         ossim-link-system-tiff.patch
# PATCH-FIX-UPSTREAM ossim-fix-include-paths.patch gh#ossimlabs/ossim@2350b999 -- Fix <base/...> and relative support_data/ include paths (post-2.12.1 upstream fix)
Patch1:         ossim-fix-include-paths.patch
# PATCH-FIX-UPSTREAM ossim-fix-test-include-paths.patch -- Same include-path bug class in the test sources, not covered upstream yet
Patch2:         ossim-fix-test-include-paths.patch
BuildRequires:  cmake >= 2.8.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  geos-devel
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgeotiff)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(openthreads)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
The OSSIM core utilities.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package devel
Summary:        Header files for the Open Source Software Image Map
Requires:       lib%{name}%{so_ver} = %{version}-%{release}

%description devel
The OSSIM development files.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package -n lib%{name}%{so_ver}
Summary:        Open Source Software Image Map libraries

%description -n lib%{name}%{so_ver}
The OSSIM shared library files.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package sample-data
Summary:        OSSIM data samples files
BuildArch:      noarch

%description sample-data
The OSSIM data samples files for tests.

%prep
%autosetup -p1
# Drop the bundled copies of standard CMake modules: they are stale and break
# against modern CMake (an old CMakeParseArguments shadows the built-in and
# breaks check_type_size; the old Find* modules include each other by path and
# error out). Use the system versions; the ossim-link-system-tiff.patch adapts
# the one spot (TIFF) where the system finder's variable name differs.
for m in CMakeParseArguments FindFreetype FindGit FindHDF5 FindJPEG \
         FindPackageHandleStandardArgs FindPackageMessage FindPostgreSQL \
         FindSubversion FindTIFF; do
    find . -name "$m.cmake" -delete
done
# Fixed interpreter path (no /usr/bin/env) in the installed helper script.
sed -i '1s|^#!/usr/bin/env bash|#!/bin/bash|' apps/ossim-config.in

%build
# vpfutil is old K&R-style C (e.g. an inline "double atof();"), which GCC's
# C23 default rejects with "conflicting types"; build the C parts as gnu17.
export CFLAGS="%{optflags} -std=gnu17"
# Generate a Ninja build (faster for this large C++ library)
# USE_OSSIM_JSONCPP=OFF: 2.12.1 defaults the bundled jsoncpp amalgamation
# ON, but its finder only searches empty OSSIM_*_PREFIX paths; use the
# system jsoncpp as before.
%define __builder ninja
%cmake \
  -DINSTALL_LIBRARY_DIR=%{_libdir} \
  -DUSE_OSSIM_JSONCPP=OFF \
  -DBUILD_OSSIM_FRAMEWORKS=ON \
  -DBUILD_OSSIM_FREETYPE_SUPPORT=ON \
  -DBUILD_OSSIM_MPI_SUPPORT=OFF \
  -DBUILD_OSSIM_ID_SUPPORT=ON \
  -DBUILD_OSSIM_APPS=ON \
  -DBUILD_OSSIM_CURL_APPS=OFF \
  -DBUILD_OSSIM_TESTS=ON \
  -DBUILD_OSSIM_HDF5_SUPPORT=ON \
  -DBUILD_SHARED_LIBS=ON

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n lib%{name}%{so_ver}

%files -n lib%{name}%{so_ver}
%{_libdir}/*.so.%{so_ver}*

%files
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%files sample-data
%{_datadir}/ossim/

%changelog
