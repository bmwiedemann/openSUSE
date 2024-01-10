#
# spec file for package vulkan-validationlayers
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


Name:           vulkan-validationlayers
Version:        1.3.268.0
Release:        0
Summary:        Validation layers for Vulkan
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source:         https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/vulkan-sdk-%version.tar.gz
Patch2:         xxhash.diff
Patch3:         glslang14.diff
BuildRequires:  cmake >= 3.7.12
%if 0%{?suse_version} >= 1599
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc11-c++
%endif
BuildRequires:  glslang-devel >= 13.1.0
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  spirv-headers >= 1.6.1+sdk268
BuildRequires:  spirv-tools-devel >= 2023.5~rc1
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-utility-libraries-devel >= 1.3.268
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(vulkan) >= 1.3.268
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Conflicts:      vulkan < 1.1
Obsoletes:      vulkan < 1.1

%description
Vulkan is a 3D graphics and compute API.

This package contains the Khronos official Vulkan validation layers.

%prep
%autosetup -n Vulkan-ValidationLayers-vulkan-sdk-%version -p1
perl -i -pe 's{\@PACKAGE_VERSION\@}{%version}' CMakeLists.txt */CMakeLists.txt

%build
%limit_build -m 2000
# C++ <thread> needs -lpthread for pthread_create
# (under glibc>=2.34 it's not strictly needed anymore due to symbol move)
cat >gxx <<-EOF
	#!/bin/sh
	exec g++ "\$@" -lpthread
EOF
%if 0%{?suse_version} < 1599
cat >gxx <<-EOF
	#!/bin/sh
	exec g++-11 "\$@" -lpthread
EOF
%endif
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
rm -Rfv "$b/%_includedir" "$b/%_libdir"/*.a

%check
find . -name "*.so" -exec ldd -r {} + >ldd.log 2>&1 || :
! grep 'undefined symbol:' ldd.log

%files
%license LICENSE.txt
%_libdir/libVkLayer_khr*.so
%_datadir/vulkan/

%changelog
