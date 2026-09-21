#
# spec file for package 0verkill
#
# Copyright (c) 2021 SUSE LLC
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


%define gitdate 20101114
%global commit0 522f11a3e40670bbf85e0fada285141448167968
%global shortcommit0 522f11a
Name:           0verkill
Version:        0.16+git%{gitdate}
Release:        0
Summary:        Bloody hell in ASCII art
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            https://github.com/hackndev/0verkill
Source0:        https://github.com/hackndev/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:        %{name}.png
Source99:       0verkill-rpmlintrc
# PATCH-FEATURE-UPSTREAM desktop-and-appdata.patch -- https://github.com/hackndev/0verkill/pull/2
Patch0:         desktop-and-appdata.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)

%description
2D ASCII art deathmatch jump'n'kill'n'smile_insane.

You were born to DIE - you will enjoy your death!
Your eyes gonna BULGE with horror...
IT is the game you always wanted to die playing !!!
This game will be your worst NIGHTMARE you ever had!

For X Window support check package 0verkill-xwindow

%package xwindow
Summary:        Bloody hell in ASCII art (with X Window support)
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}

%description xwindow
2D ASCII art deathmatch jump'n'kill'n'smile_insane.

You were born to DIE - you will enjoy your death!
Your eyes gonna BULGE with horror...
IT is the game you always wanted to die playing !!!
This game will be your worst NIGHTMARE you ever had!

%prep
%autosetup -n %{name}-%{commit0} -p1

cp %{SOURCE1} .

%build
autoreconf -fiv
export CFLAGS="$CFLAGS -fcommon"
%configure --with-x
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/0verkill/grx/make_hero

%files
%license doc/COPYING doc/AUTHORS
%doc doc/CHANGELOG doc/FILES doc/README.html doc/VERSION
%doc doc/3d.txt doc/adding_a_level.txt doc/avi.txt doc/bot.txt doc/doc.html doc/editor.txt doc/level-changing.txt
%{_bindir}/0verkill*
%{_datadir}/0verkill
%{_datadir}/appdata/0verkill.appdata.xml

%files xwindow
%{_datadir}/applications/0verkill.desktop
%{_datadir}/pixmaps/0verkill.png
%{_bindir}/x0verkill*

%changelog
