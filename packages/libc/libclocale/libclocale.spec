#
# spec file for package libclocale
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


Name:           libclocale
%define lname	libclocale1
Version:        20221218
Release:        0
Summary:        Library for C locale functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libclocale
Source:         https://github.com/libyal/libclocale/releases/download/%version/libclocale-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libclocale/releases/download/%version/libclocale-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
# Various notes: https://en.opensuse.org/libyal

%description
A library for C locale functions. libclocale is part of the libyal family of libraries.

%package -n %lname
Summary:        Library for C locale functions
Group:          System/Libraries

%description -n %lname
A library for C locale functions.

%package devel
Summary:        Development files for libclocale, a C locale library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for C locale functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libclocale.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING.LESSER
%_libdir/libclocale.so.1*

%files devel
%_includedir/libclocale*
%_libdir/libclocale.so
%_libdir/pkgconfig/libclocale.pc
%_mandir/man3/libclocale.3*

%changelog
