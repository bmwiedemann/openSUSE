#
# spec file for package zaz
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright Vincent Petry <PVince81@opensuse.org>
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


Name:           zaz
Version:        1.0.0
Release:        0
Summary:        Puzzle game about arranging balls in triplets
License:        GPL-3.0+
Group:          Amusements/Games/Logic
Url:            http://zaz.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE - zaz-extra_zaz.desktop.patch -- Add GenericName
Patch0:         %{name}-extra_zaz.desktop.patch
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  Mesa-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
%if 0%{?suse_version} <= 1320
BuildRequires:  ftgl-devel
%else
BuildRequires:  pkgconfig(ftgl)
%endif
Requires:       opengl-games-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Zaz (Zaz ain't Z***) is a game where the player has to get rid of
incoming balls by arranging them in triplets. The idea of the game
is loosely based on games like Luxor, Zuma and Puzzle Bobble.
The twists that make Zaz stand out from other games of this type are
that the balls have to be picked from the path
(insted of being randomly assigned for the player) and that
the player's "vehicle" is also attached to a path which is different
from level to level.
A 3D accelerator is needed for decent gameplay.

%prep
%setup -q
%patch0

# Convert to unix line end
find -name "*.rc" -print0 -or -name "*.cpp" -print0 -or -name "*.h" -print0 | xargs -0 dos2unix

# Correct Permissions
chmod 0644 extra/%{name}.desktop

%build
%configure --docdir=%{_defaultdocdir}/%{name}

# Inject -lvorbis into the Makefile
sed -i -e "/^LIBS\s*=*/s|$| -lvorbis|" Makefile src/Makefile

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Remove useless Documentation
rm -f %{buildroot}%{_docdir}/%{name}/{INSTALL,NEWS}

# symlink OpenGL Wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%changelog
