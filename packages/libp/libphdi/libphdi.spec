#
# spec file for package libphdi
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


Name:           libphdi
%define lname	libphdi1
Version:        20220110
Release:        0
Summary:        Library and tools to access the Parallels Hard Disk images
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libphdi
Source:         https://github.com/libyal/libphdi/releases/download/%version/libphdi-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libphdi/releases/download/%version/libphdi-experimental-%version.tar.gz.asc
Source9:        %name.keyring
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
BuildRequires:  pkgconfig(libcdirectory) >= 20200702
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200913
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libphdi is a library to access the Parallels Hard Disk image format.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing Parallels Hard Disk images
Group:          System/Libraries

%description -n %lname
libphdi is a library to access the Parallels Hard Disk image format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libphdi
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libphdi is a library to access the Parallels Hard Disk image format.

This subpackage contains libraries and header files for developing
applications that want to make use of libphdi.

%package tools
Summary:        Utilities for reading Parallels Hard Disk images
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libphdi to
read Parallels Hard Disk images.

%package -n python3-%name
Summary:        Python 3 bindings for libphdi
Group:          Development/Languages/Python

%description -n python3-%name
Python 3 bindings for libphdi.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libphdi.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/phdi*
%_mandir/man1/phdi*

%files -n python3-%name
%python3_sitearch/*.so

%changelog
