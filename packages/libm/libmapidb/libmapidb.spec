#
# spec file for package libmapidb
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


Name:           libmapidb
%define lname	libmapidb1
Version:        20210421
Release:        0
Summary:        Library for accessing the Exchange MAPI database format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libmapidb
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcnotify) >= 20200913

%description
A library for accessing the Exchange MAPI database format

libmapidb is part of the libyal library collection

%package -n %lname
Summary:        Library for MAPI data types
Group:          System/Libraries

%description -n %lname
A library for accessing the Exchange MAPI database format

libmapidb is part of the libyal library collection

%package devel
Summary:        Development files for libmapidb, a library for accessing the Exchange MAPI database format
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for accessing the Exchange MAPI database format

This subpackage contains libraries and header files for developing
applications that want to make use of libmapidb.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libmapidb.so.1*

%files devel
%_includedir/libmapidb*
%_libdir/libmapidb.so
%_libdir/pkgconfig/libmapidb.pc
%_mandir/man3/libmapidb.3*

%changelog
