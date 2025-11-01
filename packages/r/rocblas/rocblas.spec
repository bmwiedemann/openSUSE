#
# spec file for package rocblas
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
%global rocblas_name librocblas4
%else
%global rocblas_name rocblas
%endif

%global upstreamname rocBLAS
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
%global build_type RelWithDebInfo
%endif

%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif

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

# Tensile in 6.4 does not support generics
# https://github.com/ROCm/Tensile/issues/2124
%if 0%{?suse_version}
# not in tw
%bcond_with tensile
%else
%bcond_without tensile
%endif

%if %{with tensile}
%global build_tensile ON
%else
%global build_tensile OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# SUSE/OSB times out because -O is added to the make args
# This accumulates all the output from the long running tensile
# jobs.
%global _make_output_sync %{nil}

# OracleLinux 9 has a problem with it's strip not recognizing *.co's
%global __strip %rocmllvm_bindir/llvm-strip

# Use ninja if it is available
# Ninja is available on suse but obs times out with ninja build, make doesn't
%if 0%{?fedora}
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
  -DBLAS_INCLUDE_DIR=%{_includedir}/%{blaslib} \\\
  -DBLAS_LIBRARY=%{blaslib} \\\
  -DCMAKE_CXX_COMPILER=hipcc \\\
  -DCMAKE_C_COMPILER=hipcc \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DCMAKE_VERBOSE_MAKEFILE=ON \\\
  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DHIP_PLATFORM=amd \\\
  -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_FORTRAN_CLIENTS=OFF \\\
  -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \\\
  -DBUILD_WITH_HIPBLASLT=OFF \\\
  -DTensile_COMPILER=hipcc \\\
  -DTensile_CPU_THREADS=${CORES} \\\
  -DTensile_LIBRARY_FORMAT=%{tensile_library_format} \\\
  -DTensile_VERBOSE=%{tensile_verbose} \\\
  -DTensile_DIR=${TP}/cmake \\\
  -DBUILD_WITH_PIP=OFF

%bcond_with generic
%global rocm_gpu_list_generic "gfx9-generic;gfx9-4-generic;gfx10-1-generic;gfx10-3-generic;gfx11-generic;gfx12-generic"
%if %{with generic}
%global gpu_list %{rocm_gpu_list_generic}
%else
%global gpu_list %{rocm_gpu_list_default}
%endif

Name:           rocblas
Version:        %{rocm_version}
Release:        10%{?dist}
Summary:        BLAS implementation for ROCm
URL:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        BSD-3-Clause AND MIT

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch2:         0001-fixup-install-of-tensile-output.patch
Patch4:         0001-offload-compress-option.patch
Patch6:         0001-rocblas-remove-roctracer.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel

%if %{with tensile}
%if 0%{?suse_version}
BuildRequires:  msgpack-cxx-devel
%global tensile_library_format msgpack
# OBS vm times out without console output
%global tensile_verbose 2
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module tensile-devel}
%else
BuildRequires:  python3dist(tensile)
%if 0%{?rhel}
%global tensile_verbose 2
%global tensile_library_format yaml
%else
BuildRequires:  msgpack-devel
%global tensile_verbose 1
%global tensile_library_format msgpack
%endif
%endif # suse_version
%else
%global tensile_verbose %{nil}
%global tensile_library_format %{nil}
%endif # tensile

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}

BuildRequires:  libomp-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocminfo

%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  gcc-fortran
BuildRequires:  gtest
BuildRequires:  openblas-devel
%global blaslib openblas
%else
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  python3dist(pyyaml)
%if 0%{?rhel}
BuildRequires:  flexiblas-devel
%global blaslib flexiblas
%else
BuildRequires:  blas-devel
%global blaslib cblas
%endif
%endif
%endif

%if %{with ninja}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

Provides:       rocblas = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

%if 0%{?suse_version}
%package -n %{rocblas_name}
Summary:        Shared libraries for %{name}

%description -n %{rocblas_name}
%{summary}

%ldconfig_scriptlets -n %{rocblas_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{rocblas_name}%{?_isa} = %{version}-%{release}
Requires:       cmake(hip)

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       diffutils

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
sed -i -e 's@set( BLAS_LIBRARY "blas" )@set( BLAS_LIBRARY "%blaslib" )@' clients/CMakeLists.txt
sed -i -e 's@target_link_libraries( rocblas-test PRIVATE ${BLAS_LIBRARY} ${GTEST_BOTH_LIBRARIES} roc::rocblas )@target_link_libraries( rocblas-test PRIVATE %blaslib ${GTEST_BOTH_LIBRARIES} roc::rocblas )@' clients/gtest/CMakeLists.txt

# no git in this build
sed -i -e 's@find_package(Git REQUIRED)@find_package(Git)@' library/CMakeLists.txt

# On Tumbleweed Q2,2025
# /usr/include/gtest/internal/gtest-port.h:279:2: error: C++ versions less than C++14 are not supported.
#   279 | #error C++ versions less than C++14 are not supported.
# Convert the c++11's to c++14
sed -i -e 's@CXX_STANDARD 11@CXX_STANDARD 14@' clients/samples/CMakeLists.txt

%if 0%{?suse_version}
# Suse's libgfortran.so for gcc 14 is here
# /usr/lib64/gcc/x86_64-suse-linux/14/libgfortran.so
# Without adding this path with -L, it isn't found, but thankfully it isn't really needed
sed -i -e 's@list( APPEND COMMON_LINK_LIBS "-lgfortran")@#list( APPEND COMMON_LINK_LIBS "-lgfortran")@' clients/{benchmarks,gtest}/CMakeLists.txt
%endif

%build

# With compat llvm the system clang is wrong
CLANG_PATH=`hipconfig --hipclangpath`
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
# Work around problem with koji's ld
export HIPCC_LINK_FLAGS_APPEND=-fuse-ld=lld

%if %{with tensile}
TP=`/usr/bin/TensileGetPath`
%endif

CORES=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${CORES}x = x ]; then
    CORES=1
fi
# Try again..
if [ ${CORES} = 1 ]; then
    CORES=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${CORES}x = x ]; then
        CORES=4
    fi
fi

%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_WITH_TENSILE=%{build_tensile} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocblas/LICENSE.md

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library/src:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/rocblas-test --gtest_brief=1
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library/src:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocblas-test --gtest_brief=1
%endif
%endif
%endif

%files -n %{rocblas_name}
%license LICENSE.md
%{_libdir}/librocblas.so.4{,.*}
%if %{with tensile}
%dir %{_libdir}/rocblas
%dir %{_libdir}/rocblas/library
%{_libdir}/rocblas/library/Kernels*
%{_libdir}/rocblas/library/Tensile*
%endif

%files devel
%doc README.md
%dir %{_libdir}/cmake/rocblas
%dir %{_includedir}/rocblas
%{_includedir}/rocblas/*
%{_libdir}/cmake/rocblas/*.cmake
%{_libdir}/librocblas.so

%if %{with test}
%files test
%{_bindir}/rocblas*
%endif

%changelog
