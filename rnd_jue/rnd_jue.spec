#
# spec file for package rnd_jue
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


Name:           rnd_jue
Version:        3.3.0.0
Release:        0
Summary:        Colorful Boulderdash'n'Emerald Mine'n'Sokoban'n'Stuff jue
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.jb-line.de/rnd/rnd_start_e.html
Source0:        http://www.jb-line.de/rnd/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
# PATCH-FIX-UPSTREAM - rnd_jue-3.3.0.0-src_libgame_setup.c-CVE-2011-4606.patch --Fix Permissions
Patch0:         %{name}-3.3.0.0-src_libgame_setup.c-CVE-2011-4606.patch
# PATCH-FIX-UPSTREAM in rocksndiamonds 4.0.0.1 - boo#1047218
Patch1:         reproducible.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
#BuildRequires:  libsmpeg-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(sdl)
Requires:       %{name}-data
%if 0%{?suse_version} >= 1330
Requires(pre):	user(games) group(games)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
"R'n'D jue" is an alternative version of Rocks'n'Diamonds, developed in
cooperation with R&D author Holger Schemel.

In contrast to the "rnd_jue -contribution package"
(still available on Download page) it is a separate and independent program
with the same source code as the original R'n'D but with a
completely different appearance.

This is based on the wide customizing features which have been developed
recently while all the integrated games have been produced with the R'n'D
Level Editor, which is actually a great "game creation tool" for
non-programmers. So far "R'n'D jue" is also an example for what is possible
with the old Rocks'n'Diamonds and should be an inspiration for potential
level designers and game developers.

Regarding the games and levels "R'n'D jue" is intended for players who have both
an eye for an attractive design and a bent especially for "puzzle games".
The user will also find "action" and many opportunities to test his
manual-skill - nevertheless, the main feature of "R'n'D jue" is primarily
to offer some (moderate) challenges for the brain.

%prep
%setup -q -b 1
%patch0
%patch1 -p1

# Remove not needed files
find levels -name '*.broken' -delete -or -name '*.orig' -delete
rm -f %{name}

# SED-FIX-OPENSUSE -- Remove non existent library (libsmpeg-devel)
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
%doc COPYING CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%attr(0775,games,games) %{_localstatedir}/games/%{name}

%changelog
