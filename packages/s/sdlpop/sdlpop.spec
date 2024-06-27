#
# spec file for package sdlpop
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


Name:           sdlpop
Version:        1.23
Release:        0
Summary:        An open-source port of Prince of Persia
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            https://www.popot.org/get_the_games.php?game=SDLPoP
Source0:        https://github.com/NagyD/SDLPoP/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        sdlpop.wrapper
Patch0:         sdlpop-fix-sdl2-includes.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(sdl2)
ExcludeArch:    s390x

%description
SDLPoP is an open-source port of Prince of Persia 1,
that runs natively under Linux. It is based on the DOS
version of the game, and uses SDL.

Run the prince executable in a path were the original
game data files are located.

%prep
%autosetup -p1 -n SDLPoP-%{version}
sed -i 's/\r$//' doc/*.txt

%build
cd src
%make_build

%install
install -d %{buildroot}/%{_bindir}
install -Dm0755 prince %{buildroot}/%{_bindir}
install -Dm0644 data/icon.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d %{buildroot}/%{_datadir}/%{name}
install SDLPoP.ini %{buildroot}/%{_datadir}/%{name}
mv data/ %{buildroot}/%{_datadir}/%{name}
%suse_update_desktop_file -c %{name} %{name} "Platformer" %{name} %{name} Game ActionGame
%fdupes %{buildroot}/%{_datadir}

# Install Wrapper
install -Dm0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
ln -s %{_bindir}/prince %{buildroot}%{_datadir}/%{name}

%files
%doc README.md doc/tiles.md doc/mod.ini doc/ChangeLog.txt
%license COPYING
%attr(0755,root,root) %{_bindir}/sdlpop
%{_bindir}/prince
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/sdlpop.png
%{_datadir}/applications/sdlpop.desktop

%changelog
