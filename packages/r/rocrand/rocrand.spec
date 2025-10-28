#
# spec file for package rocrand
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
%global rocrand_name librocrand1
%else
%global rocrand_name rocrand
%endif

%global upstreamname rocRAND

%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' )

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# flags for testing, neither should be enabled for official builds in koji
# relevant HW is required to run %check
%bcond_with test
%bcond_with check

# do not check for rpaths when building test subpackages
%if %{with test} || %{with check}
%global __brp_check_rpaths %{nil}
%endif

# enable building of tests if check or test are enabled
%if %{with test} || %{with check}
%global build_test ON
%else
%global build_test OFF
%endif

# For docs
%bcond_with doc

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

# The common parts of the cmake configuration
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
  -DBUILD_TEST=%build_test

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%bcond_with generic
%global rocm_gpu_list_generic "gfx9-generic;gfx9-4-generic;gfx10-1-generic;gfx10-3-generic;gfx11-generic;gfx12-generic"
%if %{with generic}
%global gpu_list %{rocm_gpu_list_generic}
%else
%global gpu_list %{rocm_gpu_list_default}
%endif

Name:           rocrand
Version:        %{rocm_version}
Release:        8%{?dist}
Summary:        ROCm random number generator

URL:            https://github.com/ROCm/rocRAND
License:        BSD-3-Clause AND MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-runtime-devel

%if %{with test} || %{with check}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
%endif

%if %{with doc}
BuildRequires:  doxygen
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

Provides:       rocrand = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
The rocRAND project provides functions that generate pseudo-random and
quasi-random numbers.

The rocRAND library is implemented in the HIP programming language and
optimized for AMD's latest discrete GPUs. It is designed to run on top of AMD's
Radeon Open Compute ROCm runtime, but it also works on CUDA enabled GPUs.

%if 0%{?suse_version}
%package -n %{rocrand_name}
Summary:        Shared libraries for %{name}

%description -n %{rocrand_name}
%{summary}

%ldconfig_scriptlets -n %{rocrand_name}
%endif

%package devel
Summary:        The rocRAND development package
Requires:       %{rocrand_name}%{?_isa} = %{version}-%{release}

%description devel
The rocRAND development package.

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
# https://github.com/ROCm/rocm-libraries/issues/83
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++11's to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 11)@set(CMAKE_CXX_STANDARD 17)@' {,test/{cpp_wrapper,package}/}CMakeLists.txt

%build

%cmake %{cmake_generator} %{cmake_config} \
    -DAMDGPU_TARGETS=%{gpu_list} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocrand/LICENSE.txt

%check
%if %{with check}
%if 0%{?suse_version}
# Need some help to find librocrand.so on suse
# find . -name 'librocrand.so.1'
export LD_LIBRARY_PATH=$PWD/build/library:$LD_LIBRARY_PATH
%endif

%ctest
%endif

%files -n %{rocrand_name}
%doc README.md
%license LICENSE.txt
%{_libdir}/librocrand.so.1{,.*}

%files devel
%dir %{_libdir}/cmake/rocrand
%dir %{_includedir}/rocrand
%{_includedir}/rocrand/*.{h,hpp}
%{_libdir}/cmake/rocrand/*.cmake
%{_libdir}/librocrand.so

%if %{with test}
%files test
%dir %{_bindir}/rocRAND
%{_bindir}/test_*
%{_bindir}/rocRAND/*.cmake
%endif

%changelog
