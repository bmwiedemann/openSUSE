#
# spec file for package prboom-plus
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.5.1.5+svn4532
Release:        0
Summary:        DOOM source port with demo compatibility
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            http://prboom-plus.sf.net/

#SVN-Clone:	https://svn.prboom.org/repos/branches/prboom-plus-24/prboom2
#DL-URL:	http://downloads.sf.net/prboom-plus/prboom-plus-2.5.1.4.tar.gz
Source:         prboom2-%version.tar.xz
Patch1:         prboom-nodatetime.diff
Patch2:         prboom-types1.diff
Patch3:         prboom-types2.diff
Patch5:         prboom-enable-tessellation.diff
Patch6:         prboom-hbar-color.diff
Patch7:         prboom-hbar-all.diff
Patch8:         prboom-hbar-gradient.diff
BuildRequires:  Mesa-devel
BuildRequires:  automake
BuildRequires:  fluidsynth-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)
%if 0%{?suse_version} >= 1320
BuildRequires:  portmidi-devel
%endif
BuildRequires:  update-desktop-files
Suggests:       freedoom
Provides:       prboom = 2.5.0plus
Obsoletes:      prboom <= 2.5.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%autosetup -p1 -n prboom2-%version

%build
cp -alv data/sounds/free/*.wav data/sounds/
cp -alv data/sprites/free/* data/sprites/
autoreconf -fi
# rpm has its own optimizations, so turn off shipped defaults
%configure --enable-gl --disable-cpu-opt --program-prefix="" \
	--with-waddir="%_datadir/doom" --disable-dogs CFLAGS="%optflags -fcommon"
make %{?_smp_mflags}

%install
b="%buildroot"
%make_install gamesdir="%_bindir"

# convenience symlink
ln -s prboom-plus "%buildroot/%_bindir/prboom"
install -Dm0644 ICONS/prboom-plus.svg "$b/%_datadir/icons/hicolor/scalable/apps/prboom-plus.svg"
install -Dm0644 ICONS/prboom-plus.desktop "$b/%_datadir/applications/prboom-plus.desktop"
install -Dm0644 ICONS/prboom-plus.bash "$b/%_datadir/bash-completion/completions/prboom-plus.bash"

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
%_datadir/doc/*
%_mandir/*/*
%_datadir/applications/prboom-plus.desktop
%_datadir/icons/hicolor/scalable/apps/prboom-plus.svg
%_datadir/bash-completion/

%changelog
