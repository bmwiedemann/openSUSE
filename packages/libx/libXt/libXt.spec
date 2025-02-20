#
# spec file for package libXt
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libXt
%define lname	libXt6
Version:        1.3.1
Release:        0
Summary:        X Toolkit Intrinsics library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXt
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXt/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch0:         u_pkgconfig-file-move-sm-from-private-to-public-Requir.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.13
BuildRequires:  pkgconfig(xproto)

%description
The low level Xlib library provides functions for interacting with an
X11 server, but does not provide any function for implementing the
graphical objects (widgets) used in GUIs, such as buttons, menus,
etc. The Xt library provides support for creating and using widget
types, but does not provide any specific widget. Specific widgets are
implemented by other libraries using Xt, such as Xaw and Motif.

%package -n %lname
Summary:        X Toolkit Intrinsics library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXt = 7.6_%version-%release
Obsoletes:      xorg-x11-libXt < 7.6_%version-%release

%description -n %lname
The low level Xlib library provides functions for interacting with an
X11 server, but does not provide any function for implementing the
graphical objects (widgets) used in GUIs, such as buttons, menus,
etc. The Xt library provides support for creating and using widget
types, but does not provide any specific widget. Specific widgets are
implemented by other libraries using Xt, such as Xaw and Motif.

%package devel
Summary:        Development files for the X Toolkit Intrinsics library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXt-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXt-devel < 7.6_%version-%release

%description devel
The low level Xlib library provides functions for interacting with an
X11 server, but does not provide any function for implementing the
graphical objects (widgets) used in GUIs, such as buttons, menus,
etc. The Xt library provides support for creating and using widget
types, but does not provide any specific widget. Specific widgets are
implemented by other libraries using Xt, such as Xaw and Motif.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1

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
%_libdir/libXt.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXt.so
%_libdir/pkgconfig/xt.pc
%_mandir/man3/*
%_docdir/%name

%changelog
