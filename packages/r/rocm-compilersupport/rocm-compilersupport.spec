#
# spec file for package rocm-compilersupport
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
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 1
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 3
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%if %{with preview}
%global llvm_maj_ver 23
%else
%global llvm_maj_ver 22
%endif
%global llvm_version_suffix .rocm

# local, fedora
%global _comgr_full_api_ver %{comgr_maj_api_ver}.0
# mock, suse
%global comgr_full_api_ver %{comgr_maj_api_ver}.0.0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname llvm-project

%global toolchain clang

%global _smp_mflags %{nil}
%global _lto_cflags %{nil}
%global llvm_triple %{_target_platform}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
# T0 (auto detect) can fail if cores are high and memory low
# Use 6 threads, between OpenSUSE (4) and Fedora (8) build system defaults
%global _source_payload w7T6.xzdio
%global _binary_payload w7T6.xzdio

%bcond_with compat
%if %{with compat}
%global amd_device_libs_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm/lib/clang/%{llvm_maj_ver}/lib
%global bundle_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm
%global pkg_libdir lib
%global pkg_libdir_suffix %{nil}
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%else
%global amd_device_libs_prefix %{_libdir}/rocm/llvm/lib/clang/%{llvm_maj_ver}/lib
%global bundle_prefix %{_libdir}/rocm/llvm
%global pkg_libdir %{_lib}
%global pkg_libdir_suffix %{nil}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global device_libs_name rocm-device-libs%{pkg_suffix}
%global hipcc_name hipcc%{pkg_suffix}
%global pkg_name rocm-compilersupport%{pkg_suffix}
%global rocm_clang_analyzer_name rocm-clang-analyzer%{pkg_suffix}
%global rocm_clang_name rocm-clang%{pkg_suffix}
%global rocm_clang_tools_extra_name rocm-clang-tools-extra%{pkg_suffix}
%global rocm_libcxx_name rocm-libc++%{pkg_suffix}
%global rocm_lld_name rocm-lld%{pkg_suffix}
%global rocm_llvm_name rocm-llvm%{pkg_suffix}
%global rocm_omp_name rocm-omp%{pkg_suffix}
%if 0%{?suse_version}
# 15.6
# rocm-comgr.x86_64: E: shlib-policy-name-error (Badness: 10000) libamd_comgr2
# Your package contains a single shared library but is not named after its SONAME.
%global comgr_name libamd_comgr3%{pkg_suffix}
%else
%global comgr_name rocm-comgr%{pkg_suffix}
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Enable ppc and aarch64 builds
%bcond_with alt_arch

# buid the static analyzer
%bcond_without sa
%if %{with sa}
%global build_sa ON
%else
%global build_sa OFF
%endif

# build gold plugin
%bcond_without gold
%if %{with gold}
%global build_gold ON
%else
%global build_gold OFF
%endif

%bcond_with libcxx
%if %{with libcxx}
%global build_libcxx ON
%else
%global build_libcxx OFF
%endif

Name:           %{pkg_name}
Version:        %{llvm_maj_ver}
%if %{with preview}
Release:        1001.rocm%{rocm_version}%{?dist}
%else
Release:        13.rocm%{rocm_version}%{?dist}
%endif

Summary:        Various AMD ROCm LLVM related services
%if 0%{?suse_version}
Group:          Development/Languages/Other
%endif

URL:            https://github.com/ROCm/llvm-project
License:        (Apache-2.0 WITH LLVM-exception OR NCSA) AND NCSA AND MIT
# llvm is Apache-2.0 WITH LLVM-exception OR NCSA
# /amd breakdown
#
# /amd/comgr/*
# Apache-2.0, amd/comgr/LICENSE.txt
#
# /amd/hipcc/*
# MIT, amd/hipcc/LICENSE.txt
#
# /amd/device-libs/*
# NSCA, amd/device-libs/LICENSE.TXT

Source0:        %{url}/archive/refs/tags/%{pkg_src}.tar.gz#/rocm-compilersupport-%{rocm_version}.tar.gz
Source1:        rocm-compilersupport.prep.in

