#
# spec file for package freedoom
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           freedoom
Version:        0.11.3
Release:        0
Summary:        Replacement game files for Doom game engines
License:        BSD-3-Clause
Group:          Amusements/Games/3D/Shoot
Url:            https://freedoom.github.io/

#Git-Web:       http://github.com/freedoom/freedoom
#Git-Clone:     git://github.com/freedoom/freedoom
Source:         https://github.com/freedoom/freedoom/releases/download/v%version/freedoom-%version.zip
Source2:        https://github.com/freedoom/freedoom/releases/download/v%version/freedoom-%version.zip.asc
Source9:        %name.keyring
BuildArch:      noarch
BuildRequires:  unzip

%description
Though the Doom engine source code is libre, the original game data
(graphics, maps, etc.) is not. Freedoom is an alternate game data set
that can be used with a Doom engine, such as prboom-plus or
chocolate-doom, to form a free Doom-based game.

%prep
%setup -q

%build
# Game data files. Nothing to build!

%install
install -Dpm0644 freedoom1.wad %buildroot/%_datadir/doom/freedoom1.wad
install -Dpm0644 freedoom2.wad %buildroot/%_datadir/doom/freedoom2.wad

%post
echo "NOTE: FreeDoom WAD files are no longer named doom.wad/doom2.wad, and you may need to explicitly specify them now when starting a Doom engine."

%files
%doc COPYING.txt CREDITS.txt README.html
%_datadir/doom/

%changelog
