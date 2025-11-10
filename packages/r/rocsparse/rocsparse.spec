#
# spec file for package rocsparse
#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
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


%if 0%{?suse_version}
%global rocsparse_name librocsparse1
%else
%global rocsparse_name rocsparse
%endif

%global upstreamname rocSPARSE
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RELEASE
%endif

%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use ninja if it is available
%if 0%{?fedora} || 0%{?suse_version}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

%global cmake_config \\\
  -DCMAKE_CXX_COMPILER=hipcc \\\
  -DCMAKE_C_COMPILER=hipcc \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_BUILD_TYPE=%build_type \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DHIP_PLATFORM=amd \\\
  -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \\\
  -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_FORTRAN_CLIENTS=OFF

Name:           rocsparse
Version:        %{rocm_version}
Release:        8%{?dist}
Summary:        SPARSE implementation for ROCm
URL:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:         0001-rocsparse-offload-compress.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocprim-static

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}
BuildRequires:  libomp-devel
BuildRequires:  rocblas-devel

%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  gcc-fortran
BuildRequires:  gtest
%else
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  python3dist(pyyaml)
%endif

%endif

%if %{with ninja}
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

Provides:       rocsparse = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocSPARSE exposes a common interface that provides Basic
Linear Algebra Subroutines for sparse computation
implemented on top of AMD's Radeon Open eCosystem Platform
ROCm runtime and toolchains. rocSPARSE is created using
the HIP programming language and optimized for AMD's
latest discrete GPUs.

%if 0%{?suse_version}
%package -n %{rocsparse_name}
Summary:        Shared libraries for %{name}

%description -n %{rocsparse_name}
%{summary}

%ldconfig_scriptlets -n %{rocsparse_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{rocsparse_name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# On Tumbleweed Q3,2025
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++14 to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 14)@set(CMAKE_CXX_STANDARD 17)@' {,clients/}CMakeLists.txt

%build
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if %{with test}
    -DCMAKE_MATRICES_DIR=%{_builddir}/rocsparse-test-matrices/
%endif

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocsparse/LICENSE.md

%if %{with test}
mkdir -p %{buildroot}/%{_datadir}/rocsparse/matrices
install -pm 644 %{_builddir}/rocsparse-test-matrices/* %{buildroot}/%{_datadir}/rocsparse/matrices
%endif

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/rocsparse-test
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocsparse-test
%endif
%endif
%endif

%files -n %{rocsparse_name}
%license LICENSE.md
%{_libdir}/librocsparse.so.1{,.*}

%files devel
%doc README.md
%dir %{_libdir}/cmake/rocsparse
%dir %{_includedir}/rocsparse
%{_includedir}/rocsparse/*
%{_libdir}/librocsparse.so
%{_libdir}/cmake/rocsparse/*.cmake

%if %{with test}
%files test
%dir %{_datadir}/rocsparse
%dir %{_libdir}/rocsparse
%{_bindir}/rocsparse*
%{_datadir}/rocsparse/test/rocsparse_*
%{_libdir}/rocsparse/rocsparseio-*
%{_datadir}/rocsparse/matrices/*

%endif

%changelog
