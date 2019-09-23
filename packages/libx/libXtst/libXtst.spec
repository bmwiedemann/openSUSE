#
# spec file for package libXtst
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libXtst
%define lname	libXtst6
Version:        1.2.3
Release:        0
Summary:        Xlib-based client API for the XTEST and RECORD extensions
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXtst
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXtst/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext) >= 1.0.99.4
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.3
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12

%description
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

%package -n %lname
Summary:        Xlib-based client API for the XTEST and RECORD extensions
Group:          System/Libraries

%description -n %lname
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

%package devel
Summary:        Development files for the X11 XTEST and RECORD extensions
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXtst.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXtst.so
%_libdir/pkgconfig/xtst.pc
%_mandir/man3/*
%_docdir/%name

%changelog
