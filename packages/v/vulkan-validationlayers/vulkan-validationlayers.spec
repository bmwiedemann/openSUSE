#
# spec file for package vulkan-validationlayers
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.3.236.0
Release:        0
%define lname libVkLayer_utils-1_3_236_0
Summary:        Validation layers for Vulkan
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source:         https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/sdk-%version.tar.gz
Source9:        %name-rpmlintrc
Patch1:         ver.diff
Patch2:         xxhash.diff
BuildRequires:  cmake >= 3.4
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  glslang-devel >= 11.13
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  spirv-headers >= 1.6.1+sdk236
BuildRequires:  spirv-tools-devel >= 2022.4+sdk236
BuildRequires:  vulkan-headers
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(vulkan) >= 1.3.236
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Conflicts:      vulkan < 1.1
Obsoletes:      vulkan < 1.1

%description
Vulkan is a 3D graphics and compute API.

This package contains the Khronos official Vulkan validation layers.

%package -n %lname
Summary:        Vulkan validation layer utility library
Group:          System/Libraries

%description -n %lname
Vulkan is a 3D graphics and compute API.

This package contains a utility library.

%package devel
Summary:        Vulkan validation layer support files
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       xxhash-devel

%description devel
Vulkan is a 3D graphics and compute API.

This package contains support files for the VkLayer utility library.

%prep
%autosetup -n Vulkan-ValidationLayers-sdk-%version -p1
perl -i -pe 's{\@PACKAGE_VERSION\@}{%version}' CMakeLists.txt

%build
%limit_build -m 2000
# C++ <thread> needs -lpthread for pthread_create
# (under glibc>=2.34 it's not strictly needed anymore due to symbol move)
cat >gxx <<-EOF
	#!/bin/sh
	exec g++ "\$@" -lpthread
EOF
chmod a+x gxx
export CXX="$PWD/gxx"
%cmake -DGLSLANG_INSTALL_DIR="%_bindir" \
	-DSPIRV_HEADERS_INSTALL_DIR="%_includedir" \
	-DBUILD_LAYER_SUPPORT_FILES=ON \
	-DUSE_ROBIN_HOOD_HASHING=OFF \
	-DVulkanRegistry_DIR="%_datadir/vulkan/registry" \
	-DSPIRV_HEADERS_INSTALL_DIR="%_prefix"
%cmake_build

%install
%cmake_install
b="%buildroot"
ln -sv "libVkLayer_utils-%version.so" "$b/%_libdir/libVkLayer_utils.so"
rm -f "$b/%_includedir"/xxhash.*

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%license LICENSE.txt
%_libdir/libVkLayer_khr*.so
%_datadir/vulkan/

%files -n %lname
%_libdir/libVkLayer_utils-%version.so

%files devel
%_includedir/*
%_libdir/libVkLayer_utils.so

%changelog
