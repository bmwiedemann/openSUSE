#
# spec file for package libXrandr
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


Name:           libXrandr
%define lname   libXrandr2
Version:        1.5.3
Release:        0
Summary:        X Resize, Rotate and Reflection extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXrandr
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXrandr/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(randrproto) >= 1.5
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrender)

%description
The X Resize, Rotate and Reflect Extension (RandR) allows clients to
dynamically change X screens, so as to resize, to change the
orientation and layout of the root window of a screen.

%package -n %lname
Summary:        X Resize, Rotate and Reflection extension library
Group:          System/Libraries

%description -n %lname
The X Resize, Rotate and Reflect Extension (RandR) allows clients to
dynamically change X screens, so as to resize, to change the
orientation and layout of the root window of a screen.

%package devel
Summary:        Development files for the X Resize-Rotate-Reflection library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The X Resize, Rotate and Reflect Extension (RandR) allows clients to
dynamically change X screens, so as to resize, to change the
orientation and layout of the root window of a screen.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
#git#autoreconf -fi
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
%_libdir/libXrandr.so.2*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXrandr.so
%_libdir/pkgconfig/xrandr.pc
%_mandir/man3/*

%changelog
