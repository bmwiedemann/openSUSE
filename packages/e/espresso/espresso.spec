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
%define boostver      1_90_0
%define mypy_sitearch %{python313_sitearch}
%define py_dot_version %(echo %{modern_python} | sed -e 's/^python//' -e 's/\\([0-9]\\)/\\1./')

Name:           espresso
Version:        5.0.0
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
URL:            https://espressomd.org
Source0:        https://github.com/espressomd/espresso/archive/%{version}.tar.gz#/espresso-%{version}.tar.gz
Source1:        https://i10git.cs.fau.de/walberla/walberla/-/archive/3247aa73.tar.gz#/waberla-3247aa73.tar.gz
Source2:        https://github.com/ECP-copa/Cabana/archive/0.7.0.tar.gz#/Cabana-0.7.0.tar.gz
Source3:        https://github.com/highfive-devs/highfive/archive/v3.3.0.tar.gz#/highfive-v3.3.0.tar.gz
Source4:        https://github.com/icl-utk-edu/heffte/archive/v2.4.1.tar.gz#/heffte-v2.4.1.tar.gz
BuildRequires:  %{modern_python}-Cython >= 3.0.4
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
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-openmp-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gsl-devel
BuildRequires:  hdf5-%{mpiver}-devel
BuildRequires:  kokkos-devel
BuildRequires:  libboost_mpi%{boostver}-devel
BuildRequires:  libboost_test%{boostver}-devel
BuildRequires:  nlopt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
Requires:       %{modern_python}-h5py
Requires:       %{modern_python}-numpy
# make sure rpm pulls in the right dependency
Requires:       libhdf5-%{mpiver}
Provides:       libEspresso5 = %{version}-%{release}
Obsoletes:      libEspresso5 < 5.0
Provides:       python3-espressomd = %{version}-%{release}
Obsoletes:      python3-espressomd < %{version}-%{release}
# According to gh#espressomd/espresso#4537 32bit architectures are not supported any more
ExcludeArch:    %{ix86} armv7l

%description
ESPResSo is a highly versatile software package for performing and analyzing
scientific Molecular Dynamics many-particle simulations of coarse-grained
atomistic or bead-spring models as they are used in soft-matter research in
physics, chemistry and molecular biology. It can be used to simulate systems
such as polymers, liquid crystals, colloids, ferrofluids and biological
systems, for example DNA and lipid membranes.

%prep
%setup -q
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%setup -q -T -D -a 3
%setup -q -T -D -a 4
sed -ri "s|GIT_REPOSITORY +https://github.com/ECP-copa/Cabana.git|URL $(realpath Cabana-*/)|" CMakeLists.txt
sed -ri "s|GIT_REPOSITORY +https://github.com/icl-utk-edu/heffte.git|URL $(realpath heffte-*/)|" CMakeLists.txt
sed -ri "s|GIT_REPOSITORY +https://github.com/highfive-devs/highfive.git|URL $(realpath highfive-*/)|" CMakeLists.txt
sed -ri "s|GIT_REPOSITORY +https://i10git.cs.fau.de/walberla/walberla.git|URL $(realpath walberla-*/)|" CMakeLists.txt
# Fix shebang line for pypresso
sed -i -E '1s@^#!%{_bindir}/env[[:blank:]]+sh@#!/bin/sh@' src/python/pypresso.cmakein
# skip mpiio test - it fails if invoked with cmake, directly run with python3 -m unittest pass
sed -i '/mpiio\.py/d' testsuite/python/CMakeLists.txt
# skip long tests to avoid timeouts
sed -i 's/add_dependencies(check check_python)/add_dependencies(check check_python_skip_long)/' testsuite/python/CMakeLists.txt
# use 1 thread by default in the Python testsuite
sed -i 's/set(TEST_NUM_THREADS 2)/set(TEST_NUM_THREADS 1)/' testsuite/python/CMakeLists.txt
# silence GCC's C++17 processor-specific ABI warning
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=94383
%ifarch ppc64le
sed -i 's/,arm>>:-Wno-psabi>/,powerpc64le>>:-Wno-psabi>/' CMakeLists.txt
%endif
# enable all features except expensive assertions
sed -i '/#define ADDITIONAL_CHECKS/d' maintainer/configs/maxset.hpp

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh
# gh#espressomd/espresso#3396
%define _lto_cflags %{nil}

# overwrite .so linker flags on SUSE distros: drop --no-undefined
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now' \
  -DCMAKE_SKIP_RPATH=ON \
  -DESPRESSO_MYCONFIG_FILE=maintainer/configs/maxset.hpp \
  -DESPRESSO_BUILD_TESTS=ON \
  -DESPRESSO_CTEST_ARGS=-j1 \
  -DESPRESSO_TEST_TIMEOUT=600 \
%ifarch ppc64le
  -DESPRESSO_TEST_NP=3 \
%endif
  -DESPRESSO_BUILD_WITH_PYTHON=ON \
  -DESPRESSO_BUILD_WITH_CUDA=OFF \
  -DESPRESSO_BUILD_WITH_FFTW=ON \
  -DESPRESSO_BUILD_WITH_WALBERLA=ON \
  -DESPRESSO_BUILD_WITH_WALBERLA_AVX=OFF \
  -DESPRESSO_BUILD_WITH_SHARED_MEMORY_PARALLELISM=ON \
  -DESPRESSO_BUILD_WITH_NLOPT=ON \
  -DESPRESSO_BUILD_WITH_HDF5=OFF \
  -DESPRESSO_BUILD_WITH_GSL=ON \
  -DESPRESSO_BUILD_WITH_SCAFACOS=OFF \
  -DESPRESSO_BUILD_WITH_STOKESIAN_DYNAMICS=OFF \
  -DESPRESSO_MODULE_INSTALL_PATH=%{mypy_sitearch} \
  -DESPRESSO_INSTALL_PYPRESSO=ON

%cmake_build espresso_packaging_dependencies
cd ..

%install
%cmake_install
find %{buildroot}%{mypy_sitearch} -name \*.so \
    -exec chrpath -r %{mypy_sitearch} '{}' \;
rm -rf %{buildroot}/usr/include
rm -rf %{buildroot}/usr/share/heffte
rm -rf %{buildroot}/usr/share/cmake
rm -rf %{buildroot}/usr/walberla
rm -rf %{buildroot}/usr/lib64/cmake
rm -rf %{buildroot}/usr/lib64/libheffte.a
rm -rf %{buildroot}/usr/lib64/pkgconfig/Cabana.pc
rm -rf %{buildroot}%{mypy_sitearch}/object_in_fluid

%check
export LD_LIBRARY_PATH='%{buildroot}/%{mypy_sitearch}/espressomd::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}'
%make_build -C build check CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%files
%license COPYING
%doc Readme.md AUTHORS CITATION.cff CHANGELOG.md
%{_bindir}/pypresso
%{mypy_sitearch}/espressomd

%changelog
