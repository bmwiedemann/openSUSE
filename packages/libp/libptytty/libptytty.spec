#
# spec file for package libptytty
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

%define lname	libptytty0

Name:           libptytty
Version:        2.0
Release:        0
Summary:        Library to handle pty/tty and utmp/wtmp/lastlog
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://software.schmorp.de/pkg/libptytty.html
Source:         http://dist.schmorp.de/libptytty/%name-%version.tar.gz
Source1:        http://dist.schmorp.de/libptytty/%name-%version.tar.gz.sig
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
libptytty is an offspring of rxvt-unicode that handles
pty/tty/utmp/wtmp/lastlog handling in mostly OS-independent ways.

%package -n %lname
Summary:        Library to handle pty/tty and utmp/wtmp/lastlog
Group:          System/Libraries

%description -n %lname
libptytty is an offspring of rxvt-unicode that handles
pty/tty/utmp/wtmp/lastlog handling in mostly OS-independent ways.

%package devel
Summary:        Development files for libptytty
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libptytty is an offspring of rxvt-unicode that handles
pty/tty/utmp/wtmp/lastlog handling in mostly OS-independent ways.

This package contains the libptytty development files.

%prep
%autosetup

%build
%cmake
%make_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libptytty.so.*

%files devel
%_includedir/libptytty.h
%_libdir/libptytty.so
%_libdir/pkgconfig/libptytty.pc
%_mandir/man3/libptytty.*

%changelog
