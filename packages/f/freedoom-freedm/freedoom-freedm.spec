#
# spec file for package freedoom-freedm
#
# Copyright (c) 2024 SUSE LLC
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


Name:           freedoom-freedm
Version:        0.13.0
Release:        0
Summary:        Deathmatch levels for Doom
License:        BSD-3-Clause
Group:          Amusements/Games/3D/Shoot
URL:            https://freedoom.github.io/
Source:         https://github.com/freedoom/freedoom/releases/download/v%version/freedm-%version.zip
BuildArch:      noarch
BuildRequires:  unzip
Requires:       freedoom

%description
A set of deathmatch levels for the DOOM game engine, based on the
freely redistributable Freedoom game files.

%prep
%autosetup -n freedm-%version

%build
# Game data files.  Nothing to build!

%install
install -Dpm0644 freedm.wad %buildroot/%_datadir/doom/freedm.wad

%files
%doc CREDITS.txt freedoom-manual*.pdf README.html
%license COPYING.txt
%_datadir/doom/

%changelog
