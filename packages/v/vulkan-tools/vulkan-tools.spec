#
# spec file for package vulkan-tools
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


Name:           vulkan-tools
Version:        1.4.313
Release:        0
Summary:        Diagnostic utilities for Vulkan
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source:         https://github.com/KhronosGroup/Vulkan-Tools/archive/refs/tags/vulkan-sdk-%version.0.tar.gz
Source9:        baselibs.conf
BuildRequires:  cmake >= 3.17
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  glslang-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  pkgconfig(vulkan) >= %version
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Obsoletes:      vulkan < %version-%release
Provides:       vulkan = %version-%release

%description
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

This package contains the Khronos official Vulkan tools and utilities.

%prep
%autosetup -n Vulkan-Tools-vulkan-sdk-%version.0 -p1

%build
mkdir -p glslang/bin
ln -fsv /usr/bin/glslangValidator glslang/bin/
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%_bindir/*

%changelog
