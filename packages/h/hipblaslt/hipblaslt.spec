#
# spec file for package hipblaslt
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


%global upstreamname hipblaslt

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 0
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global skip_install_rpath ON
%endif
%if 0%{?suse_version}
%global hipblaslt_name libhipblaslt1%{pkg_suffix}
%else
%global hipblaslt_name hipblaslt%{pkg_suffix}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%if 0%{?suse_version}
# %%toolchain and %%build_cxxflags are Fedora rpm machinery; openSUSE implements
# neither, and its %%cmake injects %%optflags verbatim. Without this the host
# hardening flags reach the amdgcn device passes, where clang rejects them with
# "option 'cf-protection=return' cannot be specified on this target".
%global optflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%endif

# Fortran is only used in testing
# clang and gfortran fedora toolchain args do not mix
%global build_fflags %{nil}

# Reduce link memory pressure
%global _lto_cflags %{nil}

# may run out of memory for both compile and link
# Calculate a good -j number below
%global _smp_mflags %{nil}

# gfx90a: 10343 pass, 152 fail
%bcond_with test
# Disable rpatch checks for a local build
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif

%global tensile_version 4.33.0
# The upstream hipBLASTLt project has a hard fork of the python-tensile package
# The rocBLAS uses.  The two versions are incompatible.  It appears that the
# fork happened around version 4.33.0.  Unfortunately hipBLASLt can no longer be
# build without using this fork.
# https://github.com/ROCm/hipBLASLt/issues/535
# The problem with the fork has been raised here.
# https://github.com/ROCm/hipBLASLt/issues/908

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# hipblaslt does not support our default set
%global gpu_list %{rocm_gpu_list_hipblaslt}
# For testing
%global _gpu_list "gfx1100"

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

# Request for python-nanobind on EPEL
# https://bugzilla.redhat.com/show_bug.cgi?id=2402409
%if 0%{?fedora}
%bcond_without nanobind
%else
%bcond_with nanobind
%endif

%if 0%{!?suse_version:1}
%define python_exec python3
%define python_expand python3
%endif

Name:           hipblaslt%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        7%{?dist}
%endif
Summary:        ROCm general matrix operations beyond BLAS
%if %{without nanobind}
License:        BSD-3-Clause AND MIT
%else
License:        MIT
%endif
URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

%global nanobind_version 2.9.2
%global nanobind_giturl https://github.com/wjakob/nanobind
Source1:        %{nanobind_giturl}/archive/v%{nanobind_version}/nanobind-%{nanobind_version}.tar.gz
%global robinmap_version 1.3.0
%global robinmap_giturl https://github.com/Tessil/robin-map
Source2:        %{robinmap_giturl}/archive/v%{robinmap_version}/robin-map-%{robinmap_version}.tar.gz

%if %{with preview}
#Source3:        %{url}/releases/download/%{pkg_src}/stinkytofu.tar.gz#/stinkytofu-%{version}.tar.gz
#Source4:        %{url}/releases/download/%{pkg_src}/origami.tar.gz#/origami-%{version}.tar.gz
#Source5:        %{url}/releases/download/%{pkg_src}/mxdatagenerator.tar.gz#/mxdatagenerator-%{version}.tar.gz
Patch1:         0001-hipblaslt-preview-tensilelit-remove-yappi-dependency.patch
Patch3:         0001-hipblaslt-preview-find-origami-package.patch
Patch4:         0001-hipblaslt-preview-tensilelit-use-nanobind-tarball.patch
Patch5:         0001-hipblaslt-preview-cmake-jobpools.patch
Patch6:         0001-hipblaslt-preview-stinktofu.patch
%else
# yappi was removed from fedora
# yappi is used in tensilelite to generate profiling data, we are not using that in the build
Patch1:         0001-hipblaslt-tensilelite-remove-yappi-dependency.patch
# https://github.com/ROCm/rocm-libraries/issues/2422
Patch3:         0001-hipblaslt-find-origami-package.patch
# do not try to fetch, point to the nanobind tarball
Patch4:         0001-hipblaslt-tensilelite-use-nanobind-tarball.patch
# compile and link jobpools
Patch5:         0001-hipblaslt-cmake-compile-and-link-pools.patch
%endif

