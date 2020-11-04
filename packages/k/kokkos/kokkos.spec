#
# spec file for package kokkos
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.2.00
Release:        0
%define         sover 3
Summary:        A C++ Performance Portability Programming 
#no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
License:        BSD-3-Clause
Group:          System/Libraries
ExcludeArch:    %ix86 %arm

URL:            https://github.com/kokkos/kokkos
Source0:        https://github.com/kokkos/kokkos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 3308.patch - fix naming of printer-tool 
Patch0:         https://github.com/kokkos/kokkos/pull/3308.patch

BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel

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
Summary:        Kokkos library
Group:          System/Libraries

%description -n libkokkos%sover
%{kokkos_desc}

This package contains the kokkos library.

%package devel
Summary:        Development package for  %{name} packages
Group:          System/Libraries
Requires:       hwloc-devel
Requires:       libkokkos%sover = %{version}-%{release}
Conflicts:      trilinos-devel

%description devel
%{kokkos_desc}

This package contains the development files of %{name}.

%prep
%setup -q
%patch0 -p1

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
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:$PWD/build/core/unit_test:${LD_LIBRARY_PATH}" make -C build test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs}

%post -n libkokkos%sover -p /sbin/ldconfig
%postun -n libkokkos%sover -p /sbin/ldconfig

%files -n libkokkos%sover
%doc README.md
%license LICENSE
%{_libdir}/libkokkos*.so.%{sover}*

%files devel
%{_libdir}/libkokkos*.so
%{_libdir}/cmake/Kokkos
%{_includedir}/kokkos
%{_bindir}/nvcc_wrapper

%changelog
