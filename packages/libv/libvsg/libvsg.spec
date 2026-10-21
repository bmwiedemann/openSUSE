#
# spec file for package libvsg
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _check 0
%define _vsg_so_nr 17
%define rname VulkanSceneGraph
Name:           libvsg
Version:        1.1.16
Release:        0
Summary:        3D graphics toolkit
License:        MIT
URL:            https://vsg-dev.github.io/VulkanSceneGraph
Source0:        %{rname}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(SPIRV-Tools)
BuildRequires:  cmake(SPIRV-Tools-opt)
BuildRequires:  cmake(glslang)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)
%if %{_check}
BuildRequires:  cppcheck
%endif

%description
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan freeing the developer from implementing and optimizing low
level graphics calls, and provides many additional utilities for
development of graphics applications.

%package -n libvsg%{_vsg_so_nr}
Summary:        Shared libraries for VulkanSceneGraph

%description -n libvsg%{_vsg_so_nr}
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the shared libraries for VulkanSceneGraph.

%package -n libvsg-devel
Summary:        VulkanSceneGraph development files
Requires:       libvsg%{_vsg_so_nr} = %{version}
# vsgConfig.cmake does find_dependency(glslang): consumers need its
# CMake config files at configure time, pulled in here.
Requires:       cmake(glslang)
Requires:       pkgconfig(vulkan)

%description -n libvsg-devel
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the header and development files for
VulkanSceneGraph.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%check
%if %{_check}
cppcheck --version
cd build && make cppcheck
%endif

%install
%cmake_install

%ldconfig_scriptlets -n libvsg%{_vsg_so_nr}

%files -n libvsg%{_vsg_so_nr}
%license LICENSE.md
%{_libdir}/lib*.so.*

%files -n libvsg-devel
%{_includedir}/vsg*/
%{_libdir}/lib*.so
%{_libdir}/cmake

%changelog
