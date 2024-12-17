#
# spec file for package lfortran
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Version:        0.42.0
%global         sover 0
Name:           lfortran
Release:        0
Summary:        A modern interactive Fortran compiler built on top of LLVM

# Main code is BSD-3-Clause
# src/libasr/codegen/KaleidoscopeJIT.h is available under the Apache 2.0
# License with LLVM exception
License:        Apache-2.0 WITH LLVM-exception AND BSD-3-Clause
URL:            https://lfortran.org/
Source0:        https://lfortran.github.io/tarballs/release/lfortran-%{version}.tar.gz

# https://github.com/lfortran/lfortran/issues/2981
ExclusiveArch:  x86_64

BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++ >= 8
BuildRequires:  kokkos-devel
BuildRequires:  nlohmann_json-devel
# kokkos is not link, but only use for backend=cpp
Requires:       kokkos-devel
BuildRequires:  libffi-devel
BuildRequires:  libunwind-devel
BuildRequires:  libuuid-devel
BuildRequires:  libzstd-devel
BuildRequires:  libzstd-devel-static
BuildRequires:  llvm18-devel
BuildRequires:  python3-devel
BuildRequires:  rapidjson-devel
BuildRequires:  re2c
BuildRequires:  zlib-devel
BuildRequires:  zlib-devel-static

%global lfortran_desc \
LFortran is a modern open-source (BSD licensed) interactive Fortran \
compiler built on top of LLVM. It can execute user's code interactively \
to allow exploratory work (much like Python, MATLAB or Julia) as well as \
compile to binaries with the goal to run user's code on modern \
architectures such as multi-core CPUs and GPUs.

%description
%{lfortran_desc}

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblfortran%{sover}%{?_isa} = %{version}-%{release}

%description devel
%{lfortran_desc}

This package contains development headers and libraries for %{name}.

%package -n liblfortran%{sover}
Summary:        %{name} runtime library

%description -n liblfortran%{sover}
%{lfortran_desc}

This package contains shared runtime libraries of %{name}.

%package devel-static
Summary:        %{name} static runtime library
Requires:       %{name}-devel = %{version}

%description devel-static
%{lfortran_desc}

This package contains static runtime library for %{name}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_PREFIX_PATH=%{_libdir}/llvm18/ \
       -DWITH_LLVM=ON \
       -DWITH_RUNTIME_LIBRARY=ON \
       -DWITH_FMT=ON \
       -DWITH_JSON=ON \
       -DWITH_KOKKOS=ON \
       -DWITH_STACKTRACE=OFF \
       -DWITH_UNWIND=ON \
       -DWITH_WHEREAMI=OFF \
       -DWITH_XEUS=OFF \
       -DWITH_ZLIB=ON \
       ..
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n liblfortran%sover

%files
%doc README.md
%{_bindir}/lfortran
%{_mandir}/man1/lfortran.1.*

%files -n liblfortran%{sover}
%license LICENSE
%{_libdir}/liblfortran_runtime.so.%{sover}*

%files devel
%dir %{_includedir}/lfortran
%dir %{_includedir}/lfortran/impure
%{_includedir}/lfortran/impure/lfortran_intrinsics.h
%{_libdir}/liblfortran_runtime.so
%{_libdir}/lfortran_*.mod
%dir %{_datadir}/lfortran
%{_datadir}/lfortran/*.py
%{_libdir}/omp_lib.mod

%files devel-static
%{_libdir}/liblfortran_runtime_static.a

%changelog
