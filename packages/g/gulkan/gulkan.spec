#
# spec file for package gulkan
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _libver 0.15
%define _sover 0
%define _underver 0_15

Name:           gulkan
Version:        0.15.2
Release:        0
Summary:        A GLib library for Vulkan abstraction
License:        MIT
Url:            https://gitlab.freedesktop.org/xrdesktop/gulkan
Source:         %{name}-%{version}.tar.bz2
Patch0:         gulkan-incompatible-types.patch
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libglfw)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(json-glib-1.0)

%description
A GLib library for Vulkan abstraction. It provides classes for handling Vulkan instances, devices, shaders and initialize textures GDK Pixbufs, Cairo surfaces and DMA buffers.

%package -n %{name}%{_underver}-%{_sover}
Summary:        A GLib library for Vulkan abstraction

%description -n %{name}%{_underver}-%{_sover}
A GLib library for Vulkan abstraction. It provides classes for handling Vulkan instances, devices, shaders and initialize textures GDK Pixbufs, Cairo surfaces and DMA buffers.

%package devel
Summary:        A GLib library for Vulkan abstraction
Group:          Development/Libraries/C and C++
License:        MIT
Requires:       %{name}%{_underver}-%{_sover} = %{version}

%description devel
A GLib library for Vulkan abstraction. It provides classes for handling Vulkan instances, devices, shaders and initialize textures GDK Pixbufs, Cairo surfaces and DMA buffers.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="-Wno-error"
%meson
%meson_build

%install
%meson_install

%post -n %{name}%{_underver}-%{_sover} -p /sbin/ldconfig
%postun -n %{name}%{_underver}-%{_sover} -p /sbin/ldconfig

%files -n %{name}%{_underver}-%{_sover}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}-%{_libver}.so.*
%{_bindir}/%{name}-cube
%{_bindir}/%{name}-toy

%files devel
%dir %{_includedir}/%{name}-%{_libver}
%{_includedir}/%{name}-%{_libver}/*.h
%{_libdir}/pkgconfig/%{name}-%{_libver}.pc
%{_libdir}/lib%{name}-%{_libver}.so

%changelog
