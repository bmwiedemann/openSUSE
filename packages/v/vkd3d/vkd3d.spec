#
# spec file for package vkd3d
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


%define         major 1
Name:           vkd3d
Version:        1.14
Release:        0
Summary:        Direct3D 12 to Vulkan translation library
License:        LGPL-2.1-or-later
URL:            https://winehq.org
Source0:        https://dl.winehq.org/vkd3d/source/vkd3d-%{version}.tar.xz
Source1:        https://dl.winehq.org/vkd3d/source/vkd3d-%{version}.tar.xz.sign
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xda23579a74d4ad9af9d3f945cefac8eaaf17519d#/%{name}.keyring
Source3:        baselibs.conf
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  spirv-headers
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(vulkan) >= 1.3.228
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)

%package -n lib%{name}%{major}
Summary:        Direct3D 12 to Vulkan translation library
Group:          System/Libraries

%package -n lib%{name}-utils%{major}
Summary:        Direct3D 12 to Vulkan translation library utilities
Group:          System/Libraries

%package -n lib%{name}-shader%{major}
Summary:        Direct3D 12 to Vulkan translation shader library
Group:          System/Libraries

%package devel
Summary:        Development headers for the Direct3D 12 to Vulkan translation library
Group:          Development/Libraries/X11
Requires:       lib%{name}%{major} = %{version}
Requires:       lib%{name}-utils%{major} = %{version}

%package demos
Summary:        Demos for %{name}
Group:          System/Libraries
Requires:       libvkd3d%{major} = %{version}

%package docs
Summary:        Documentation for %{name}
Group:          System/Libraries
BuildArch:      noarch

%description
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description demos
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description docs
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description -n lib%{name}%{major}
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description -n lib%{name}-utils%{major}
This is a Direct3D 12 to Vulkan translation utilities library for use by e.g. Wine.

%description -n lib%{name}-shader%{major}
This is a Direct3D 12 to Vulkan shader library for use by e.g. Wine.

%description devel
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

These are its development libraries and headers.

%prep
%autosetup

%build
%configure \
  --disable-static \
  --disable-tests \
  --with-ncurses \
  --with-opengl \
  --enable-demos \
  --with-xcb \
  --with-spirv-tools
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}
%fdupes -s %{_builddir}/%{name}-%{version}/doc

%check
%make_build check

%ldconfig_scriptlets -n libvkd3d%{major}
%ldconfig_scriptlets -n libvkd3d-utils%{major}
%ldconfig_scriptlets -n libvkd3d-shader%{major}

%files -n lib%{name}%{major}
%license COPYING LICENSE
%doc README ANNOUNCE AUTHORS
%{_libdir}/lib%{name}.so.%{major}*

%files -n lib%{name}-utils%{major}
%license COPYING LICENSE
%{_libdir}/lib%{name}-utils.so.%{major}*

%files -n lib%{name}-shader%{major}
%license COPYING LICENSE
%{_libdir}/lib%{name}-shader.so.%{major}*

%files demos
%license COPYING LICENSE
%{_bindir}/%{name}-gears
%{_bindir}/%{name}-triangle

%files devel
%license COPYING LICENSE
%doc AUTHORS README ANNOUNCE
%{_includedir}/%{name}
%{_libdir}/lib%{name}{,-shader,-utils}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/pkgconfig/lib%{name}-shader.pc
%{_libdir}/pkgconfig/lib%{name}-utils.pc
%{_bindir}/%{name}-compiler
%{_bindir}/%{name}-dxbc

%files docs
%doc doc/html

%changelog
