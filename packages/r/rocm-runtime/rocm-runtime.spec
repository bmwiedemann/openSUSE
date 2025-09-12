#
# spec file for package rocm-runtime
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
# 15.6
# rocm-runtime.x86_64: E: shlib-policy-name-error (Badness: 10000) libhsa-runtime64-1
# Your package contains a single shared library but is not named after its SONAME.
%global runtime_name libhsa-runtime64-1
%else
%global runtime_name rocm-runtime
%endif
%global forge_name rocm-runtime

#Image support is x86 only
%ifarch x86_64
%global enableimage 1
%endif
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_without kfdtest

%bcond_with compat_gcc
%if %{with compat_gcc}
%global compat_gcc_major 13
%global gcc_major_str -13
%else
%global compat_gcc_major %{nil}
%global gcc_major_str %{nil}
%endif

Name:           %{runtime_name}
Version:        %{rocm_version}
Release:        5%{?dist}
Summary:        ROCm Runtime Library

License:        NCSA
URL:            https://github.com/ROCm/ROCR-Runtime
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{forge_name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc%{compat_gcc_major}-c++
BuildRequires:  libdrm-devel
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-static

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

Provides:       rocm-runtime = %{version}-%{release}
Obsoletes:      hsakmt < 6.3
Provides:       hsakmt = %{version}-%{release}

%description
The ROCm Runtime Library is a thin, user-mode API that exposes the necessary
interfaces to access and interact with graphics hardware driven by the AMDGPU
driver set and the AMDKFD kernel driver. Together they enable programmers to
directly harness the power of AMD discrete graphics devices by allowing host
applications to launch compute kernels directly to the graphics hardware.

%package devel
Summary:        ROCm Runtime development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       hsakmt-devel = %{version}-%{release}
Obsoletes:      hsakmt-devel < 6.3
Provides:       rocm-runtime-devel = %{version}-%{release}

%description devel
ROCm Runtime development files

%if %{with kfdtest}
%package -n kfdtest
Summary:        Test suite for ROCm's KFD kernel module
Requires:       rocm-smi

%description -n kfdtest
This package includes ROCm's KFD kernel module test suite (kfdtest), the list of
excluded tests for each ASIC, and a convenience script to run the test suite.
%endif

%prep
%autosetup -n ROCR-Runtime-rocm-%{version} -p1

# Use llvm's static libs kfdtest
sed -i -e 's@LLVM_LINK_LLVM_DYLIB@0@' libhsakmt/tests/kfdtest/CMakeLists.txt

# gcc 15 include cstdint
sed -i '/#include <memory>.*/a#include <cstdint>' runtime/hsa-runtime/core/inc/amd_elf_image.hpp

%build

export PATH=%{rocmllvm_bindir}:$PATH

export CC=/usr/bin/gcc%{gcc_major_str}
export CXX=/usr/bin/g++%{gcc_major_str}

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
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
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON -DLLVM_DIR=%{rocmllvm_cmakedir}
%cmake_build

%endif

%install
%cmake_install

%if %{with kfdtest}
cd libhsakmt/tests/kfdtest
%cmake_install
%endif

rm -f %{buildroot}%{_prefix}/share/doc/hsa-runtime64/LICENSE.md
rm -f %{buildroot}%{_prefix}/share/doc/packages/%{name}/LICENSE.md
rm -f %{buildroot}%{_libdir}/libhsakmt.*
rm -rf %{buildroot}%{_libdir}/cmake/hsakmt
rm -f %{buildroot}%{_libdir}/pkgconfig/libhsakmt.pc

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libhsa-runtime64.so.1{,.*}

%files devel
%{_includedir}/hsa/
%{_includedir}/hsakmt
%{_libdir}/libhsa-runtime64.so
%{_libdir}/cmake/hsa-runtime64/

%if %{with kfdtest}
%files -n kfdtest
%doc libhsakmt/tests/kfdtest/README.txt
%license libhsakmt/tests/kfdtest/LICENSE.kfdtest
%{_bindir}/kfdtest
%{_bindir}/run_kfdtest.sh
%{_datadir}/kfdtest
%endif

%changelog
