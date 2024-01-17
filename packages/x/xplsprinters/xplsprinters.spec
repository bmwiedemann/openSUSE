#
# spec file for package xplsprinters
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

Name:           xplsprinters
Version:        1.0.1
Release:        0
License:        MIT
Summary:        Utility to list Xprint printers
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xprintutil)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xplsprinters is a utility for Xprint, the printing system for the
X Window system. It can deliver both a list of printers and
attributes supported for a specific list of printers.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/xplsprinters
%{_mandir}/man1/xplsprinters.1x%{?ext_man}

%changelog
