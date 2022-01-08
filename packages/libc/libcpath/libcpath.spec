#
# spec file for package libcpath
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


Name:           libcpath
%define lname	libcpath1
Version:        20220108
Release:        0
Summary:        Library for C path functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcpath
Source:         https://github.com/libyal/libcpath/releases/download/%version/libcpath-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libcpath/releases/download/%version/libcpath-alpha-%version.tar.gz.asc
Source9:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libuna) >= 20210801

%description
A library for C path functions. Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for C path functions
Group:          System/Libraries

%description -n %lname
A library for C path functions. Part of the libyal family of libraries.

%package devel
Summary:        Development files for libcpath, a C path library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for C path functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcpath.

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
%_libdir/libcpath.so.1*

%files devel
%_includedir/libcpath*
%_libdir/libcpath.so
%_libdir/pkgconfig/libcpath.pc
%_mandir/man3/libcpath.3*

%changelog
