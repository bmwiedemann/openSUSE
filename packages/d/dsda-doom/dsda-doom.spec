#
# spec file for package dsda-doom
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dsda-doom
Version:        0.28.3
Release:        0
Summary:        DOOM source port with Hexen support and demo compatibility
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/kraflab/dsda-doom

#Changelog:     https://github.com/kraflab/dsda-doom/tree/master/patch_notes
#Announce:      https://www.doomworld.com/forum/topic/118074-dsda-doom-source-port-v0243/
Source:         https://github.com/kraflab/dsda-doom/archive/refs/tags/v%version.tar.gz
Patch1:         prboom-hbar-all.diff
Patch2:         prboom-hbar-gradient.diff
BuildRequires:  Mesa-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fluidsynth
BuildRequires:  fluidsynth-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmad-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libzip-devel
BuildRequires:  libzip-tools
BuildRequires:  pcre-devel
BuildRequires:  portmidi-devel
BuildRequires:  portmidi-java
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)
Suggests:       freedoom
Provides:       prboom

%description
DSDA-Doom is a source port derived from the PrBoom history line.
It features:

* Extra tooling for demo recording, with focus on speedrunning:
  record-rewind support
* Heretic and Hexen support
* MBFv21, UMAPINFO and DSDHacked specification support

%prep
%autosetup -p1

%build
pushd prboom2/
%cmake -DDOOMWADDIR="%_datadir/doom" -DDSDAPWADDIR="%_datadir/doom"
%cmake_build
popd

%install
pushd prboom2/
%cmake_install
rm -f "%buildroot/usr/share/doc/dsda-doom/COPYING" # via %%license instead
popd

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%_bindir/*
%_datadir/doom/
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/
%doc docs/*.md
%license prboom2/COPYING

%changelog
