#
# spec file for package retroarch
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


Name:           retroarch
Version:        1.8.9
Release:        0
Summary:        Emulator frontend
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.gz
Patch0:         retroarch-config.patch

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  p7zip
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
%if ( 0%{?suse_version} || 0%{?leap_version} )
BuildRequires:  update-desktop-files
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif

# Shared data
Recommends:     retroarch-joypad-autoconfig
Recommends:     retroarch-assets
Recommends:     libretro-core-info
Recommends:     libretro-database

# Emulation cores

# Arcade/MAME
# MAME 2003 Plus has the best performance, supporting most games before 2000
Recommends:     libretro-mame2003-plus

# Atari 2600
Recommends:     libretro-stella
# Atari 5200
Recommends:     libretro-atari800
# Atari 7800
Recommends:     libretro-prosystem
# Atari Jaguar
Recommends:     libretro-virtualjaguar
# Atari Lynx
Recommends:     libretro-handy

# Nintendo Entertainment System (NES)
Recommends:     libretro-nestopia
# Super Nintendo Entertainment System (SNES)
Recommends:     libretro-bsnes
# Nintendo 64 (N64)
Recommends:     libretro-parallel-n64
# GameCube (GC) and Wii (not fully working yet)
Recommends:     libretro-dolphin

# Nintendo Game Boy Color (GBC)
Recommends:     libretro-gambatte
# Nintendo Game Boy Advance (GBA)
Recommends:     libretro-mgba
# Nintendo DS (NDS)
Recommends:     libretro-desmume
# Nintendo 3DS (3DS)
Recommends:     libretro-citra

# Sega Genesis/Mega Drive (MD)
Recommends:     libretro-blastem
# Sega Saturn (SS)
Recommends:     libretro-yabause
# Sega Dreamcast (DC)
Recommends:     libretro-flycast

# Sony PlayStation (PSX)
Recommends:     libretro-pcsx-rearmed
# Sony PlayStation 2 (PS2)
Recommends:     libretro-play
# Sony PlayStation Portable (PSP)
Recommends:     libretro-ppsspp

# Amstrad
Recommends:     libretro-crocods
# Amstrad CPC
Recommends:     libretro-cap32
# Bandai WonderSwan
Recommends:     libretro-beetle-wswan
# Fairchild ChannelF
Recommends:     libretro-freechaf
# Game & Watch
Recommends:     libretro-gw
# Mattel Intellivision
Recommends:     libretro-freeintv
# MS DOS
Recommends:     libretro-dosbox
# MSX
Recommends:     libretro-bluemsx
# Neo Geo Pocket
Recommends:     libretro-beetle-ngp
# PC Engine/TurboGrafx-16
Recommends:     libretro-beetle-pce-fast
# ZX 81
Recommends:     libretro-81
# ZX Spectrum
Recommends:     libretro-fuse

# Game and game engine cores

Recommends:     libretro-2048
Recommends:     libretro-3dengine
Recommends:     libretro-chailove
Recommends:     libretro-craft
Recommends:     libretro-easyrpg
Recommends:     libretro-ffmpeg
Recommends:     libretro-gme

%description
RetroArch is a modular multi-system emulator system that is designed to be
fast, lightweight, and portable. It has features few other emulators frontends
have, such as real-time rewinding and game-aware shading.

%prep
%setup -q

%autopatch -p1

# Change /usr/lib/ to /usr/lib64/ on 64-bit platform
sed -i s~/usr/lib/~%{_libdir}/~g retroarch.cfg
# Change /usr/bin/env python to /usr/bin/python
sed -i s~%{_bindir}/env\ python~%{_bindir}/python~g tools/cg2glsl.py

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
./configure --prefix=%{_prefix} \
    --enable-materialui \
    --enable-xmb \
    --enable-sdl2 \
    --enable-libusb \
    --enable-udev \
    --enable-threads \
    --enable-thread_storage \
    --enable-ffmpeg \
    --enable-ssa \
    --enable-dylib \
    --enable-networking \
    --enable-networkgamepad \
    --enable-opengl \
    --enable-x11 \
    --enable-xinerama\
    --enable-kms \
    --enable-wayland \
    --enable-egl \
    --enable-zlib \
    --enable-alsa \
    --enable-al \
    --enable-jack \
    --enable-pulse \
    --enable-freetype \
    --enable-xvideo \
    --enable-v4l2 \
    --enable-qt \
    --enable-dbus \
%ifarch x86
    --enable-sse \
%endif
%if ( 0%{?suse_version} || 0%{?leap_version} )
    --enable-vulkan \
%endif
    --enable-7zip \
    --enable-mmap
make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_bindir}/%{name}-cg2glsl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man?/%{name}.?*
%{_mandir}/man?/%{name}-cg2glsl.?*
%{_datadir}/doc/%{name}

%changelog
