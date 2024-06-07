#
# spec file for package libei
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

%define lname libei1
Name:           libei
Version:        1.2.1
Release:        0
Summary:        Library for emulated input in Wayland
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/libinput/libei/
Source0:        https://gitlab.freedesktop.org/libinput/libei/-/archive/%version/%name-%version.tar.gz
Source99:       baselibs.conf
BuildRequires:  meson >= 0.57
BuildRequires:  ninja
BuildRequires:  protobuf-c
BuildRequires:  python3-attrs
BuildRequires:  python3-jinja2
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(xkbcommon)

%description
libei is a library to send Emulated Input (EI) to a matching Emulated
Input Server (EIS) which can receive those events with libeis.

It targets Wayland and provides separation, distinction and control,
which, for comparison, are not available with XTEST (X11's emulated
input).

%package -n %lname
Summary:        Library for emulated input in Wayland
Group:          System/Libraries

%description -n %lname
libei is a library to send Emulated Input (EI) to a matching Emulated
Input Server (EIS) which can receive those events with libeis.

It targets Wayland and provides separation, distinction and control,
which, for comparison, are not available with XTEST (X11's emulated
input).

%package devel
Summary:        Header files for libei, a library for emulated input under Wayland
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libei is a library for Emulated Input, targeting the Wayland stack.

%prep
%autosetup -p1

%build
%meson -Dtests=disabled
%meson_build

%install
%meson_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/lib*.so.*

%files devel
%_bindir/ei-debug-*
%_includedir/%name-1.0
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%license COPYING

%changelog
