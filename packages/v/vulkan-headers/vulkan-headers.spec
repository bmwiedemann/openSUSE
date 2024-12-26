#
# spec file for package vulkan-headers
#
# Copyright (c) 2024 SUSE LLC
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


# vkinfo reports vulkan-headers's version even if the loader/tools/etc.
# are at an older version, which in the past confused some users.
# Consider only updating the sources in lockstep.
#

Name:           vulkan-headers
Version:        1.4.304
Release:        0
Summary:        Vulkan C and C++ API header files
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/Vulkan-Headers
#Source:         https://github.com/KhronosGroup/Vulkan-Headers/archive/refs/tags/vulkan-sdk-%version.0.tar.gz
Source:         https://github.com/KhronosGroup/Vulkan-Headers/archive/refs/tags/v%version.tar.gz
Source9:        %name-rpmlintrc
BuildRequires:  cmake >= 2.8.11
BuildRequires:  c++_compiler
BuildArch:      noarch
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xrandr)
Conflicts:      vulkan-devel < 1.1.91

%description
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

This package contains the development headers for packages wanting
to make use of Vulkan.

%prep
%autosetup -n Vulkan-Headers-%version -p1

%build
%cmake \
	-DCMAKE_INSTALL_SYSCONFDIR="%_sysconfdir" \
	-DBUILD_WSI_MIR_SUPPORT=OFF \
	-DBUILD_TESTS=OFF \
	-DVULKAN_HEADERS_ENABLE_MODULE=OFF
%cmake_build

%install
%cmake_install
%if 0%{?suse_version} >= 1600
%python3_fix_shebang_path %buildroot%_datadir/vulkan/registry/*
%python3_fix_shebang_path %buildroot%_datadir/vulkan/registry/spec_tools/*
%endif

%files
%license LICENSE.md
%_includedir/vulkan/
%_includedir/vk_video/
%_datadir/cmake/
%_datadir/vulkan/

%changelog
