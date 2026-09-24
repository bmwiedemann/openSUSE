#
# spec file for package hiprand
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


%global upstreamname hiprand

%global pkg_library_name %{upstreamname}
%global pkg_library_version 1

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
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%global skip_install_rpath ON
%endif

%if 0%{?suse_version}
%global pkg_name lib%{pkg_library_name}%{pkg_library_version}%{pkg_suffix}
%else
%global pkg_name %{name}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%if 0%{?suse_version}
# %%toolchain and %%build_cxxflags are Fedora rpm machinery; openSUSE implements
# neither, and its %%cmake injects %%optflags verbatim. Without this the host
# hardening flags reach the amdgcn device passes, where clang rejects them with
# "option 'cf-protection=return' cannot be specified on this target".
%global optflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%if 0%{?fedora}
%bcond_without test
%else
%bcond_with test
%endif
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
%bcond_with check
# For docs
%bcond_with doc

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           hiprand%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        5%{?dist}
%endif

Summary:        HIP random number generator
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocrand%{pkg_suffix}-devel

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
%endif

%if %{with doc}
BuildRequires:  doxygen
%endif

Provides:       hiprand%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocrand%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipRAND is a RAND marshaling library, with multiple supported backends. It
sits between the application and the backend RAND library, marshaling inputs
into the backend and results back to the application. hipRAND exports an
interface that does not require the client to change, regardless of the chosen
backend. Currently, hipRAND supports either rocRAND or cuRAND.

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        The hipRAND runtime package

%description -n %{pkg_name}
%summary

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        The hipRAND development package
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocrand%{pkg_suffix}-devel
Provides:       hiprand%{pkg_suffix}-devel = %{version}-%{release}

%description devel
The hipRAND development package.

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

#Remove RPATH:
sed -i '/INSTALL_RPATH/d' CMakeLists.txt

# On Tumbleweed 20250817
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++11's to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD *11)@set(CMAKE_CXX_STANDARD 17)@' {,test/package/}CMakeLists.txt

# Remove some tests we do not use to make license easier
rm -rf test/fortran/fruit

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
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DBUILD_TEST=%{build_test} \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/hiprand/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/bin/hipRAND/CTestTestfile.cmake

%if %{with compat}
# ERROR   0008: file '/usr/lib64/rocm/rocm-7.2/lib/libhiprand.so.1.1'
#   contains the $ORIGIN runpath specifier at the wrong position in
#   [/usr/lib64/rocm/rocm-7.2/lib:$ORIGIN/../lib:$ORIGIN/../lib/hipRAND/lib]
%if %{with debug}
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-d.so.%{pkg_library_version}.*
%else
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}.*
%endif

%if %{with test}
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/test_hiprand_api
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/test_hiprand_cpp_wrapper
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/test_hiprand_kernel
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/test_hiprand_linkage
%endif

%endif

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=$PWD/build/library:$LD_LIBRARY_PATH
%endif

%ctest
%endif
%endif

%files -n %{pkg_name}
%doc README.md
%license LICENSE.md
%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-d.so.%{pkg_library_version}{,.*}
%else
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%endif

%files devel
%{pkg_prefix}/include/hiprand/
%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-d.so
%else
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%endif
%{pkg_prefix}/%{pkg_libdir}/cmake/hiprand/

%if %{with test}
%files test
%{pkg_prefix}/bin/test*
%endif

%changelog
