#
# spec file for package libzbc
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


Name:           libzbc
%define lname   libzbc6
Version:        6.0.0
Release:        0
Summary:        Library for manipulating ZBC and ZAC disks
License:        BSD-2-Clause AND LGPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/westerndigitalcorporation/libzbc

Source:         https://github.com/westerndigitalcorporation/libzbc/archive/v%version.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gtk+-3.0)

%description
libzbc is a simple library providing functions for manipulating Zoned
Block Command (ZBC) and Zoned-device ATA command set (ZAC) disks.
libzbc also has an mode for emulating the behavior of a zoned disk
using a regular file or raw block device.

%package -n %lname
Summary:        Library for manipulating ZBC and ZAC disks
Group:          System/Libraries

%description -n %lname
libzbc is a simple library providing functions for manipulating Zoned
Block Command (ZBC) and Zoned-device ATA command set (ZAC) disks.
libzbc also has an mode for emulating the behavior of a zoned disk
using a regular file or raw block device.

%package devel
Summary:        Development files for libzbc, a ZBC/ZAC disk manipulation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libzbc is a simple library providing functions for manipulating Zoned
Block Command (ZBC), Zoned-device ATA command set (ZAC) disks.

This subpackage contains the files needed to build against libzbc.

%package gui
Summary:        Graphical frontend for ZBC tools
Group:          Hardware/Other

%description gui
A simple graphical interface showing zone information of a zoned device.
It also displays the write status (write pointer position) of zones
graphically using color coding (red for written space and green for
unwritten space).

%package tools
Summary:        Command line utilities for ZBC/ZAC disk manipulation
Group:          Hardware/Other

%description tools
libzbc is a simple library providing functions for manipulating Zoned
Block Command (ZBC), Zoned-device ATA command set (ZAC) disks.

%prep
%autosetup -p1

%build
autoreconf -fi
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name" CFLAGS="%optflags -fno-common"
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete
rm -Rf "%buildroot/%_datadir/polkit-1"
%fdupes %buildroot/%_prefix

%check
%make_build check

%ldconfig_scriptlets -n %lname

%files tools
%_bindir/zbc_*
%_mandir/man*/*z*
%license COPYING.LESSER

%files gui
%_bindir/gz*
%_datadir/applications/
%_datadir/pixmaps/*

%files -n %lname
%_libdir/libzbc.so.*
%license COPYING.BSD

%files devel
%_includedir/%name/
%_libdir/libzbc.so
%_libdir/pkgconfig/libzbc.pc

%changelog
