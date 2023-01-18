#
# spec file for package flare-game
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


Name:           flare-game
Version:        1.14
Release:        0
Summary:        Free Libre Action Roleplaying Engine — Game
License:        CC-BY-SA-3.0+
Group:          Amusements/Games/RPG
URL:            https://flarerpg.org
Source0:        https://github.com/flareteam/flare-game/releases/download/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Requires:       flare-engine = %{version}
Provides:       flare-data = %{version}
Obsoletes:      flare-data < %{version}
BuildArch:      noarch

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built
to handle a very specific kind of game: single-player 2D action RPGs.
Flare is not a reimplementation of an existing game or engine. It is a
tribute to and exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style config files) for most of the
game data, allowing anyone to easily modify game contents. Open formats
are preferred (png, ogg). The game code is C++.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake \
    -DBINDIR="bin" \
    -DDATADIR="share/flare" \
    -DCMAKE_BUILD_TYPE="Release" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}"

%install
%cmake_install
%fdupes -s %{buildroot}/%{_prefix}

%files
%doc README* CREDITS.txt
%{_datadir}/flare
%{_datadir}/metainfo/org.flarerpg.Flare.appdata.xml

%changelog
