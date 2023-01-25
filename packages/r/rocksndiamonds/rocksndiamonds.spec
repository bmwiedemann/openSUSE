#
# spec file for package rocksndiamonds
#
# Copyright (c) 2023 SUSE LLC
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
Version:        4.3.4.0
Release:        0
Summary:        Colorful Boulderdash'n'Emerald Mine'n'Sokoban'n'Stuff
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.artsoft.org/rocksndiamonds/
Source0:        https://www.artsoft.org/RELEASES/linux/%{name}/%{name}-%{version}-linux.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
# PATCH-FIX-UPSTREAM Permissions
Patch0:         %{name}-src_libgame_setup.c-CVE-2011-4606.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  system-user-games
BuildRequires:  update-desktop-files
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
%setup -q -b 1
%patch0 -p1

# Remove not needed files
find levels -name '*.orig' -delete
rm -f %{name}

%build
%make_build \
    OPTIONS="%{optflags}" \
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

# install icons
for i in 32 48 64 72 96 ; do
    install -Dm 0644 ../icons/%{name}_${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install desktop file
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm 755 -d %{buildroot}%{_localstatedir}/games/%{name}

%suse_update_desktop_file %{name}

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
