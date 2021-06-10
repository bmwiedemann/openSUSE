#
# spec file for package libbfio
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


Name:           libbfio
%define lname	libbfio1
Version:        20210416
Release:        0
Summary:        Library to provide basic file input/output abstraction
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libbfio
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

%package -n %lname
Summary:        Library to provide basic file input/output abstraction
Group:          System/Libraries

%description -n %lname
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

%package devel
Summary:        Development files for libbfio, a basic file input/output abstraction library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

This subpackage contains libraries and header files for developing
applications that want to make use of libbfio.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libbfio.so.1*

%files devel
%_includedir/libbfio*
%_libdir/libbfio.so
%_libdir/pkgconfig/libbfio.pc
%_mandir/man3/libbfio.3*

%changelog
