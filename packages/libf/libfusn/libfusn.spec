#
# spec file for package libfusn
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libfusn
%define lname	libfusn1
Version:        20220119
Release:        0
Summary:        Library for Update Sequence Number (USN) Journal data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfusn
Source:         https://github.com/libyal/libfusn/releases/download/%version/libfusn-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfusn/releases/download/%version/libfusn-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libuna) >= 20220102
# Various notes: https://en.opensuse.org/libyal

%description
libfusn is a library for Update Sequence Number (USN) Journal data types.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Update Sequence Number (USN) Journal data types
Group:          System/Libraries

%description -n %lname
libfusn is a library for Update Sequence Number (USN) Journal data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfusn
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfusn is a library for Update Sequence Number (USN) Journal data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfusn.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfusn.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