%if %{with preview}
BuildRequires:  amdsmi-devel
%endif
BuildRequires:  chrpath
BuildRequires:  cmake
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
BuildRequires:  hipblas%{pkg_suffix}-devel
BuildRequires:  hipcc%{pkg_suffix}
BuildRequires:  libzstd-devel
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-llvm%{pkg_suffix}-devel
BuildRequires:  rocm-origami%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-smi%{pkg_suffix}-devel
BuildRequires:  rocminfo%{pkg_suffix}
BuildRequires:  zlib-devel

# For tensilelite
%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  msgpack-cxx-devel
BuildRequires:  python-rpm-macros
%global tensile_verbose 2
BuildRequires:  %{python_module dataclasses if %python-base < 3.11}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module ujson}
%else
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
%if %{with nanobind}
BuildRequires:  python3dist(nanobind)
%endif
%if %{with preview}
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(wheel)
%endif
%global tensile_verbose 1
BuildRequires:  python3dist(joblib)
# https://github.com/ROCm/hipBLASLt/issues/1734
BuildRequires:  python3dist(msgpack)
BuildRequires:  msgpack-devel
%endif

%if %{with test}
BuildRequires:  blis-devel
BuildRequires:  lapack-devel
%if 0%{?suse_version}
BuildRequires:  gmock
BuildRequires:  gtest
%else
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
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

Provides:       bundled(python-tensile) = %{tensile_version}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}
Requires:       rocm-origami%{pkg_suffix}

%if %{without nanobind}
# BSD-3-Clause
Provides:       bundled(nanobind) = %{nanobind_version}
Provides:       bundled(robin-map) = %{robinmap_version}
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipBLASLt is a library that provides general matrix-matrix
operations. It has a flexible API that extends functionalities
beyond a traditional BLAS library, such as adding flexibility
to matrix data layouts, input types, compute types, and
algorithmic implementations and heuristics.


%if 0%{?suse_version}
%package -n %{hipblaslt_name}
Summary:        Runtime for %{name}

%description -n %{hipblaslt_name}
%summary

