#
# spec file for package xman
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


Name:           xman
Version:        1.1.5
Release:        0
Summary:        Manual page display program for the X Window System
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        xman.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xman is a graphical manual page browser.

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
%{_bindir}/xman
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xman
%{_datadir}/X11/xman.help
%{_mandir}/man1/xman.1%{?ext_man}

%changelog
