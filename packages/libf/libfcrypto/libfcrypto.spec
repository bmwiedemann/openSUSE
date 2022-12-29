#
# spec file for package libfcrypto
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


Name:           libfcrypto
%define lname	libfcrypto1
Version:        20221228
Release:        0
Summary:        Library for encryption formats
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfcrypto
Source:         https://github.com/libyal/libfcrypto/releases/download/%version/libfcrypto-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfcrypto/releases/download/%version/libfcrypto-alpha-%version.tar.gz.asc
Source9:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.21
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101

%description
libfcrypto is a library for encryption formats.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for encryption formats
Group:          System/Libraries

%description -n %lname
libfcrypto is a library for encryption formats.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfcrypto
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfcrypto is a library for encryption formats.

This subpackage contains libraries and header files for developing
applications that want to make use of libfcrypto.

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
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfcrypto.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
