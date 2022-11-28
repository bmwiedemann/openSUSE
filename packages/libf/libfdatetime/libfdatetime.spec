#
# spec file for package libfdatetime
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


Name:           libfdatetime
%define lname	libfdatetime1
Version:        20220112
Release:        0
Summary:        A library for date and time data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfdatetime
Source:         https://github.com/libyal/libfdatetime/releases/download/%version/libfdatetime-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfdatetime/releases/download/%version/libfdatetime-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
# Various notes: https://en.opensuse.org/libyal

%description
A library for date and time data types. Part of the libyal family of libraries.

%package -n %lname
Summary:        A library for date and time data types
Group:          System/Libraries

%description -n %lname
A library for date and time data types. Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfdatetime, a date and time data type library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for date and time data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdatetime.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfdatetime.so.1*

%files devel
%_includedir/libfdatetime*
%_libdir/libfdatetime.so
%_libdir/pkgconfig/libfdatetime.pc
%_mandir/man3/libfdatetime.3*

%changelog
