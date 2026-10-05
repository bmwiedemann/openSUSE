#
# spec file for package miopen
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


%global upstreamname miopen

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 1
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%if 0%{?suse_version}
%global miopen_name libMIOpen1%{pkg_suffix}
%else
%global miopen_name miopen%{pkg_suffix}
%endif

%global toolchain rocm

# hipcc does not support some clang flags
# build_cxxflags does not honor CMAKE_BUILD_TYPE, strip out -g
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' -e 's/-mtls-dialect=gnu2//')
%if 0%{?suse_version}
# %%toolchain and %%build_cxxflags are Fedora rpm machinery; openSUSE implements
# neither, and its %%cmake injects %%optflags verbatim. Without this the host
# hardening flags reach the amdgcn device passes, where clang rejects them with
# "option 'cf-protection=return' cannot be specified on this target".
%global optflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-g / /' -e 's/-mtls-dialect=gnu2//')
%endif

%bcond_with debug
%if 0%{?suse_version}
%if %{without debug}
%global build_type RELEASE
%global build_cxxflags %(echo %{optflags} | sed -e 's/-g\\( \\|$\\)/ /')
%endif
%else
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%endif

# For testing
# hardcoded use of gtest and dirs is not suitable for mock building
# Testsuite is not in great shape, fails instead of skips ck tests
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Change this to the gpu family you are testing on
%bcond_with check
%global gpu_test default
%if %{with test}
%if %{with check}
# Do not build everything to do the test on one thing
%global rocm_gpu_list %{gpu_test}
%endif
%endif

# Needs to match rocblas
%bcond_without tensile

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

# Use ninja if it is available
%bcond_without ninja

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

Name:           %{miopen_name}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        3%{?dist}
%endif
Summary:        AMD's Machine Intelligence Library
License:        MIT AND BSD-2-Clause AND Apache-2.0 AND %{?fedora:LicenseRef-Fedora-Public-Domain}%{?suse_version:SUSE-Public-Domain}
# The base license is MIT with a couple of exceptions
# BSD-2-Clause
#   driver/mloSoftmaxHost.hpp
#   src/include/miopen/mlo_internal.hpp
# Apache-2.0
#   src/include/miopen/kernel_cache.hpp
#   src/kernel_cache.cpp
# Public Domain
#   src/md5.cpp
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%if %{with preview}
# New source needed for testing
# Request a real ctest project here
# https://github.com/ROCm/rocm-libraries/issues/6500
#Source1:        %{url}/releases/download/%{pkg_src}/ctest.tar.gz#/ctest-%{version}.tar.gz
%endif

# So we do not thrash memory
Patch1:         0001-miopen-add-link-and-compile-pools.patch
# See https://github.com/ROCm/rocm-libraries/pull/9586
Patch2:         miopen-fix-with-boost-1.90+.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(eigen3)
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  fplus-devel
BuildRequires:  frugally-deep-devel
BuildRequires:  half-devel
BuildRequires:  hipblas%{pkg_suffix}-devel
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocrand%{pkg_suffix}-devel
BuildRequires:  roctracer%{pkg_suffix}-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(sqlite3)

%if 0%{?suse_version}
BuildRequires:  libbz2-devel
BuildRequires:  libzstd-devel-static
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_filesystem1_75_0-devel
BuildRequires:  libboost_system1_75_0-devel
%else
BuildRequires:  libboost_filesystem-devel
%endif
%else
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(bzip2)
%endif

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gmock
BuildRequires:  gtest
%else
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
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

%if %{with preview}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

Provides:       miopen%{pkg_suffix} = %{version}-%{release}

# MIOpen compiles on the fly, so it needs ROCm devel at runtime
# This rpmlint
#   miopen.x86_64: E: devel-dependency rocm-hip-devel
# is a false positive
Requires:       rocm-hip%{pkg_suffix}-devel
Requires:       rocrand%{pkg_suffix}-devel
# Also needs c++ to work
# From pytorch-examples/word_language_model
# MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: MIOpenDropoutHIP.cpp
# MIOpen(HIP): Warning [BuildHip] In file included from /tmp/comgr-78a343/input/MIOpenDropoutHIP.cpp:32:
# In file included from /tmp/comgr-78a343/include/miopen_rocrand.hpp:45:
# In file included from /usr/include/rocrand/rocrand_xorwow.h:24:
# /usr/include/rocrand/rocrand_common.h:39:10: fatal error: 'utility' file not found
#   39 | #include <utility>
#      |          ^~~~~~~~~
Requires:       gcc-c++

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
AMD's library for high performance machine learning primitives.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       miopen%{pkg_suffix}-devel = %{version}-%{release}

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
%autosetup -p1 -n %{upstreamname}
%if %{with preview}
tar xf %{SOURCE1}
sed -i -e 's@include(${ROCM_LIBRARIES_ROOT}/shared/ctest/TestCategories.cmake)@include(${CMAKE_CURRENT_SOURCE_DIR}/../../ctest/TestCategories.cmake)@' test/gtest/CMakeLists.txt

