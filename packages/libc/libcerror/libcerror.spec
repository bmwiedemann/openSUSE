#
# spec file for package libcerror
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


Name:           libcerror
%define lname	libcerror1
Version:        20220101
Release:        0
Summary:        Library for C error functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcerror
Source:         https://github.com/libyal/libcerror/releases/download/%version/libcerror-beta-%version.tar.gz
Source2:        https://github.com/libyal/libcerror/releases/download/%version/libcerror-beta-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
# Various notes: https://en.opensuse.org/libyal

%description
A library for C error functions.

This package is part of the libyal library collection and is used by
other libraries in the collection.

%package -n %lname
Summary:        Library for C error functions
Group:          System/Libraries

%description -n %lname
A library for C error functions.

This package is part of the libyal library collection and is used by
other libraries in the collection.

%package devel
Summary:        Development files for libcerror, a C error library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for C error functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%autosetup

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
%license COPYING.LESSER
%_libdir/libcerror.so.1*

%files devel
%_includedir/libcerror*
%_libdir/libcerror.so
%_libdir/pkgconfig/libcerror.pc
%_mandir/man3/libcerror.3*

%changelog
