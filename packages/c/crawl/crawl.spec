#
# spec file for package crawl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define major_ver 0.23
%define about Crawl is a fun game in the grand tradition of games like Rogue, Hack, and Moria.\
Your objective is to travel deep into a subterranean cave complex and retrieve the Orb of Zot, \
which is guarded by many horrible and hideous creatures.
Name:           crawl
Version:        %{major_ver}.2
Release:        0
Summary:        Roguelike dungeon exploration game
License:        GPL-2.0-or-later
Group:          Amusements/Games/RPG
Url:            https://crawl.develz.org/
Source:         https://crawl.develz.org/release/%{major_ver}/stone_soup-%{version}-nodeps.tar.xz
# PATCH-FIX-OPENSUSE for reproducible builds
Patch0:         %{name}-0.17.1-datetime.patch
# PATCH-FIX-UPSTREAM https://github.com/crawl/crawl/pull/464
Patch1:         desktop.patch
Patch2:         icon.patch
Patch3:         appdata.patch
BuildRequires:  dejavu-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  lua51-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pngcrush
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python
BuildRequires:  python-PyYAML
Requires:       %{name}-data = %{version}
%if 0%{?suse_version} >= 1330
Requires:       group(games)
Requires:       user(games)
%else
Requires(pre):  pwdutils
%endif

%description
%about

This is the Stone Soup version of Dungeon Crawl.

Note: You need to be in the 'games' group in order to play the game.

%package sdl
Summary:        Roguelike dungeon exploration game (SDL version)
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}

%description sdl
%about

This is the (SDL-based) tiled Stone Soup version of Dungeon Crawl.

Note: You need to be in the 'games' group in order to play the game.

%package data
Summary:        Roguelike dungeon exploration game (Data files)
Group:          Amusements/Games/RPG
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
%about

These are the data files for Dungeon Crawl Stone Soup.

%prep
%setup -q -n stone_soup-%{version}
%patch0 -p1
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
cd source
tmpflags="%{optflags}"
%ifarch ppc64le
# avoid contentions between SDL vector and gcc defines
# disable the include of altivec.h in /usr/include/SDL2/SDL_cpuinfo.h
# note that --disable-altivec not supported by gcc 4.8
tmpflags="$tmpflags -U__ALTIVEC__"
%endif
make %{?_smp_mflags} clean
make %{?_smp_mflags} prefix=%{_prefix} bin_prefix=bin DATADIR="%{_datadir}/%{name}/" BINDIR=%{_bindir} EXTRA_FLAGS="${tmpflags}"
mv crawl crawl.tty # avoid name clashes temporarily
make %{?_smp_mflags} clean
make %{?_smp_mflags} prefix=%{_prefix} bin_prefix=bin DATADIR="%{_datadir}/%{name}/" BINDIR=%{_bindir} EXTRA_FLAGS="${tmpflags}" TILES="1"
mv crawl crawl-sdl
mv crawl.tty crawl

%pre
%if 0%{?suse_version} < 1330
# Anything after Leap 42.x / SLE12 base uses user/group package dependencies
getent group games >/dev/null || groupadd -r games
getent passwd games >/dev/null || useradd -r -g games -d %{_localstatedir}/games -s /sbin/nologin
%endif
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
make DESTDIR=%{buildroot} prefix=%{_prefix} install-linux-desktop install-linux-appdata -C source
%fdupes %{buildroot}%{_datadir}/%{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

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
