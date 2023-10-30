#
# spec file for package vulkan-utility-libraries
#
# Copyright (c) 2023 SUSE LLC
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


%define lname libVulkanLayerSettings-1_3_268_0
Name:           vulkan-utility-libraries
Version:        1.3.268.0
Release:        0
Summary:        Utility libraries for Vulkan
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source:         https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/refs/tags/vulkan-sdk-%version.tar.gz
Patch1:         shared.diff
%if 0%{?suse_version} && 0%{?suse_version} < 1599
BuildRequires:  gcc11-c++
%else
BuildRequires:  c++_compiler
%endif
BuildRequires:  cmake >= 3.17.2
BuildRequires:  pkg-config
BuildRequires:  vulkan-headers >= 1.3.268
Obsoletes:      vulkan < %version-%release
Provides:       vulkan = %version-%release

%description
The Vulkan::LayerSettings library standardizes layer
configuration code for various SDK layer deliverables.

%package -n %lname
Summary:        Utility library for Vulkan
Group:          System/Libraries

%description -n %lname
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

The Vulkan::LayerSettings library standardizes layer
configuration code for various SDK layer deliverables.

%package devel
Summary:        Utility library for Vulkan
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
The Vulkan::LayerSettings library standardizes layer
configuration code for various SDK layer deliverables.

This package contains the headers and build system integration.

%prep
%autosetup -p1 -n Vulkan-Utility-Libraries-vulkan-sdk-%version

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1599
# Need something that knows <filesystem>
export CC=gcc-11 CXX=g++-11
%endif
%cmake
%cmake_build

%install
%cmake_install
ln -s libVulkanLayerSettings-%version.so "%buildroot/%_libdir/libVulkanLayerSettings.so"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libVulkanLayerSettings-*.so

%files devel
%_includedir/vulkan/
%_libdir/cmake/
%_libdir/libVulkanLayerSettings.so
%license LICENSE.md

%changelog
