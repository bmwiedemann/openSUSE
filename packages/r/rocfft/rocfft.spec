#
# spec file for package rocfft
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


%global upstreamname rocfft

%global pkg_library_name %{upstreamname}
%global pkg_library_version 0

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
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif

%if 0%{?suse_version}
%global pkg_name lib%{pkg_library_name}%{pkg_library_version}%{pkg_suffix}
%else
%global pkg_name %{NAME}
%endif

%global toolchain rocm

# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# kernel oops on gfx1201
# https://github.com/ROCm/rocFFT/issues/560
%bcond_with test
%if %{with test}
# Disable rpatch checks for a local build
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

# For docs
%bcond_with doc

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# Use rocm-llvm strip
%global __strip %rocmllvm_bindir/llvm-strip

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

%if 0%{?fedora} || 0%{?suse_version}
%global system_sqlite ON
%else
%if 0%{?rhel} < 10
# rhel 9's sqlite is too old, fetch whatever rocfft bundles
# assumes --enable-network
%global system_sqlite OFF
%else
%global system_sqlite ON
%endif
%endif

%global cmake_config \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_CXX_FLAGS="--rtlib=compiler-rt --unwindlib=libgcc" \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DROCFFT_BUILD_OFFLINE_TUNER=OFF \\\
  -DROCFFT_KERNEL_CACHE_ENABLE=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DSQLITE_USE_SYSTEM_PACKAGE=%{system_sqlite}

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           rocfft%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        9%{?dist}
%endif
Summary:        ROCm Fast Fourier Transforms (FFT) library
License:        BSD-3-Clause AND MIT
# MIT: The main license
# BSD-3-Clause:
#  shared/CLI11.hpp

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
BuildRequires:  pkgconfig(sqlite3)

%if %{with test}
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  hiprand%{pkg_suffix}-devel
BuildRequires:  rocrand%{pkg_suffix}-devel

%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif

# rocfft-test compiles some things and requires rocm-hip-devel
Requires:       rocm-hip%{pkg_suffix}-devel

%endif

%if %{with doc}
%if 0%{?suse_version}
BuildRequires:  %{python_module Sphinx}
%else
BuildRequires:  python3dist(sphinx)
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

Provides:       rocfft%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-runtime%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Shared libraries for %{name}

%description -n %{pkg_name}
%{summary}

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        The rocFFT development package
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}-devel

%description devel
The rocFFT development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}

# Do not care so much about the sqlite version
sed -i -e 's@SQLite3 3.50.2 @SQLite3 @' cmake/sqlite.cmake

%build

# ensuring executables are PIE enabled
export LDFLAGS="${LDFLAGS} -pie"

# OpenMP tests are disabled because upstream sets rpath in that case without
# a way to skip
#
# RHEL 9 has an issue with missing symbol __truncsfhf2 in libgcc.
# So switch from libgcc to rocm-llvm's libclang-rt.builtins with
# the rtlib=compiler-rt. Leave unwind unchange with unwindlib=libgcc
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{gpu_list}

%cmake_build

%install
%cmake_install

# we don't need the rocfft_rtc_helper binary, don't package it
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"

# we don't need or want the client-info file installed by rocfft
rm -rf %{buildroot}/%{pkg_prefix}/.info

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocfft/LICENSE.md

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
%{__builddir}/clients/staging/rocfft-test
%else
%{_vpath_builddir}/clients/staging/rocfft-test
%endif
%endif
%endif

%files -n %{pkg_name}
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}

%files devel
%{pkg_prefix}/include/rocfft/
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocfft/

%if %{with test}
%files test
%{pkg_prefix}/bin/rocfft-test
%{pkg_prefix}/bin/rtc_helper_crash
%endif

%changelog