%if %{without preview}
# Link comgr with static versions of llvm's libraries
Patch1:         0001-comgr-link-with-static-llvm.patch
%else
Patch1:         0001-preview-comgr-link-with-static-llvm.patch
%endif
# On Fedora the assert came in gcc 15, on RHEL 10.2 gcc 14
# Reduce the gcc version check below
Patch2:         0001-rocm-llvm-work-around-new-assert-in-array.patch
# https://github.com/ROCm/llvm-project/issues/301
Patch3:         0001-rocm-compilersupport-force-hip-runtime-detection.patch
Patch4:         0001-rocm-compilersupport-simplify-use-runtime-wrapper-ch.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2415065
Patch5:         0001-lld-workaround-.gnu.version-change.patch
%if %{without preview}
# backport
# https://github.com/ROCm/llvm-project/commit/23f010f1ab09263d79027c70d5f4cddfe0055ca9
Patch6:         0001-SemaConcept.cpp-fix-MSVC-not-all-control-paths-retur.patch
%endif
%if %{with preview}
# When clang bungles the rocm install path, it gets the linking of libamdhip64 wrong
# Convert from an absolute path <path-to>/libamdhip64.so to using -lamdhip64
Patch7:         0001-clang-23-link-libamdhip64.patch
%endif

BuildRequires:  cmake
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  zlib-devel
%if %{with gold}
BuildRequires:  binutils-devel
%endif
BuildRequires:  gcc-c++
%if %{with preview}
# For omp
BuildRequires:  python-devel
%endif
Provides:       bundled(llvm-project) = %{llvm_maj_ver}

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"
%else
%if %{with alt_arch}
ExclusiveArch:  x86_64 aarch64 ppc64le
%else
ExclusiveArch:  x86_64
%endif

%ifarch x86_64
%global targets_to_build "X86;AMDGPU"
%endif
%ifarch aarch64
%global targets_to_build "AArch64;AMDGPU"
%endif
%ifarch ppc64le
%global targets_to_build "PowerPC;AMDGPU"
%endif
%endif

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros
BuildArch:      noarch

Requires:       rpm
# Compat version of macros conflict with the normal version
%if %{with compat}
Conflicts:      rocm-compilersupport-macros
%else
Conflicts:      rocm-compilersupport7.2-macros
%endif

%description macros
This package contains ROCm compiler related RPM macros.

%package -n %{device_libs_name}
Summary:        AMD ROCm LLVM bit code libraries
Requires:       %{rocm_clang_name}-devel = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       %{rocm_llvm_name}-static = %{version}-%{release}
Requires:       rocm-lld%{pkg_suffix} = %{version}-%{release}

%description -n %{device_libs_name}
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%package -n %{comgr_name}
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       rocm-filesystem%{pkg_suffix}
Provides:       rocm-comgr%{pkg_suffix} = %{comgr_full_api_ver}-%{release}
Provides:       comgr%{pkg_suffix}(major) = %{comgr_maj_api_ver}

%description -n %{comgr_name}
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%if 0%{?suse_version}
%ldconfig_scriptlets -n %{comgr_name}
%endif

%package -n %{comgr_name}-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       %{comgr_name}%{?_isa} = %{version}-%{release}
Requires:       %{device_libs_name} = %{version}-%{release}
%if 0%{?suse_version}
Provides:       rocm-comgr%{pkg_suffix}-devel = %{version}-%{release}
%endif

%description -n %{comgr_name}-devel
The AMD Code Object Manager (Comgr) development package.

%package -n %{hipcc_name}
Summary:        HIP compiler driver
Requires:       %{device_libs_name} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocminfo%{pkg_suffix} >= %{rocm_release}
%if 0%{?suse_version}
Provides:       hip = %{version}-%{release}
Obsoletes:      hip <= %{version}-%{release}
%endif

%description -n %{hipcc_name}
hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

# ROCM LLVM

%package -n %{rocm_llvm_name}-filesystem
Summary:        Filesystem package that owns the rocm llvm directory
Requires:       rocm-filesystem%{pkg_suffix}

%description -n %{rocm_llvm_name}-filesystem
This package owns the rocm llvm directory : %{bundle_prefix}

%package -n %{rocm_llvm_name}-libs
Summary:        The ROCm LLVM lib
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
%if %{with libcxx}
Requires:       %{rocm_libcxx_name}%{?_isa} = %{version}-%{release}
%endif

%description -n %{rocm_llvm_name}-libs
%{summary}

%package -n %{rocm_llvm_name}
Summary:        The ROCm LLVM
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
# https://bugzilla.redhat.com/show_bug.cgi?id=2362780
#  /usr/lib64/rocm/llvm/bin/amdgpu-arch
#  Failed to 'dlopen' libhsa-runtime64.so
Recommends:     rocm-runtime%{pkg_suffix}-devel

%description -n %{rocm_llvm_name}
%{summary}

%package -n %{rocm_llvm_name}-devel
Summary:        Libraries and header files for ROCm LLVM
Requires:       %{rocm_llvm_name}%{?_isa} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       zlib-devel

%description -n %{rocm_llvm_name}-devel
%{summary}

%if 0%{?suse_version}
%ldconfig_scriptlets -n %{rocm_llvm_name}-devel
%endif