# problem with trying to use ck for tests even when disabled
# https://github.com/ROCm/rocm-libraries/issues/6518
sed -i -e '/implicitgemm_ck_util/d' src/include/miopen/conv/heuristics/ai_conv_nd_kernel_tuning_utils.hpp

# No Werror, that is too strict
sed -i '/Werror/d' cmake/EnableCompilerWarnings.cmake
%endif

# Readme has executable bit
chmod 644 README.md

# clang-tidy is brittle and not needed for rebuilding from a tarball
sed -i -e 's@clang-tidy@true@' cmake/ClangTidy.cmake

# workaround error on finding lbunzip2
sed -i -e 's@lbunzip2 bunzip2@bunzip2@' CMakeLists.txt

# https://github.com/ROCm/MIOpen/issues/2672
sed -i -e 's@find_path(HALF_INCLUDE_DIR half/half.hpp)@#find_path(HALF_INCLUDE_DIR half/half.hpp)@' CMakeLists.txt
# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done
# On 6.4.0
# ../test/verify.hpp:198:56: error: no member named 'expr' in namespace 'half_float::detail'
#  198 |     if constexpr(std::is_same_v<T, half_float::detail::expr>)
# This is not our float, hack it out
sed -i -e 's@std::is_same_v<T, half_float::detail::expr>@0@' test/verify.hpp

# Tries to download its own googletest
# No good knob to turn it off so hack the cmake
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt
sed -i -e 's@add_subdirectory(speedtests)@#add_subdirectory(speedtests)@' CMakeLists.txt
%endif

%if %{without tensile}
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/include/miopen/handle.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/solver/mha/mha_common.hpp
sed -i -e 's@#define ROCBLAS_BETA_FEATURES_API 1@#define ROCBLAS_BETA_FEATURES_API 0@' src/gemm_v2.cpp
%endif

# Our use of modules confuse install locations
# The db is not installed relative to the lib dir.
# Hardcode its location
sed -i -e 's@GetLibPath().parent_path() / "share/miopen/db"@"/usr/share/miopen/db"@' src/db_path.cpp.in

# Unsupported compiler flags
sed -i -e 's@opts.push_back("-fno-offload-uniform-block");@//opts.push_back("-fno-offload-uniform-block");@' src/comgr.cpp

# Paths to clang
sed -i -e 's@llvm/bin/clang@bin/clang@' src/hip/hip_build_utils.cpp

%build
# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
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

%{?suse_version:%{?build_cxxflags:CXXFLAGS="%{build_cxxflags}"}}

%cmake %{cmake_generator} \
       -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
       -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DROCM_SYMLINK_LIBS=OFF \
       -DHIP_PLATFORM=amd \
       -DGPU_TARGETS=%{gpu_list} \
       -DBUILD_TESTING=%{build_test} \
       %{?build_type:-DCMAKE_BUILD_TYPE=%{build_type}} \
       -DCMAKE_SKIP_RPATH=ON \
       -DBoost_USE_STATIC_LIBS=OFF \
       -DMIOPEN_PARALLEL_COMPILE_JOBS=$COMPILE_JOBS \
       -DMIOPEN_PARALLEL_LINK_JOBS=$LINK_JOBS \
       -DMIOPEN_BACKEND=HIP \
       -DMIOPEN_BUILD_DRIVER=OFF \
       -DMIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK=OFF \
       -DMIOPEN_ENABLE_AI_KERNEL_TUNING=OFF \
       -DMIOPEN_TEST_ALL=%{build_test} \
       -DMIOPEN_USE_HIPBLASLT=OFF \
       -DMIOPEN_USE_MLIR=OFF \
       -DMIOPEN_USE_COMPOSABLEKERNEL=OFF

%cmake_build

%if %{with test}
%if 0%{?suse_version}
%cmake_build tests
%else
%cmake_build -t tests
%endif
%endif

%if %{with test}
%if %{with check}
%check
find . -name 'libMIOpen.so.1'
%if 0%{?suse_version}
export LD_LIBRARY_PATH=${PWD}/%{__builddir}/lib:$LD_LIBRARY_PATH
%else
export LD_LIBRARY_PATH=${PWD}/%{_vpath_builddir}/lib:$LD_LIBRARY_PATH
%endif
%ctest
%endif
%endif

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/miopen-hip/LICENSE.md

%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{pkg_prefix}
%endif

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/libMIOpen.so.1{,.*}
%{pkg_prefix}/libexec/miopen/

%files devel
%{pkg_prefix}/share/miopen/
%{pkg_prefix}/include/miopen/
%{pkg_prefix}/%{pkg_libdir}/libMIOpen.so
%{pkg_prefix}/%{pkg_libdir}/cmake/miopen/

%if %{with test}
%files test
%if %{without preview}
# TODO: Something wrong here
%{pkg_prefix}/bin/test*
%endif
%endif

%changelog
