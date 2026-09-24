#
# spec file for package rocwmma
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


%bcond_with preview
%if %{with preview}
%global upstreamname rocwmma
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
# ROCm 7.2 is still in the old URL
%global upstreamname rocWMMA
%global rocm_release 7.2
%global rocm_patch 0
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Testing needs to be done manually

%bcond_with test
%if %{with test}
%global build_test ON
# ERROR   0002: file '/usr/bin/io_traits_test' contains an invalid runpath
# silence warning.
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
# This is a header only
%global debug_package %{nil}
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# May not be supported on every arch
# Only offically supported are called out here
# library/include/rocwmma/internal/config.hpp
# Adjust our list
%global gpu_list "gfx908;gfx90a;gfx942;gfx950;gfx1100;gfx1101;gfx1102;gfx1151;gfx1150;gfx1200;gfx1201"
%global _gpu_list gfx1100

# Building the tests may run out of memory for both compile and link
# The normal build is just headers so whatever we do here will not matter
# Calculate a good -j number below
%global _smp_mflags %{nil}

Name:           rocwmma%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        5%{?dist}
%endif

Summary:        ROCm Matrix Multiple and Accumulate library
%if %{with preview}
URL:            https://github.com/ROCm/rocm-libraries
%else
URL:            https://github.com/ROCm/%{upstreamname}
%endif
License:        MIT

%if %{with preview}
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# TBD: Needs to be rebased to rocm-libraries and upstreamed.
Patch0:         0001-rocwmma-ninja-job-pools.patch
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?fedora}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-omp%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

%if %{with test}

BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-smi%{pkg_suffix}-devel
BuildRequires:  rocminfo%{pkg_suffix}

%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocWMMA is a C++ library for accelerating mixed-precision matrix
multiply-accumulate (MMA) operations leveraging AMD GPU hardware.
rocWMMA makes it easier to break down MMA problems into fragments
and distribute block-wise MMA operations in parallel across GPU
wavefronts. Our API consists of a header library, that you can
use to compile MMA acceleration directly into GPU kernel device
code. This can benefit from compiler optimization in the
generation of kernel assembly, and doesn't incur additional
overhead costs of linking to external runtime libraries or having
to launch separate kernels.

%package devel
Summary:        Headers for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}

%description test
%{summary}
%endif

%prep
%if %{with preview}
%autosetup -p1 -n %{upstreamname}
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# Remove parallel-jobs, it interfers with ninja jobs and attempts to reduce memory usage
# https://github.com/ROCm/rocm-libraries/issues/4949
sed -i -e 's@-parallel-jobs=4@@' CMakeLists.txt

%build
cat /proc/cpuinfo
cat /proc/meminfo
lscpu

# Real cores, No hyperthreading
COMPILE_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Try again..
if [ ${COMPILE_JOBS} = 1 ]; then
    COMPILE_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${COMPILE_JOBS}x = x ]; then
        COMPILE_JOBS=4
    fi
fi

# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=4
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=32
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

# When switch to ninja, this error..
# CMake Error at test/CMakeLists.txt:89 (add_executable):
#   The install of the gemm_PGR1_LB2_MP0_MB_CP_ad_hoc-validate target requires
#   changing an RPATH from the build tree, but this is not supported with the
#   Ninja generator unless on an ELF-based or XCOFF-based platform.  The
#   CMAKE_BUILD_WITH_INSTALL_RPATH variable may be set to avoid this relinking
# So use it.

%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=%build_type \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-O2 -I%{pkg_prefix}/include" \
    -DCMAKE_EXE_LINKER_FLAGS="-L%{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DROCWMMA_BUILD_SAMPLES=OFF \
    -DROCWMMA_BUILD_TESTS=%{build_test} \
    -DROCWMMA_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DROCWMMA_PARALLEL_LINK_JOBS=${LINK_JOBS}

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocwmma/LICENSE.md

# cmake test cruft
rm -f %{buildroot}%{pkg_prefix}/bin/rocwmma/*.cmake

%files devel
%license LICENSE.md
%{pkg_prefix}/include/rocwmma
%{pkg_prefix}/share/cmake/rocwmma

%if %{with test}
%files test
%{pkg_prefix}/bin/*_test
%{pkg_prefix}/bin/*-validate
%{pkg_prefix}/bin/rocwmma/
%if %{with preview}
%{pkg_prefix}/bin/*_tests
%endif
%endif

%changelog
