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


%global upstreamname rocrand

%bcond_with preview
%if %{with preview}
%global rocm_release 7.11
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
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix %{rocm_release}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%if 0%{?suse_version}
%global rocrand_name librocrand1%{pkg_suffix}
%else
%global rocrand_name rocrand%{pkg_suffix}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' )
%if 0%{?suse_version}
# %%toolchain and %%build_cxxflags are Fedora rpm machinery; openSUSE implements
# neither, and its %%cmake injects %%optflags verbatim. Without this the host
# hardening flags reach the amdgcn device passes, where clang rejects them with
# "option 'cf-protection=return' cannot be specified on this target".
%global optflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fstack-clash-protection/-Xarch_host -fstack-clash-protection/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# flags for testing, neither should be enabled for official builds in koji
# relevant HW is required to run %check
%bcond_with test
# enable building of tests if test is enabled
%if %{with test}
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
  -DBUILD_TEST=%build_test \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%build_type \\\
  -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DROCM_SYMLINK_LIBS=OFF

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

# export an llvm compilation database
# Useful for input for other llvm tools
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

Name:           rocrand%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        3%{?dist}
%endif
Summary:        ROCm random number generator

URL:            https://github.com/ROCm/rocm-libraries
License:        0BSD AND MIT AND BSL-1.0 AND MIT AND BSD-3-Clause AND MIT
# The main license is MIT
# These other licenses apply to these files
# MIT AND BSL-1.0
#   library/include/rocrand/rocrand_common.h
# MIT AND BSD-3-Clause
#   library/include/rocrand/rocrand_mtgp32.h
#   library/include/rocrand/rocrand_mtgp32_11213.h
#   library/include/rocrand/rocrand_philox4x32_10.h
#   library/include/rocrand/rocrand_threefry2_impl.h
#   library/include/rocrand/rocrand_threefry2x32_20.h
#   library/include/rocrand/rocrand_threefry2x64_20.h
#   library/include/rocrand/rocrand_threefry4_impl.h
#   library/include/rocrand/rocrand_threefry4x32_20.h
#   library/include/rocrand/rocrand_threefry4x64_20.h
#   library/include/rocrand/rocrand_threefry_common.h
#   library/src/rng/mt19937.hpp
#   library/src/rng/mt19937_octo_engine.hpp
#   library/src/rng/mtgp32.hpp
#   library/src/rng/philox4x32_10.hpp

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-rpm-macros%{pkg_suffix}-modules
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

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

Provides:       rocrand%{pkg_suffix} = %{version}-%{release}

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
Requires:       %{rocrand_name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}

# On Tumbleweed Q3,2025
# https://github.com/ROCm/rocm-libraries/issues/83
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++11's to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 11)@set(CMAKE_CXX_STANDARD 17)@' {,test/{cpp_wrapper,package}/}CMakeLists.txt

# Remove some files not needed and reduce the licenses
rm -rf test/fortran/fruit

%build
%cmake %{cmake_generator} %{cmake_config} \
       -DAMDGPU_TARGETS=%{gpu_list} \

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/rocrand/LICENSE.md

%files -n %{rocrand_name}
%if %{with gitcommit}
%doc projects/rocrand/README.md
%license projects/rocrand/LICENSE.md
%else
%doc README.md
%license LICENSE.md
%endif

%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/librocrand-d.so.1{,.*}
%else
%{pkg_prefix}/%{pkg_libdir}/librocrand.so.1{,.*}
%endif

%files devel
%{pkg_prefix}/include/rocrand/
%{pkg_prefix}/%{pkg_libdir}/cmake/rocrand/
%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/librocrand-d.so
%else
%{pkg_prefix}/%{pkg_libdir}/librocrand.so
%endif

%if %{with test}
%files test
%{pkg_prefix}/bin/test_*
%{pkg_prefix}/bin/rocRAND/
%endif

%changelog
