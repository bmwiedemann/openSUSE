#
# spec file for package libfontenc
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


Name:           libfontenc
%define lname	libfontenc1
Version:        1.1.4
Release:        0
Summary:        X11 font encoding library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libfontenc
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libfontenc/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(fontutil) >= 1.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%description
The libfontenc library is used by the Xorg server and other X font
tools for handling fonts with different character set encodings.

%package -n %lname
Summary:        X11 font encoding library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libfontenc = 7.6_%version-%release
Obsoletes:      xorg-x11-libfontenc < 7.6_%version-%release

%description -n %lname
The libfontenc library is used by the Xorg server and other X font
tools for handling fonts with different character set encodings.

%package devel
Summary:        Development files for the X11 font encoding library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libfontenc-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libfontenc-devel < 7.6_%version-%release

%description devel
The libfontenc library is used by the Xorg server and other X font
tools for handling fonts with different character set encodings.

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
%_libdir/libfontenc.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libfontenc.so
%_libdir/pkgconfig/fontenc.pc

%changelog
