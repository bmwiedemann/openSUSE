#
# spec file for package tint
#
# Copyright (c) 2021 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           tint
Version:        0.06
Release:        0
Summary:        A Clone of the Original Tetris Game
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Puzzle
URL:            https://packages.debian.org/source/sid/tint
Source:         http://deb.debian.org/debian/pool/main/t/tint/tint_%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE tint-0.04-scores-in-home.patch guido+opensuse.org@berhoerster.name -- Save highscore on a per-user basis under $XDG_DATA_HOME
Patch0:         tint-0.04-per-user-highscore.patch
BuildRequires:  ncurses-devel

%description
TINT is a clone of the original tetris game written by Alexey Pajitnov, Dmitry
Pavlovsky, and Vadim Gerasimov. The game is close to the original, but
there are a few differences.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
install -D -m 755 tint %{buildroot}%{_bindir}/tint
install -D -m 644 tint.6 %{buildroot}%{_mandir}/man6/tint.6
install -D -m 644 debian/tint.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 debian/tint.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc CREDITS NOTES
%license debian/copyright
%{_bindir}/tint
%{_mandir}/man6/tint.6*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
