#
# spec file for package libXprintAppUtil
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libXprintAppUtil
%define lname	libXprintAppUtil1
Version:        1.0.1
Release:        0
Summary:        Xprint application utility routines
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXprintAppUtil
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXprintAppUtil/
Source:         http://ftp.x.org/pub/X11R7.1/src/lib/%name-X11R7.0-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xprintutil)

%description
libxprintapputil provides utility Xpau APIs allowing client
applications to access information about and control Xprint jobs from
an Xprint server.

%package -n %lname
Summary:        Xprint application utility routines
Group:          System/Libraries

%description -n %lname
libxprintapputil provides utility Xpau APIs allowing client
applications to access information about and control Xprint jobs from
an Xprint server.

%package devel
Summary:        Development files for the Xprint application utility routines
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libxprintapputil provides utility Xpau APIs allowing client
applications to access information about and control Xprint jobs from
an Xprint server.

This package contains the development headers for the library found
in %lname.

%prep
%setup -qn %name-X11R7.0-%version

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXprintAppUtil.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXprintAppUtil.so
%_libdir/pkgconfig/xprintapputil.pc

%changelog
