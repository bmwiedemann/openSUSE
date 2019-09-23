#
# spec file for package rocksndiamonds
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


Name:           rocksndiamonds
Version:        4.1.1.0
Release:        0
Summary:        Colorful Boulderdash'n'Emerald Mine'n'Sokoban'n'Stuff
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.artsoft.org/rocksndiamonds/
Source0:        http://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
# PATCH-FIX-UPSTREAM Permissions
Patch0:         %{name}-3.3.1.2-src_libgame_setup.c-CVE-2011-4606.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
#BuildRequires:  libsmpeg-devel
BuildRequires:  update-desktop-files
BuildRequires:  update-desktop-files
Requires:       %{name}-data
%if 0%{?suse_version} >= 1330
Requires(pre):  group(games)
Requires(pre):  user(games)
%else
Requires(pre):	/usr/sbin/groupadd /usr/sbin/useradd
%endif

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

sed -i 's|-lsmpeg||' src/Makefile

%build
make %{?_smp_mflags} sdl \
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
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm 755 -d %{buildroot}%{_localstatedir}/games/%{name}

%suse_update_desktop_file %{name}

%fdupes -s %{buildroot}%{_prefix}

%if 0%{?suse_version} < 1330
%pre
getent group games >/dev/null || groupadd -r games
getent passwd games >/dev/null || useradd -r -g games -d /var/games -s /sbin/nologin
%endif

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%attr(0775,games,games) %{_localstatedir}/games/%{name}

%changelog
