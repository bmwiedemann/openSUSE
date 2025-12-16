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
Name:           linux-npu-driver
Version:        1.26.0
Release:        0
Summary:        Driver for Intel NPU device.
License:        MIT
URL:            https://github.com/intel/linux-npu-driver
Source0:        %{name}-%{version}.tar.xz
Patch0:         gtest.patch 
BuildRequires:  cmake
BuildRequires:  gtest level-zero-devel gmock
BuildRequires:  gmock
BuildRequires:  git
%if 0%{?suse_version} >= 1600 && 0%{?is_opensuse}
BuildRequires:  gcc-c++ gcc
%else
BuildRequires:  gcc12-c++ gcc12
%endif
BuildRequires:  xz

%description
Intel NPU device is an AI inference accelerator integrated with Intel
client CPUs starting from Intel Core Ultra generation of CPUs
(formerly known as Meteor Lake). It enables execution of artificial
neural network tasks.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600 && 0%{?is_opensuse}
export CC=gcc-12 CXX=g++-12
%endif

cat third_party/CMakeLists.txt 
%cmake \
	-DENABLE_NPU_COMPILER_BUILD=OFF \
	-DCMAKE_CXX_FLAGS="-fcf-protection=none" \
	-DCMAKE_C_FLAGS="-fcf-protection=none" 
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%{_libdir}/libze_*.so.*
%{_libdir}/libze_*.so
%{_bindir}/npu-kmd-test
%{_bindir}/npu-umd-test
%{_firmwaredir}

%changelog
