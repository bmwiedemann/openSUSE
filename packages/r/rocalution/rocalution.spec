#
# spec file for package rocalution
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


%global pkg_library_name rocalution
%global pkg_library_version 1

%bcond_with preview
%if %{with preview}
%global upstreamname rocalution
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global upstreamname rocALUTION
%global rocm_release 7.2
%global rocm_patch 0
%global pkg_src rocm-%{rocm_version}
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
%global pkg_name %{NAME}-libs
%else
%global pkg_name %{NAME}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

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

Name:           rocalution%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        6%{?dist}
%endif

Summary:        Next generation library for iterative sparse solvers for ROCm platform
License:        MIT

%if %{with preview}
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
URL:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocprim%{pkg_suffix}-static
BuildRequires:  rocrand%{pkg_suffix}-devel
BuildRequires:  rocsparse%{pkg_suffix}-devel

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
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

Provides:       rocalution%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%if 0%{?suse_version}
# Got the name wrong
Obsoletes:      libalution1 <= 6.4.1
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocALUTION is a sparse linear algebra library that can be used
to explore fine-grained parallelism on top of the ROCm platform
runtime and toolchains. Based on C++ and HIP, rocALUTION
provides a portable, generic, and flexible design that allows
seamless integration with other scientific software packages.

rocALUTION offers various backends for different (parallel) hardware:

Host
* OpenMP: Designed for multi-core CPUs
* HIP: Designed for ROCm-compatible devices
* MPI: Designed for multi-node clusters and multi-GPU setups

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Runtime for %{name}

%description -n %{pkg_name}
%summary

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Provides:       rocalution%{pkg_suffix}-devel = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description test
%{summary}
%endif

%prep
%if %{with preview}
%autosetup -p3 -n %{upstreamname}
%else
%autosetup -p1 -n %{upstreamname}-%{pkg_src}
%endif

%if 0%{?suse_version}
# On TW
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
sed -i -e 's@set(CMAKE_CXX_STANDARD 14)@set(CMAKE_CXX_STANDARD 17)@' clients/CMakeLists.txt
%endif

# rocalution.x86_64: E: undefined-non-weak-symbol /usr/lib64/librocalution_hip.so.1.0.0 _ZNK10rocalution10BaseVectorIdE5CheckEv	(/usr/lib64/librocalution_hip.so.1.0.0)
# Need to add -lrocalution to link
# Try this..
# sed -i -e 's@rocalution_hip PRIVATE roc::rocblas@rocalution_hip PRIVATE roc::rocalution roc::rocblas@' src/CMakeLists.txt
# Leads to
# CMake Error: The inter-target dependency graph contains the following strongly connected component (cycle):
#  "rocalution" of type SHARED_LIBRARY
#    depends on "rocalution_hip" (weak)
#  "rocalution_hip" of type SHARED_LIBRARY
#    depends on "rocalution" (weak)
# At least one of these targets is not a STATIC_LIBRARY.  Cyclic dependencies are allowed only among static libraries.
# CMake Generate step failed.  Build files cannot be regenerated correctly.

%build
%cmake %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
    -DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=%rocmllvm_bindir/ld.lld \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_MODULE_PATH=%{pkg_prefix}/%{pkg_libdir}/cmake/hip \
    -DHIP_ROOT_DIR=%{pkg_prefix} \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DBUILD_CLIENTS_TESTS=%{build_test}

%cmake_build

%install
%cmake_install
# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocalution/LICENSE.md

%if %{with compat}
# ERROR   0008: file '/usr/lib64/rocm/rocm-7.2/lib/librocalution.so.1.0'
#   contains the $ORIGIN runpath specifier at the wrong position in
#   [/usr/lib64/rocm/rocm-7.2/lib:$ORIGIN/../lib:$ORIGIN/../lib/rocalution/lib]
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}.*
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_hip.so.%{pkg_library_version}.*
%endif

%files -n %{pkg_name}
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_hip.so.%{pkg_library_version}{,.*}

%files devel
%doc README.md
%{pkg_prefix}/include/rocalution/
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_hip.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocalution/

%if %{with test}
%files test
%{pkg_prefix}/bin/rocalution*
%endif

%changelog
