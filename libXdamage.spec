#
# spec file for package libXdamage
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


Name:           libXdamage
%define lname	libXdamage1
Version:        1.1.6
Release:        0
Summary:        X Damage Extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://wiki.freedesktop.org/wiki/Software/XDamage

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXdamage
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXdamage/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(damageproto) >= 1.1
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3

%description
The X Damage Extension allows applications to track modified regions
of drawables.

%package -n %lname
Summary:        X Damage Extension library
Group:          System/Libraries

%description -n %lname
The X Damage Extension allows applications to track modified regions
of drawables.

%package devel
Summary:        Development files for the X Damage Extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The X Damage Extension allows applications to track modified regions
of drawables.

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
%_libdir/libXdamage.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXdamage.so
%_libdir/pkgconfig/xdamage.pc

%changelog
