#
# spec file for package libftxf
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


Name:           libftxf
%define lname	libftxf1
Version:        20220116
Release:        0
Summary:        Library for Transactional NTFS (TxF) data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libftxf
Source:         https://github.com/libyal/libftxf/releases/download/%version/libftxf-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libftxf/releases/download/%version/libftxf-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfusn) >= 20180726
BuildRequires:  pkgconfig(libuna) >= 20220102
# Various notes: https://en.opensuse.org/libyal

%description
libftxf is a library for Transactional NTFS (TxF) data types.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Transactional NTFS (TxF) data types
Group:          System/Libraries

%description -n %lname
libftxf is a library for Transactional NTFS (TxF) data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libftxf
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libftxf is a library for Transactional NTFS (TxF) data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libftxf.

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
%_libdir/libftxf.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
