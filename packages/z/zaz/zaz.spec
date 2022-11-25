#
# spec file for package zaz
#
# Copyright (c) 2022 SUSE LLC
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


Name:           zaz
Version:        1.0.1
Release:        0
Summary:        Puzzle game about arranging balls in triplets
License:        GPL-3.0-or-later
Group:          Amusements/Games/Logic
URL:            https://zaz.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - zaz-extra_zaz.desktop.patch -- Add GenericName
Patch0:         %{name}-extra_zaz.desktop.patch
BuildRequires:  Mesa-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  opengl-games-utils
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
Requires:       opengl-games-utils

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
%make_build

%install
%make_install

# Remove useless Documentation or license (we install manually)
rm -f %{buildroot}%{_docdir}/%{name}/{INSTALL,NEWS,COPYING}
# symlink OpenGL Wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper

%suse_update_desktop_file %{name}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%changelog
