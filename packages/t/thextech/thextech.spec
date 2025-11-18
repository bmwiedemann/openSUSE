#
# spec file for package thextech
#
# Copyright (c) 2023-2025, Martin Hauke <mardnh@gmx.de>
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           thextech
Version:        1.3.7.1+git20250722
Release:        0
Summary:        A Super Mario Brothers Fan game engine (SMBX)
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://wohlsoft.ru/projects/TheXTech/
#Git-Clone:     https://github.com/Wohlstand/TheXTech
Source:         TheXTech-%{version}.tar.xz
Patch0:         no-rpath.patch
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
Provides:       bundled(AudioCodecs)
Provides:       bundled(DirManager)
Provides:       bundled(FileMapper)
Provides:       bundled(FreeImageLite)
Provides:       bundled(IniProcessor)
Provides:       bundled(LuaJIT)
Provides:       bundled(PGE_File_Formats)
Provides:       bundled(SDL-Mixer-X)
Provides:       bundled(SDL_net)
Provides:       bundled(freetype)
Provides:       bundled(hextech-discord-rpc)
Provides:       bundled(luabind)
Provides:       bundled(luau)
Provides:       bundled(mbediso)

%description
TheXTech is a free and open-source game engine for Mario-like
platforming games. There is a complete and extended source code
port of the Super Mario Bros. X 1.3 game engine (later just "SMBX"),
and its direct unofficial continuation after development halted in
the 2011th year. This engine preserves full compatibility with
levels and episodes made for the original SMBX game, including its
repacks. And it's allowed to create brand-new Levels, Episodes,
and content packs. Unlike the original SMBX game that depends on
Windows and x86, TheXTech can work on many operating systems
(including Linux distros, macOS, xBSD, Android, Haiku, etc.) and
processor architectures (including x86_64, ARM, PowerPC, MIPS, etc.).

Note:
This package contain the runtime engine binary only,
*no game assets included*.

See the following links on how to install game assets:
https://github.com/TheXTech/TheXTech/wiki/Game-assets-packages
https://github.com/TheXTech/TheXTech/wiki/Running-game-assets-on-Linux-or-xBSD

%prep
%autosetup -p1 -n TheXTech-%{version}
sed -i 's/\r$//' changelog.txt README.md

# remove bundled libs
rm -Rfv 3rdparty/{angle-shader-translator}

%build
%cmake \
    -DUSE_SYSTEM_SDL2=ON \
    -DUSE_FREEIMAGE_SYSTEM_LIBS=ON \
    -DTHEXTECH_BUILD_GL_DESKTOP_MODERN=ON \
    -DPGE_SHARED_SDLMIXER=OFF
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/doc/%{name}/{License.TheXTech.txt,ReadMe.txt,changelog.txt}
install -d %{buildroot}%{_datadir}/games/TheXTech

%files
%license LICENSE
%doc changelog.txt README.md
%{_bindir}/thextech
%{_datadir}/games/TheXTech
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
