#
# spec file for package ginkgo
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define so_ver 1_10_0
Name:           ginkgo
Version:        1.10.0
Release:        0
Summary:        Numerical linear algebra library focusing on solution of sparse linear systems
License:        BSD-3-Clause
URL:            https://ginkgo-project.github.io/
Source:         https://github.com/ginkgo-project/ginkgo/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  memory-constraints
BuildRequires:  metis-devel
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(yaml-cpp)
# 32-bit archs not supported
ExcludeArch:    %ix86 %arm32 ppc

%description
Ginkgo is a high-performance numerical linear algebra library for many-core
systems, with a focus on solution of sparse linear systems. It is implemented
using modern C++ (you will need an at least C++17 compliant compiler to build
it), with GPU kernels implemented for NVIDIA, AMD and Intel GPUs.

%package -n lib%{name}%{so_ver}
Summary:        Numerical linear algebra library for sparse linear systems - shared library

%description -n lib%{name}%{so_ver}
Ginkgo is a high-performance numerical linear algebra library for many-core
systems, with a focus on solution of sparse linear systems.

This package provides the shared libraries for %{name}.

%package devel
Summary:        Headers and sources for developing against ginkgo - a linear algebra library
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       metis-devel
Requires:       cmake(nlohmann_json)
Requires:       cmake(yaml-cpp)

%description devel
Ginkgo is a high-performance numerical linear algebra library for many-core
systems, with a focus on solution of sparse linear systems.

This package provides the headers and sources needed for developing programs
against %{name}.

%prep
%autosetup -p1

%build
%limit_build -m 2000
%cmake -DGINKGO_FAST_TESTS=ON
%cmake_build

%install
%cmake_install
rm -fr %{buildroot}%{_includedir}/CMakeFiles

%check
%ifarch %arm64 %power64
# exclude flaky tests on arm64, power64: https://github.com/ginkgo-project/ginkgo/issues/1866
%ctest --exclude-regex 'cgs_kernels'
%else
# exclude tests that take a long time (>= 1000 s) to run and may time-out
%ctest --exclude-regex '(solver_omp|example_ir-ilu-preconditioned-solver_omp|matrix_omp|gmres_kernels_omp|gcr_kernels_omp)'
%endif

%ldconfig_scriptlets -n lib%{name}%{so_ver}

%files -n lib%{name}%{so_ver}
%license LICENSES/*
%{_libdir}/lib%{name}*.so.%{version}

%files devel
%license LICENSES/*
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.so
%{_libdir}/cmake/Ginkgo/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}*-gdb.py

%changelog
