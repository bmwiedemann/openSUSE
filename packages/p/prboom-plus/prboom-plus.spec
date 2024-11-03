#
# spec file for package prboom-plus
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


Name:           prboom-plus
Version:        2.6.66
Release:        0
Summary:        DOOM source port with demo compatibility
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            http://prboom-plus.sf.net/
#Git-Clone:	https://github.com/coelckers/prboom-plus
Source:         https://github.com/coelckers/prboom-plus/archive/refs/tags/v%version.tar.gz
Patch1:         prboom-nodatetime.diff
Patch3:         prboom-hbar-all.diff
Patch4:         prboom-hbar-gradient.diff
Patch5:         gcc14.diff
BuildRequires:  Mesa-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fluidsynth-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pcre-devel
BuildRequires:  portmidi-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)
Suggests:       freedoom
Provides:       prboom = 2.6um
Obsoletes:      prboom <= 2.6

%description
PrBoom+ is a conservative Doom source port. It features:

* The removal of engine limits and bugs, like the visplane limit,
  savegame size limit, the tutti-frutti and medusa visual effects,
  and others.
* BOOM editing extensions, e.g. configurable animated/switch
  textures, deep water effect, scrolling walls/floors/ceilings,
  conveyor belts, translucent walls and sprites, friction effects,
  and generic linedef actions.
* Focus on retaining compatibility with the original Doom engines
  for the purpose of demo recording and playback.
* High resolution rendering of map geometry, optionally in OpenGL
  mode.

%prep
%autosetup -p0

%build
pushd prboom2/
%cmake -DDOOMWADDIR="%_datadir/doom" -DPRBOOMDATADIR="%_datadir/doom"
%cmake_build
popd

%install
s="$PWD"
pushd prboom2/
%cmake_install
# convenience symlink
b="%buildroot"
ln -s prboom-plus "$b/%_bindir/prboom"
install -Dm0644 ICONS/prboom-plus.svg "$b/%_datadir/icons/hicolor/scalable/apps/prboom-plus.svg"
install -Dm0644 ICONS/prboom-plus.desktop "$b/%_datadir/applications/prboom-plus.desktop"
install -Dm0644 ICONS/prboom-plus.bash "$b/%_datadir/bash-completion/completions/prboom-plus.bash"
popd
# TW switched doc location in %%cmake
(cd "%buildroot"; find "./%_datadir/doc" -type d -name prboom-plus | cut -b2-) >"$s/doc.files"
ls -al "$s/doc.files"

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -f doc.files
%_bindir/*
%_datadir/doom/
%_mandir/*/*
%_datadir/applications/prboom-plus.desktop
%_datadir/icons/hicolor/scalable/apps/prboom-plus.svg
%_datadir/bash-completion/

%changelog
