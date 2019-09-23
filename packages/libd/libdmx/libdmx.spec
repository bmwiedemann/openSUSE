#
# spec file for package libdmx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libdmx
%define lname	libdmx1
Version:        1.1.4
Release:        0
Summary:        Distributed Multihead X extension library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libdmx
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libdmx/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dmxproto) >= 2.2.99.1
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libdmx is an interface to the DMX extension for X, which allows a
single server to be set up as a proxy spanning multiple servers --
not unlike Xinerama across discrete physical machines. It can be
reconfigured on the fly to change the layout, and it is presented as
a single logical display to clients.

%package -n %lname
Summary:        Distributed Multihead X extension library
Group:          System/Libraries

%description -n %lname
libdmx is an interface to the DMX extension for X, which allows a
single server to be set up as a proxy spanning multiple servers --
not unlike Xinerama across discrete physical machines. It can be
reconfigured on the fly to change the layout, and it is presented as
a single logical display to clients.

libdmx allows clients to configure the layout of DMX servers by
adding and removing screens, input devices, et al.

%package devel
Summary:        Development files for the Distributed Multihead X extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libdmx is an interface to the DMX extension for X, which allows a
single server to be set up as a proxy spanning multiple servers --
not unlike Xinerama across discrete physical machines. It can be
reconfigured on the fly to change the layout, and it is presented as
a single logical display to clients.

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
%_libdir/libdmx.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libdmx.so
%_libdir/pkgconfig/dmx.pc
%_mandir/man3/*

%changelog
