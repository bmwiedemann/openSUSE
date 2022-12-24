#
# spec file for package vulkan-loader
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


# Prefer to go with just /^sdk-.*/ tags
%define lname	libvulkan1
Name:           vulkan-loader
Version:        1.3.236.0
Release:        0
Summary:        Reference ICD loader for Vulkan
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/Vulkan-Loader
Source:         https://github.com/KhronosGroup/Vulkan-Loader/archive/refs/tags/sdk-%version.tar.gz
Source9:        baselibs.conf
BuildRequires:  cmake >= 3.4
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  pkg-config
BuildRequires:  python3-xml
BuildRequires:  vulkan-headers >= %version
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

This package contains the reference ICD loader for Vulkan.

%package -n %lname
Summary:        The Vulkan 3D graphics and compute API
Group:          System/Libraries

%description -n %lname
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

%package -n vulkan-devel
Summary:        Vulkan development package
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
Requires:       vulkan-headers >= %version

%description -n vulkan-devel
Vulkan is a 3D graphics and compute API providing cross-platform
access to modern GPUs with low overhead and targeting realtime
graphics applications such as games and interactive media.

This subpackage contains the development headers for packages wanting
to make use of Vulkan.

%prep
%autosetup -p1 -n Vulkan-Loader-sdk-%version

%build
%cmake \
	-DVulkanHeaders_INCLUDE_DIR:PATH="%_includedir" \
	-DVulkanRegistry_DIR:PATH="%_datadir/vulkan/registry" \
	-DLIB_SUFFIX:STRING=""

%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n libvulkan1
%license LICENSE.txt
%_libdir/libvulkan.so.1*

%files -n vulkan-devel
%_libdir/libvulkan.so
%_libdir/pkgconfig/vulkan.pc

%changelog
