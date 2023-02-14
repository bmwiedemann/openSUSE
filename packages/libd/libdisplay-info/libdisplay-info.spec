#
# spec file for package libdisplay-info
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


Name:           libdisplay-info
%define lname libdisplay-info1
Version:        0.1.0
Release:        0
Summary:        EDID and DisplayID library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
Source:         https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/%version/downloads/libdisplay-info-%version.tar.xz
Source2:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/releases/%version/downloads/libdisplay-info-%version.tar.xz.sig
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(hwdata)

%description
libdisplay-info is an EDID and DisplayID library. It provides a
low-level API exposing all of the details of these formats, plus a
high-level API (of opinionated functions) which abstracts these
details for common operations.

%package -n %lname
Summary:        EDID and DisplayID library
Group:          System/Libraries

%description -n %lname
libdisplay-info is an EDID and DisplayID library. It provides a
low-level API exposing all of the details of these formats, plus a
high-level API (of opinionated functions) which abstracts these
details for common operations.

%package devel
Summary:        Header files for libdisplay-info, an EDID library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The library provides a set of low- and high-level functions
for EDID and DisplayID.

This package contains headers for the library.

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
%_libdir/lib*.so.[0-9]*

%files devel
%_bindir/di-edid-decode
%_includedir/%name/
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%license LICENSE

%changelog
