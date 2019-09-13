#
# spec file for package libXinerama
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


Name:           libXinerama
%define lname	libXinerama1
Version:        1.1.4
Release:        0
Summary:        Xinerama extension to the X11 Protocol
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXinerama
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXinerama/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xineramaproto) >= 1.1.99.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
Xinerama is an extension to the X Window System which enables
multi-headed X applications and window managers to use two or more
physical displays as one large virtual display.

%package -n %lname
Summary:        Xinerama extension to the X11 Protocol
Group:          System/Libraries

%description -n %lname
Xinerama is an extension to the X Window System which enables
multi-headed X applications and window managers to use two or more
physical displays as one large virtual display.

%package devel
Summary:        Development files for the X11 Xinerama extension
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Xinerama is an extension to the X Window System which enables
multi-headed X applications and window managers to use two or more
physical displays as one large virtual display.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXinerama.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXinerama.so
%_libdir/pkgconfig/xinerama.pc
%_mandir/man3/*

%changelog
