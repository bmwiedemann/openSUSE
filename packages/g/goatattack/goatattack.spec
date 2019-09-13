#
# spec file for package goatattack
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           goatattack
Version:        0.4.4
Release:        0
Summary:        Fast-paced multiplayer pixel art shooter game
License:        GPL-3.0+
Group:          Amusements/Games/Action/Shoot
Url:            http://www.goatattack.net
Source:         https://github.com/goatattack/goatattack/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data >= %{version}

%description
Goat Attack is a multiplayer 2D platformer pixel art shooter game.
You can play it in a local network or over the Internet. This project
is split into three parts: the game itself, its map editor, and a
master server. Six gameplay modes are supported: Deathmatch, Team
Deathmatch, Capture The Flag, Speed Race, Catch The Coin and Goat Of
The Hill.

%package data
Summary:        Arch-independent data files for the game Goat Attack
License:        CC-BY-SA-4.0
Group:          Amusements/Games/Action/Shoot
BuildArch:      noarch

%description data
This package contains arch-independent data files (graphics, sounds, music,
levels) for the multiplayer game Goat Attack.

%prep
%setup -q

rm -rf src/shared/zlib

%build
autoreconf -vfi

# TODO build the dedicated server as well
%configure \
  --bindir=%{_bindir} \
  --datadir=%{_datadir} \
  --enable-map-editor

make %{?_smp_mflags}

%install
%make_install

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.md COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-mapeditor
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/%{name}-mapeditor.6*
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}*.appdata.xml
%{_datadir}/applications/%{name}*.desktop

%files data
%defattr(-,root,root)
%{_datadir}/%{name}/

%changelog
