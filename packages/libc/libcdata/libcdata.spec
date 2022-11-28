#
# spec file for package libcdata
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


Name:           libcdata
%define lname	libcdata1
Version:        20220115
Release:        0
Summary:        Library for C generic data functions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcdata
Source:         https://github.com/libyal/libcdata/releases/download/%version/libcdata-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libcdata/releases/download/%version/libcdata-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcthreads) >= 20200508
# Various notes: https://en.opensuse.org/libyal

%description
A library for C generic data functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package -n %lname
Summary:        Library for C generic data functions
Group:          System/Libraries

%description -n %lname
A library for C generic data functions.

This subpackage contains the actual shared object library

%package devel
Summary:        Development files for libcdata, a C generic data library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for C generic data functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdata.

%prep
%autosetup -p1

%build
# Enabling MTS in libcdata means data structures are protected by
# libcdata itself, with an implicit rwlock. Every downstream use
# (e.g. by libpff) suffers, even if libpff already made sure that any
# one libcdata object is not used concurrently. Therefore, we disable
# MTS. - https://github.com/libyal/libcdata/issues/6
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --disable-multi-threading-support LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libcdata.so.1*

%files devel
%_includedir/libcdata*
%_libdir/libcdata.so
%_libdir/pkgconfig/libcdata.pc
%_mandir/man3/libcdata.3*

%changelog
