#
# spec file for package vsgImGui
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


%define _vsg_so_nr 0

Name:           vsgImGui
Version:        0.3.0
Release:        0
Summary:        3D graphics toolkit
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://vsg-dev.github.io/VulkanSceneGraph
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(vsg)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)

%description
Integration of VulkanSceneGraph with ImGui

%package -n libvsgImGui%{_vsg_so_nr}
Summary:        Shared libraries for vsgImGui
Group:          System/Libraries

%description -n libvsgImGui%{_vsg_so_nr}
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the shared libraries for ImGui.

%package -n libvsgImGui-devel
Summary:        VulkanSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       libvsgImGui%{_vsg_so_nr} == %{version}

%description -n libvsgImGui-devel
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the header and development files for vsgImGui.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%install
%cmake_install

%post -n libvsgImGui%{_vsg_so_nr} -p /sbin/ldconfig
%postun -n libvsgImGui%{_vsg_so_nr} -p /sbin/ldconfig

%files -n libvsgImGui%{_vsg_so_nr}
%defattr(-,root,root)
%license LICENSE.md
%{_libdir}/lib*.so.*

%files -n libvsgImGui-devel
%defattr(-,root,root)
%{_includedir}/vsg*/
%{_libdir}/lib*.so
%{_libdir}/cmake

%changelog
