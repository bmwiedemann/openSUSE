#
# spec file for package commandergenius
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


Name:           commandergenius
Version:        3.5.2
Release:        0
Summary:        A clone of the Commander Keen engines
License:        GPL-2.0-only
Group:          Amusements/Games/Action/Arcade
URL:            http://clonekeenplus.sf.net/
#Git-Clone:     https://gitlab.com/Dringgstein/Commander-Genius
Source:         https://gitlab.com/Dringgstein/Commander-Genius/-/archive/v%version/Commander-Genius-v%version.tar.bz2
Patch1:         fix-icons.patch
Patch2:         gs.patch
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
# changelog.txt in the archive is only sometimes updated

%description
Commander Genius is a software piece that interprets the Commander
Keen Vorticon (1-3) and Galaxy (3½-6) series.

It has 4-player cooperative mode and six difficulty modes.

%prep
%autosetup -p1 -n Commander-Genius-v%version
if pkg-config 'SDL2_ttf < 2.24'; then
%patch -P 2 -R -p1
fi

%build
%cmake \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DAPPDIR="%_bindir"
%cmake_build

%install
%cmake_install
install -Dm0644 share/cg.svg "%buildroot/%_datadir/icons/hicolor/scalable/apps/cg.svg"
%fdupes %buildroot/%_datadir

%files
%license COPYRIGHT
%_bindir/CGeniusExe
%_datadir/applications/cgenius.desktop
%_datadir/metainfo/io.sourceforge.clonekeenplus.appdata.xml
%_datadir/icons/hicolor/
%_datadir/games/%name/

%changelog
