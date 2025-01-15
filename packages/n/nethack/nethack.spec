#
# spec file for package nethack
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


Name:           nethack
Version:        3.4.3
Release:        0
Summary:        Turn-based role-playing game
License:        NGPL
Group:          Amusements/Games/RPG
URL:            https://www.nethack.org
Source0:        nethack-343-src.tar.bz2
Source1:        nethack-rpmlintrc
# PATCH-FIX-OPENSUSE nethack-config.patch Adapt build to openSUSE systems
Patch0:         nethack-config.patch
# PATCH-FIX-OPENSUSE nethack-decl.patch Do not redeclare system interfaces
Patch1:         nethack-decl.patch
# PATCH-FIX-OPENSUSE nethack-escape-char.patch
Patch2:         nethack-escape-char.patch
# PATCH-FIX-OPENSUSE nethack-secure.patch Handle SECURE in recover utility
Patch3:         nethack-secure.patch
# PATCH-FIX-OPENSUSE nethack-gzip.patch Use gzip compression
Patch4:         nethack-gzip.patch
# PATCH-FIX-OPENSUSE nethack-reproducible.patch boo#1047218
Patch5:         nethack-reproducible.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  groff
BuildRequires:  ncurses-devel
Requires:       gzip
Requires(pre):  user(games) group(games)
Requires(pre):  permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NetHack is a turn-based role-playing game with complex game mechanics.
Descent into the Maze of Menace and retrieve the Amulet of Yendor. Play
as different character classes, such as fighter, wizard, rogue and others.
Persist against various monsters and defeat the Wizard of Yendor.

This package contains the text interface.

%prep
%setup -q
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5 -p1

%build
# copy Makefiles and add optimization flags
sh sys/unix/setup.sh
sed -i "s/^CFLAGS.*/& %{optflags}/" Makefile dat/Makefile doc/Makefile src/Makefile util/Makefile

# The Makefiles do not track dependencies correctly, which can result
# in link errors on parallel builds. Prevent this by building the object
# files for makedefs first.
%make_build -C src monst.o
%make_build -C src objects.o
%make_build -C src dlb.o

# Build the game binary, then some data files. Finally build all
# remaining default targets. Although 'all' covers the first three
# make calls as well, we have to resort to sequential building
# to make it work.
%make_build nethack
%make_build dungeon
%make_build spec_levs
%make_build all

# We also package a nicely formatted manual in PostScript format. It
# is not covered by 'all', so build it here.
%make_build -C doc Guidebook.ps

%install
# directories
install -d %{buildroot}%{_prefix}/lib/nethack/
install -d %{buildroot}%{_prefix}/games
install -d %{buildroot}%{_datadir}/games/nethack
install -d %{buildroot}/%{_mandir}/man6/
# game directory
install -d %{buildroot}%{_localstatedir}/games/nethack/
install -d %{buildroot}%{_localstatedir}/games/nethack/save/
for file in logfile paniclog perm record ; do
	touch %{buildroot}%{_localstatedir}/games/nethack/$file
done
# binaries
install src/nethack %{buildroot}%{_prefix}/lib/nethack/
# options
install dat/options %{buildroot}%{_prefix}/lib/nethack/
# man pages
install doc/{nethack,lev_comp,dlb,dgn_comp,recover}.6 %{buildroot}/%{_mandir}/man6/
# common data
install dat/nhdat %{buildroot}%{_datadir}/games/nethack/
install dat/license %{buildroot}%{_datadir}/games/nethack/
# main launcher script
install -d %{buildroot}%{_bindir}
install sys/unix/nethack.sh %{buildroot}%{_bindir}/nethack
# utils
install util/{dgn_comp,dlb,lev_comp,makedefs,recover} %{buildroot}%{_prefix}/lib/nethack/

%fdupes -s %{buildroot}%{_datadir}/games/nethack/license

%post
%set_permissions

%verifyscript
%verify_permissions -e /usr/lib/nethack/nethack

%files
%defattr(0644,root,root)
%license dat/license
%doc doc/fixes*
%doc doc/Guidebook.ps
%doc doc/Guidebook.txt
%attr(0755,-,-) %{_bindir}/nethack
%{_mandir}/man6/*
%dir %{_datadir}/games/nethack
%{_datadir}/games/nethack/license
%{_datadir}/games/nethack/nhdat
%dir %{_prefix}/lib/nethack
%attr(0755,-,-) %{_prefix}/lib/nethack/dgn_comp
%attr(0755,-,-) %{_prefix}/lib/nethack/dlb
%attr(0755,-,-) %{_prefix}/lib/nethack/lev_comp
%attr(0755,-,-) %{_prefix}/lib/nethack/makedefs
%attr(0755,-,-) %{_prefix}/lib/nethack/nethack
%attr(0755,-,-) %{_prefix}/lib/nethack/recover
%{_prefix}/lib/nethack/options
%dir %attr(0770,games,games) %{_localstatedir}/games/nethack
%dir %attr(0770,games,games) %{_localstatedir}/games/nethack/save
%config(noreplace) %attr(0660,games,games) %{_localstatedir}/games/nethack/logfile
%config(noreplace) %attr(0660,games,games) %{_localstatedir}/games/nethack/paniclog
%config(noreplace) %attr(0660,games,games) %{_localstatedir}/games/nethack/record
%attr(0660,games,games) %{_localstatedir}/games/nethack/perm

%changelog
