#
# spec file for package tint
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Guido Berhoerster <guido+opensuse.org@berhoerster.name>.
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


Name:           tint
Version:        0.04
Release:        0
Summary:        A Clone of the Original Tetris Game
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Puzzle
Url:            http://packages.debian.org/source/sid/tint
Source:         tint_%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE tint-0.04-scores-in-home.patch guido+opensuse.org@berhoerster.name -- Save highscore on a per-user basis under $XDG_DATA_HOME
Patch0:         tint-0.04-per-user-highscore.patch
# PATCH-FIX-UPSTREAM tint-0.04-fix-buffer-overflow.patch guido+opensuse.org@berhoerster.name -- Fix two buffer overflows
Patch1:         tint-0.04-fix-buffer-overflow.patch
BuildRequires:  ncurses-devel

%description
TINT is a clone of the original tetris game written by Alexey Pajitnov, Dmitry
Pavlovsky, and Vadim Gerasimov. The game is as close to the original as
possible, but there are a few differences. Nevertheless, it is probably the
closest to the original that you'll ever find in the UNIX world.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -D -m 755 tint %{buildroot}%{_bindir}/tint
install -D -m 644 tint.6 %{buildroot}%{_mandir}/man6/tint.6

%files
%doc CREDITS NOTES debian/copyright
%{_mandir}/man6/tint.6*
%{_bindir}/tint

%changelog
