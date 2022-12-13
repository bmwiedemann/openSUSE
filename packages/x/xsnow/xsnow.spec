#
# spec file for package xsnow
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


Name:           xsnow
Version:        3.6.0
Release:        0
Summary:        A Christmas Animation
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://www.ratrabbit.nl/ratrabbit/xsnow
Source:         https://www.ratrabbit.nl/downloads/xsnow/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE xsnow-desktop_file.patch -- Fix desktop categories
Patch0:         xsnow-desktop_file.patch
# PATCH-FIX-OPENSUSE xsnow-bindir.patch -- Install in /usr/bin instead /usr/games
Patch1:         xsnow-bindir.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Xsnow is an application that animates snowfall, Santa and some scenery on your desktop.
It is NOT a kind of screen saver: snow is falling, Santa rides his sleigh with reindeer
while you are using your system.
Xsnow runs on most varieties of Linux, and probably on other Unix systems as well.

Xsnow is derived from Rick Jansen's xsnow-1.42.

%prep
%setup -q
%autopatch -p1

%build
%configure --disable-selfrep
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/pixmaps/%{name}.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
