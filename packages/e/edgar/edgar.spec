#
# spec file for package edgar
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


Name:           edgar
Version:        1.36
Release:        0
Summary:        2D platform game with a persistent world
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            http://www.parallelrealities.co.uk/games/edgar/
Source0:        https://github.com/riksweeney/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
Requires:       %{name}-data = %{version}
Recommends:     %{name}-lang = %{version}
%lang_package

%description
The Legend of Edgar is a platform game, not unlike those found on the Amiga and
SNES. Edgar must battle his way across the world, solving puzzles and defeating
powerful enemies to achieve his quest.

A 2D platform game with a persistent world.
When Edgar's father fails to return home after venturing out one dark and stormy
night, Edgar fears the worst: he has been captured by the evil sorcerer who
lives in a fortress beyond the forbidden swamp.

Donning his armour, Edgar sets off to rescue him, but his quest will not be
easy...

%package data
Summary:        Architecture independent data for %{name}
Group:          Amusements/Games/Action/Arcade
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package contains the game data for %{name}.
It is required to play the game.

%prep
%setup -q
mv makefile Makefile

# SED-FIX-OPENSUSE -- Fix paths
sed -i -e 's|$(PREFIX)/games/|$(PREFIX)/bin/|;
           s|/share/doc/|/share/doc/packages/|;
           s|/share/games/edgar/|/share/edgar/|' Makefile

%build
make %{?_smp_mflags} CC="cc %{optflags}"

%install
%make_install
%find_lang %{name}

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%doc doc/*
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%files lang -f %{name}.lang

%files data
%{_datadir}/%{name}

%changelog
