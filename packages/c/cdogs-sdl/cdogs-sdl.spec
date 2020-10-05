#
# spec file for package cdogs-sdl
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cdogs-sdl
Version:        0.9.1
Release:        0
Summary:        Classic overhead run-and-gun game
License:        GPL-2.0-only AND BSD-2-Clause AND CC-BY-3.0 AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Shoot
URL:            https://cxong.github.io/cdogs-sdl
Source:         https://github.com/cxong/cdogs-sdl/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE cdogs-sdl-fix-desktop-and-appdata.patch mardnh@gmx.de -- Fix desktop/appdata filenames.
Patch0:         cdogs-sdl-fix-desktop-and-appdata.patch
# PATCH-FIX-UPSTREAM nanopb.patch -- https://github.com/nanopb/nanopb/issues/521
Patch1:         nanopb.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  dos2unix
BuildRequires:  enet-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sdl2)

%description
C-Dogs SDL is a classic overhead run-and-gun game, supporting up to
4 players in co-op and deathmatch modes. Customize your player, choose
from up to 11 weapons, and try over 100 user-created campaigns. Have fun!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i 's|env python|python3|' src/proto/nanopb/generator/{protoc,nanopb_generator.py}

# use system enet
rm -rf src/cdogs/enet

#dos2unix doc/original_readme.txt

# disable -Werror (aborts build on mere warnings)
#sed 's| -Werror||' -i CMakeLists.txt

%build
%cmake -DCDOGS_DATA_DIR=%{_datadir}/%{name}/ -DUSE_SHARED_ENET=ON
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}

%files
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
