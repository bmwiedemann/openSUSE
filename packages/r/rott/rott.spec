#
# spec file for package rott
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


Name:           rott
Version:        1.2~git66
Release:        0
Summary:        SDL port of the Rise of the Triad engine
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://icculus.org/rott/
Source:         %name-%version.tar.xz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)

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
%autosetup

%build
export CFLAGS="%optflags -fno-strict-aliasing"
autoreconf -fi
%define _configure ../configure

mkdir obj-darkwar
pushd obj-darkwar/
%configure --program-suffix=-darkwar
%make_build
popd

mkdir obj-huntbgin
pushd obj-huntbgin/
%configure --enable-shareware --program-suffix=-huntbgin
%make_build
popd

%install
b="%buildroot"
%make_install -C obj-darkwar
%make_install -C obj-huntbgin
ln -s rott-darkwar "$b/%_bindir/rott"
mkdir -p "$b/%_datadir/icons/hicolor"/{32x32,scalable}/"apps" \
	"$b/%_datadir/applications"
cp -a misc/rott.desktop "$b/%_datadir/applications"
cp -a misc/rott.{xpm,png} "$b/%_datadir/icons/hicolor/32x32/apps/"
cp -a misc/rott.svg "$b/%_datadir/icons/hicolor/scalable/apps/"
cp -a misc/runrott.sh "$b/%_bindir/"
mkdir -p "$b/%_mandir/man6"
cp -a doc/rott.6 "$b/%_mandir/man6/"

%files
%_bindir/rott*
%_bindir/runrott.sh
%_mandir/man6/rott.*
%_datadir/applications/*.desktop
%_datadir/icons/*
%doc README doc/cheats.txt doc/cmdline.txt
%license COPYING

%changelog
