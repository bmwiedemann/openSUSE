#
# spec file for package rocksndiamonds
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           rocksndiamonds
Version:        4.4.1.3
Release:        0
Summary:        Colorful Boulderdash'n'Emerald Mine'n'Sokoban'n'Stuff
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.artsoft.org/rocksndiamonds/
#Git-Clone:     https://git.artsoft.org/rocksndiamonds.git
Source0:        https://www.artsoft.org/RELEASES/linux/%{name}/%{name}-%{version}-linux.tar.gz
Source1:        %{name}-icons.tar.gz
Source2:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  system-user-games
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data
Requires(pre):  user(games)

%description
This is a nice little game with color graphics and sound for your Unix system
with color X11.  You need an 8-Bit color display or better.  It will not work
on black&white systems, and maybe not on gray scale systems.

If you know the game Boulder Dash (Commodore C64) or Emerald Mine (Amiga),
you know what Rocks'n'Diamonds is about.

%prep
%autosetup -p1

# Remove not needed files
find levels -name '*.orig' -delete
rm -f %{name}

%build
%make_build \
    OPTIONS="%{optflags}" \
    BASE_PATH=%{_datadir}/%{name} \
    RO_GAME_DIR=%{_datadir}/%{name} \
    RW_GAME_DIR=%{_localstatedir}/games/%{name}

%install
# install executable
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,levels,music,sounds}
for d in graphics levels music sounds ; do
    cp -a $d %{buildroot}%{_datadir}/%{name}
done

# install icon
install -Dm 0644 graphics/gfx_classic/icons/icon.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# install desktop file
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm 755 -d %{buildroot}%{_localstatedir}/games/%{name}

%fdupes -s %{buildroot}%{_prefix}

%files
%license COPYING
%doc CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%attr(0775,games,games) %{_localstatedir}/games/%{name}

%changelog
