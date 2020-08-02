#
# spec file for package evieproto
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


%define name_archive evieext

Name:           evieproto
Version:        1.1.1
Release:        0
Url:            http://xorg.freedesktop.org/
Summary:        The X11 Protocol: Event Interception extension
License:        MIT
Group:          Development/Libraries/X11

#Git-Clone:	git://anongit.freedesktop.org/xorg/proto/evieproto
#Git-Web:	http://cgit.freedesktop.org/xorg/proto/evieproto/
Source:         http://xorg.freedesktop.org/releases/individual/proto/%{name_archive}-%{version}.tar.bz2
#BuildRequires:  autoconf >= 2.60
#BuildRequires:  automake
#BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Evie protocol headers for X11 development.

%package devel
Summary:        The X11 Protocol: Event Interception extension
Group:          Development/Libraries/X11

# Added within the 13.2 Development Cycle
Provides:       xorg-x11-proto-devel:%_libdir/pkgconfig/evieproto.pc

%description devel
The Evie protocol headers for X11 development.
XEvIE is a X extension providing functionalities to allow a client to
intercept keyboard/mouse events, and optionally modify them or consume
them before delivery through the normal event delivery mechanisms.

It was included in X11R6.8 through Xorg server 1.5, but is no
longer supported in current X server releases.

%prep
%setup -n %{name_archive}-%{version} -q

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

%changelog
