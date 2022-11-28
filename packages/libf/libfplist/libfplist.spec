#
# spec file for package libfplist
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


Name:           libfplist
%define lname	libfplist1
Version:        20220116
Release:        0
Summary:        Library for plist formats
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfplist
Source:         https://github.com/libyal/libfplist/releases/download/%version/libfplist-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfplist/releases/download/%version/libfplist-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20220102
# Various notes: https://en.opensuse.org/libyal

%description
libfplist is a library for plist formats.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for plist formats
Group:          System/Libraries

%description -n %lname
libfplist is a library for plist formats.

Part of the libyal family of libraries.

Read-only supported formats:

  * XML plist format

Unsupported formats:

  * ASCII plist format
  * Binary plist format

%package devel
Summary:        Development files for libfplist
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfplist is a library for plist formats.

This subpackage contains libraries and header files for developing
applications that want to make use of libfplist.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfplist.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
