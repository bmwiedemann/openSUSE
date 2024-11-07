#
# spec file for package crawl
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011 Sascha Peilicke <sasch.pe@gmx.de>
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


%define about Crawl is a fun game in the grand tradition of games like Rogue, Hack, and Moria.\
Your objective is to travel deep into a subterranean cave complex and retrieve the Orb of Zot, \
which is guarded by many horrible and hideous creatures.
Name:           crawl
Version:        0.32.1
Release:        0
Summary:        Roguelike dungeon exploration game
License:        GPL-2.0-or-later
Group:          Amusements/Games/RPG
URL:            https://crawl.develz.org/
Source:         https://github.com/crawl/crawl/releases/download/%{version}/stone_soup-%{version}-nodeps.tar.xz
Patch0:         desktop.patch
Patch1:         icon.patch
Patch2:         appdata.patch
BuildRequires:  dejavu-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  lua51-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pngcrush
BuildRequires:  python3
BuildRequires:  python3-PyYAML
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
Requires:       %{name}-data = %{version}
Requires:       group(games)
Requires:       user(games)

%description
%{about}

This is the Stone Soup version of Dungeon Crawl.

Note: You need to be in the 'games' group in order to play the game.

%package sdl
Summary:        Roguelike dungeon exploration game (SDL version)
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}

%description sdl
%{about}

This is the (SDL-based) tiled Stone Soup version of Dungeon Crawl.

Note: You need to be in the 'games' group in order to play the game.

%package data
Summary:        Roguelike dungeon exploration game (Data files)
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%{about}

These are the data files for Dungeon Crawl Stone Soup.

%prep
%autosetup -p1 -n stone_soup-%{version}

%build
cd source
tmpflags="%{optflags}"
%ifarch ppc64le
# avoid contentions between SDL vector and gcc defines
# disable the include of altivec.h in /usr/include/SDL2/SDL_cpuinfo.h
# note that --disable-altivec not supported by gcc 4.8
tmpflags="$tmpflags -U__ALTIVEC__"
%endif
%make_build clean
%make_build prefix=%{_prefix} bin_prefix=bin DATADIR="%{_datadir}/%{name}/" BINDIR=%{_bindir} EXTRA_FLAGS="${tmpflags}"
mv crawl crawl.tty # avoid name clashes temporarily
%make_build clean
%make_build prefix=%{_prefix} bin_prefix=bin DATADIR="%{_datadir}/%{name}/" BINDIR=%{_bindir} EXTRA_FLAGS="${tmpflags}" TILES="1"
mv crawl crawl-sdl
mv crawl.tty crawl

%pre
# move old saves
if [ -d %{_localstatedir}/games/crawl ]; then
	if [ -d /root/.crawl ]; then
		mv /root/.crawl /root/.crawl_old
	fi
	mv %{_localstatedir}/games/crawl /root/.crawl
fi

%install
%make_install -C source prefix=%{_prefix} bin_prefix=bin DATADIR=%{_datadir}/%{name} BINDIR=%{_bindir} TILES=y
install -D -m0644 docs/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m0755 source/crawl-sdl %{buildroot}%{_bindir}/crawl-sdl
%fdupes %{buildroot}%{_datadir}/%{name}

%files sdl
%attr(0755,root,root) %{_bindir}/%{name}-sdl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files data
%{_datadir}/%{name}

%files
%license LICENSE
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/*

%changelog
