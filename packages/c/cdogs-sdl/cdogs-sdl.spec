#
# spec file for package cdogs-sdl
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


Name:           cdogs-sdl
Version:        2.1.0
Release:        0
Summary:        Classic overhead run-and-gun game
License:        BSD-2-Clause AND GPL-2.0-only AND CC-BY-3.0 AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Shoot
URL:            https://cxong.github.io/cdogs-sdl
Source:         https://github.com/cxong/cdogs-sdl/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        cdogs-sdl.rpmlintrc
Patch0:         fix-build.patch
Patch1:         fix-env-script-interpreter.patch
BuildRequires:  cmake >= 3.12
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
%autosetup -p1
# use system enet
rm -rf src/cdogs/enet

%build
%cmake \
    -DCDOGS_BIN_DIR=%{_bindir}/ \
    -DCDOGS_DATA_DIR=%{_datadir}/%{name}/ \
    -DUSE_SHARED_ENET=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/cdogs-sdl/README.md
%fdupes %{buildroot}%{_datadir}
find %{buildroot}%{_datadir}/cdogs-sdl/ -name '*.sh' | xargs chmod a+x

%check
%ctest

%files
%license COPYING
%doc README.md
%{_datadir}/applications/*.desktop
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.appdata.xml

%changelog
