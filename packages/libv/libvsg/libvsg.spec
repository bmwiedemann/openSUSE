#
# spec file for package libvsg
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


%define _check 0
%define _vsg_so_nr 13
%define rname VulkanSceneGraph
%define glslang_version 20230222+git.e4075496

Name:           libvsg
Version:        1.0.7
Release:        0
Summary:        3D graphics toolkit
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://vsg-dev.github.io/VulkanSceneGraph
Source0:        %{rname}-%{version}.tar.xz
Source1:        glslang-%{glslang_version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %_check
BuildRequires:  cppcheck
%endif
BuildRequires:  cmake(SPIRV-Tools)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)

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
# try to cover up past mistakes
Group:          System/Libraries

%description -n libvsg%{_vsg_so_nr}
The VulkanSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
Vulkan.

This package contains the shared libraries for VulkanSceneGraph.

%package -n libvsg-devel
Summary:        VulkanSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       libvsg%{_vsg_so_nr} = %{version}
Requires:       cmake(glslang)
Requires:       pkgconfig(SPIRV-Tools)
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
tar -xJf %{SOURCE1}
mv glslang-%{glslang_version} src/glslang

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_RELWITHDEBINFO_POSTFIX=
%cmake_build

%check
%if %_check
cppcheck --version
cd build && make cppcheck
%endif

%install
%cmake_install

%post -n libvsg%{_vsg_so_nr} -p /sbin/ldconfig
%postun -n libvsg%{_vsg_so_nr} -p /sbin/ldconfig

%files -n libvsg%{_vsg_so_nr}
%defattr(-,root,root)
%license LICENSE.md
%{_libdir}/lib*.so.*

%files -n libvsg-devel
%defattr(-,root,root)
%{_includedir}/vsg*/
%{_libdir}/lib*.so
%{_libdir}/cmake

%changelog
