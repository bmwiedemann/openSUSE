#
# spec file for package dsda-doom
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.30.1
Release:        0
Summary:        DOOM source port with Hexen support and demo compatibility
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/dsda-org/dsda-doom
#Changelog:     https://github.com/dsda-org/dsda-doom/tree/master/patch_notes
Source:         https://github.com/dsda-org/dsda-doom/archive/refs/tags/v%version.tar.gz
Patch1:         prboom-hbar-all.diff
Patch2:         prboom-hbar-gradient.diff
BuildRequires:  Mesa-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.17
BuildRequires:  fluidsynth
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  libzip-tools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(portmidi)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile) >= 1.0.29
BuildRequires:  pkgconfig(vorbis)
%if 0%{?suse_version} >= 1600
# CMake Error at [portmidi-devel]:/usr/lib64/cmake/PortMidi/PortMidiTargets.cmake:100 (message):
#   The imported target "PortMidi::pmjni" references the file
#      "[portmidi-java]:/usr/lib64/libpmjni.so.2.0.3"
BuildRequires:  portmidi-java
%endif
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
cd prboom2/
%cmake -DDOOMWADDIR="%_datadir/doom" -DDSDAPWADDIR="%_datadir/doom" -D_IMPORT_PREFIX=$PWD/usr
%cmake_build

%install
cd prboom2/
%cmake_install
rm -f "%buildroot/usr/share/doc/dsda-doom/COPYING" # via %%license instead

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
