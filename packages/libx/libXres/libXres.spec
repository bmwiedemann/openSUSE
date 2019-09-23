#
# spec file for package libXres
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libXres
%define lname	libXRes1
Version:        1.2.0
Release:        0
Summary:        X Resource extension client library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXRes
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXRes/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(resourceproto) >= 1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

%package -n %lname
Summary:        X Resource extension client library
Group:          System/Libraries

%description -n %lname
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

%package devel
Summary:        Development files for the X Resource extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libXRes provides an X Window System client interface to the Resource
extension to the X protocol. The Resource extension allows for X
clients to see and monitor the X resource usage of various clients
(pixmaps, et al).

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

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc COPYING
%_libdir/libXRes.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXRes.so
%_libdir/pkgconfig/xres.pc
%_mandir/man3/*

%changelog
