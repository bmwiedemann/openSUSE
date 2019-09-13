#
# spec file for package liblbxutil
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


Name:           liblbxutil
%define lname	liblbxutil1
Version:        1.1.0
Release:        0
Summary:        Low Bandwith X extension utility routines
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/liblbxutil
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/liblbxutil/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%description
liblbxutil is a library of routines for LBX (Low Bandwidth X)
extension support shared between the lbxproxy program and an
LBX-supporting X server.

%package -n %lname
Summary:        Low Bandwith X extension utility routines
Group:          System/Libraries

%description -n %lname
liblbxutil is a library of routines for LBX (Low Bandwidth X)
extension support shared between the lbxproxy program and an
LBX-supporting X server.

%package devel
Summary:        Development files for the Low Bandwith X extension routines
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
liblbxutil is a library of routines for LBX (Low Bandwidth X)
extension support shared between the lbxproxy program and an
LBX-supporting X server.

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
%_libdir/liblbxutil.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/liblbxutil.so
%_libdir/pkgconfig/lbxutil.pc

%changelog
