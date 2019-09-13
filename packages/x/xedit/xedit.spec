#
# spec file for package xedit
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xedit
Version:        1.2.2
Release:        0
Summary:        Simple text editor for X
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt) >= 1.0
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xedit is a simple text editor for X.

%prep
%setup -q
# bnc#684116
cp lisp/README README.lisp
cp lisp/re/README README.re

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README README.lisp README.re
%{_bindir}/xedit
%{_libdir}/X11/xedit/
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1%{?ext_man}
%ifnarch %ix86
%dir %{_libdir}/X11
%endif

%changelog
