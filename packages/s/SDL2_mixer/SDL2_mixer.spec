#
# spec file for package SDL2_mixer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           SDL2_mixer
%define lname	libSDL2_mixer-2_0-0
Version:        2.6.3
Release:        0
Summary:        SDL2 sound mixer library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://libsdl.org/projects/SDL_mixer/

#Git-Clone:     https://github.com/libsdl-org/SDL_mixer
Source:         https://github.com/libsdl-org/SDL_mixer/releases/download/release-%version/SDL2_mixer-%version.tar.gz
Source2:        https://github.com/libsdl-org/SDL_mixer/releases/download/release-%version/SDL2_mixer-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  SDL2-devel >= 2.24
BuildRequires:  dos2unix
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
Suggests:       timidity

%description
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%package -n %lname
Summary:        Simple DirectMedia Layer 2 – Sound mixer library
Group:          System/Libraries
Provides:       SDL2_mixer = %version-%release

%description -n %lname
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%package devel
Summary:        Development files for the SDL2 sound mixer library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Obsoletes:      libSDL2_mixer-devel < %version-%release
Provides:       libSDL2_mixer-devel = %version-%release

%description devel
A multi-channel audio mixer. It supports 4 channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%prep
%autosetup -p1
dos2unix *.txt
rm -rf external

%build
# --disable-*-shared: Link, rather than dlopen
#
%configure \
	--disable-music-ogg-stb --enable-music-ogg-vorbis \
	--disable-music-flac-drflac --enable-music-flac-libflac \
	--disable-music-mp3-drmp3 --enable-music-mp3-mpg123 \
	--disable-music-mod-modplug --enable-music-mod-xmp \
	--disable-music-mod-xmp-shared \
	--disable-music-midi-fluidsynth-shared \
	--disable-music-ogg-shared \
	--disable-music-flac-shared \
	--enable-music-mp3-mpg123-shared \
	--disable-static
%make_build

%install
%make_install install-bin
rm -f "%buildroot/%_libdir"/*.la
# We have these debug tools in SDL_mixer-devel already
rm -f "%buildroot/%_bindir"/play*

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE.txt
%doc CHANGES.txt README.txt
%_libdir/libSDL2_mixer-2*.so.*

%files devel
%_includedir/SDL2/
%_libdir/libSDL2_mixer.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/

%changelog
