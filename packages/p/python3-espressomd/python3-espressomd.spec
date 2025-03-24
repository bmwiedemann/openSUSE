#
# spec file for package python3-espressomd
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2014 Christoph Junghans
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


# Build with OpenMPI
%if 0%{?suse_version} > 1600 && 0%{?is_opensuse}
%define is_tumbleweed 1
%define boostver      %{nil}
%define pyver         3
%else
%define is_tumbleweed 0
%define boostver      1_75_0
%define pyver         311
%endif
%define mpiver  openmpi4
%define pkgname espresso
%define modname %{pkgname}md
Name:           python3-%{modname}
Version:        4.2.2
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
URL:            http://espressomd.org
Source:         https://github.com/%{modname}/%{pkgname}/releases/download/%{version}/%{pkgname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM numpy.patch gh#espressomd/espresso#4992
Patch0:         numpy.patch
# PATCH-FIX-UPSTREAM cmake.patch gh#espressomd/espresso#4992
Patch1:         cmake.patch
# PATCH-FIX-UPSTREAM https://github.com/espressomd/espresso/commit/2111342
Patch2:         espresso-cython.patch
# According to gh#espressomd/espresso#4537 32bit architectures are not supported any more
ExcludeArch:    %{ix86} armv7l
BuildRequires:  %{mpiver}-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libboost_filesystem%{boostver}-devel
BuildRequires:  libboost_mpi%{boostver}-devel
BuildRequires:  libboost_system%{boostver}-devel
BuildRequires:  libboost_test%{boostver}-devel
BuildRequires:  python%{pyver}-Cython < 3.0.13
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-numpy-devel
BuildRequires:  python%{pyver}-setuptools
%if 0%{?is_tumbleweed}
BuildRequires:  python%{pyver}-scipy
%endif
BuildRequires:  zlib-devel
Provides:       libEspresso4 = %{version}-%{release}
Obsoletes:      libEspresso4 < 4.1
Requires:       python3-numpy

%description
ESPResSo is a highly versatile software package for performing and analyzing
scientific Molecular Dynamics many-particle simulations of coarse-grained
atomistic or bead-spring models as they are used in soft-matter research in
physics, chemistry and molecular biology. It can be used to simulate systems
such as polymers, liquid crystals, colloids, ferrofluids and biological
systems, for example DNA and lipid membranes.

%prep
%autosetup -p1 -n %{pkgname}
# Fix shebang line for pypresso
sed -i -E '1s@^#!/usr/bin/env[[:blank:]]+sh@#!/bin/sh@' src/python/pypresso.cmakein
# skip mpiio test - it fails if invoked with cmake, directly run with python3 -m unittest pass
sed -i '/mpiio\.py/d' testsuite/python/CMakeLists.txt
%if 0%{?is_tumbleweed} == 0
# remove tests that depend on scipy (unavailable in Leap 15.6)
sed -i '/checkpoint_test(/d' testsuite/python/CMakeLists.txt
sed -i '/                MAX_NUM_PROC 1)/d' testsuite/python/CMakeLists.txt
sed -i '/rotation\.py/d' testsuite/python/CMakeLists.txt
sed -i '/reaction_complex\.py/d' testsuite/python/CMakeLists.txt
sed -i '/canonical_ensemble\.py/d' testsuite/python/CMakeLists.txt
sed -i '/lb_pressure_tensor\.py/d' testsuite/python/CMakeLists.txt
sed -i '/analyze_acf\.py/d' testsuite/python/CMakeLists.txt
sed -i '/analyze_distribution\.py/d' testsuite/python/CMakeLists.txt
sed -i '/random_pairs\.py/d' testsuite/python/CMakeLists.txt
sed -i '/oif_volume_conservation\.py/d' testsuite/python/CMakeLists.txt
%endif

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh
# gh#espressomd/espresso#3396
%define _lto_cflags %{nil}

# overwrite .so linker flags on SUSE distros: drop --no-undefined
# we don't install {i,}pypresso scripts as they aren't needed when installing in /usr
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now' \
  -DCMAKE_SKIP_RPATH=ON \
  -DWITH_HDF5=OFF \
  -DLIBDIR=%{_libdir} \
%if 0%{?is_tumbleweed}
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
%else
  -DPYTHON_EXECUTABLE=%{_bindir}/python3.11 \
%endif
  -DPYTHON_INSTDIR=%{python3_sitearch} \
  -DINSTALL_PYPRESSO=ON
%make_jobs

%install
%cmake_install
find %{buildroot}%{python3_sitearch} -name \*.so \
    -exec chrpath -r %{python3_sitearch} '{}' \;

%check
LD_LIBRARY_PATH='%{buildroot}/%{python3_sitearch}/espressomd::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}' make -C build check CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%files
%license COPYING
%doc Readme.md AUTHORS NEWS ChangeLog
%{_bindir}/pypresso
%{python3_sitearch}/espressomd

%changelog
