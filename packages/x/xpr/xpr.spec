#
# spec file for package xpr
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


Name:           xpr
Version:        1.1.0
Release:        0
Summary:        Utility to print an X window dump
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xpr takes as input a window dump file produced by xwd
and formats it for output on various types of printers.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xdpr
%{_bindir}/xpr
%{_mandir}/man1/xdpr.1%{?ext_man}
%{_mandir}/man1/xpr.1%{?ext_man}

%changelog
