#
# spec file for package flare
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


Name:           flare
Version:        1.14
Release:        0
Summary:        Free Libre Action Roleplaying Engine
License:        (CC-BY-SA-3.0 OR CC-BY-SA-4.0) AND GPL-3.0-or-later
Group:          Amusements/Games/RPG
URL:            https://flarerpg.org
Source0:        https://github.com/flareteam/flare-game/releases/download/v%{version}/%{name}-engine-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
Requires:       %{name}-game = %{version}
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):update-desktop-files
Recommends:     python
Provides:       %{name}-engine = %{version}

%description
Flare (Free Libre Action Roleplaying Engine) is a game engine built
to handle a very specific kind of game: single-player 2D action RPGs.
Flare is not a reimplementation of an existing game or engine. It is a
tribute to and exploration of the action RPG genre.

The usecase of this project is to build several real games and
reuse code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses .ini-style config files for most of the
game data to modify game contents. The game code is C++.

%prep
%setup -q -n %{name}-engine-v%{version}
# W: desktopfile-without-binary flare.desktop /usr/bin/flare
sed -i 's/@FLARE_EXECUTABLE_PATH@/%{name}/g' distribution/flare.desktop.in

%build
%cmake \
    -DBINDIR="bin" \
    -DDATADIR="share/flare" \
    -DCMAKE_BUILD_TYPE="Release" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}"
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}/%{_prefix}

%files
%license COPYING
%doc README* RELEASE_NOTES.txt
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
