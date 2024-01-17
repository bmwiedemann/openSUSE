#
# spec file for package osg2vsg
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


%define _vsg_so_nr 0

Name:           osg2vsg
Version:        0.1.0
Release:        0
Summary:        3D graphics toolkit
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://vsg-dev.github.io/VulkanSceneGraph
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(vsg)
BuildRequires:  pkgconfig(openscenegraph)

%description
Utility library adding osg features to VulkanSceneGraph

%package -n lib%{name}%{_vsg_so_nr}
Summary:        Shared libraries for osg2vsg
Group:          System/Libraries

%description -n lib%{name}%{_vsg_so_nr}
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the shared libraries for osg2vsg

%package -n lib%{name}-devel
Summary:        VulkanSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{_vsg_so_nr} == %{version}

%description -n lib%{name}-devel
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the header and development files for osg2vsg.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{_vsg_so_nr} -p /sbin/ldconfig
%postun -n lib%{name}%{_vsg_so_nr} -p /sbin/ldconfig

%files -n lib%{name}%{_vsg_so_nr}
%defattr(-,root,root)
%license LICENSE.md
%{_libdir}/lib*.so.*
%dir %{_libdir}/osgPlugins-*/
%{_libdir}/osgPlugins-*/osgdb_vsg.so

%files -n lib%{name}-devel
%defattr(-,root,root)
%{_includedir}/osg2vsg/
%{_libdir}/lib*.so
%{_libdir}/cmake

%changelog
