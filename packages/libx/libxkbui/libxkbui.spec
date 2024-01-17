#
# spec file for package libxkbui
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libxkbui
%define lname	libxkbui1
Version:        1.0.2
Release:        0
Summary:        X11 keyboard UI presentation library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libxkbui
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libxkbui/
Source:         http://ftp.x.org/pub/X11R7.1/src/lib/%{name}-X11R7.1-%{version}.tar.bz2
Source1:        baselibs.conf
Patch1:         libxkbui.diff
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xt)

%description
libxkbui provides an interface to easily present XKB layouts as
graphical widgets.

%package -n %lname
Summary:        X11 keyboard UI presentation library
Group:          System/Libraries

%description -n %lname
libxkbui provides an interface to easily present XKB layouts as
graphical widgets.

%package devel
Summary:        Development files for the X11 keyboard UI presentation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libxkbui provides an interface to easily present XKB layouts as
graphical widgets.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -n %name-X11R7.1-%version -p0

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libxkbui.so.1*

%files devel
%_includedir/X11/*
%_libdir/libxkbui.so
%_libdir/pkgconfig/xkbui.pc

%changelog
