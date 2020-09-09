#
# spec file for package minetest-game
#
# Copyright (c) 2020 SUSE LLC
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


Name:           minetest-game
Version:        5.3.0
Release:        0
Summary:        Minetest Game
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC-BY-3.0 AND CC0-1.0
Group:          Amusements/Games/3D/Simulation
URL:            https://minetest.net/
Source0:        https://github.com/minetest/minetest_game/archive/%{version}/minetest_game-%{version}.tar.gz
Source99:       minetest-game-rpmlintrc
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       minetest-runtime >= %{version}

%description
The main game for the Minetest game engine.

%prep
%setup -q -n minetest_game-%{version}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/minetest/games/minetest_game
cp -ar * %{buildroot}%{_datadir}/minetest/games/minetest_game
%fdupes -s %{buildroot}%{_datadir}/minetest/games/minetest_game

%files
%license LICENSE.txt
%doc README.md
%dir %{_datadir}/minetest/
%dir %{_datadir}/minetest/games/
%{_datadir}/minetest/games/minetest_game/

%changelog
