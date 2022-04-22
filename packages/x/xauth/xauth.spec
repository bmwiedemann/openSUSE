#
# spec file for package xauth
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


Name:           xauth
Version:        1.1.2
Release:        0
Summary:        Utility to edit and display the X authorization information
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Patch1:         xauth-tolerant-hostname-changes.diff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# Name of subpackage when this was part of the xorg-x11 package up to version 7.6
Provides:       xorg-x11-xauth = 7.6
Obsoletes:      xorg-x11-xauth <= 7.6

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server.

%prep
%setup -q
%patch1 -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xauth
%{_mandir}/man1/xauth.1%{?ext_man}

%changelog
