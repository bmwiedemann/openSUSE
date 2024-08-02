#
# spec file for package ltris
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ltris
Version:        1.3.2
Release:        0
Summary:        Tetris Clone with Multiplayer and CPU Opponents
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
URL:            http://lgames.sourceforge.net/index.php?project=LTris
Source:         https://sourceforge.net/projects/lgames/files/ltris/ltris-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         ltris-no_system_wide_hiscore_file.patch
# PATCH-FIX-UPSTREAM ltris-gamepad-pause-exit.patch badshah400@gmail.com -- Interpret pause button from gamepad (https://sourceforge.net/p/lgames/patches/35/)
Patch1:         ltris-gamepad-pause-exit.patch
BuildRequires:  SDL-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_mixer)

%description
LTris is a very polished Tetris clone. It is highly configurable due to
its menu. It offers the well-known game type Classic, a funny game type
Figures (a new figure each level, suddenly appearing tiles and lines),
and multiplayer with up to three players either human or CPU
controlled.

%prep
%autosetup -p1
# we patch both Makefile.am and Makefile.in; touch Makefile.in here again
# to make sure configure won't run autoreconf (which it does if the .am file
# is newer than the .in file):
touch src/Makefile.in

%build
export CFLAGS="%{optflags} -fPIC -fPIE"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-pie"
%configure \
  --datadir=%{_datadir}/games \
  --localstatedir=%{_localstatedir}/games
%make_build

%install
%make_install
install -D -m 0644 icons/ltris48.xpm %{buildroot}%{_datadir}/pixmaps/ltris.xpm
mv %{buildroot}%{_datadir}/games/locale %{buildroot}%{_datadir}/locale
rm -rf "%{buildroot}%{_datadir}/games/applications"
rm -rf "%{buildroot}%{_datadir}/games/icons"
%fdupes -s "%{buildroot}%{_datadir}/games/ltris"
%suse_update_desktop_file -i %{name} Game ArcadeGame
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/ltris
%{_datadir}/games/ltris/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ltris.xpm

%changelog
