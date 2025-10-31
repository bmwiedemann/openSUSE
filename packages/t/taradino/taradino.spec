#
# spec file for package taradino
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           taradino
Version:        20251031
Release:        0
Summary:        SDL port of the Rise of the Triad engine
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
#URL:            https://icculus.org/rott/
URL:            https://github.com/fabiangreffrath/taradino
Source:         https://github.com/fabiangreffrath/taradino/archive/refs/tags/%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)
Provides:       rott = 1.4
Obsoletes:      rott < 1.4

%description
The package contains an SDL port of the engine used for the
first-person 3D action game "Rise of the Triad".

The ROTT engine is a derivative of the Wolfenstein 3D one, inheriting
level design limits like orthogonal walls and flat floor and ceiling
heights throughout a map. However, the engine did pioneer panoramic
skies, simulated dynamic lighting, fog, bullet holes, breakable glass
walls, and synthetic level-over-level environments through use of
individual collision objects.

%prep
%autosetup -p1

%build
export CFLAGS="%optflags -fno-strict-aliasing"
srcdir="$PWD"
%define __builddir darkwar
%cmake
%cmake_build

cd "$srcdir/"
%define __builddir huntbgin
%cmake -DTARADINO_SHAREWARE:BOOL=ON -DTARADINO_SUFFIX:STRING=huntbgin
%cmake_build

%install
srcdir="$PWD"
%define __builddir darkwar
%cmake_install

cd "$srcdir/"
%define __builddir huntbgin
%cmake_install

ln -sv taradino "%buildroot/%_bindir/rott"
ln -sv taradino-huntbgin "%buildroot/%_bindir/rott-huntbgin"
rm -fv "%buildroot/%_defaultdocdir/%name/COPYING"

%files
%_bindir/rott*
%_bindir/taradino*
%_mandir/man6/taradino*
%_datadir/applications/*.desktop
%_datadir/icons/*
%doc README.md doc/cheats.txt doc/cmdline.txt
%license COPYING

%changelog
