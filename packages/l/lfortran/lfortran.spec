#
# spec file for package lfortran
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%global         sover 0
%global lfortran_desc \
LFortran is a modern open-source (BSD licensed) interactive Fortran \
compiler built on top of LLVM. It can execute user's code interactively \
to allow exploratory work (much like Python, MATLAB or Julia) as well as \
compile to binaries with the goal to run user's code on modern \
architectures such as multi-core CPUs and GPUs.
Name:           lfortran
Version:        0.65.0
Release:        0
Summary:        A modern interactive Fortran compiler built on top of LLVM
# Main code is BSD-3-Clause
# src/libasr/codegen/KaleidoscopeJIT.h is available under the Apache 2.0
# License with LLVM exception
License:        Apache-2.0 WITH LLVM-exception AND BSD-3-Clause
URL:            https://lfortran.org/
Source0:        https://github.com/lfortran/lfortran/releases/download/v%{version}/lfortran-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 8
BuildRequires:  kokkos-devel
BuildRequires:  libzstd-devel-static
BuildRequires:  llvm22-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
# test-only: asr test scripts import toml
BuildRequires:  python3-toml
BuildRequires:  re2c
BuildRequires:  zlib-devel-static
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd)
# spec-cleaner would expand python3-devel to stale versioned pkgconfig() names
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
# kokkos is not link, but only use for backend=cpp
Requires:       kokkos-devel
# Upstream tests fail on other arches (lfortran/lfortran#2981);
# Debian builds this release on arm64, so allow aarch64 too
ExclusiveArch:  x86_64 aarch64

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
# WITH_ZSD is just used to fix static linking of llvm
# not needed on Fedora
# WASM=OFF due to lfortran/lfortran#3899
# WITH_STACKTRACE=OFF like Fedora and upstream CI: ON bakes
# stacktrace providers into stacktrace.cpp.o, which is also bundled
# into the standalone liblfortran_parser/liblfortran_c shared libs
# that link neither LLVM-symbolize nor BFD, failing --no-undefined
%cmake -DWITH_LLVM=ON \
       -DWITH_ZSTD=OFF \
       -DWITH_RUNTIME_LIBRARY=ON \
       -DWITH_FMT=ON \
       -DWITH_JSON=ON \
       -DWITH_KOKKOS=ON \
       -DWITH_STACKTRACE=OFF \
       -DWITH_TARGET_WASM=OFF \
       -DWITH_UNWIND=ON \
       -DWITH_WHEREAMI=ON \
       -DWITH_XEUS=OFF \
       -DWITH_ZLIB=ON \
       ..
%cmake_build

%install
%cmake_install

%check
# tests link with a bare clang, use gcc instead (upstream's own
# LFORTRAN_LINKER escape hatch); clang22 only ships clang-22
export LFORTRAN_LINKER="gcc"
# lfortran/lfortran#2981: the FortranEvaluator complex case fails on
# aarch64 (complex return convention unimplemented for non-x86), run
# the full suite everywhere else
%ifarch aarch64
(cd build && ctest --output-on-failure -E '^test_lfortran$')
./build/src/lfortran/tests/test_lfortran --test-case-exclude='*single complex*'
%else
%ctest
%endif

%ldconfig_scriptlets -n liblfortran%{sover}

%files
%doc README.md
%{_bindir}/lfortran
%{_mandir}/man1/lfortran.1%{?ext_man}

%files -n liblfortran%{sover}
%license LICENSE
%{_libdir}/liblfortran_runtime.so.%{sover}*

%files devel
%dir %{_includedir}/lfortran
%dir %{_includedir}/lfortran/impure
%{_includedir}/lfortran/ISO_Fortran_binding.h
%{_includedir}/lfortran/impure/lfortran_intrinsics.h
%{_libdir}/liblfortran_runtime.so
%{_libdir}/lfortran_*.mod
%dir %{_datadir}/lfortran
%{_datadir}/lfortran/*.py
%{_libdir}/omp_lib.mod

%files devel-static
%{_libdir}/liblfortran_runtime_static.a

%changelog
