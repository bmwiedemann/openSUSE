#
# spec file for package kokkos
#
# Copyright (c) 2024 SUSE LLC
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


%define major_ver 4
%define minor_ver 3
%define patch_ver 00
%define shlib   libkokkos-%{major_ver}_%{minor_ver}
%global kokkos_desc \
Kokkos Core implements a programming model in C++ for writing performance \
portable applications targeting all major HPC platforms. For that purpose \
it provides abstractions for both parallel execution of code and data \
management.  Kokkos is designed to target complex node architectures with \
N-level memory hierarchies and multiple types of execution resources. It \
currently can use OpenMP, Pthreads and CUDA as backend programming models.

Name:           kokkos
Version:        %{major_ver}.%{minor_ver}.%{patch_ver}
Release:        0
Summary:        A C++ Performance Portability Programming
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/kokkos/kokkos
Source0:        kokkos-%{version}.tar.gz
BuildRequires:  cmake >= 3.16
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hwloc-devel
BuildRequires:  memory-constraints
BuildRequires:  ninja
#no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
ExcludeArch:    %{ix86} %{arm} powerpc %{sparc}

%description
%{kokkos_desc}

%package -n %{shlib}
Summary:        A C++ Performance Portability Programming Library
Group:          System/Libraries

%description -n %{shlib}
%{kokkos_desc}

This package contains the kokkos library.

%package devel
Summary:        Development package for  %{name} packages
Group:          System/Libraries
Requires:       %{shlib} = %{version}-%{release}
Requires:       hwloc-devel
Conflicts:      trilinos-devel

%description devel
%{kokkos_desc}

This package contains the development files of %{name}.

%prep
%setup -q
sed -i '1c #!/usr/bin/bash' bin/hpcbind bin/runtest
sed -i '1s|/usr/bin/env bash|/usr/bin/bash|' bin/kokkos_launch_compiler bin/nvcc_wrapper

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%global __builder ninja

%cmake \
  -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
%if 0%{?suse_version} <= 1500
  -DCMAKE_CXX_COMPILER=g++-11 \
%endif
  -DCMAKE_CXX_FLAGS=-pthread \
  -DCMAKE_INSTALL_INCLUDEDIR=include/kokkos \
  -DKokkos_ENABLE_AGGRESSIVE_VECTORIZATION=ON \
  -DKokkos_ENABLE_DEPRECATED_CODE_4=ON \
  -DKokkos_ENABLE_DEPRECATION_WARNINGS=OFF \
  -DKokkos_ENABLE_HWLOC=ON \
  -DKokkos_ENABLE_TESTS=ON \
  -DKokkos_ENABLE_SERIAL=ON \
  -DKokkos_ENABLE_OPENMP=ON \
  %{nil}
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:$PWD/build/core/unit_test:${LD_LIBRARY_PATH}"
export OMP_PROC_BIND=false
%ctest --parallel 4 --exclude-regex 'Kokkos_CoreUnitTest_OpenMP|Kokkos_Containers*|Kokkos_Algorithms*'

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%doc README.md
%license LICENSE
%{_libdir}/libkokkos*.so.%{major_ver}.%{minor_ver}*

%files devel
%{_libdir}/libkokkos*.so
%{_libdir}/cmake/Kokkos
%{_includedir}/kokkos
%{_bindir}/nvcc_wrapper
%{_bindir}/hpcbind
%{_bindir}/kokkos_launch_compiler

%changelog
