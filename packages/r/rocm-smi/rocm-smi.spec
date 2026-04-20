#
# spec file for package rocm-smi
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


%global upstreamname rocm-smi-lib

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
%global pkg_skip_install_rpath FALSE
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_skip_install_rpath TRUE
%endif
%global pkg_name rocm-smi%{pkg_suffix}

%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with doc

Name:           %{pkg_name}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        3%{?dist}
%endif
Summary:        ROCm System Management Interface Library

License:        MIT AND NCSA
# The main license is MIT
# The NCSA license applies to these files
#  cmake_modules/utils.cmake
#  include/rocm_smi/rocm_smi.h
#  include/rocm_smi/rocm_smi_common.h
#  include/rocm_smi/rocm_smi_counters.h
#  include/rocm_smi/rocm_smi_device.h
#  include/rocm_smi/rocm_smi_exception.h
#  include/rocm_smi/rocm_smi_io_link.h
#  include/rocm_smi/rocm_smi_kfd.h
#  include/rocm_smi/rocm_smi_logger.h
#  include/rocm_smi/rocm_smi_main.h
#  include/rocm_smi/rocm_smi_monitor.h
#  include/rocm_smi/rocm_smi_power_mon.h
#  include/rocm_smi/rocm_smi_properties.h
#  include/rocm_smi/rocm_smi_utils.h
#  rocm_smi/example/rocm_smi_example.cc
#  src/rocm_smi.cc
#  src/rocm_smi_counters.cc
#  src/rocm_smi_device.cc
#  src/rocm_smi_io_link.cc
#  src/rocm_smi_kfd.cc
#  src/rocm_smi_logger.cc
#  src/rocm_smi_main.cc
#  src/rocm_smi_monitor.cc
#  src/rocm_smi_power_mon.cc
#  src/rocm_smi_properties.cc
#  src/rocm_smi_utils.cc
#  oam/src/oamConfig.in
#  src/rocm_smi64Config.in

URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%else
# SMI requires the AMDGPU kernel module, which only builds on:
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%endif

BuildRequires:  cmake
%if %{with doc}
# Fedora 38 has doxygen 1.9.6
%if 0%{?fedora} > 38
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
%endif
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  rocm-filesystem%{pkg_suffix}

%if %{with test}
BuildRequires:  gtest-devel
%endif

%if %{with compat}
Requires:       rocm-filesystem%{pkg_suffix}
%endif

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary:        ROCm SMI Library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
# /usr/include/rocm_smi/kfd_ioctl.h:26:10: fatal error: 'libdrm/drm.h' file not found
Requires:       libdrm-devel

%description devel
ROCm System Management Interface Library development files

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i -e 's@env python3@python3@' python_smi_tools/*.py
sed -i -e 's@env python3@python3@' python_smi_tools/rsmiBindingsInit.py.in

# do not download gtest and install
# https://github.com/ROCm/rocm-systems/issues/1022
sed -i -e 's@FetchContent_MakeAvailable(googletest)@#FetchContent_MakeAvailable(googletest)@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e 's@PUBLIC GTest::gtest_main@PUBLIC gtest_main gtest@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e '/TARGETS gtest gtest_main/,+3d' tests/rocm_smi_test/CMakeLists.txt

# fix iomanip include
# https://github.com/ROCm/rocm-systems/issues/1021
sed -i '/#include <string.*/a#include <iomanip>' tests/rocm_smi_test/test_base.h

# Do not package tests if we are building them
%if %{without test}
rm -rf tests
%endif

%build
%cmake \
    -DBUILD_TESTS=%{build_test} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{pkg_skip_install_rpath} \
    -DSHARE_INSTALL_PREFIX=%{pkg_prefix}/share

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-smi-lib/LICENSE.md

%if 0%{?suse_version}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc README.md
%license LICENSE.md
%{pkg_prefix}/bin/rocm-smi
%{pkg_prefix}/libexec/rocm_smi/
%{pkg_prefix}/%{pkg_libdir}/librocm_smi64.so.1{,.*}
%{pkg_prefix}/%{pkg_libdir}/liboam.so.1{,.*}

%files devel
%{pkg_prefix}/include/rocm_smi/
%{pkg_prefix}/include/oam/
%{pkg_prefix}/%{pkg_libdir}/librocm_smi64.so
%{pkg_prefix}/%{pkg_libdir}/liboam.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocm_smi/

%if %{with test}
%files test
%{pkg_prefix}/share/rsmitst_tests
%endif

%changelog
