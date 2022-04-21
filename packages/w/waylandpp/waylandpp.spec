#
# spec file for package waylandpp
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


%define sover 0

Name:           waylandpp
Version:        0.2.10
Release:        0
Summary:        Wayland C++ bindings
License:        BSD-2-Clause AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/NilsBrause/waylandpp
Source0:        %name-%version.tar.xz
BuildRequires:  cmake >= 3.4
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(pugixml) >= 1.4
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
%if 0%{?sle_version} == 150100
BuildRequires:  Mesa-KHR-devel
%endif

%description
Wayland C++ bindings

%package devel
Summary:        Development files for lib%name
Group:          Development/Libraries/C and C++
Requires:       lib%name%{sover} = %version

%description    devel
The %name-devel package contains libraries and header files for
developing applications that use lib%name.

%package     -n lib%name%{sover}
Summary:        Wayland C++ bindings
Group:          System/Libraries

%description -n lib%name%{sover}
Wayland C++ bindings

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post   -n lib%name%{sover} -p /sbin/ldconfig
%postun -n lib%name%{sover} -p /sbin/ldconfig

%files
%_bindir/*
%_libdir/pkgconfig/wayland-scanner++.pc

%files -n lib%name%{sover}
%license LICENSE
%_libdir/lib*.so.%{sover}*

%files devel
%_includedir/*
%_datadir/*
%_libdir/pkgconfig/*.pc
%_libdir/lib*.so
%_libdir/cmake
%exclude %_libdir/pkgconfig/wayland-scanner++.pc

%changelog