%ldconfig_scriptlets -n %{hipblaslt_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{hipblaslt_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description test
%{summary}
%endif

%prep
%if %{with preview}
# Make a sparse rocm-libraries
mkdir shared projects
cd shared
# stinkytofu
tar xf %{SOURCE3}
cd stinkytofu
# src/serialization/asm/PatternParser.cpp:794:13: error: unknown type name 'uint32_t'
sed -i -e '/#include <sstream>.*/a#include <stdint.h>' src/serialization/asm/PatternParser.cpp
sed -i -e '/#include <vector>.*/a#include <stdint.h>' include/stinkytofu/serialization/logical/IRSerializer.hpp
# src/transforms/asm/dag/ReadyQueue.hpp:49:31: error: use of undeclared identifier 'UINT_MAX'
sed -i -e '/#include <queue>.*/a#include <limits.h>' src/transforms/asm/dag/ReadyQueue.hpp
sed -i -e '/#include <string_view>.*/a#include <limits.h>' src/serialization/asm/IRParser.cpp
sed -i -e '/#include <utility>.*/a#include <limits.h>' src/transforms/asm/StinkyWmmaVgprReorderPass.cpp
# No clang-tidy
sed -i -e 's@include(ClangTidy)@@' CMakeLists.txt
sed -i -e 's@add_clang_tidy_custom_target()@@' CMakeLists.txt
# No ../../cmake/modues/default_amdclang.cmake
sed -i -e '/default_amdclang/d' CMakeLists.txt
cd ..
tar xf %{SOURCE4}
tar xf %{SOURCE5}
cd ../projects
tar xf %{SOURCE0}
cd hipblaslt
# tensile path to tools need to change
sed -i -e 's@globalParameters["ROCmPath"] = "/opt/rocm"@globalParameters["ROCmPath"] = "%{pkg_prefix}"@' tensilelite/Tensile/Common/GlobalParameters.py
sed -i -e 's@DEFAULT_ROCM_BIN_PATH_POSIX = Path("/opt/rocm/bin")@DEFAULT_ROCM_BIN_PATH_POSIX = Path("%{pkg_prefix}/bin")@' tensilelite/Tensile/Toolchain/Validators.py
sed -i -e 's@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("/opt/rocm/lib/llvm/bin")@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("%{rocmllvm_bindir}")@' tensilelite/Tensile/Toolchain/Validators.py

# nanobind bundle
tar xf %{SOURCE1}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE2}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
cd ../..
%patch 1 -p1
%patch 4 -p1
%else
%autosetup -p3 -n %{upstreamname}

# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# defer to cmdline
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# Do not use virtualenv_install
sed -i -e 's@virtualenv_install@#virtualenv_install@'                          CMakeLists.txt

# Disable trying to download rocm-cmake
sed -i -e 's@if(NOT ROCmCMakeBuildTools_FOUND)@if(FALSE)@' cmake/dependencies.cmake

# compat has this issue
# /usr/lib64/rocm/rocm-7.2/llvm/bin/amdclang++ -x hip .../device-library/matrix-transform/matrix_transform.cpp
# In file included from /builddir/build/BUILD/hipblaslt7.2-7.2.0-build/hipblaslt/device-library/matrix-transform/matrix_transform.cpp:26:
# /builddir/build/BUILD/hipblaslt7.2-7.2.0-build/hipblaslt/device-library/matrix-transform/matrix_transform.h:27:10: fatal error: 'hip/hip_bfloat16.h' file not found
#   27 | #include <hip/hip_bfloat16.h>
#      |          ^~~~~~~~~~~~~~~~~~~~
#
# Add include path to the custom build command
sed -i -e 's@${CMAKE_CXX_COMPILER} -x hip @${CMAKE_CXX_COMPILER} -x hip -I%{pkg_prefix}/include @' device-library/matrix-transform/CMakeLists.txt
# Similar on tensile command
sed -i -e 's@"--offload-device-only",@"--offload-device-only", "-I%{pkg_prefix}/include",@' tensilelite/Tensile/Toolchain/Component.py

# tensile path to tools need to change
sed -i -e 's@globalParameters["ROCmPath"] = "/opt/rocm"@globalParameters["ROCmPath"] = "%{pkg_prefix}"@' tensilelite/Tensile/Common/GlobalParameters.py
sed -i -e 's@DEFAULT_ROCM_BIN_PATH_POSIX = Path("/opt/rocm/bin")@DEFAULT_ROCM_BIN_PATH_POSIX = Path("%{pkg_prefix}/bin")@' tensilelite/Tensile/Toolchain/Validators.py
sed -i -e 's@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("/opt/rocm/lib/llvm/bin")@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("%{rocmllvm_bindir}")@' tensilelite/Tensile/Toolchain/Validators.py

%if %{with nanobind}
# Disable download of nanobind
sed -i -e 's@FetchContent_MakeAvailable(nanobind)@find_package(nanobind)@' tensilelite/rocisa/CMakeLists.txt
%else
# Use bundled nanobind
tar xf %{SOURCE1}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE2}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
%endif

# As of 6.4, there is a long poll
# compile_code_object.sh gfx90a,gfx1100,gfx1101,gfx1151,gfx1200,gfx1201 RelWithDebInfo sha1 hipblasltTransform.hsaco
# This compiles a large file with multiple gpus.
GPUS=`echo %{gpu_list} | grep -o 'gfx' | wc -l`

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
if [ "$GPUS" -lt "$HIP_JOBS" ]; then
    HIP_JOBS=$GPUS
fi

# HIPBLASLT_ENABLE_OPENMP is OFF yet it is still being used
# https://github.com/ROCm/rocm-libraries/issues/3201
sed -i -e '/OpenMP::OpenMP_CXX/d' clients/CMakeLists.txt
sed -i -e '/omp/d'                clients/common/src/blis_interface.cpp
sed -i -e '/#include <omp.h>/d'   clients/common/include/testing_matmul.hpp
sed -i -e '/#include <omp.h>/d'   clients/common/include/hipblaslt_init.hpp
sed -i -e '/#include <omp.h>/d'   clients/common/src/cblas_interface.cpp

# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' cmake/dependencies.cmake

%endif

%build
%if %{with preview}
cd projects/hipblaslt
%else
# Do a manual install instead of cmake's virtualenv
cd tensilelite
TL=$PWD

%if %{with preview}

cd rocisa
/usr/bin/python3 -m pip install -vvv --no-build-isolation --no-index --find-links /usr/lib/python%{python3_version}/site-packages --find-links /usr/lib64/python%{python3_version}/site-packages --target $TL .
cd ..

# so tensilelite picks up rocisa
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH

