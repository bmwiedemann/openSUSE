#
# spec file for package viewres
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


Name:           viewres
Version:        1.0.8
Release:        0
Summary:        Graphical class browser for Xt
License:        X11
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
viewres displays a tree showing the widget class hierarchy of the
Athena Widget Set (libXaw).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%doc ChangeLog README.md
%license COPYING
%{_bindir}/viewres
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color
%{_mandir}/man1/viewres.1%{?ext_man}

%changelog
