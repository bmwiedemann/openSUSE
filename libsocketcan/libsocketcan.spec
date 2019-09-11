#
# spec file for package libsocketcan
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libsocketcan
%define lname	libsocketcan2
Version:        0.0.10
Release:        0
Summary:        Library for SocketCAN
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://pengutronix.de/software/libsocketcan/download/

#Git-Clone:	git://git.pengutronix.de/git/tools/libsocketcan
Source:         http://pengutronix.de/software/libsocketcan/download/%name-%version.tar.bz2
Patch3:         0003-build-avoid-overriding-user-s-CFLAGS.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig

%description
This library allows you to control some basic functions in socketcan
from userspace. A recent kernel with integrated SocketCAN (at least
2.6.30) is needed.

%package -n %lname
Summary:        Library for SocketCAN
Group:          System/Libraries

%description -n %lname
This library allows you to control some basic functions in socketcan
from userspace. A recent kernel with integrated SocketCAN (at least
2.6.30) is needed.

%package devel
Summary:        Development files for the SocketCAN library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This library allows you to control some basic functions in socketcan
from userspace. A recent kernel with integrated SocketCAN (at least
2.6.30) is needed.

This package contains the libsocketcan development files.

%prep
%setup -q
%patch -P 3 -p1

%build
./autogen.sh;
%configure --disable-static --docdir="%_docdir/%name"
make %{?_smp_mflags};

%install
b="%buildroot";
make install DESTDIR="$b";
rm -f "$b/%_libdir"/*.la "$b/%_docdir/%name/INSTALL"

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libsocketcan.so.2*

%files devel
%defattr(-,root,root)
%_includedir/can_netlink.h
%_includedir/libsocketcan.h
%_libdir/libsocketcan.so
%_libdir/pkgconfig/libsocketcan.pc
%_docdir/%name/

%changelog
