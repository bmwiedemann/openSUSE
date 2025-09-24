#
# spec file for package apotris
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           apotris
Version:        4.1.0
Release:        0
Summary:        A block stacking puzzle game
License:        AGPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://apotris.com/
#Git-Clone:     https://gitea.com/akouzoukos/apotris.git
Source:         %{name}-%{version}.tar.xz
Source1:        apotris.sh
Patch0:         apotris-fix-tileenngine.patch
Patch1:         apotris-install.patch
Patch2:         apotris-use-system-libs.patch
Patch3:         soloud-use-system-libs.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  xxd
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(SoLoud)
Provides:       bundled(Tileengine)

%description
Apotris is a block stacking game in the style of Tetris.
It features satisfying graphics, responsive controls and a large amount
of customization so that you can tailor the game to your preferences!
There are 11 game-modes to explore, with various options to keep
yourself entertained (or challenged).

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -Dm 0755 %{SOURCE1} %{buildroot}/%{_bindir}/apotris
install -Dm 0644 dist/Apotris-switch.jpg %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/apotris.png
%suse_update_desktop_file -c %{name} 'Apotris' 'Apotris block stacking puzzle game' %{name} %{name} Game Amusement

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/apotris
%dir %{_prefix}/lib/apotris/
%{_prefix}/lib/apotris/Apotris
%dir %{_datadir}/apotris/
%{_datadir}/apotris/assets/
%{_datadir}/applications/apotris.desktop
%{_datadir}/icons/hicolor/256x256/apps/apotris.png

%changelog
