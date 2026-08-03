#
# spec file for package xkbprint
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           xkbprint
Version:        1.0.8
Release:        0
Summary:        Utility to print an XKB keyboard description
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 1.1.0
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xkbprint generates a printable or encapsulated PostScript description
of an XKB keyboard description.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xkbprint
%{_mandir}/man1/xkbprint.1%{?ext_man}

%changelog
