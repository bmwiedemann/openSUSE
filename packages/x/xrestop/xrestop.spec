#
# spec file for package xrestop
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           xrestop
Version:        0.4
Release:        0
License:        GPL-2.0+
Summary:        Utility to monitor server resources used by X11 clients
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://downloads.yoctoproject.org/releases/xrestop/%{name}-%{version}.tar.gz
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
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/xrestop
%{_mandir}/man1/xrestop.1%{?ext_man}

%changelog
