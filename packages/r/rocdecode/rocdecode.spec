#
# spec file for package rocdecode
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


%global pkg_library_name rocdecode
%global pkg_library_version 1

%bcond_with preview
%if %{with preview}
%global upstreamname rocdecode
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global upstreamname rocDecode
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
%global pkg_name %{NAME}-libs
%else
%global pkg_name %{NAME}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

# Requires actual HW, so disabled by default.
# Tests also have issues and possibly requires ffmpeg from rpmfusion to work
%bcond_with check

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

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

Name:           rocdecode%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        6%{?dist}
%endif
Summary:        High-performance video decode SDK for AMD GPUs

# Note: MIT with a clause clarifying that AMD will not pay for codec royalties
# The clause has little weight on the licensing, it is just a clarification
License:        MIT
%if %{with preview}
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
URL:            https://github.com/ROCm/rocDecode
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

%if 0%{?suse_version}
BuildRequires:  Mesa-libva
BuildRequires:  ffmpeg
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
%else
BuildRequires:  ffmpeg-free
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  mesa-va-drivers
BuildRequires:  rocprofiler-register%{pkg_suffix}-devel
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

# Rocdecode isn't useful without AMD's mesa va drivers:
Requires:       mesa-va-drivers
Provides:       rocdecode%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}
Requires:       rocprofiler-register%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocDecode is a high-performance video decode SDK for AMD GPUs. Using the
rocDecode API, you can access the video decoding features available on your GPU.

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Runtime for %{name}

%description -n %{pkg_name}
%summary

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        The rocDecode development package
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Provides:       rocdecode%{pkg_suffix}-devel = %{version}-%{release}

%description devel
The rocDecode development package.

%prep
%if %{with preview}
%autosetup -n %{upstreamname} -p3
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif
# Allow overriding CMAKE_CXX_COMPILER:
# https://github.com/ROCm/rocDecode/pull/436
sed -i -e 's@set(CMAKE_C_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang)@set(CMAKE_C_COMPILER "%rocmllvm_bindir/amdclang")@' {,test/,samples/*/}CMakeLists.txt
sed -i -e 's@set(CMAKE_CXX_COMPILER ${ROCM_PATH}/lib/llvm/bin/amdclang++)@set(CMAKE_CXX_COMPILER "%rocmllvm_bindir/amdclang++")@' {,test/,samples/*/}CMakeLists.txt

# Problems finding va.h
# https://github.com/ROCm/rocDecode/issues/477
sed -i "s|/opt/amdgpu/include NO_DEFAULT_PATH|/usr/include|" cmake/FindLibva.cmake

# cpack cruft in the middle of the configure, this breaks TW and is only used for ubuntu
sed -i -e 's@file(READ "/etc/os-release" OS_RELEASE)@#file(READ "/etc/os-release" OS_RELEASE)@'  CMakeLists.txt
sed -i -e 's@string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@#string(REGEX MATCH "22.04" UBUNTU_22_FOUND ${OS_RELEASE})@'  CMakeLists.txt

# Need to add libdrm_amdgpu to link
# https://github.com/ROCm/rocDecode/issues/571
sed -i -e 's@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY}@${LINK_LIBRARY_LIST} ${LIBVA_DRM_LIBRARY} -ldrm_amdgpu@' CMakeLists.txt

%build
%cmake \
    %{cmake_generator} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DROCM_PATH=%{pkg_prefix}

%cmake_build

%install
%cmake_install

# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocdecode/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocdecode-asan/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/%{name}/LICENSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/%{name}-asan/LICENSE

# Need to install the sample first
%if %{with check}
%check
%ctest
%endif

%files -n %{pkg_name}
%license LICENSE
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-host.so.%{pkg_library_version}{,.*}

%files devel
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-host.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocdecode/
%{pkg_prefix}/%{pkg_libdir}/cmake/rocdecode-host/
%{pkg_prefix}/include/rocdecode
%{pkg_prefix}/share/rocdecode

%changelog
