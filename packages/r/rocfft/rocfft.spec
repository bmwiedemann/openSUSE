#
# spec file for package rocfft
#
# Copyright (c) 2025 SUSE LLC
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
%global rocfft_name librocfft0
%else
%global rocfft_name rocfft
%endif

%global upstreamname rocFFT

%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

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
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
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

%global cmake_config \\\
  -DCMAKE_CXX_COMPILER=hipcc \\\
  -DCMAKE_CXX_FLAGS="--rtlib=compiler-rt --unwindlib=libgcc" \\\
  -DCMAKE_C_COMPILER=hipcc \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DROCFFT_BUILD_OFFLINE_TUNER=OFF \\\
  -DROCFFT_KERNEL_CACHE_ENABLE=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DSQLITE_USE_SYSTEM_PACKAGE=ON

%bcond_with generic
%global rocm_gpu_list_generic "gfx9-generic;gfx9-4-generic;gfx10-1-generic;gfx10-3-generic;gfx11-generic;gfx12-generic"
%if %{with generic}
%global gpu_list %{rocm_gpu_list_generic}
%else
%global gpu_list %{rocm_gpu_list_default}
%endif

Name:           rocfft
Version:        %{rocm_version}
Release:        6%{?dist}
Summary:        ROCm Fast Fourier Transforms (FFT) library

URL:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-runtime-devel
BuildRequires:  pkgconfig(sqlite3)

%if %{with test}
BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  hiprand-devel
BuildRequires:  rocrand-devel

%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif

# rocfft-test compiles some things and requires rocm-hip-devel
Requires:       rocm-hip-devel

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

Provides:       rocfft = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Patch0:         0001-cmake-use-gnu-installdirs.patch

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%if 0%{?suse_version}
%package -n %{rocfft_name}
Summary:        Shared libraries for %{name}

%description -n %{rocfft_name}
%{summary}

%ldconfig_scriptlets -n %{rocfft_name}
%endif

%package devel
Summary:        The rocFFT development package
Requires:       %{rocfft_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-hip-devel

%description devel
The rocFFT development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p 1

# Do not care so much about the sqlite version
sed -i -e 's@SQLite3 3.36 @SQLite3 @' cmake/sqlite.cmake

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
    -DGPU_TARGETS=%{gpu_list} \
    -DCMAKE_INSTALL_LIBDIR=%_libdir

%cmake_build

%install
%cmake_install

# we don't need the rocfft_rtc_helper binary, don't package it
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"

# we don't need or want the client-info file installed by rocfft
rm -rf %{buildroot}/%{_prefix}/.info

rm -f %{buildroot}%{_prefix}/share/doc/rocfft/LICENSE.md

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

%files -n %{rocfft_name}
%doc README.md
%license LICENSE.md
%{_libdir}/librocfft.so.0{,.*}

%files devel
%dir %{_libdir}/cmake/rocfft
%dir %{_includedir}/rocfft
%{_includedir}/rocfft/*.h
%{_libdir}/librocfft.so
%{_libdir}/cmake/rocfft/*.cmake

%if %{with test}
%files test
%{_bindir}/rocfft-test
%{_bindir}/rtc_helper_crash
%endif

%changelog
