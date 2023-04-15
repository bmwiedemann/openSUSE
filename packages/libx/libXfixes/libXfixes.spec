#
# spec file for package libXfixes
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


%define lname	libXfixes3
Name:           libXfixes
Version:        6.0.1
Release:        0
Summary:        X11 miscellaneous "fixes" extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXfixes
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXfixes/
Source:         https://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.xz
Source1:        https://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.xz.sig
Source2:        libXfixes.keyring
Source3:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fixesproto) >= 5.0
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
The X Fixes extension provides applications with work-arounds for
various limitations in the core protocol.

%package -n %lname
Summary:        X11 miscellaneous "fixes" extension library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXfixes = 7.6_%version-%release
Obsoletes:      xorg-x11-libXfixes < 7.6_%version-%release

%description -n %lname
The X Fixes extension provides applications with work-arounds for
various limitations in the core protocol.

%package devel
Summary:        Development files for the X11 Xfixes extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXfixes-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXfixes-devel < 7.6_%version-%release

%description devel
The X Fixes extension provides applications with work-arounds for
various limitations in the core protocol.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libXfixes.so.3*

%files devel
%doc README.md
%_includedir/X11/*
%_libdir/libXfixes.so
%_libdir/pkgconfig/xfixes.pc
%_mandir/man3/*

%changelog