/usr/bin/python3 -m pip install -vvv --no-build-isolation --no-index --find-links /usr/lib/python%{python3_version}/site-packages --find-links /usr/lib64/python%{python3_version}/site-packages --target $TL .
%else
%python_exec setup.py install --root $TL
%endif

cd ..

# Should not have to do this
export PATH=%{pkg_prefix}/bin:$PATH
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler

# Look for the just built tensilelite
export PATH=${TL}/%{_bindir}:$PATH
%if 0%{?suse_version}
%{python_expand} export PYTHONPATH=${TL}%{python_sitelib}:$PYTHONPATH
%{python_expand} export Tensile_DIR=${TL}%{python_sitelib}/Tensile
%else
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile
%endif
# Uncomment and see if the path is sane
# TensileGetPath

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
%endif

%cmake %{cmake_generator} \
       -DGPU_TARGETS=%{gpu_list} \
       -DBLIS_INCLUDE_DIR=%{_includedir}/blis \
       -DBLIS_LIB=%{_libdir}/libblis.so \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
       -DCMAKE_PREFIX_PATH=%{python3_sitelib}/nanobind \
       -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
       -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DHIP_PLATFORM=amd \
       -DHIPBLASLT_ENABLE_CLIENT=%{build_test} \
       -DHIPBLASLT_ENABLE_MARKER=OFF \
       -DHIPBLASLT_ENABLE_OPENMP=OFF \
       -DHIPBLASLT_ENABLE_ROCROLLER=OFF \
       -DHIPBLASLT_ENABLE_SAMPLES=OFF \
       -DROCM_SYMLINK_LIBS=OFF \
       -DTensile_LIBRARY_FORMAT=msgpack \
       -DTensile_VERBOSE=%{tensile_verbose} \
       -DVIRTUALENV_BIN_DIR=%{_bindir} \
       -DHIPBLASLT_PARALLEL_COMPILE_JOBS=${COMPILE_JOBS} \
       -DHIPBLASLT_PARALLEL_LINK_JOBS=${LINK_JOBS} \
       %{nil}

%if %{with preview}
# To find the just built stinkytofu
export LD_LIBRARY_PATH=${PWD}/%{_vpath_builddir}/tensilelite/rocisa/stinkytofu:$LD_LIBRARY_PATH
%endif

%cmake_build

%install
%if %{with preview}
cd projects/hipblaslt
%endif
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipblaslt/LICENSE.md

%if %{without preview}
# hipblaslt.x86_64: W: unstripped-binary-or-object /usr/lib64/hipblaslt/library/extop_gfx1201.co
%{rocmllvm_bindir}/llvm-strip %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipblaslt/library/Kernels.so-000-*.hsaco
%{rocmllvm_bindir}/llvm-strip %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipblaslt/library/extop_*.co
%endif

%if %{without compat}
# hipblaslt.x86_64: E: binary-or-shlib-defines-rpath /usr/lib64/libhipblaslt.so.1.2 (RUNPATH: $ORIGIN/../lib:$ORIGIN/../llvm/lib:$ORIGIN/../lib:$ORIGIN/../lib/hipblaslt/lib)
chrpath -d %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipblaslt.so.*
%else
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipblaslt.so.*
%endif

# hipblaslt-devel.x86_64: W: cross-directory-hard-link /usr/include/hipblaslt/hipblaslt-export.h /usr/include/hipblaslt-export.h
# Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{pkg_prefix}
%endif

%if 0%{?suse_version}
%post  -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files -n %{hipblaslt_name}
%if %{with preview}
%doc projects/hipblaslt/README.md
%license projects/hipblaslt/LICENSE.md
%else
%doc README.md
%license LICENSE.md
%endif
%{pkg_prefix}/%{pkg_libdir}/libhipblaslt.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/hipblaslt/

%files devel
%{pkg_prefix}/include/hipblaslt/
%{pkg_prefix}/include/hipblaslt-export.h
%{pkg_prefix}/include/hipblaslt-version.h
%{pkg_prefix}/%{pkg_libdir}/cmake/hipblaslt/
%{pkg_prefix}/%{pkg_libdir}/libhipblaslt.so

%if %{with test}
%files test
%{pkg_prefix}/bin/hipblaslt*
%{pkg_prefix}/bin/sequence.yaml
%if %{with preview}
%{pkg_prefix}/share/hipblaslt/
%endif
%endif

%changelog
