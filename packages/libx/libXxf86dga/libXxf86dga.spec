#
# spec file for package libXxf86dga
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


Name:           libXxf86dga
%define lname	libXxf86dga1
Version:        1.1.6
Release:        0
Summary:        XFree86-DGA extension client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXxf86dga
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXxf86dga/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86dgaproto) >= 2.0.99.2
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
libXxf86dga provides the XFree86-DGA extension, which allows direct
graphics access to a framebuffer-like region, and also allows
relative mouse reporting, et al. It is mainly used by games and
emulators for games.

%package -n %lname
Summary:        XFree86-DGA extension client library
Group:          System/Libraries

%description -n %lname
libXxf86dga provides the XFree86-DGA extension, which allows direct
graphics access to a framebuffer-like region, and also allows
relative mouse reporting, et al. It is mainly used by games and
emulators for games.

%package devel
Summary:        Development files for the XFree86-DGA extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libXxf86dga provides the XFree86-DGA extension, which allows direct
graphics access to a framebuffer-like region, and also allows
relative mouse reporting, et al. It is mainly used by games and
emulators for games.

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
%_libdir/libXxf86dga.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXxf86dga.so
%_libdir/pkgconfig/xxf86dga.pc
%_mandir/man3/*

%changelog
