#
# spec file for package kokkos
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Christoph Junghans
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


Name:           kokkos
Version:        3.3.00
Release:        0
%define         sover 3_3_0
Summary:        A C++ Performance Portability Programming Library
License:        BSD-3-Clause
Group:          System/Libraries
#no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
ExcludeArch:    %ix86 %arm powerpc %sparc

URL:            https://github.com/kokkos/kokkos
Source0:        https://github.com/kokkos/kokkos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  memory-constraints

%global kokkos_desc \
Kokkos Core implements a programming model in C++ for writing performance \
portable applications targeting all major HPC platforms. For that purpose \
it provides abstractions for both parallel execution of code and data \
management.  Kokkos is designed to target complex node architectures with \
N-level memory hierarchies and multiple types of execution resources. It \
currently can use OpenMP, Pthreads and CUDA as backend programming models.

%description
%{kokkos_desc}

%package -n libkokkos%sover
Summary:        A C++ Performance Portability Programming Library
Group:          System/Libraries
Conflicts:      libkokkos3 <= 3.3.00

%description -n libkokkos%sover
%{kokkos_desc}

This package contains the kokkos library.

%package devel
Summary:        Development package for %{name} packages
Group:          Development/Libraries/C and C++
Requires:       hwloc-devel
Requires:       libkokkos%sover = %{version}-%{release}
Conflicts:      trilinos-devel

%description devel
%{kokkos_desc}

This package contains the development files of %{name}.

%prep
%autosetup

%build
%{cmake} \
  -DKokkos_ENABLE_TESTS=On \
  -DCMAKE_INSTALL_INCLUDEDIR=include/kokkos \
  -DKokkos_ENABLE_AGGRESSIVE_VECTORIZATION=ON \
  -DKokkos_ENABLE_DEPRECATED_CODE=ON \
  -DKokkos_ENABLE_OPENMP=ON \
  -DKokkos_ENABLE_SERIAL=ON \
  -DKokkos_ENABLE_HWLOC=ON \
  ..
%cmake_build

%install
%cmake_install

%check
# OpenMP tests need quite some memory, run up to two tests in parallel, each with half the cores
%limit_build -m 1600
export OMP_NUM_THREADS=$((%{jobs} / 2))
# Recommended for unit tests
export OMP_PROC_BIND=false
export LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:$PWD/build/core/unit_test:${LD_LIBRARY_PATH}"
%ctest --parallel 1 --tests-regex KokkosContainers_UnitTest_OpenMP --timeout 3600
%ctest --parallel 2 --exclude-regex KokkosContainers_UnitTest_OpenMP

%post -n libkokkos%sover -p /sbin/ldconfig
%postun -n libkokkos%sover -p /sbin/ldconfig

%files -n libkokkos%sover
%doc README.md
%license LICENSE
%{_libdir}/libkokkos*.so.3.3.0

%files devel
%{_libdir}/libkokkos*.so
%{_libdir}/cmake/Kokkos
%{_includedir}/kokkos
%{_bindir}/nvcc_wrapper
%{_bindir}/hpcbind
%{_bindir}/kokkos_launch_compiler

%changelog
