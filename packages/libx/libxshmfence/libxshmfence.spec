#
# spec file for package libxshmfence
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libxshmfence
Version:        1.3
Release:        0
%define lname   libxshmfence1
Summary:        A tiny library that exposes a event API on top of Linux futexes
License:        HPND
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libxshmfence
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libxshmfence/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
This is a tiny library that exposes a event API on top of Linux
futexes. There was some discussion about using eventfd instead of this,
but the cost of adding two FDs to the X server for every DRI application
seems excessive, and by using PresentIdleNotify events, to work around
the limitations of futexes.

%package -n %lname
Summary:        A tiny library that exposes a event API on top of Linux futexes
Group:          System/Libraries

%description -n %lname
This is a tiny library that exposes a event API on top of Linux
futexes. There was some discussion about using eventfd instead of this,
but the cost of adding two FDs to the X server for every DRI application
seems excessive, and by using PresentIdleNotify events, to work around
the limitations of futexes.

%package devel
Summary:        Development files for the X Shm-Fence library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This is a tiny library that exposes a event API on top of Linux
futexes.

This package contains the development headers for the library found
in %name.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libxshmfence.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libxshmfence.so
%_libdir/pkgconfig/xshmfence.pc

%changelog
