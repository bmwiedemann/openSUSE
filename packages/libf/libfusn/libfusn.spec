#
# spec file for package libfusn
#
# Copyright (c) 2021 SUSE LLC
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
Version:        20210415
Release:        0
Summary:        Library for Update Sequence Number (USN) Journal data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfusn
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libuna) >= 20201204

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
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static
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
