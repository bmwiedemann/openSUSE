#
# spec file for package neverball
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


Name:           neverball
Version:        1.6.0
Release:        0
Summary:        Deftly Guide a Rolling Ball through Many Slick 3D Levels
License:        GPL-2.0+
Group:          Amusements/Games/3D/Other
Url:            http://neverball.org
Source:         http://%{name}.org/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://github.com/Neverball/neverball/pull/142
Patch1:         appdata.patch
%define	        name2 neverputt
%define	        name3 mapc
BuildRequires:  dejavu-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libSDL2-devel
BuildRequires:  libSDL2_ttf-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  libpng16-devel
BuildRequires:  libvorbis-devel
BuildRequires:  physfs-devel
BuildRequires:  update-desktop-files
Requires:       opengl-games-utils

%description
Tilt the floor to roll a ball through an obstacle course within the
given time. If the ball falls or time expires, a ball is lost.

Collect 100 coins to save your progress and earn an extra ball.
Red coins are worth 5. Blue coins are worth 10.

In the grand tradition of Marble Madness and Super Monkey Ball,
Neverball has you guide a rolling ball through dangerous territory.
Balance on narrow bridges, navigate mazes, ride moving platforms,
and dodge pushers and shovers to get to the goal.
Race against the clock to collect coins to earn extra balls.

%package %{name2}
Summary:        3D mini golf game
Group:          Amusements/Games/3D/Other
Requires:       %{name}

%description %{name2}
A hot-seat multiplayer miniature golf game, built on the physics
and graphics engine of Neverball.

Based on the physics and graphics of Neverball, Neverputt is a hot-seat
multi-player miniature golf game for 1 to 4 players. The available
courses take advantage of all the elements that challenge Neverball
players, including moving platforms and barriers, teleporters, ramps,
and drop-offs. A simple putting interface and golf scoring system
have been added.

%package %{name3}
Summary:        Mapc is a program designed to compile the levels
Group:          Development/Tools/Other
BuildRequires:  libSDL2_net-devel
Requires:       %{name}

%description %{name3}
Mapc is a program designed to compile the levels made with Radiant
to make them usable in Neverball and Neverputt.
All instructions are based upon using command lines.

The output will be saved to Imap.sol.

http://wiki.nevercorner.net/doku.php/mapc

https://icculus.org/neverball/mapping/

%package -n %{name}-doc
Summary:        Documentation for the %{name}
Group:          Documentation
BuildArch:      noarch

%description -n %{name}-doc
Tilt the floor to roll a ball through an obstacle course within the
given time. If the ball falls or time expires, a ball is lost.

Collect 100 coins to save your progress and earn an extra ball.
Red coins are worth 5. Blue coins are worth 10.

In the grand tradition of Marble Madness and Super Monkey Ball,
Neverball has you guide a rolling ball through dangerous territory.
Balance on narrow bridges, navigate mazes, ride moving platforms,
and dodge pushers and shovers to get to the goal.
Race against the clock to collect coins to earn extra balls.

Documentation for the %{name}.

%prep
%setup -q
%patch1 -p1

# Add missing libraries
sed -i -e 's|-lphysfs|-lphysfs -lm|' \
       -e 's|$(OGL_LIBS)|$(OGL_LIBS) -lX11|' Makefile

# Change executebles for OpenGL Wrapper
sed -i 's|Exec=%{name}|Exec=%{name}-wrapper|' dist/%{name}.desktop.in
sed -i 's|Exec=%{name2}|Exec=%{name2}-wrapper|' dist/%{name2}.desktop.in

%build
make %{?_smp_mflags} CC="gcc %{optflags} -fomit-frame-pointer"  \
        DATADIR=%{_datadir}/%{name} LOCALEDIR=%{_datadir}/locale \
        ENABLE_NLS=1 ENABLE_RADIANT_CONSOLE=1

%install
# install executables and mans
for f in %{name} %{name2} %{name3} ; do
    install -Dm 0755 $f %{buildroot}%{_bindir}/$f
done
for f in %{name} %{name2} ; do
    install -Dm 0644 dist/$f.6 %{buildroot}%{_mandir}/man6/$f.6
done
install -Dm 0644 dist/%{name3}.1 %{buildroot}%{_mandir}/man1/%{name3}.1

# Adjust permissions
find data -name '*.sol' -exec chmod 644 '{}' \;

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r data/* %{buildroot}%{_datadir}/%{name}/

# Symlink executables
for f in %{name} %{name2} %{name3} ; do
    ln -s %{_bindir}/$f %{buildroot}%{_datadir}/%{name}/$f
done

# Use system fonts instead of bundling our own
rm -f %{buildroot}%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf
ln -s %{_datadir}/fonts/truetype/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf

# install icons
for i in 24 32 48 64 128 256 512 ; do
    install -Dm 0644 dist/%{name}_${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
    install -Dm 0644 dist/%{name2}_${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name2}.png
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
for f in %{name} %{name2} ; do
    ln -s %{_datadir}/%{name}/icon/$f.png %{buildroot}%{_datadir}/pixmaps/$f.png
done

# install desktop file
install -Dm 0644 dist/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 dist/%{name2}.desktop %{buildroot}%{_datadir}/applications/%{name2}.desktop

# install software gallery metadata
install -Dm 0644 dist/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

cp -r locale %{buildroot}%{_datadir}/

# symlink OpenGL Wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name2}-wrapper

%find_lang %name

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name2}

%fdupes -s %{buildroot}%{_prefix}

%files -f %name.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/*
%{_datadir}/%{name}

%files %{name2}
%defattr(-,root,root,-)
%{_bindir}/%{name2}
%{_bindir}/%{name2}-wrapper
%{_mandir}/man6/%{name2}.6%{ext_man}
%{_datadir}/applications/%{name2}.desktop

%files %{name3}
%defattr(-,root,root,-)
%{_bindir}/%{name3}
%{_mandir}/man1/%{name3}.1%{ext_man}

%files -n %{name}-doc
%defattr(-,root,root,-)
%doc LICENSE.md README.md doc/*.{txt,md}

%changelog
