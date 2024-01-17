#
# spec file for package omnispeak
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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


Name:           omnispeak
Version:        1.1+git20230213
Release:        0
Summary:        An reimplementation of "Commander Keen in Goodbye Galaxy!"
License:        GPL-2.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://davidgow.net/keen/omnispeak.html
#Git-Clone:     https://github.com/sulix/omnispeak.git
Source:         %{name}-%{version}.tar.xz
Source1:        omnispeak-keen4-wrapper.sh
Source2:        omnispeak-keen5-wrapper.sh
Source3:        omnispeak-keen6-wrapper.sh
Patch1:         0001-sd_opl2alsa-Don-t-include-x86-specific-headers.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(sdl2)

%description
Omnispeak is an open-source reimplementation of Commander Keen
episodes 4, 5, and 6. It aims to be a pixel-perfect, bug-for-bug
clone of the original games, and is compatible with savegames
from the DOS version.

Omnispeak also includes several new features, including:
 * Improved graphics scaling and compatibility support.
 * Dramatically improved joystick/gamepad support.
 * QuickLoad and QuickSave support (F5 and F9 by default)
 * Support for real AdLib / OPL2 compatible sound cards
 * Support for the OPL2LPT

NOTE:
To play the Commander Keen games with omnispeak you need the
original game files!

Run
 * omnispeak-keen4
 * omnispeak-keen5
 * omnispeak-keen6
from the directory where the original game files are located.

%prep
%autosetup -p1

%build
%cmake \
  -DVANILLA=OFF \
  -DXDGUSERPATH=OFF \
  -DOMNIPATH=%{_datadir}/omnispeak \
  -DWITH_ALSA=ON \
  -DWITH_IEEE1284=OFF
%cmake_build

%install
install -d %{buildroot}/%{_bindir}
install -m0755 build/omnispeak %{buildroot}/%{_bindir}/omnispeak
install -m0755 %{SOURCE1} %{buildroot}/%{_bindir}/omnispeak-keen4
install -m0755 %{SOURCE2} %{buildroot}/%{_bindir}/omnispeak-keen5
install -m0755 %{SOURCE3} %{buildroot}/%{_bindir}/omnispeak-keen6
install -Dm644 unixicon.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/omnispeak.png
#
install -d %{buildroot}/%{_datadir}/omnispeak/
for keen_ver in keen4 keen5 keen6e15; do
  install -m644 data/$keen_ver/*CK? -t %{buildroot}/%{_datadir}/omnispeak/
done

%files
%license LICENSE
%doc AUTHORS README
%{_bindir}/omnispeak
%{_bindir}/omnispeak-keen4
%{_bindir}/omnispeak-keen5
%{_bindir}/omnispeak-keen6
%{_datadir}/omnispeak
%{_datadir}/icons/hicolor/64x64/apps/omnispeak.png

%changelog
