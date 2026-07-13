#
# spec file for package xstdcmap
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


Name:           xstdcmap
Version:        1.0.6
Release:        0
Summary:        Utility to define standard colormap properties
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 1.1.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
The xstdcmap utility can be used to selectively define standard colormap
properties. It is intended to be run from a user's X startup script to
create standard colormap definitions in order to facilitate sharing of
scarce colormap resources among clients using PseudoColor visuals.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xstdcmap
%{_mandir}/man1/xstdcmap.1%{?ext_man}

%changelog
