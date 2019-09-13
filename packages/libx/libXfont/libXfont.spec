#
# spec file for package libXfont
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


Name:           libXfont
%define lname	libXfont1
Version:        1.5.4
Release:        0
Summary:        X font handling library for server and utilities
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXfont
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXfont/
Source:         %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.10
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(zlib)
#optional#BuildRequires:	pkgconfig(bzip2), + --with-bzip2

%description
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%package -n %lname
Summary:        X font handling library for server and utilities
Group:          System/Libraries

%description -n %lname
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%package devel
Summary:        Development files for the X font handling library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

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
%_libdir/libXfont.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXfont.so
%_libdir/pkgconfig/xfont.pc

%changelog
