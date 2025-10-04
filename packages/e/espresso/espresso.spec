#
# spec file for package espresso
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


%define mpiver  openmpi4
%define pkgname espresso
%define modname %{pkgname}md
# Build with OpenMPI
%if 0%{?suse_version} > 1600 && 0%{?is_opensuse}
%bcond_without scipy
%define boostver      %{nil}
%define mypy_sitearch %{python3_sitearch}
%else
%bcond_with scipy
%define boostver      1_75_0
%define mypy_sitearch %{python311_sitearch}
%endif
%define py_dot_version %(echo %{modern_python} | sed -e 's/^python//' -e 's/\\([0-9]\\)/\\1./')

Name:           espresso
Version:        4.2.2
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
URL:            https://espressomd.org
Source:         https://github.com/espressomd/espresso/releases/download/%{version}/%{pkgname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM numpy.patch gh#espressomd/espresso#4992
Patch0:         numpy.patch
# PATCH-FIX-UPSTREAM cmake.patch gh#espressomd/espresso#4992
Patch1:         cmake.patch
# PATCH-FIX-UPSTREAM https://github.com/espressomd/espresso/commit/2111342
Patch2:         espresso-cython.patch
# PATCH-FIX-OPENSUSE - Boost.System is headers only since 1.69.0
Patch3:         espresso-boost-system.patch
BuildRequires:  %{modern_python}-Cython < 3.0.13
BuildRequires:  %{modern_python}-Sphinx
BuildRequires:  %{modern_python}-devel
BuildRequires:  %{modern_python}-h5py
BuildRequires:  %{modern_python}-numpy-devel
BuildRequires:  %{modern_python}-scipy
BuildRequires:  %{modern_python}-setuptools
# Currently libboost_mpi-devel and hdf5 use different mpi versions
# BuildRequires:  hdf5-devel
BuildRequires:  %{mpiver}-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gsl-devel
BuildRequires:  hdf5-%{mpiver}-devel
BuildRequires:  libboost_filesystem%{boostver}-devel
BuildRequires:  libboost_mpi%{boostver}-devel
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system%{boostver}-devel
%endif
BuildRequires:  libboost_test%{boostver}-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
Requires:       %{modern_python}-h5py
Requires:       %{modern_python}-numpy
# make sure rpm pulls in the right dependency
Requires:       libhdf5-%{mpiver}
Provides:       libEspresso4 = %{version}-%{release}
Obsoletes:      libEspresso4 < 4.1
Provides:       python3-espressomd = %{version}-%{release}
Obsoletes:      python3-espressomd < %{version}-%{release}
# According to gh#espressomd/espresso#4537 32bit architectures are not supported any more
ExcludeArch:    %{ix86} armv7l
%if %{with scipy}
BuildRequires:  %{modern_python}-scipy
%endif

%description
ESPResSo is a highly versatile software package for performing and analyzing
scientific Molecular Dynamics many-particle simulations of coarse-grained
atomistic or bead-spring models as they are used in soft-matter research in
physics, chemistry and molecular biology. It can be used to simulate systems
such as polymers, liquid crystals, colloids, ferrofluids and biological
systems, for example DNA and lipid membranes.

%prep
%setup -q -n %{pkgname}
%patch -P0 -P1 -P2 -p1
%if 0%{?suse_version} >= 1600
%patch -P3 -p1
%endif
# Fix shebang line for pypresso
sed -i -E '1s@^#!%{_bindir}/env[[:blank:]]+sh@#!/bin/sh@' src/python/pypresso.cmakein
# skip mpiio test - it fails if invoked with cmake, directly run with python3 -m unittest pass
sed -i '/mpiio\.py/d' testsuite/python/CMakeLists.txt
%if %{without scipy}
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
  -DPYTHON_EXECUTABLE=%{_bindir}/python%{py_dot_version} \
  -DPYTHON_INCLUDE_DIRS=%{_includedir}/python%{py_dot_version} \
  -DPYTHON_INSTDIR=%{mypy_sitearch} \
  -DINSTALL_PYPRESSO=ON

%cmake_build
cd ..

%install
%cmake_install
find %{buildroot}%{mypy_sitearch} -name \*.so \
    -exec chrpath -r %{mypy_sitearch} '{}' \;

%check
export LD_LIBRARY_PATH='%{buildroot}/%{mypy_sitearch}/espressomd::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}'
%make_build -C build check CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%files
%license COPYING
%doc Readme.md AUTHORS NEWS ChangeLog
%{_bindir}/pypresso
%{mypy_sitearch}/espressomd

%changelog
