#
# spec file for package libfmapi
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


Name:           libfmapi
%define lname	libfmapi1
Version:        20220114
Release:        0
Summary:        Library for MAPI data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfmapi
Source:         https://github.com/libyal/libfmapi/releases/download/%version/libfmapi-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfmapi/releases/download/%version/libfmapi-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfwnt) >= 20210717
BuildRequires:  pkgconfig(libuna) >= 20220102
# Various notes: https://en.opensuse.org/libyal

%description
A library for MAPI data types

libfmapi is part of the libyal library collection

%package -n %lname
Summary:        Library for MAPI data types
Group:          System/Libraries

%description -n %lname
A library for MAPI data types.

libfmapi is part of the libyal library collection

%package devel
Summary:        Development files for libfmapi, a library for MAPI data types
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for MAPI data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfmapi.

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
%_libdir/libfmapi.so.1*

%files devel
%_includedir/libfmapi*
%_libdir/libfmapi.so
%_libdir/pkgconfig/libfmapi.pc
%_mandir/man3/libfmapi.3*

%changelog
