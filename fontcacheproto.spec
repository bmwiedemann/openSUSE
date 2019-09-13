#
# spec file for package fontcacheproto
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


Name:           fontcacheproto
Version:        0.1.3
Release:        0
Url:            http://xorg.freedesktop.org/
Summary:        The X11 Protocol: Fontcache extension
License:        BSD-2-Clause
Group:          Development/Libraries/X11

#Git-Clone:	git://anongit.freedesktop.org/xorg/proto/fontcacheproto
#Git-Web:	http://cgit.freedesktop.org/xorg/proto/fontcacheproto/
Source:         http://xorg.freedesktop.org/releases/individual/proto/%name-%version.tar.bz2
#BuildRequires:  autoconf >= 2.57
#BuildRequires:  automake
#BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Fontcache protocol headers for X11 development.

%package devel
Summary:        The X11 Protocol: Fontcache extension
Group:          Development/Libraries/X11

# Added within the 13.2 Development Cycle
Provides:       xorg-x11-proto-devel:%_libdir/pkgconfig/fontcacheproto.pc

%description devel
The Fontcache protocol headers for X11 development.

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

%changelog
