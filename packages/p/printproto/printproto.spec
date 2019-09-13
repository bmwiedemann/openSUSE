#
# spec file for package printproto
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           printproto
Version:        1.0.5
Release:        0
Url:            http://xorg.freedesktop.org/
Summary:        The X11 Protocol: Xprint extension
License:        X11
Group:          Development/Libraries/X11

#Git-Clone:	git://anongit.freedesktop.org/xorg/proto/printproto
#Git-Web:	http://cgit.freedesktop.org/xorg/proto/printproto/
Source:         http://xorg.freedesktop.org/releases/individual/proto/%name-%version.tar.bz2
#BuildRequires:  autoconf >= 2.60
#BuildRequires:  automake
#BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Print protocol headers for X11 development.
Xprint is a portable, network-transparent printing system.
It is no longer maintained and solely provided for ABI compatibility.

%package devel
Summary:        The X11 Protocol: Xprint extension
Group:          Development/Libraries/X11

# Added within the 13.2 Development Cycle
Provides:       xorg-x11-proto-devel:%_libdir/pkgconfig/printproto.pc

%description devel
The Print protocol headers for X11 development.
Xprint is a portable, network-transparent printing system.
It is no longer maintained and solely provided for ABI compatibility.

%prep
%setup -q

%build
#autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files devel
%defattr(-,root,root)
%doc COPYING

%_includedir/X11/extensions/
%_libdir/pkgconfig/*.pc
/usr/share/man/man7/Xprint.7%{?ext_man}

%changelog
