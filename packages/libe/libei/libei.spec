#
# spec file for package libei
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


Name:           libei
%define lname libei-suse0
Version:        0+git134
Release:        0
Summary:        Library for emulated input in Wayland
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/whot/libei/

Source:         %name-%version.tar.xz
Patch1:         system-munit.diff
Patch2:         ver.diff
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  protobuf-c
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(munit)
BuildRequires:  pkgconfig(protobuf-lite)

%description
libei is a library for Emulated Input, targeting the Wayland stack.
It provides separation, distinction and control, which, for
comparison, are not available with XTEST (X11's emulated input).

%package -n %lname
Summary:        OpenGL and OpenGL ES shader front end implementation
Group:          System/Libraries

%description -n %lname
libei is a library for Emulated Input, targeting the Wayland stack.

%package devel
Summary:        OpenGL and OpenGL ES shader front end and validator
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libei is a library for Emulated Input, targeting the Wayland stack.

%prep
%autosetup -p1

%build
%meson --includedir="%_includedir/%name"
%meson_build

%install
%meson_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/lib*.so.suse0

%files devel
%_includedir/%name/
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%license COPYING

%changelog
