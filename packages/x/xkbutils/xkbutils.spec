#
# spec file for package xkbutils
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xkbutils
Version:        1.0.4
Release:        0
Summary:        Collection of small utilities utilizing the X11 XKeyboard extension
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xkbutils is a collection of small utilities utilizing the XKeyboard
(XKB) extension to the X11 protocol.

It includes:
 xkbbell  - generate XKB bell events
 xkbvleds - display the state of LEDs on an XKB keyboard in a window
 xkbwatch - reports changes in the XKB keyboard state

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xkbbell
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
%{_mandir}/man1/xkbbell.1%{?ext_man}
%{_mandir}/man1/xkbvleds.1%{?ext_man}
%{_mandir}/man1/xkbwatch.1%{?ext_man}

%changelog
