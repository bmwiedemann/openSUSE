#
# spec file for package ballerburg
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


Name:           ballerburg
Version:        1.2.3
Release:        0
Summary:        Two players, two castles, and a hill in between
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://baller.frama.io/
#Git-Clone:     git://framagit.org/baller/ballerburg.git
Source:         https://framagit.org/baller/ballerburg/-/archive/v%{version}/ballerburg-v%{version}.tar.gz
Source1:        %{name}.xpm
BuildRequires:  cmake >= 3.10
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sdl2)

%description
Ballerburg is a castle combat game. Two players (which can be human or
computer-controlled) try to destroy the opponent's castle with their cannons.

Eckhard Kruse's original Ballerburg from 1987 ported to SDL.

%prep
%setup -q -n ballerburg-v%{version}

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%make_build

%install
%cmake_install
install -D -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/%{name}.xpm
%suse_update_desktop_file -c %{name} %{name} "Turn-based castle computer game" %{name} %{name} Game BoardGame
rm -rf %{buildroot}%{_datadir}/doc/ballerburg/
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.txt
%doc LIESMICH.txt README.txt doc/de/anleitung.html doc/en/manual.html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
