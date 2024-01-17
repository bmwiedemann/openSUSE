#
# spec file for package libfsclfs
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


Name:           libfsclfs
%define lname	libfsclfs1
Version:        20210417
Release:        0
Summary:        Library and tools for accessing the Common Log File System (CLFS)
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfsclfs
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libftxf) >= 20180815
BuildRequires:  pkgconfig(libftxr) >= 20180815
BuildRequires:  pkgconfig(libfusn) >= 20180726
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
libfsclfs is a library to access the Common Log File System (CLFS).

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the Common Log File System (CLFS)
Group:          System/Libraries

%description -n %lname
libfsclfs is a library to access the Common Log File System (CLFS).

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfsclfs
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libfsclfs is a library to access the Common Log File System (CLFS).

This subpackage contains libraries and header files for developing
applications that want to make use of libfsclfs.

%package tools
Summary:        Utilities to inspect Common Log File Systems
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libfsclfs, which allows for
reading Common Log File Systems (CLFS).

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfsclfs.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/fsclfs*
%_mandir/man1/fsclfs*

%changelog
