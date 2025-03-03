#
# spec file for package libcthreads
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libcthreads
%define lname	libcthreads1
Version:        20240413
Release:        0
Summary:        Library for C threads functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcthreads
Source:         https://github.com/libyal/libcthreads/releases/download/%version/libcthreads-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libcthreads/releases/download/%version/libcthreads-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20240413
# Various notes: https://en.opensuse.org/libyal

%description
A library for C threads functions.

libcthreads is part of the libyal library collection

%package -n %lname
Summary:        Library for C thread functions
Group:          System/Libraries

%description -n %lname
A library for C thread functions.

libcthreads is part of the libyal library collection

%package devel
Summary:        Development files for libcthreads, a C thread library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for C thread functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcthreads.

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

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING.LESSER
%_libdir/libcthreads.so.1*

%files devel
%_includedir/libcthreads*
%_libdir/libcthreads.so
%_libdir/pkgconfig/libcthreads.pc
%_mandir/man3/libcthreads.3*

%changelog
