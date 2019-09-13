#
# spec file for package twind
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           twind
Version:        1.1.0
Release:        0
Summary:        Match and remove all of the blocks before time runs out
License:        GPL-2.0
Group:          Amusements/Games/Arcade/LogicGame
Url:            http://twind.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
# PATCH-FIX-OPENSUSE - twind-1.1.0.twind.c.patch -- Correct bad code
Patch0:         %{name}-1.1.0.twind.c.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The object of the game is to remove all of the blocks from the screen
before the time runs out. Two blocks are removed at a time,
and must be of the same color. After completing a level,
you will be rewarded with a bonus point for every tick left on the clock.
For each level thereafter, the time to complete the the level will be shorter.

Shortcut Keys Used During the Game

 b - change the block set
 c - change the corner style of the blocks
 f, F4 - toggle between full screen/window mode (can be used anywhere)
 h, F1 - display the help screen
 m - turn background music on/off (can be used anywhere)
 n, F2 - start a new game (highscores won't be saved ending a game this way)
 p, Pause, F3 - pause/unpause the game
 q, Esc - quit the game
 s - turn sound effects on/off (can be used anywhere)
 0 - 9 - toggle the L & R colors on Insane mode (can be used anywhere)

%prep
%setup -q
%patch0

# SED-FIX-OPENSUSE -- Correct Path and Highscore
sed -i -e 's|chown |true |;
           s|/usr/local/bin|${DESTDIR}%{_libexecdir}/%{name}|;
           s|/usr/local/share/games/%{name}|${DESTDIR}%{_libexecdir}/%{name}|;
           s|HIGH_SCORE_PREFIX =|#HIGH_SCORE_PREFIX =|;
           s|mkdir -p $(HIGH_SCORE_PREFIX)||' Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fgnu89-inline"

%install
mkdir -p %{buildroot}%{_bindir}
%make_install

# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install icon
install -Dm 0644 graphics/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README
%{_bindir}/%{name}
%attr(0755,root,games) %{_libexecdir}/%{name}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_libexecdir}/%{name}

%changelog