%package -n %{rocm_llvm_name}-static
Summary:        Static libraries for ROCm LLVM
Requires:       %{rocm_llvm_name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Provides:       %{rocm_llvm_name}-static = %{version}-%{release}

%description -n %{rocm_llvm_name}-static
%{summary}

# ROCM CLANG
%package -n %{rocm_clang_name}-libs
Summary:        The ROCm compiler libs
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description -n %{rocm_clang_name}-libs
%{summary}

%if 0%{?suse_version}
%ldconfig_scriptlets -n %{rocm_clang_name}-libs
%endif

%package -n %{rocm_clang_name}-runtime-devel
Summary:        The ROCm compiler runtime
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Provides:       %{rocm_clang_name}-runtime-static = %{version}-%{release}

%description -n %{rocm_clang_name}-runtime-devel
%{summary}

%package -n %{rocm_clang_name}
Summary:        The ROCm compiler
Requires:       %{rocm_clang_name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{rocm_clang_name}-runtime-static = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       git
Requires:       python3
%if %{with libcxx}
Requires:       %{rocm_libcxx_name}-devel%{?_isa} = %{version}-%{release}
%endif

%description -n %{rocm_clang_name}
%{summary}

%package -n %{rocm_clang_name}-devel
Summary:        Libraries and header files for ROCm CLANG
Requires:       %{rocm_clang_name}%{?_isa} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}

%description -n %{rocm_clang_name}-devel
%{summary}

# CLANG TOOLS EXTRA
%package -n %{rocm_clang_tools_extra_name}
Summary:        Extra tools for clang
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       rocm-clang%{pkg_suffix}-libs%{?_isa} = %{version}-%{release}

%description -n %{rocm_clang_tools_extra_name}
A set of extra tools built using Clang's tooling API.

%package -n %{rocm_clang_tools_extra_name}-devel
Summary:        Development header files for clang tools
Requires:       %{rocm_clang_tools_extra_name} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}

%description -n %{rocm_clang_tools_extra_name}-devel
Development header files for clang tools.

# ROCM LLD

%package -n %{rocm_lld_name}
Summary:        The ROCm Linker
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
Requires:       %{rocm_llvm_name}-libs%{?_isa} = %{version}-%{release}

%description -n %{rocm_lld_name}
%{summary}

%if %{with libcxx}
# ROCM LIBC++
%package -n %{rocm_libcxx_name}
Summary:        The ROCm libc++
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}

%description -n %{rocm_libcxx_name}
%{summary}

%package -n %{rocm_libcxx_name}-devel
Summary:        The ROCm libc++ libraries and headers
Requires:       %{rocm_libcxx_name}%{?_isa} = %{version}-%{release}

%description -n %{rocm_libcxx_name}-devel
%{summary}

%package -n %{rocm_libcxx_name}-static
Summary:        The ROCm libc++ static libraries
Requires:       %{rocm_libcxx_name}-devel%{?_isa} = %{version}-%{release}

%description -n %{rocm_libcxx_name}-static
%{summary}

%else
Obsoletes:      %{rocm_libcxx_name} <= %{version}-%{release}
%endif

%if %{with sa}
%package -n %{rocm_clang_analyzer_name}
Summary:        The ROCm code analysis framework
Requires:       %{rocm_clang_name} = %{version}-%{release}
Requires:       %{rocm_llvm_name}-filesystem = %{version}-%{release}
# For scan-build
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(FindBin)
Requires:       perl(Hash::Util)
Requires:       perl(Sys::Hostname)

%description -n %{rocm_clang_analyzer_name}
%{summary}
%endif

%if %{with preview}
%package -n %{rocm_omp_name}-devel
Summary:        The ROCm OMP devel

%description -n %{rocm_omp_name}-devel
%{summary}

Requires:       %{device_libs_name} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

Obsoletes:      rocm-omp-devel <= 7.3

%endif

%prep
%autosetup -p1 -n %{upstreamname}-%{pkg_src}

