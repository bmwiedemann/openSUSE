#
# spec file for package xcalc
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


Name:           xcalc
Version:        1.1.2
Release:        0
Summary:        Scientific calculator for X
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz.sig
Source2:        xcalc.keyring
Source3:        xcalc.desktop
Source4:        xcalc.png
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xcalc is a scientific calculator X11 client that can emulate a TI-30
or an HP-10C.

%prep
%setup -q
cp %{SOURCE3} .

%build
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i -u xcalc Utility Calculator
install -m0644 -D %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/xcalc.png

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xcalc
%{_datadir}/applications/xcalc.desktop
%{_datadir}/pixmaps/xcalc.png
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_mandir}/man1/xcalc.1%{?ext_man}

%changelog
