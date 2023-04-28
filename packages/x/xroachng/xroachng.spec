#
# spec file for package xroachng
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


Name:           xroachng
Version:        1.0.3
Release:        0
Summary:        Shows cockroaches running over the desktop
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://www.ratrabbit.nl/ratrabbit/software/xroach_ng
Source:         https://www.ratrabbit.nl/downloads/xroachng/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE xroachng-desktop_file.patch -- Fix desktop categories
Patch0:         xroachng-desktop_file.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)

%description
The classic xroach game for X11: displays disgusting cockroaches on your root
window. These creepy crawlies scamper around until they find a window to
hide under. Whenever you move or iconify a window, the exposed beetles again
scamper for cover.

Adapted for desktop environments like Gnome and KDE. Still works for FVWM, TWM
and the like.

Original copyright 1991 by J. T. Anderson. Squish option contributed by
Rick Petkiewizc. Virtual root code adapted from patch sent by Colin
Rafferty who borrowed it from Tom LaStrange. Several other folks sent
similar fixes. Some glitches removed by patch from Guus Sliepen.

Willem Vermin adapted Xroach for Gnome, KFE etc. and added a graphical 
user interface.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/pixmaps/%{name}.png

%changelog