# Remove third-party
#
# Need SipHash.h
# .../llvm/lib/Support/SipHash.cpp:15:10: fatal error: siphash/SipHash.h: No such file or directory
#   15 | #include "siphash/SipHash.h"
# move siphash out of the way
mv third-party/siphash .
%if %{with preview}
mv third-party/unittest .
%endif
# remove everything else
rm -rf third-party/*
# move siphash back
mv siphash third-party/
%if %{with preview}
mv unittest third-party/
%endif

# rm llvm-project bits we do not need
rm -rf {bolt,flang,flang-rt,libclc,lldb,llvm-libgcc,mlir,polly}

#Force static linking of libclang in comgr
sed -i "s/TARGET clangFrontendTool/true/" amd/comgr/CMakeLists.txt

# change version check of array assert work around
%if 0%{?rhel}
sed -i -e 's@#if _GLIBCXX_RELEASE >= 15@#if _GLIBCXX_RELEASE >= 11@' clang/lib/Headers/cuda_wrappers/array
%endif

# Reduce diskspace pressure
# There are a number of object files in clang/tests we will not be running
find .  \( -name '*.o' -o -name '*.a' \) -delete

install -pm 755 %{SOURCE1} prep.sh
sed -i -e 's@%%{pkg_prefix}@%{pkg_prefix}@' prep.sh
sed -i -e 's@%%{pkg_libdir}@%{pkg_libdir}@' prep.sh
sed -i -e 's@%%{amd_device_libs_prefix}@%{amd_device_libs_prefix}@' prep.sh
sed -i -e 's@%%{bundle_prefix}@%{bundle_prefix}@' prep.sh
grep -v '%%{' prep.sh

. ./prep.sh

%build
CLANG_VERSION=%llvm_maj_ver
LLVM_BINDIR=%{bundle_prefix}/bin
LLVM_LIBDIR=%{bundle_prefix}/lib
LLVM_CMAKEDIR=%{bundle_prefix}/lib/cmake/llvm

echo "%%rocmllvm_version $CLANG_VERSION"   > macros.rocmcompiler
echo "%%rocmllvm_bindir $LLVM_BINDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_libdir $LLVM_LIBDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR" >> macros.rocmcompiler

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
LINK_MEM=4
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%global llvm_projects "clang;clang-tools-extra;lld"
%if %{with libcxx}
%global llvm_runtimes "compiler-rt;libcxx;libcxxabi"
%else
%if %{with preview}
# rocm-omp is going away
# CMake Error at CMakeLists.txt:24 (message):
#  The legacy standalone build mode has been removed.  Please change
#      cmake <llvm-project>/openmp
#  to
#      cmake <llvm-project>/runtimes -DLLVM_ENABLE_RUNTIMES=openmp
%global llvm_runtimes "compiler-rt;openmp"
%else
%global llvm_runtimes "compiler-rt"
%endif
%endif

p=$PWD

#
# BASE LLVM
#
%global llvmrocm_cmake_config \\\
 -DBUILD_SHARED_LIBS=OFF \\\
 -DBUILD_TESTING=OFF \\\
 -DCLANG_ENABLE_STATIC_ANALYZER=%{build_sa} \\\
 -DCLANG_ENABLE_ARCMT=OFF \\\
 -DCLANG_ENABLE_CLANGD=OFF \\\
 -DCLANG_TOOL_CLANG_FUZZER_BUILD=OFF \\\
 -DCLANG_TOOL_C_INDEX_TEST_BUILD=OFF \\\
 -DCMAKE_BUILD_TYPE=%{build_type} \\\
 -DCMAKE_INSTALL_DO_STRIP=ON \\\
 -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \\\
 -DCOMPILER_RT_BUILD_BUILTINS=ON \\\
 -DCOMPILER_RT_BUILD_CTX_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_GWP_ASAN=OFF \\\
 -DCOMPILER_RT_BUILD_LIBFUZZER=OFF \\\
 -DCOMPILER_RT_BUILD_MEMPROF=OFF \\\
 -DCOMPILER_RT_BUILD_ORC=OFF \\\
 -DCOMPILER_RT_BUILD_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_SANITIZERS=OFF \\\
 -DCOMPILER_RT_BUILD_XRAY=OFF \\\
 -DENABLE_LINKER_BUILD_ID=ON \\\
 -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
 -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
 -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \\\
 -DLIBOMPTARGET_NVPTX_CUDA_COMPILER="" \\\
 -DLIBOMPTARGET_NVPTX_BC_LINKER="" \\\
 -DLIBOMP_OMPD_GDB_SUPPORT=OFF \\\
 -DLIBOMPTARGET_BUILD_AMDGPU_PLUGIN=ON \\\
 -DLIBOMPTARGET_BUILD_CUDA_PLUGIN=OFF \\\
 -DLIBOMPTARGET_BUILD_DEVICERTL_BCLIB=ON \\\
 -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \\\
 -DLIBOMP_INSTALL_ALIASES=OFF \\\
 -DLIBOMP_ARCHER_SUPPORT=OFF \\\
 -DLLVM_BINUTILS_INCDIR=%{_includedir} \\\
 -DLLVM_BUILD_RUNTIME=ON \\\
 -DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
 -DLLVM_ENABLE_EH=ON \\\
 -DLLVM_ENABLE_FFI=ON \\\
 -DLLVM_ENABLE_LIBCXX=%{build_libcxx} \\\
 -DLLVM_ENABLE_OCAMLDOC=OFF \\\
 -DLLVM_ENABLE_RTTI=ON \\\
 -DLLVM_ENABLE_ZLIB=ON \\\
 -DLLVM_ENABLE_ZSTD=ON \\\
 -DLLVM_INCLUDE_BENCHMARKS=OFF \\\
 -DLLVM_INCLUDE_EXAMPLES=OFF \\\
 -DLLVM_INCLUDE_TESTS=OFF \\\
 -DLLVM_LIBDIR_SUFFIX=%{pkg_libdir_suffix} \\\
 -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
 -DLLVM_TOOL_GOLD_BUILD=%{build_gold} \\\
 -DLLVM_TOOL_LLVM_AS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DIS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DLANG_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_EXEGESIS_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ISEL_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ITANIUM_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_ASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_DISASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MICROSOFT_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_OPT_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_RUST_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_SPECIAL_CASE_LIST_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_NUMERIC_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_VFABI_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_VERSION_SUFFIX=%{llvm_version_suffix} \\\
 -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
 -DLLVM_BUILD_LLVM_DYLIB=ON \\\
 -DLLVM_LINK_LLVM_DYLIB=ON \\\
 -DLLVM_BUILD_TOOLS=ON \\\
 -DLLVM_BUILD_UTILS=ON \\\
 -DMLIR_BUILD_MLIR_C_DYLIB=ON

pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm
%else
%global _vpath_srcdir llvm
%global _vpath_builddir build-llvm
%endif

# Mixing use of gcc and clang in the build conflicts with rpm's setting of flags.
# Set them manually as CMAKE_<LANG>_FLAGS
export CFLAGS=""
export CXXFLAGS=""
export LDFLAGS=""

# So just built tools can find their *.so's
export LD_LIBRARY_PATH=$PWD/build-llvm/lib
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++

%if 0%{?suse_version}
%cmake \
%else
%__cmake -S llvm -B build-llvm \
%endif
       %{llvmrocm_cmake_config} \
       -DCMAKE_CXX_COMPILER=/usr/bin/g++ \
       -DCMAKE_C_COMPILER=/usr/bin/gcc \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects}

%if 0%{?suse_version}
%cmake_build -j ${JOBS}
cd ..
%else
%make_build -C build-llvm -j ${JOBS}
%endif

# Reduce diskspace pressure
# Remove files that won't be needed anymore
find build-llvm  \( -name '*.o' -o -name '*.a' \) -delete

popd

build_stage1=$p/build-llvm

%global llvmrocm_stage1_config \\\
    -DCMAKE_AR=$build_stage1/bin/llvm-ar \\\
    -DCMAKE_C_COMPILER=$build_stage1/bin/clang \\\
    -DCMAKE_CXX_COMPILER=$build_stage1/bin/clang++ \\\
    -DCMAKE_LINKER=$build_stage1/bin/ld.lld \\\
    -DCMAKE_RANLIB=$build_stage1/bin/llvm-ranlib \\\
    -DLLVM_DIR=$build_stage1/lib/cmake/llvm \\\
    -DClang_DIR=$build_stage1/lib/cmake/clang \\\
    -DLLD_DIR=$build_stage1/lib/cmake/lld

#
# Rebuild and add libc++
#
pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm-2
%else
%global _vpath_srcdir llvm
%global _vpath_builddir build-llvm-2
%endif

export LD_LIBRARY_PATH=$PWD/build-llvm-2/lib

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_stage1_config} \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF \
       -DCLANG_DEFAULT_LINKER=lld \
       -DLLVM_ENABLE_LLD=ON \
       -DLLVM_TOOL_COMPILER_RT_BUILD=ON \
       -DLLVM_TOOL_LIBCXXABI_BUILD=%{build_libcxx} \
       -DLLVM_TOOL_LIBCXX_BUILD=%{build_libcxx} \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects} \
       -DLLVM_ENABLE_RUNTIMES=%{llvm_runtimes}

%cmake_build -j ${JOBS}

popd

build_stage2=$p/build-llvm-2

%global llvmrocm_tools_config \\\
       -DLLVM_DIR=$build_stage2/lib/cmake/llvm \\\
       -DClang_DIR=$build_stage2/lib/cmake/clang \\\
       -DLLD_DIR=$build_stage2/lib/cmake/lld

export CC=$build_stage2/bin/clang
export CXX=$build_stage2/bin/clang++
export LD=$build_stage2/bin/ld.lld

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%global _vpath_srcdir amd/device-libs
%global _vpath_builddir build-devicelibs
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{amd_device_libs_prefix}

%cmake_build -j ${JOBS}
popd

build_devicelibs=$p/build-devicelibs
%global llvmrocm_devicelibs_config \\\
       -DAMDDeviceLibs_DIR=$build_devicelibs/%{pkg_libdir}/cmake/AMDDeviceLibs

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/hipcc
%define __builddir build-hipcc
%else
%global _vpath_srcdir amd/hipcc
%global _vpath_builddir build-hipcc
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF

%cmake_build -j ${JOBS}
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/comgr
%define __builddir build-comgr
%else
%global _vpath_srcdir amd/comgr
%global _vpath_builddir build-comgr
%endif

%cmake -G "Unix Makefiles" \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir}

# cmake produces a link.txt that includes libLLVM*.so, hack it out
%if 0%{?suse_version}
sed -i -e 's@libLLVM.so.%{llvm_maj_ver}.0%{llvm_version_suffix}@libLLVMCore.a@' CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' CMakeFiles/amd_comgr.dir/link.txt
%else
sed -i -e 's@libLLVM.so.%{llvm_maj_ver}.0%{llvm_version_suffix}@libLLVMCore.a@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
%if %{with preview}
# Remove libclang-cpp.so from link
sed -i -e 's/[^ ]*libclang-cpp[^ ]*//g' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
# Add libraries to cover the removal
sed -i -e 's@-lrt -lm@-lclangSerialization -lclangAST -lclangDriver -lclangScalableStaticAnalysisFrameworkAnalyses -lclangDependencyScanning -lclangOptions -lclangFrontend -lclangFrontendTool -lclangScalableStaticAnalysisFrameworkFrontend -lclangScalableStaticAnalysisFrameworkCore -lclangExtractAPI -lclangInstallAPI -lclangIndex -lclangCodeGen -lclangStaticAnalyzerFrontend -lclangStaticAnalyzerCore -lclangStaticAnalyzerCheckers -lclangASTMatchers -lclangCrossTU -lclangUnifiedSymbolResolution -lclangTooling -lclangToolingCore -lclangRewriteFrontend -lclangRewrite -lclangParse -lclangSema -lclangAPINotes -lclangAnalysis -lclangFormat -lclangToolingInclusions -lclangAnalysisLifetimeSafety -lclangLex -lclangEdit -lclangBasic -lclangSupport -lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMDTLTO -lLLVMLTO -lLLVMPlugins -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
%else
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
%endif
%endif

