#
# spec file for package vulkan-utility-libraries
#
# Copyright (c) 2025 SUSE LLC
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


%define lname libVulkanLayerSettings-1_4_321
%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           vulkan-utility-libraries
Version:        1.4.321
Release:        0
Summary:        Utility libraries for Vulkan
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source:         https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/refs/tags/vulkan-sdk-%version.0.tar.gz
Patch1:         shared.diff
BuildRequires:  cmake >= 3.17.2
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  pkg-config
BuildRequires:  vulkan-headers >= %version
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
%autosetup -n Vulkan-Utility-Libraries-vulkan-sdk-%version.0 -p1
find . -type f -name CMakeLists.txt -exec perl -i -lpe 's{\@PACKAGE_VERSION\@}{%version}g' {} +

%build
%cmake \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%gcc_version}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%gcc_version}"
%cmake_build

%install
%cmake_install
ln -s libVulkanLayerSettings-%version.so "%buildroot/%_libdir/libVulkanLayerSettings.so"
ln -s libVulkanSafeStruct-%version.so "%buildroot/%_libdir/libVulkanSafeStruct.so"

%ldconfig_scriptlets -n %lname

%files -n %lname
# lockstep updated (SLPP §6)
%_libdir/libVulkanLayerSettings-*.so
%_libdir/libVulkanSafeStruct-*.so

%files devel
%_includedir/vulkan/
%_libdir/cmake/
%_libdir/libVulkanLayerSettings.so
%_libdir/libVulkanSafeStruct.so
%license LICENSE.md

%changelog
