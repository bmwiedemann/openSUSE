#
# spec file for package libXpm
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


Name:           libXpm
%define lname	libXpm4
Version:        3.5.14
Release:        0
Summary:        X Pixmap image file format library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXpm
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXpm/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)

%description
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

%package -n %lname
Summary:        X Pixmap image file format library
Group:          System/Libraries

%description -n %lname
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

%package devel
Summary:        Development files for the X Pixmap image file format library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXpm-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXpm-devel < 7.6_%version-%release

%description devel
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

This package contains the development headers for the library found
in %lname.

%package tools
Summary:        Conversion utilities for X Pixmap (XPM) files
# O/P added for 12.2
Group:          Productivity/Graphics/Convertors
Provides:       xorg-x11-libXpm = 7.6_%version-%release
Obsoletes:      xorg-x11-libXpm < 7.6_%version-%release

%description tools
The spxm tool converts XPM1/XPM2 files to XPM version 3.
The cxpm tool will check whether an XPM file is correct or not with
regard to its format.

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
%_libdir/libXpm.so.4*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXpm.so
%_libdir/pkgconfig/xpm.pc
%_mandir/man3/*.3*

%files tools
%defattr(-,root,root)
%_bindir/cxpm
%_bindir/sxpm
%_mandir/man1/cxpm.1*
%_mandir/man1/sxpm.1*

%changelog
