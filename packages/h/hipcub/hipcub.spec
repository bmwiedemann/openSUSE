#
# spec file for package hipcub
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


%global upstreamname hipcub

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
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
# there is no debug package
%{!?suse_version:%global debug_package %{nil}}

# build test subpackage
%bcond_with test

# Option to test suite for testing on real HW:
%bcond_with check

%if %{with check} || %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           hipcub%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        5%{?dist}
%endif
Summary:        ROCm port of CUDA CUB library

License:        BSD-3-Clause AND MIT
# The main license is BSD-3-Clause because hipcub is a derivative of cub
# https://github.com/NVIDIA/cub/blob/main/LICENSE.TXT
#
# New changes are MIT, these files
#  CMakeLists.txt
#  cmake/*
#  cmake/VerifyCompiler.cmake
#  hipcub/CMakeLists.txt
#  hipcub/include/hipcub/agent/single_pass_scan_operators.hpp
#  hipcub/include/hipcub/backend/cub/iterator/tex_obj_input_iterator.hpp
#  hipcub/include/hipcub/backend/cub/thread/thread_operators.hpp
#  hipcub/include/hipcub/backend/cub/tuple.hpp
#  hipcub/include/hipcub/backend/rocprim/iterator/iterator_category.hpp
#  hipcub/include/hipcub/backend/rocprim/iterator/iterator_wrapper.hpp
#  hipcub/include/hipcub/backend/rocprim/tuple.hpp
#  hipcub/include/hipcub/backend/rocprim/warp/specializations/warp_exchange_shfl.hpp
#  hipcub/include/hipcub/backend/rocprim/warp/specializations/warp_exchange_smem.hpp
#  hipcub/include/hipcub/hipcub.hpp
#  hipcub/include/hipcub/hipcub_version.hpp.in
#  hipcub/include/hipcub/tuple.hpp

URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocprim%{pkg_suffix}-static

%if %{with check} || %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
BuildRequires:  rocminfo%{pkg_suffix}
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipCUB is a thin wrapper library on top of rocPRIM or CUB. It enables developers
to port a project using the CUB library to the HIP layer to run on AMD hardware.
In the ROCm environment, hipCUB uses the rocPRIM library as the backend.

%package devel
Summary:        The %{upstreamname} development package
Provides:       %{name}-static = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocprim%{pkg_suffix}-devel

# the devel subpackage is only headers and cmake infra
BuildArch:      noarch

%description devel
The %{upstreamname} development package.

%if %{with test}
%package test
Summary:        Self-tests for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description test
Precompiled self-tests for %{name}
%endif

%prep
%autosetup -p1 -n %{upstreamname}

#
# The ROCMExportTargetsHeaderOnly.cmake file
# generates a files that reference the install location of other files
# Make this change so they match
sed -i -e 's/ROCM_INSTALL_LIBDIR lib/ROCM_INSTALL_LIBDIR share/' cmake/ROCMExportTargetsHeaderOnly.cmake

# simplify the source for licensing when not testing
%if %{without test}
rm -rf examples test benchmark
%endif

%build

%if %{with check}
# Building all the gpu's does not make sense
# Build only the first one, this only works well with rpmbuild.
gpu=`rocm_agent_enumerator | head -n 1`
%endif

%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DBUILD_TEST=%{build_test} \
%if %{with check}
    -DAMDGPU_TARGETS=${gpu} \
%else
    -DAMDGPU_TARGETS=${gpu_list} \
%endif
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipcub/LICENSE.txt

%if %{with check}
%check
%ctest
%endif

%files devel
%doc README.md
%license LICENSE.txt NOTICES.txt
%{pkg_prefix}/include/hipcub
%{pkg_prefix}/share/cmake/hipcub

%if %{with test}
%files test
%{pkg_prefix}/bin/test_*
%{pkg_prefix}/bin/hipcub/
%endif

%changelog
