#
# spec file for package rott
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rott
Version:        1.1.2+svn287
Release:        0
Summary:        Icculus SDL port of the Rise of the Triad engine
License:        GPL-2.0+
Group:          Amusements/Games/3D/Shoot
Url:            https://icculus.org/rott/

#SVN-Clone:	svn://svn.icculus.org/rott/trunk/
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(SDL_mixer) >= 1.2
BuildRequires:  pkgconfig(sdl) >= 1.2

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
%setup -qn %name

%build
export CFLAGS="%optflags -fno-strict-aliasing"
autoreconf -fi
%define _configure ../configure

mkdir obj-darkwar
pushd obj-darkwar/
%configure --program-suffix=-darkwar
make %{?_smp_mflags}
popd

mkdir obj-huntbgin
pushd obj-huntbgin/
%configure --enable-shareware --program-suffix=-huntbgin
make %{?_smp_mflags}
popd

%install
b="%buildroot"
make -C obj-darkwar install DESTDIR="$b"
make -C obj-huntbgin install DESTDIR="$b"
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
%defattr(-,root,root)
%_bindir/rott*
%_bindir/runrott.sh
%_mandir/man6/rott.*
%_datadir/applications/*.desktop
%_datadir/icons/*
%doc COPYING README doc/cheats.txt doc/cmdline.txt

%changelog
