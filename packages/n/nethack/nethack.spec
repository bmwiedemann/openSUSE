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
Summary:        Character Based RPG
License:        NGPL
Group:          Amusements/Games/RPG
URL:            http://www.nethack.org/
Source0:        nethack-343-src.tar.bz2
# PATCH-FIX-UPSTREAM nethack-config.patch
Patch0:         nethack-config.patch
# PATCH-FIX-UPSTREAM nethack-decl.patch
Patch1:         nethack-decl.patch
# PATCH-FIX-UPSTREAM nethack-misc.patch
Patch2:         nethack-misc.patch
# PATCH-FIX-UPSTREAM nethack-syscall.patch
Patch3:         nethack-syscall.patch
# PATCH-FIX-UPSTREAM nethack-gzip.patch
Patch5:         nethack-gzip.patch
Patch6:         reproducible.patch
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
This RPG is somewhat cryptic with its character based output. But a
true fan knows and appreciates its complexity and possibilities.

This package contains the text interface.

%prep
%setup -q
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P5
%patch -P6 -p1

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
install -m 775 -d %{buildroot}%{_localstatedir}/games/nethack/
install -m 775 -d %{buildroot}%{_localstatedir}/games/nethack/save/
for file in logfile perm record ; do
	touch %{buildroot}%{_localstatedir}/games/nethack/$file
	chmod 0664 %{buildroot}%{_localstatedir}/games/nethack/$file
done
# binaries
install -m 2755 src/nethack %{buildroot}%{_prefix}/lib/nethack/
# options
install -m 644 dat/options %{buildroot}%{_prefix}/lib/nethack/
# man pages
install -m 644 doc/{nethack,lev_comp,dlb,dgn_comp,recover}.6 %{buildroot}/%{_mandir}/man6/
# doc
install -d %{buildroot}/%{_docdir}/nethack
install doc/fixes* %{buildroot}/%{_docdir}/nethack
install doc/Guidebook.{ps,txt} %{buildroot}/%{_docdir}/nethack
# common data
install -m0644 dat/nhdat %{buildroot}%{_datadir}/games/nethack/
install -m0644 dat/license %{buildroot}%{_datadir}/games/nethack/
# configs
install -m0755 -d %{buildroot}%{_sysconfdir}/nethack
# main launcher script
install -d %{buildroot}%{_bindir}
install -m0755 sys/unix/nethack.sh %{buildroot}%{_bindir}/nethack
# utils
install -m 755 util/{dgn_comp,dlb,lev_comp,makedefs,recover} %{buildroot}%{_prefix}/lib/nethack/

%fdupes -s %{buildroot}%{_datadir}/games/nethack/license

%post
%set_permissions

%verifyscript
%verify_permissions -e /usr/lib/nethack/nethack

%files
%license dat/license
%doc doc/fixes*
%doc doc/Guidebook.ps
%doc doc/Guidebook.txt
%defattr(-,root,root)
%verify(not mode) %attr(0755,games,games) %{_prefix}/lib/nethack/nethack
%{_prefix}/lib/nethack/options
%dir %{_prefix}/lib/nethack
%{_datadir}/games/nethack
%{_prefix}/lib/nethack/dgn_comp
%{_prefix}/lib/nethack/dlb
%{_prefix}/lib/nethack/lev_comp
%{_prefix}/lib/nethack/makedefs
%{_prefix}/lib/nethack/recover
%{_mandir}/man6/*
%dir %attr(0770,games,games) %{_localstatedir}/games/nethack
%dir %attr(0770,games,games) %{_localstatedir}/games/nethack/save
%config(noreplace) %attr(0660,games,games) %{_localstatedir}/games/nethack/logfile
%config(noreplace) %attr(0660,games,games) %{_localstatedir}/games/nethack/record
%attr(0660,games,games) %{_localstatedir}/games/nethack/perm
%{_bindir}/nethack

%changelog
