#
# spec file for package rocprim
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


%global upstreamname rocPRIM
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}
# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with test
# Option to build test subpackage
# enable building of tests if check or test are enabled
%if %{with test}
%global build_test ON
%else
%global build_test OFF
# there is no debug package, this just headers
%global debug_package %{nil}
%endif

# For documentation
%bcond_with doc

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rocprim
Version:        %{rocm_version}
Release:        6%{?dist}
Summary:        ROCm parallel primatives

License:        BSD-3-Clause AND MIT

URL:            https://github.com/ROCm/%{name}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch0:         0001-Add-macros-for-128-bit-atomic-loads-stores-on-gfx950.patch

# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  python3dist(marshalparser)
%endif

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
BuildRequires:  rocminfo
%endif

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:        ROCm parallel primatives
Provides:       rocprim-static = %{version}-%{release}

# the devel subpackage is only headers and cmake infra
BuildArch:      noarch

%description devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%if %{with test}
%package test
Summary:        upstream tests for ROCm parallel primatives
Provides:       rocprim-test = %{version}-%{release}
Requires:       gtest
Requires:       rocprim-devel

%description test
tests for the rocPRIM package
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# In file included from rocPRIM-rocm-6.4.2/test/rocprim/test_texture_cache_iterator.cpp:26:
# ../rocprim/include/rocprim/iterator/texture_cache_iterator.hpp:231:13: error:
#   'tex1Dfetch<int, nullptr>' is unavailable: The image/texture API not supported on the device
# Remove fail to build test
sed -i -e 's@add_rocprim_test("rocprim.texture_cache_iterator"@#add_rocprim_test("rocprim.texture_cache_iterator"@' test/rocprim/CMakeLists.txt
grep texture_cach test/rocprim/CMakeLists.txt

%build

%cmake \
	-DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	-DBUILD_TEST=%{build_test} \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_BUILD_TYPE=%build_type \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_INSTALL_LIBDIR=share \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
	-DGPU_TARGETS=%{rocm_gpu_list_test} \
	-DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.txt

%if %{with test}
# force the cmake test file to use absolute paths for its referenced binaries
sed -i -e 's@\.\.@\/usr\/bin@' %{buildroot}%{_bindir}/%{name}/CTestTestfile.cmake
%endif

%files devel
%doc README.md
%license LICENSE.txt
%license NOTICES.txt
%{_includedir}/%{name}
%{_datadir}/cmake/rocprim

%if %{with test}
%files test
%{_bindir}/test*
%dir %{_bindir}/%{name}
%{_bindir}/%{name}/CTestTestfile.cmake
%endif

%changelog
