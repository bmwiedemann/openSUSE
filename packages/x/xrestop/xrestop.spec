#
# spec file for package xrestop
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


Name:           xrestop
Version:        0.6
Release:        0
Summary:        Utility to monitor server resources used by X11 clients
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
XResTop is a 'top' like tool for monitoring X Client server resource
usage.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/xrestop
%{_mandir}/man1/xrestop.1%{?ext_man}

%changelog
