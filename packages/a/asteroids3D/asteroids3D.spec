#
# spec file for package asteroids3D
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


Name:           asteroids3D
Version:        1.0
Release:        0
Summary:        First-person shooter blowing up asteroids
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://inai.de/projects/asteroids3D

Source:         https://inai.de/files/asteroids3D/%name-%version.tar.xz
Source2:        https://inai.de/files/asteroids3D/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  pkg-config >= 0.19
BuildRequires:  xz
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glut)

%description
A simple first person shooter of blowing up asteroids in 3D space.
The codebase also serves as an introduction to trigonometry and
OpenGL.

%prep
%autosetup

%build
%configure --with-gamesdir=%_bindir --with-gamedatadir=%_datadir/games/%name
%make_build

%install
%make_install

%files
%_bindir/asteroids3D
%_datadir/applications/*.desktop
%_datadir/games/%name

%changelog
