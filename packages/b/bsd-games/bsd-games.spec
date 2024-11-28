#
# spec file for package bsd-games
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


Name:           bsd-games
Version:        2.17
Release:        0
Summary:        Several Text-Mode Games
License:        BSD-3-Clause
Group:          Amusements/Games/Other
URL:            http://www.advogato.org/proj/bsd-games/
Source:         ftp://metalab.unc.edu/pub/Linux/games/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM bsd-games-2.17.diff
Patch0:         %{name}-%{version}.diff
# PATCH-FIX-UPSTREAM bsd-games-2.17-inc.diff
Patch1:         %{name}-%{version}-inc.diff
# PATCH-FIX-UPSTREAM bsd-games-2.17-ppc64.diff
Patch2:         %{name}-%{version}-ppc64.diff
# PATCH-FIX-UPSTREAM bsd-games-2.17-strictaliasing.diff
Patch3:         %{name}-%{version}-strictaliasing.diff
# PATCH-FIX-UPSTREAM bsd-games-2.17-execl.diff
Patch4:         %{name}-%{version}-execl.diff
# PATCH-FIX-UPSTREAM bsd-games-2.17-codecleanup.diff
Patch5:         %{name}-%{version}-codecleanup.diff
# PATCH-FIX-UPSTREAM hunt-64bit.patch
Patch7:         hunt-64bit.patch
# PATCH-FIX-UPSTREAM bsd-games-2.17-compile.patch
Patch8:         %{name}-%{version}-compile.patch
# PATCH-FIX-UPSTREAM bsd-games-2.17-gcc4.3.diff
Patch9:         %{name}-%{version}-gcc4.3.diff
# PATCH-FIX-UPSTREAM fix building with gcc 14
Patch10:        bsd-games-gcc14.diff
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  words
BuildRequires:  pkgconfig(ncursesw)
Requires(pre):  user(games) group(games)

%description
This package provides these games: arithmetic, atc,
backgammon, battlestar, bcd, bog, caesar, canfield, cfscores, cribbage,
fish, fortune, hangman, hunt, mille, monop, morse, number,
paranoia, pom, ppt, primes, rain, robots, sail, snake, snscore,
teachgammon, trek, wargames, worm, worms, and wump.

%prep
%setup -q -n bsd-games-%{version}
%patch -P 0
%patch -P 1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5
%patch -P 7
%patch -P 8
%patch -P 9
%patch -P 10 -p1

%build
# easier than patching :-)
sed -i -e 's#/usr/share/dict/words#/var/lib/dict/words#' configure

(echo %{buildroot}
echo "fortune factor cribbage mille robots"		# don't build fortune; factor is in coreutils, cribbage, robots  and mille fail
echo
echo "%{_bindir}"					# use bindir instead of /usr/games
for i in {1..9}; do echo; done	    			# 9 times default
echo "n" 						# Set owners/groups on installed files
yes "") | ./configure
make CC="gcc" CXX="g++" OPTIMIZE="%{optflags} $(pkg-config --cflags-only-I ncursesw) -DNCURSES_WIDECHAR" \
	dab_CXXFLAGS="-DHAVE_fgetln" %{?_smp_mflags} NCURSES_LIB="$(pkg-config --libs ncursesw)"

%install
make INSTALL_PREFIX=%{buildroot} install SBINDIR="%{_bindir}"
# get rid of dm functionality as it needs a setgid, dm is only used to restrict which games may be played

rm %{buildroot}%{_bindir}/dm

rm -Rf %{buildroot}%{_mandir}/man5 %{buildroot}%{_mandir}/man8

find %{buildroot}%{_localstatedir}/games/ -exec chmod g-w,o-rw {} \;
rm %{buildroot}%{_datadir}/doc/bsd-games/trek.me

# avoid conflict with mono-devel
mv %{buildroot}%{_bindir}/monop           %{buildroot}%{_bindir}/monopoly
mv %{buildroot}%{_mandir}/man6/monop.6.gz %{buildroot}%{_mandir}/man6/monopoly.6.gz

# avoid conflict with the fish shell
mv %{buildroot}%{_bindir}/fish %{buildroot}%{_bindir}/fish-game

%files
%license COPYING
%doc AUTHORS BUGS NEWS README SECURITY THANKS TODO YEAR2000
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/misc/*
%{_datadir}/games/*
%dir %attr(770,games,games) %{_localstatedir}/games/hack
%dir %attr(770,games,games) %{_localstatedir}/games/phantasia
%dir %attr(770,games,games) %{_localstatedir}/games/sail
%attr(660,games,games) %{_localstatedir}/games/hack/data
%attr(660,games,games) %{_localstatedir}/games/hack/help
%attr(660,games,games) %{_localstatedir}/games/hack/hh
%attr(660,games,games) %{_localstatedir}/games/hack/perm
%attr(660,games,games) %{_localstatedir}/games/hack/record
%attr(660,games,games) %{_localstatedir}/games/hack/rumors
%attr(660,games,games) %{_localstatedir}/games/phantasia/characs
%attr(660,games,games) %{_localstatedir}/games/phantasia/gold
%attr(660,games,games) %{_localstatedir}/games/phantasia/lastdead
%attr(660,games,games) %{_localstatedir}/games/phantasia/mess
%attr(660,games,games) %{_localstatedir}/games/phantasia/monsters
%attr(660,games,games) %{_localstatedir}/games/phantasia/motd
%attr(660,games,games) %{_localstatedir}/games/phantasia/scoreboard
%attr(660,games,games) %{_localstatedir}/games/phantasia/void
%attr(660,games,games) %{_localstatedir}/games/atc_score
%attr(660,games,games) %{_localstatedir}/games/battlestar.log
%attr(660,games,games) %{_localstatedir}/games/cfscores
#%attr(660,games,games) %{_localstatedir}/games/criblog
#%attr(660,games,games) %{_localstatedir}/games/robots_roll
%attr(660,games,games) %{_localstatedir}/games/saillog
%attr(660,games,games) %{_localstatedir}/games/snake.log
%attr(660,games,games) %{_localstatedir}/games/snakerawscores
%attr(660,games,games) %{_localstatedir}/games/tetris-bsd.scores

%changelog
