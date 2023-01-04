#
# spec file for package libagdb
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


Name:           libagdb
%define lname	libagdb1
Version:        20210429
Release:        0
Summary:        Library and tools to access the Windows SuperFetch database format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libagdb
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
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
libagdb is a library to access the SuperFetch database format.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library to access the Windows SuperFetch database format
Group:          System/Libraries

%description -n %lname
libagdb is a library to access the SuperFetch database format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libagdb
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libagdb is a library to access the SuperFetch database format.

This subpackage contains libraries and header files for developing
applications that want to make use of libagdb.

%package tools
Summary:        Utilities for reading SuperFetch databases
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libagdb to
read SuperFetch databases.

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
%_libdir/libagdb.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/agdb*
%_mandir/man1/agdb*

%changelog
