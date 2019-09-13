#
# spec file for package libXevie
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


Name:           libXevie
%define lname	libXevie1
Version:        1.0.3
Release:        0
Summary:        X Event Interception Extension library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://wiki.freedesktop.org/wiki/Software/XEvIE

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXevie
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXevie/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(evieproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

%description
libXevie provides an X Window System client interface to the EvIE
extension to the X protocol. The EvIE (Event Interception Extension)
allows for clients to be able to intercept all events coming through
the server and then decide what to do with them, including being able
to modify or discard events.

%package -n %lname
Summary:        X Event Interception Extension library
Group:          System/Libraries

%description -n %lname
libXevie provides an X Window System client interface to the EvIE
extension to the X protocol. The EvIE (Event Interception Extension)
allows for clients to be able to intercept all events coming through
the server and then decide what to do with them, including being able
to modify or discard events.

%package devel
Summary:        Development files for the X Event Interception Extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libXevie provides an X Window System client interface to the EvIE
extension to the X protocol. The EvIE (Event Interception Extension)
allows for clients to be able to intercept all events coming through
the server and then decide what to do with them, including being able
to modify or discard events.

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
%_libdir/libXevie.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXevie.so
%_libdir/pkgconfig/xevie.pc
%_mandir/man3/*

%changelog
