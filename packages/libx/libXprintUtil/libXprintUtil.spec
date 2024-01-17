#
# spec file for package libXprintUtil
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libXprintUtil
%define lname	libXprintUtil1
Version:        1.0.1
Release:        0
Summary:        Xprint printer utility client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://cgit.freedesktop.org/xorg/lib/libXprintUtil/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXprintUtil
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXprintUtil/
Source:         http://ftp.x.org/pub/X11R7.1/src/lib/%name-X11R7.0-%version.tar.bz2
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(printproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xt)

%description
libXprintUtil provides utility Xpu APIs allowing client applications
to access and manipulate information about printer capabilities from
an Xprint server.

%package -n %lname
Summary:        Xprint printer utility client library
Group:          System/Libraries
# O/P added for 12.2
Provides:       xorg-x11-libXprintUtil = 7.6_%version-%release
Obsoletes:      xorg-x11-libXprintUtil < 7.6_%version-%release

%description -n %lname
libXprintUtil provides utility Xpu APIs allowing client applications
to access and manipulate information about printer capabilities from
an Xprint server.

%package devel
Summary:        Development files for the Xprint printer utility library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXprintUtil-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXprintUtil-devel < 7.6_%version-%release

%description devel
libXprintUtil provides utility Xpu APIs allowing client applications
to access and manipulate information about printer capabilities from
an Xprint server.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -n %name-X11R7.0-%version

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libXprintUtil.so.1*

%files devel
%_includedir/X11/*
%_libdir/libXprintUtil.so
%_libdir/pkgconfig/xprintutil.pc

%changelog
