#
# spec file for package rocsolver
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
%global rocsolver_name librocsolver0
%else
%global rocsolver_name rocsolver
%endif

%global upstreamname rocSOLVER
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
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

# may run out of memory for both compile and link
# Calculate a good -j number below
%global _smp_mflags %{nil}

# Fortran is only used in testing
%global build_fflags %{nil}

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

# export an llvm compilation database
# Useful for input for other llvm tools
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

Name:           rocsolver
Version:        %{rocm_version}
Release:        5%{?dist}
Summary:        Next generation LAPACK implementation for ROCm platform
URL:            https://github.com/ROCm/rocSOLVER

# License check reports BSD 2-Clause
# But reviewing LICENSE.md, this is only for AMD
# Later in the file are BSD 3-Clause for LAPACK and MAGMA
License:        BSD-2-Clause AND BSD-3-Clause

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# https://github.com/ROCm/rocSOLVER/pull/652
Patch0:         0001-Add-llvm-style-compile-and-link-options.patch
Patch1:         0001-rocsolver-offload-compress.patch
# https://github.com/ROCm/rocSOLVER/pull/962
Patch2:         0001-rocsolver-parallel-jobs.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
# RFE to replace fmt:: with std::
# https://github.com/ROCm/rocSOLVER/issues/929
BuildRequires:  fmt-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocsparse-devel

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}

%if 0%{?suse_version}
BuildRequires:  blas-devel-static
BuildRequires:  gcc-fortran
BuildRequires:  gtest
BuildRequires:  lapack-devel-static

# Problem on Tumbleweed
# CMake Error at /usr/lib64/cmake/lapack-3.12.0/lapack-targets.cmake:98 (message):
#  The imported target "blas" references the file
#
#     "/usr/lib64/libblas.so.3.12.0"

%else
BuildRequires:  blas-static
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  lapack-static
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

Provides:       rocsolver = %{version}-%{release}

%description
rocSOLVER is a work-in-progress implementation of a subset
of LAPACK functionality on the ROCm platform.

%if 0%{?suse_version}
%package -n %{rocsolver_name}
Summary:        Shared libraries for %{name}

%description -n %{rocsolver_name}
%{summary}

%ldconfig_scriptlets -n %{rocsolver_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{rocsolver_name}%{?_isa} = %{version}-%{release}

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

# As of 6.4, there are 2 long running hip jobs
# There are ~20 gpu targets
# Most builders will have between 4 and 32 cores
# Default to 2 cpu's per hip job
# Increase to half of the systems maximum
# Real cores, No hyperthreading
HIP_JOBS=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${HIP_JOBS}x = x ]; then
    HIP_JOBS=1
fi
# Try again..
if [ ${HIP_JOBS} = 1 ]; then
    HIP_JOBS=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${HIP_JOBS}x = x ]; then
        HIP_JOBS=4
    fi
fi
HIP_JOBS=`eval "expr ${HIP_JOBS} / 2"`

# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=32
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
HIP_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$HIP_JOBS_MEM" -lt "$HIP_JOBS" ]; then
    HIP_JOBS=$HIP_JOBS_MEM
fi

sed -i -e "s@-parallel-jobs=4@-parallel-jobs=${HIP_JOBS}@" library/src/CMakeLists.txt

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
BUILD_MEM=8
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

%cmake %{cmake_generator} \
    -DCMAKE_CXX_COMPILER=hipcc \
    -DCMAKE_C_COMPILER=hipcc \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DROCSOLVER_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
    -DROCSOLVER_PARALLEL_LINK_JOBS=${LINK_JOBS} \
    -DBUILD_PARALLEL_HIP_JOBS=ON

%if %{with ninja}
%cmake_build
%else
%cmake_build -j ${JOBS}
%endif

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocsolver/LICENSE.md

%files -n %{rocsolver_name}
%license LICENSE.md
%{_libdir}/librocsolver.so.0{,.*}

%files devel
%doc README.md
%dir %{_libdir}/cmake/rocsolver
%dir %{_includedir}/rocsolver
%{_includedir}/rocsolver/*
%{_libdir}/librocsolver.so
%{_libdir}/cmake/rocsolver/*.cmake

%if %{with test}
%files test
%dir %{_datadir}/rocsolver
%{_datadir}/rocsolver/test/*
%{_bindir}/rocsolver*
%endif

%changelog
