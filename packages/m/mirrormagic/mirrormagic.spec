#
# spec file for package mirrormagic
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


Name:           mirrormagic
Version:        2.0.2
Release:        0
Summary:        Puzzle game where you steer a beam of light using mirrors
License:        GPL-2.0
Group:          Amusements/Games/Logic
Url:            http://www.artsoft.org/mirrormagic/
Source0:        http://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
# Fix deprecated code
Patch0:         %{name}-%{version}-src_editor.c.patch
# Correct SDL code
Patch1:         %{name}-%{version}-src_events.c.patch
# Correct highscore
Patch2:         %{name}-%{version}-src_files.c.patch
# Correct GCC code
Patch3:         %{name}-%{version}-src_main.h.patch
# Correct that works with 64 and 386 bit
Patch4:         %{name}-%{version}-src_libgame_gadgets.c.patch
# Correct SDL code
Patch5:         %{name}-%{version}-src_libgame_sdl.c.patch
# Correct SDL code
Patch6:         %{name}-%{version}-src_libgame_sdl.h.patch
# Correct security code
Patch7:         %{name}-%{version}-src_tools.c.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
%if 0%{?suse_version} < 1330
Requires(pre):	/usr/sbin/useradd /usr/sbin/groupadd
%else
Requires(pre):  group(games) user(games)
%endif

%description
This is a nice little game with color graphics and sound for your
Unix system with color X11. You need an 8-bit color display or better.
It will not work on black&white systems, and maybe not on gray scale
systems.

It was first released as "Mindbender" in the year 1989 on the Amiga
(with ports on other computer systems) and is in fact a clone of the
C64 game "Deflektor".

%prep
%setup -q -b 1
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7

%build
make %{?_smp_mflags} sdl \
    OPTIONS="%{optflags} -w -fgnu89-inline" \
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

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm 755 -d %{buildroot}%{_localstatedir}/games/%{name}

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%if 0%{?suse_version} < 1330
%pre
getent group games >/dev/null || groupadd -r games
getent passwd games >/dev/null || useradd -r -g games -d /var/games -s /sbin/nologin
%endif

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%attr(0775,games,games) %{_localstatedir}/games/%{name}

%changelog
