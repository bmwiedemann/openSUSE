#
# spec file for package libXdmcp
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


Name:           libXdmcp
%define lname	libXdmcp6
Version:        1.1.4
Release:        0
Summary:        X Display Manager Control Protocol library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXdmcp
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXdmcp/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)

%description
The X Display Manager Control Protocol (XDMCP) provides a uniform
mechanism for an autonomous display to request login service from a
remote host. By autonomous, we mean the display consists of hardware
and processes that are independent of any particular host where login
service is desired. An X terminal (screen, keyboard, mouse,
processor, network interface) is a prime example of an autonomous
display.

%package -n %lname
Summary:        X Display Manager Control Protocol library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXdmcp = 7.6_%version-%release
Obsoletes:      xorg-x11-libXdmcp < 7.6_%version-%release

%description -n %lname
The X Display Manager Control Protocol (XDMCP) provides a uniform
mechanism for an autonomous display to request login service from a
remote host. By autonomous, we mean the display consists of hardware
and processes that are independent of any particular host where login
service is desired. An X terminal (screen, keyboard, mouse,
processor, network interface) is a prime example of an autonomous
display.

%package devel
Summary:        Development files for the XDM Control Protocol library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXdmcp-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXdmcp-devel < 7.6_%version-%release

%description devel
The X Display Manager Control Protocol (XDMCP) provides a uniform
mechanism for an autonomous display to request login service from a
remote host. By autonomous, we mean the display consists of hardware
and processes that are independent of any particular host where login
service is desired. An X terminal (screen, keyboard, mouse,
processor, network interface) is a prime example of an autonomous
display.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
autoreconf -fi
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXdmcp.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXdmcp.so
%_libdir/pkgconfig/xdmcp.pc
%_docdir/%name

%changelog
