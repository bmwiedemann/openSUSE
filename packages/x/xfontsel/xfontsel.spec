#
# spec file for package xfontsel
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


Name:           xfontsel
Version:        1.1.0
Release:        0
Summary:        Utility to display X11 font names
License:        X11
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz.sig
Source2:        xfontsel.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xfontsel application provides a simple way to display the X11 core
protocol fonts known to your X server, examine samples of each, and
retrieve the X Logical Font Description ("XLFD") full name for a font.

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
%{_bindir}/xfontsel
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1%{?ext_man}

%changelog
