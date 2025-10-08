#
# spec file for package vulkan-validationlayers
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           vulkan-validationlayers
Version:        1.4.328
Release:        0
Summary:        Validation layers for Vulkan
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source:         https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/vulkan-sdk-%version.0.tar.gz
Patch2:         xxhash.diff
BuildRequires:  cmake >= 3.7.12
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  glslang-devel >= 15.4
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  spirv-headers >= 1.6.4+sdk313+git19
BuildRequires:  spirv-tools-devel >= 2025.4~rc1
BuildRequires:  vulkan-headers >= %version
BuildRequires:  vulkan-utility-libraries-devel >= %version
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(vulkan) >= %version
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Conflicts:      vulkan < 1.1
Obsoletes:      vulkan < 1.1

%description
Vulkan is a 3D graphics and compute API.

This package contains the Khronos official Vulkan validation layers.

%prep
%autosetup -n Vulkan-ValidationLayers-vulkan-sdk-%version.0 -p1
perl -i -lpe 's{\@PACKAGE_VERSION\@}{%version}' CMakeLists.txt */CMakeLists.txt
rm -Rfv layers/external/xxhash* layers/external/parallel_hashmap

%build
%limit_build -m 2000
# C++ <thread> needs -lpthread for pthread_create
# (under glibc>=2.34 it's not strictly needed anymore due to symbol move)
cat >gxx <<-EOF
	#!/bin/sh
	exec "g++%{?gcc_version:-%{gcc_version}}" "\$@" -lpthread
EOF
chmod a+x gxx
export CXX="$PWD/gxx"
%cmake -DGLSLANG_INSTALL_DIR="%_bindir" \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%gcc_version}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%gcc_version}" \
	-DSPIRV_HEADERS_INSTALL_DIR="%_includedir" \
	-DBUILD_LAYER_SUPPORT_FILES=ON \
	-DUSE_ROBIN_HOOD_HASHING=OFF \
	-DVulkanRegistry_DIR="%_datadir/vulkan/registry" \
	-DSPIRV_HEADERS_INSTALL_DIR="%_prefix"
%cmake_build

%install
%cmake_install
b="%buildroot"
rm -Rfv "$b/%_includedir" "$b/%_libdir"/*.a

%check
find . -name "*.so" -exec ldd -r {} + >ldd.log 2>&1 || :
! grep 'undefined symbol:' ldd.log

%files
%license LICENSE.txt
%_libdir/libVkLayer_khr*.so
%_datadir/vulkan/

%changelog
