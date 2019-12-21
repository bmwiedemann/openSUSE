#
# spec file for package vulkan-validationlayers
#
# Copyright (c) 2019 SUSE LLC
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


Name:           vulkan-validationlayers
Version:        1.1.130
Release:        0
Summary:        Validation layers for Vulkan
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers

Source:         https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/v%version.tar.gz
Source9:        %name-rpmlintrc
BuildRequires:  cmake >= 3.4
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  glslang-devel >= 7.13.3496
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  spirv-tools-devel >= 2019.5~git136
BuildRequires:  pkgconfig(vulkan) >= 1.1.112
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

This package contains the Khronos official Vulkan validation layers.

%prep
%autosetup -n Vulkan-ValidationLayers-%version

%build
%limit_build -m 2000
%cmake -DGLSLANG_INSTALL_DIR="%_bindir"
make %{?_smp_mflags}

%install
%cmake_install
# no header files
rm -f "%buildroot/%_libdir"/*.a

%files
%license LICENSE.txt
%_libdir/libVkLayer*.so
%_datadir/vulkan/

%changelog
