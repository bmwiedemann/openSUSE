#
# spec file for package vkd3d
#
# Copyright (c) 2020 SUSE LLC
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


%define major 1

Name:           vkd3d
BuildRequires:  fdupes
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
URL:            https://winehq.org/
Summary:        Direct3D 12 to Vulkan translation library
License:        LGPL-2.1-or-later
Group:          System/X11/Utilities
Version:        1.1
Release:        0
Source0:        https://dl.winehq.org/vkd3d/source/vkd3d-%version.tar.xz
Source3:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package -n libvkd3d%major
Summary:        Direct3D 12 to Vulkan translation library
Group:          System/Libraries

%package -n libvkd3d-utils%major
Summary:        Direct3D 12 to Vulkan translation library utilities
Group:          System/Libraries

%package devel
Summary:        Development headers for the Direct3D 12 to Vulkan translation library
Group:          Development/Libraries/X11
Requires:       libvkd3d%major = %version
Requires:       libvkd3d-utils%major = %version

%description
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description -n libvkd3d%major
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

%description -n libvkd3d-utils%major
This is a Direct3D 12 to Vulkan translation utilities library for use by e.g. Wine.

%description devel
This is a Direct3D 12 to Vulkan translation library for use by e.g. Wine.

These are its development libraries and headers.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
%make_install
rm %buildroot/%_libdir/*.la

%fdupes %buildroot/%_prefix

%files -n libvkd3d%{major}
%defattr(-,root,root)
%_libdir/libvkd3d.so.%{major}*

%files -n libvkd3d-utils%{major}
%defattr(-,root,root)
%_libdir/libvkd3d-utils.so.%{major}*

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/libvkd3d-utils.pc
%_libdir/pkgconfig/libvkd3d.pc

%post -n libvkd3d%{major} -p /sbin/ldconfig

%postun -n libvkd3d%{major} -p /sbin/ldconfig

%post -n libvkd3d-utils%{major} -p /sbin/ldconfig

%postun -n libvkd3d-utils%{major} -p /sbin/ldconfig

%changelog
