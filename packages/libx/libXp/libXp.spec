#
# spec file for package libXp
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libXp
%define lname	libXp6
Version:        1.0.3
Release:        0
Summary:        X Printing Extension client library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXp
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXp/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(printproto)
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libXp provides APIs to allow client applications to render to
non-display devices.

%package -n %lname
Summary:        X Printing Extension client library
Group:          System/Libraries
# O/P added for 12.2
Provides:       xorg-x11-libXp = 7.6_%version-%release
Obsoletes:      xorg-x11-libXp < 7.6_%version-%release

%description -n %lname
libXp provides APIs to allow client applications to render to
non-display devices.

%package devel
Summary:        Development files for the X Printing Extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXp-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXp-devel < 7.6_%version-%release

%description devel
libXp provides APIs to allow client applications to render to
non-display devices.

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
%_libdir/libXp.so.6*

%files devel
%defattr(-,root,root)
%_libdir/libXp.so
%_libdir/pkgconfig/xp.pc
%_mandir/man3/*

%changelog
