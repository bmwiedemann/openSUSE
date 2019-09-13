#
# spec file for package lmarbles
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lmarbles
Version:        1.0.8
Release:        0
Summary:        Atomix-like Game of moving Marbles in Puzzle
License:        GPL-2.0
Group:          Amusements/Games/Arcade/Logic
Url:            http://lgames.sourceforge.net/index.php?project=LMarbles
Source0:        http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
LMarbles is a game similar to Atomix and was heavily inspired by it.
The goal is to arrange a figure out of single marbles within a time
limit to reach the next level.

Your goal in the puzzle game marbles is to create a more or less complex
figure out of single marbles within a time limit to reach the next
level. Sounds easy? Well, there is a problem: If a marble starts to
move, it will not stop until it hits a wall or another marble.

%prep
%setup -q
sed -i 's|Categories=Game;|Categories=Game;ArcadeGame;LogicGame;|' %{name}.desktop.in
sed -i 's|(datadir)/icons|(datadir)/pixmaps|' Makefile.in

%build

%configure --prefix=/usr --localstatedir=%{_localstatedir}/games/lmarbles
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README README-SDL.txt
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}48.gif
%{_datadir}/%{name}
%dir %{_localstatedir}/games
%attr(0664,root,games) %{_localstatedir}/games/lmarbles

%changelog
