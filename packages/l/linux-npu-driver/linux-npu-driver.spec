#
# spec file for package linux-npu-drive
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Alessandro de Oliveira Faria (A.K.A CABELO) <cabelo@opensuse.org>
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

%define _firmwaredir /lib/firmware
%define sover 1
%define libname libze_intel_npu%{sover}
Name:           linux-npu-driver
Version:        1.35.0
Release:        0
Summary:        Driver for Intel NPU device
License:        MIT
URL:            https://github.com/intel/linux-npu-driver
Source0:        %{name}-%{version}.tar.xz
Patch0:         https://github.com/intel/linux-npu-driver/commit/84819fb90b5786fcde13552df772467f9d6b7ffe.patch#/fix-resource-cleaner-overflow.patch
BuildRequires:  cmake
BuildRequires:  git
%if 0%{?suse_version} >= 1600 && 0%{?is_opensuse}
BuildRequires:  gcc-c++ gcc
%else
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
BuildRequires:  libasan8
BuildRequires:  libtsan2
%endif
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(level-zero)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  xz yaml-cpp-devel
ExclusiveArch:  x86_64

%description
Intel NPU device is an AI inference accelerator integrated with Intel
client CPUs starting from Intel Core Ultra generation of CPUs
(formerly known as Meteor Lake). It enables execution of artificial
neural network tasks.

%package -n %{libname}
Summary:        Intel NPU Level Zero user-mode driver library

%description -n %{libname}
This package contains the Intel NPU Level Zero user-mode driver
shared library.

%package devel
Summary:        Development files for the Intel NPU Level Zero driver
Requires:       %{libname} = %{version}

%description devel
This package contains the development linker files for the Intel NPU
Level Zero user-mode driver.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600 && 0%{?is_opensuse}
export CC=gcc-12
export CXX=g++-12
%endif

%cmake \
	-DENABLE_NPU_COMPILER_BUILD=OFF \
        -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
        -DCMAKE_EXE_LINKER_FLAGS:STRING="-pie" \
        -DCMAKE_C_FLAGS:STRING="%{optflags} -fcf-protection=none" \
        -DCMAKE_CXX_FLAGS:STRING="%{optflags} -fcf-protection=none -Wno-error=missing-field-initializers"

%cmake_build

%install
%cmake_install
DESTDIR=%{buildroot} /usr/bin/cmake --install build --component fw-npu

%ldconfig_scriptlets  -n %{libname}

%files
%{_bindir}/npu-kmd-test
%{_bindir}/npu-umd-test
%{_firmwaredir}

%files -n %{libname}
%{_libdir}/libze_intel_npu.so.*

%files devel
%{_libdir}/libze_intel_npu.so

%changelog
