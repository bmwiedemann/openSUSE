#
# spec file for package libwtcdb
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


Name:           libwtcdb
%define lname	libwtcdb1
Version:        20210417
Release:        0
Summary:        Library and tools to access Windows thumbnail cache databases
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libwtcdb
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  bison
BuildRequires:  c_compiler
BuildRequires:  flex
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200913
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
libwtcdb is a library to access the Windows (Vista/7) Explorer
thumbnail cache database (WTCDB) format (thumbcache.db).

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing Windows thumbnail cache databases
Group:          System/Libraries

%description -n %lname
libwtcdb is a library to access the Windows (Vista/7) Explorer
thumbnail cache database (WTCDB) format (thumbcache.db).

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libwtcdb
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libwtcdb is a library to access the Windows (Vista/7) Explorer
thumbnail cache database (WTCDB) format (thumbcache.db).

This subpackage contains libraries and header files for developing
applications that want to make use of libwtcdb.

%package tools
Summary:        Utilities for reading Windows thumbnail cache databases
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libwtcdb to
read Windows thumbnail cache databases.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libwtcdb.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/wtcdb*
%_mandir/man1/wtcdb*

%changelog
