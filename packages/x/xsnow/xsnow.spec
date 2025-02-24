#
# spec file for package xsnow
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


Name:           xsnow
Version:        3.8.3
Release:        0
Summary:        A Christmas Animation
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://www.ratrabbit.nl/ratrabbit/xsnow
Source:         https://www.ratrabbit.nl/downloads/xsnow/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE xsnow-bindir.patch -- Install in /usr/bin instead /usr/games
Patch0:         xsnow-bindir.patch
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
Xsnow is an application that animates snowfall, Santa and some scenery on your desktop.
It is NOT a kind of screen saver: snow is falling, Santa rides his sleigh with reindeer
while you are using your system.
Xsnow runs on most varieties of Linux, and probably on other Unix systems as well.

Xsnow is derived from Rick Jansen's xsnow-1.42.

%lang_package

%prep
%autosetup -p1

%build
%configure --disable-selfrep
%make_build

%install
%make_install

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS ChangeLog README README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/pixmaps/%{name}.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
