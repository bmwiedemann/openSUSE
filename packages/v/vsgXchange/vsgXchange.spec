#
# spec file for package vsgXchange
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


%define _vsg_so_nr 3
Name:           vsgXchange
Version:        1.1.14
Release:        0
Summary:        3D graphics toolkit
License:        MIT
URL:            https://github.com/vsg-dev/vsgXchange
Source0:        %{name}-%{version}.tar.xz
# not found by default
#BuildRequires:  libassimp5
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(assimp)
BuildRequires:  cmake(osg2vsg)
BuildRequires:  cmake(vsg) >= 1.1.14
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openscenegraph)

%description
Utility library for converting data+materials to/from VulkanSceneGraph.

%package -n libvsgXchange%{_vsg_so_nr}
Summary:        Shared libraries for vsgXchange

%description -n libvsgXchange%{_vsg_so_nr}
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the shared libraries for vsgXchange.

%package -n libvsgXchange-devel
Summary:        VulkanSceneGraph development files
Requires:       libvsgXchange%{_vsg_so_nr} = %{version}

%description -n libvsgXchange-devel
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the development header and libraries for vsgXchange.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%install
%cmake_install

%post -n libvsgXchange%{_vsg_so_nr} -p /sbin/ldconfig
%postun -n libvsgXchange%{_vsg_so_nr} -p /sbin/ldconfig

%files
%{_bindir}/vsgconv

%files -n libvsgXchange%{_vsg_so_nr}
%license LICENSE.md
%{_libdir}/lib*.so.*

%files -n libvsgXchange-devel
%{_includedir}/vsg*/
%{_libdir}/lib*.so
%{_libdir}/cmake

%changelog
