#
# spec file for package hipsolver
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


%global upstreamname hipsolver

%global pkg_library_name %{upstreamname}
%global pkg_library_version 1

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global upstreamname hipsolver
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

%if 0%{?rhel} && 0%{?rhel} < 10
# RHEL 9 has a problem finding cblas.h, so disable testing
%else
%bcond_with test
%endif
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# gfortran and clang rpm macros do not mix
%global build_fflags %{nil}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           hipsolver%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        6%{?dist}
%endif
Summary:        ROCm SOLVER marshaling library
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
BuildRequires:  patchelf
BuildRequires:  rocblas%{pkg_suffix}-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocsolver%{pkg_suffix}-devel
BuildRequires:  rocsparse%{pkg_suffix}-devel
%if 0%{?fedora}
BuildRequires:  suitesparse-devel
%endif

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  hipsparse%{pkg_suffix}-devel
%if 0%{?suse_version}
BuildRequires:  blas-devel
BuildRequires:  cblas-devel
BuildRequires:  lapack-devel
%else
BuildRequires:  blas-static
BuildRequires:  lapack-static
%endif
%endif

%if %{with preview}
# needed for geev
# https://www.netlib.org/lapack/explore-html/d4/d68/group__geev.html
#
# Trying just lapack-devel, gives this error
# CMake Error at /usr/lib64/cmake/lapack-3.12.0/lapack-targets.cmake:102 (message):
#  The imported target "blas" references the file
#     "/usr/lib64/libblas.a"
BuildRequires:  blas-static
BuildRequires:  lapack-static
%endif

Provides:       hipsolver%{pkg_suffix} = %{version}-%{release}
Requires:       rocblas%{pkg_suffix}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}
Requires:       rocsolver%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipSOLVER is a LAPACK marshaling library, with multiple supported
backends. It sits between the application and a 'worker'
LAPACK library, marshaling inputs into the backend library and
marshaling results back to the application. hipSOLVER exports an
interface that does not require the client to change, regardless
of the chosen backend. Currently, hipSOLVER supports rocSOLVER
and cuSOLVER as backends.

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
Requires:       rocm-filesystem%{pkg_suffix}
Provides:       hipsolver%{pkg_suffix}-devel = %{version}-%{release}

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
%autosetup -p3 -n %{upstreamname}

%build
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DHIPSOLVER_INTERNAL_LAPACK_BUILD=OFF

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipsolver/LICENSE.md

%if %{with compat}
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}.*
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_fortran.so.%{pkg_library_version}.*
%endif

# E: unused-direct-shlib-dependency .../libhipsolver_fortran.so.1.0 /lib64/libm.so.6
patchelf --remove-needed libm.so.6 %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_fortran.so.%{pkg_library_version}.*
# E: unused-direct-shlib-dependency .../libhipsolver_fortran.so.1.0 /lib64/libgcc_s.so.1
patchelf --remove-needed libgcc_s.so.1 %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_fortran.so.%{pkg_library_version}.*

%files -n %{pkg_name}
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_fortran.so.%{pkg_library_version}{,.*}

%files devel
%{pkg_prefix}/include/hipsolver/
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}_fortran.so
%{pkg_prefix}/%{pkg_libdir}/cmake/hipsolver/

%if %{with test}
%files test
%{pkg_prefix}/share/hipsolver/
%{pkg_prefix}/bin/hipsolver*
%endif

%changelog
