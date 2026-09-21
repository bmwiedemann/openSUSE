#
# spec file for package rocm-runtime
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


%global upstreamname rocr-runtime

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
# 15.6
# rocm-runtime.x86_64: E: shlib-policy-name-error (Badness: 10000) libhsa-runtime64-1
# Your package contains a single shared library but is not named after its SONAME.
%global pkg_name libhsa-runtime64-1%{pkg_suffix}
# [  130s] libhsa-runtime64-1-static.x86_64: E: lto-no-text-in-archive (Badness: 10000) /usr/lib64/libhsakmt.a
# [  130s] This archive does not contain a non-empty .text section.  The archive was not
# [  130s] created with -ffat-lto-objects option.
#
# Disable building static on SUSE
%bcond_with static
%else
%global pkg_name rocm-runtime%{pkg_suffix}
%bcond_without static
%endif

%bcond_without kfdtest

Name:           rocm-runtime%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        4%{?dist}
%endif
Summary:        ROCm Runtime Library

License:        BSD-2-Clause AND MIT AND BSD-3-Clause AND NCSA AND GPL-2.0-only WITH Linux-syscall-note
# Main license is NCSA AND BSD-3-Clause
# libhsakmt is MIT AND BSD-2-Clause
# Misc files:
#  libhsakmt/include/hsakmt/linux/udmabuf.h
#  GPL-2.0-only WITH Linux-syscall-note
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

ExclusiveArch:  x86_64

# Image support is x86 only
%ifarch x86_64
%global enableimage 1
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-device-libs%{pkg_suffix}
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-llvm%{pkg_suffix}-static

%if 0%{?suse_version}
BuildRequires:  libelf-devel
BuildRequires:  libnuma-devel
BuildRequires:  zlib-devel
%if %{suse_version} > 1500
BuildRequires:  xxd
%else
BuildRequires:  vim
%endif
%else
BuildRequires:  elfutils-libelf-devel
BuildRequires:  numactl-devel
BuildRequires:  vim-common
%endif

Requires:       rocm-filesystem%{pkg_suffix}

%description
The ROCm Runtime Library is a thin, user-mode API that exposes the necessary
interfaces to access and interact with graphics hardware driven by the AMDGPU
driver set and the AMDKFD kernel driver. Together they enable programmers to
directly harness the power of AMD discrete graphics devices by allowing host
applications to launch compute kernels directly to the graphics hardware.

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Shared libraries for %{name}
Requires:       rocm-filesystem%{pkg_suffix}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}%{pkg_suffix} = %{version}-%{release}

%description -n %{pkg_name}
%{summary}
%endif

%package devel
Summary:        ROCm Runtime development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description devel
ROCm Runtime development files

%if %{with static}
%package static
Summary:        ROCm Runtime hsakmt development files
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       %{name}%{pkg_suffix}-static = %{version}-%{release}

%description static
%{summary}
%endif

%if %{with kfdtest}
%package -n kfdtest
Summary:        Test suite for ROCm's KFD kernel module
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-smi%{pkg_suffix}

%description -n kfdtest
This package includes ROCm's KFD kernel module test suite (kfdtest), the list of
excluded tests for each ASIC, and a convenience script to run the test suite.
%endif

%prep
%autosetup -n %{upstreamname} -p3

# Use llvm's static libs kfdtest
sed -i -e 's@LLVM_LINK_LLVM_DYLIB@0@' libhsakmt/tests/kfdtest/CMakeLists.txt

# gcc 15 include cstdint
sed -i '/#include <memory>.*/a#include <cstdint>' runtime/hsa-runtime/core/inc/amd_elf_image.hpp

# Remove source we are not using to make license review easier
rm -rf rocrtst
rm -f clang-format-diff.py

# libhsakmt license
cp -p libhsakmt/LICENSE.md LICENSE_libhsakmt.md

%build

export PATH=%{rocmllvm_bindir}:$PATH

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SHARED_LINKER_FLAGS=-ldrm_amdgpu \
    -DINCLUDE_PATH_COMPATIBILITY=OFF \
    %{?!enableimage:-DIMAGE_SUPPORT=OFF}
%cmake_build

%if %{with kfdtest}
%if 0%{?suse_version}
cd ..
export LIBHSAKMT_PATH=$(pwd)/build/libhsakmt/archive
%else
export LIBHSAKMT_PATH=$(pwd)/%__cmake_builddir/libhsakmt/archive
%endif
cd libhsakmt/tests/kfdtest
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLVM_DIR=%{rocmllvm_cmakedir}
%cmake_build

%endif

%install
%cmake_install

%if %{with kfdtest}
cd libhsakmt/tests/kfdtest
%cmake_install
%endif

# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/hsa-rocr/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/%{name}/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocr/LICENSE.md

%if %{without static}
rm -f %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhsakmt.a
rm -rf %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake/hsakmt/
rm -f %{buildroot}%{pkg_prefix}/%{pkg_libdir}/pkgconfig/libhsakmt.pc
%endif

%ldconfig_scriptlets -n %{pkg_name}

%files -n %{pkg_name}
%doc README.md
%license LICENSE.txt LICENSE_libhsakmt.md
%{pkg_prefix}/%{pkg_libdir}/libhsa-runtime64.so.1{,.*}

%files devel
%{pkg_prefix}/include/hsa/
%{pkg_prefix}/include/hsakmt
%{pkg_prefix}/%{pkg_libdir}/libhsa-runtime64.so
%{pkg_prefix}/%{pkg_libdir}/cmake/hsa-runtime64/

%if %{with static}
%files static
%{pkg_prefix}/%{pkg_libdir}/libhsakmt.a
%{pkg_prefix}/%{pkg_libdir}/cmake/hsakmt/
%{pkg_prefix}/%{pkg_libdir}/pkgconfig/libhsakmt.pc
%endif

%if %{with kfdtest}
%files -n kfdtest
%doc libhsakmt/tests/kfdtest/README.txt
%license libhsakmt/tests/kfdtest/LICENSE.kfdtest
%{pkg_prefix}/bin/kfdtest
%{pkg_prefix}/bin/run_kfdtest.sh
%{pkg_prefix}/share/kfdtest
%endif

%changelog
