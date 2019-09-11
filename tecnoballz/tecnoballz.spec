#
# spec file for package tecnoballz
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright Vincent Petry <PVince81@yahoo.fr>
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


Name:           tecnoballz
Version:        0.93.1
Release:        0
Summary:        An exciting Brick Breaker
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Breakout
URL:            http://linux.tlk.fr/games/TecnoballZ/
Source:         http://linux.tlk.fr/games/TecnoballZ/download/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.png
# PATCH-FIX-OPENSUSE 0001-Workaround-compilation-warnings-with-gccs-8.0.patch
Patch0:         0001-Workaround-compilation-warnings-with-gccs-8.0.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(sdl)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
A exciting Brick Breaker with 50 levels of game and 11 special levels,
distributed on the 2 modes of game to give the player a sophisticated system
of attack weapons with an enormous power of fire that can be build by
gaining bonuses.  Numerous decors, musics and sounds complete this great
game. This game was ported from the Commodore Amiga.

%prep
%setup -q
%if 0%{?suse_version} >= 1550
%patch0 -p1
%endif

# Fix games path to %{_bindir} instead of /usr/games
find -name Makefile.am -exec sed -i -e "s|^gamesdir =.*$|gamesdir = %{_bindir}|g" \{\} \;

sed -i -e "s|^CXXFLAGS=\"\(.*\)\"|CXXFLAGS=\"\1 %{optflags}\"|" configure.ac

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install-strip
install -Dm 0644 man/%{name}.fr.6 %{buildroot}%{_mandir}/fr/man6/%{name}.6
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%endif

%fdupes -s %{buildroot}%{_prefix}

%files
%license COPYING
%doc AUTHORS CHANGES NEWS README
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/fr/man6/%{name}.6%{?ext_man}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_localstatedir}/games/
%attr(0775,games,games) %dir %{_localstatedir}/games/%{name}/
%attr(0664,games,games)%{_localstatedir}/games/%{name}/%{name}.hi

%changelog