%cmake_build -j ${JOBS}

# Check that static linking happened
# ldd build-comgr/libamd_comgr.so
# false

popd

%check
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%global _vpath_srcdir amd/device-libs
%global _vpath_builddir build-devicelibs
%endif
pushd .
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn build-devicelibs/amdgcn
%if %{with broken_tests}
%ctest
%endif
popd

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

#
# BASE LLVM
#
pushd .
%if 0%{?suse_version}
%define __builddir build-llvm-2
%else
%global _vpath_builddir build-llvm-2
%endif

%cmake_install

popd

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __builddir build-devicelibs
%else
%global _vpath_builddir build-devicelibs
%endif

%cmake_install

# move cmake bits to where the others are
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
mv %{buildroot}%{amd_device_libs_prefix}/%{pkg_libdir}/cmake/* %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
# no extra license please
rm -rf %{buildroot}%{amd_device_libs_prefix}/share

popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __builddir build-comgr
%else
%global _vpath_builddir build-comgr
%endif

%cmake_install
popd

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __builddir build-hipcc
%else
%global _vpath_builddir build-hipcc
%endif

%cmake_install
popd

rm -rf %{buildroot}%{pkg_prefix}/hip
rm -rf %{buildroot}%{pkg_prefix}/share/doc/packages/*

%if 0%{?suse_version}
find %{buildroot}%{bundle_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{pkg_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{bundle_prefix}/lib -type f -name '*.so*' -exec strip {} \;
find %{buildroot}%{pkg_prefix}/lib64 -type f -name '*.so*' -exec strip {} \;
%endif

# Remove lld's libs
rm -rf %{buildroot}%{bundle_prefix}/include/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/liblld*
# rm wasm-ld
rm -rf %{buildroot}%{bundle_prefix}/bin/wasm-ld

# Remove exec perm
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/optpmap.py
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/style.css

# Lingering perl
rm -f %{buildroot}%{pkg_prefix}/bin/hipvars.pm

# Extra docs
rm -rf %{buildroot}%{pkg_prefix}/share/doc/ROCm-Device-Libs/LICENSE.TXT
rm -rf %{buildroot}%{pkg_prefix}/share/doc/amd_comgr/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/doc/amd_comgr/README.md
rm -rf %{buildroot}%{pkg_prefix}/share/doc/hipcc/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/doc/hipcc/README.md
rm -rf %{buildroot}%{bundle_prefix}/share/man/man1/scan-build.1

# rocm-clang.x86_64: W: dangling-relative-symlink /usr/lib64/rocm/llvm/bin/nvptx-arch offload-arch
rm -f %{buildroot}%{bundle_prefix}/bin/nvptx-arch

# rocm-clang-analyzer.x86_64: E: non-executable-script /usr/lib64/rocm/llvm/share/scan-view/Reporter.py 644 /usr/bin/env python
sed -i -e 's@/usr/bin/env python@/usr/bin/python3@' %{buildroot}%{bundle_prefix}/share/scan-view/*.py
chmod a+x %{buildroot}%{bundle_prefix}/share/scan-view/*.py

# rocm-clang-devel.x86_64: E: zero-length /usr/lib64/rocm/llvm/include/clang/Basic/DiagnosticASTCompatIDs.inc
# Removing these causea a problem later
# In file included from /usr/lib64/rocm/llvm/include/clang/Basic/DiagnosticIDs.h:103:
# /usr/lib64/rocm/llvm/include/clang/Basic/DiagnosticCommonInterface.inc:22:10: fatal error: 'clang/Basic/DiagnosticCommonEnums.inc' file not found
   22 | #include "clang/Basic/DiagnosticCommonEnums.inc"

# rocm-clang-analyzer.x86_64: W: devel-file-in-non-devel-package /usr/lib64/rocm/llvm/lib/libear/ear.c
rm %{buildroot}%{bundle_prefix}/lib/libear/ear.c

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n %{device_libs_name}
%license amd/device-libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{pkg_prefix}/%{pkg_libdir}/cmake/AMDDeviceLibs/
%{amd_device_libs_prefix}/amdgcn

%files -n %{comgr_name}
%license amd/comgr/LICENSE.txt
%doc amd/comgr/README.md
%{pkg_prefix}/%{pkg_libdir}/libamd_comgr.so.*

%files -n %{comgr_name}-devel
%{pkg_prefix}/include/amd_comgr/
%{pkg_prefix}/%{pkg_libdir}/cmake/amd_comgr/
%{pkg_prefix}/%{pkg_libdir}/libamd_comgr.so

%files -n %{hipcc_name}
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md
%{pkg_prefix}/bin/hipcc
%{pkg_prefix}/bin/hipconfig

# ROCM LLVM
%files -n %{rocm_llvm_name}-filesystem
%dir %{bundle_prefix}
%dir %{bundle_prefix}/bin
%dir %{bundle_prefix}/include
%dir %{bundle_prefix}/include/clang
%dir %{bundle_prefix}/include/clang-c
%dir %{bundle_prefix}/include/llvm
%dir %{bundle_prefix}/include/llvm-c
%dir %{bundle_prefix}/include/clang-tidy
%dir %{bundle_prefix}/lib
%dir %{bundle_prefix}/lib/clang
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/cuda_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/llvm_libc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/openmp_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/ppc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux
%dir %{bundle_prefix}/lib/cmake
%dir %{bundle_prefix}/lib/cmake/clang
%dir %{bundle_prefix}/lib/cmake/llvm
%dir %{bundle_prefix}/libexec
%dir %{bundle_prefix}/share
%dir %{bundle_prefix}/share/clang
%dir %{bundle_prefix}/share/opt-viewer

%files -n %{rocm_llvm_name}-libs
%license llvm/LICENSE.TXT
%{bundle_prefix}/lib/libLLVM-*.so
%{bundle_prefix}/lib/libLLVM.so.*
%{bundle_prefix}/lib/libLTO.so.*
%{bundle_prefix}/lib/libRemarks.so.*

%if 0%{?suse_version}
%ldconfig_scriptlets -n %{rocm_llvm_name}-libs
%endif

%files -n %{rocm_llvm_name}
%license llvm/LICENSE.TXT
%if %{without preview}
%{bundle_prefix}/bin/bugpoint
%else
%{bundle_prefix}/bin/llubi
%endif
%{bundle_prefix}/bin/llc
%{bundle_prefix}/bin/lli
%{bundle_prefix}/bin/amdgpu-arch
%{bundle_prefix}/bin/dsymutil
%{bundle_prefix}/bin/llvm*
%{bundle_prefix}/bin/offload-arch
%{bundle_prefix}/bin/opt
%{bundle_prefix}/bin/reduce-chunk-list
%{bundle_prefix}/bin/sancov
%{bundle_prefix}/bin/sanstats
%{bundle_prefix}/bin/verify-uselistorder
%{bundle_prefix}/share/opt-viewer/

%files -n %{rocm_llvm_name}-devel
%license llvm/LICENSE.TXT
%{bundle_prefix}/include/llvm/
%{bundle_prefix}/include/llvm-c/
%{bundle_prefix}/lib/cmake/llvm/
%{bundle_prefix}/lib/libLLVM.so
%{bundle_prefix}/lib/libLTO.so
%{bundle_prefix}/lib/libRemarks.so
%if %{with gold}
%{bundle_prefix}/lib/LLVMgold.so
%endif

%files -n %{rocm_llvm_name}-static
%license llvm/LICENSE.TXT
%{bundle_prefix}/lib/libLLVM*.a

# ROCM CLANG
%files -n %{rocm_clang_name}-libs
%license clang/LICENSE.TXT
%{bundle_prefix}/lib/libclang*.so.*

%files -n %{rocm_clang_name}-runtime-devel
%license clang/LICENSE.TXT
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/clang_rt.*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/libclang_rt.*

%files -n %{rocm_clang_name}
%license clang/LICENSE.TXT
%{bundle_prefix}/bin/clang*
%{bundle_prefix}/bin/diagtool
%{bundle_prefix}/bin/find-all-symbols
%{bundle_prefix}/bin/flang
%{bundle_prefix}/bin/git-clang-format
%{bundle_prefix}/bin/hmaptool
%{bundle_prefix}/bin/modularize
%{bundle_prefix}/bin/pp-trace
%{bundle_prefix}/share/clang/
%{bundle_prefix}/share/clang-doc
%{bundle_prefix}/bin/amdclang*
%{bundle_prefix}/bin/amdflang*
%{bundle_prefix}/bin/amdlld
%{bundle_prefix}/bin/amdllvm
%if %{with preview}
%endif

%files -n %{rocm_clang_name}-devel
%license clang/LICENSE.TXT
%{bundle_prefix}/include/clang/
%{bundle_prefix}/include/clang-c/
%{bundle_prefix}/lib/cmake/clang/
%{bundle_prefix}/lib/libclang*.so

# ROCM CLANG TOOLS EXTRA
%files -n %{rocm_clang_tools_extra_name}
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/bin/run-clang-tidy

%files -n %{rocm_clang_tools_extra_name}-devel
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/include/clang-tidy/

# ROCM LLD
%files -n %{rocm_lld_name}
%license lld/LICENSE.TXT
%{bundle_prefix}/bin/ld.lld
%{bundle_prefix}/bin/ld64.lld
%{bundle_prefix}/bin/lld
%{bundle_prefix}/bin/lld-link

# ROCM LIBC++
%if %{with libcxx}
%files -n %{rocm_libcxx_name}
%license libcxx/LICENSE.TXT
%{bundle_prefix}/lib/libc++.so.*
%{bundle_prefix}/lib/libc++abi.so.*
%{bundle_prefix}/lib/libc++.modules.json

%if 0%{?suse_version}
%ldconfig_scriptlets -n %{rocm_libcxx_name}
%endif

%files -n %{rocm_libcxx_name}-devel
%dir %{bundle_prefix}/share/libc++
%{bundle_prefix}/include/c++/
%{bundle_prefix}/share/libc++/
%{bundle_prefix}/lib/libc++.so
%{bundle_prefix}/lib/libc++abi.so

%files -n %{rocm_libcxx_name}-static
%{bundle_prefix}/lib/libc++.a
%{bundle_prefix}/lib/libc++abi.a
%{bundle_prefix}/lib/libc++experimental.a
%endif

%if %{with sa}
%files -n %{rocm_clang_analyzer_name}
%{bundle_prefix}/bin/analyze-build
%{bundle_prefix}/bin/intercept-build
%{bundle_prefix}/bin/scan-build
%{bundle_prefix}/bin/scan-build-py
%{bundle_prefix}/bin/scan-view
%{bundle_prefix}/lib/libear/
%{bundle_prefix}/lib/libscanbuild/
%{bundle_prefix}/libexec/analyze-c++
%{bundle_prefix}/libexec/analyze-cc
%{bundle_prefix}/libexec/c++-analyzer
%{bundle_prefix}/libexec/ccc-analyzer
%{bundle_prefix}/libexec/intercept-c++
%{bundle_prefix}/libexec/intercept-cc
%{bundle_prefix}/share/scan-build/
%{bundle_prefix}/share/scan-view/
%endif

%if %{with preview}
%files -n %{rocm_omp_name}-devel
%{bundle_prefix}/lib/cmake/openmp/
%{bundle_prefix}/lib/libomp*.so
%endif

%changelog
