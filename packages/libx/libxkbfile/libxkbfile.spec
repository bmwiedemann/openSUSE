#
# spec file for package libxkbfile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libxkbfile
%define lname	libxkbfile1
Version:        1.1.0
Release:        0
Summary:        X11 keyboard file manipulation library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libxkbfile
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libxkbfile/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

%package -n %lname
Summary:        X11 keyboard file manipulation library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libxkbfile = 7.6_%version-%release
Obsoletes:      xorg-x11-libxkbfile < 7.6_%version-%release
Requires:       xkeyboard-config

%description -n %lname
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

%package devel
Summary:        Development files for the X11 keyboard file manipulation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libxkbfile-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libxkbfile-devel < 7.6_%version-%release

%description devel
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

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
%_libdir/libxkbfile.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libxkbfile.so
%_libdir/pkgconfig/xkbfile.pc

%changelog
