#
# spec file for package libhmac
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


Name:           libhmac
%define lname	libhmac1
Version:        20220425
Release:        0
Summary:        Library to support various HMACs
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libhmac
Source:         https://github.com/libyal/libhmac/releases/download/%version/libhmac-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libhmac/releases/download/%version/libhmac-alpha-%version.tar.gz.asc
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libuna) >= 20220102
BuildRequires:  pkgconfig(openssl) >= 1.0

%description
A library and tools to support various Hash-based Message Authentication Codes (HMAC).

%package -n %lname
Summary:        Library to support various HMACs
Group:          System/Libraries

%description -n %lname
A library to support various Hash-based Message Authentication Codes (HMAC).

%package devel
Summary:        Development files for libhmac
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Development files for libhmac, a library to support various Hash-based Message Authentication Codes (HMAC).

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package tools
Summary:        Utilities for HMACs
Group:          Productivity/File utilities

%description tools
Use hmacsum to calculate a Hash-based Message Authentication Code (HMAC) of the data in a file.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --enable-wide-character-type
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libhmac.so.1*

%files devel
%_includedir/libhmac*
%_libdir/libhmac.so
%_libdir/pkgconfig/libhmac.pc
%_mandir/man3/libhmac.3*

%files tools
%_bindir/hmacsum
%_mandir/man1/hmacsum.1*

%changelog
