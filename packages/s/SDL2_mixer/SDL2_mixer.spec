#
# spec file for package SDL2_mixer
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


Name:           SDL2_mixer
%define lname	libSDL2_mixer-2_0-0
Version:        2.0.4
Release:        0
Summary:        SDL2 sound mixer library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://libsdl.org/projects/SDL_mixer/

#Hg-Clone:	http://hg.libsdl.org/SDL_mixer/
Source:         http://libsdl.org/projects/SDL_mixer/release/%name-%version.tar.gz
Source1:        baselibs.conf
BuildRequires:  dos2unix
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug) >= 0.8.8
BuildRequires:  pkgconfig(opusfile)
%if !(0%{?sle_version} == 120200 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(libmpg123)
%endif
BuildRequires:  pkgconfig(sdl2)
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

%package -n libSDL2_mixer-devel
Summary:        Development files for the SDL2 sound mixer library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       SDL2_mixer-devel = %version-%release

%description -n libSDL2_mixer-devel
A multi-channel audio mixer. It supports 4 channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%prep
%autosetup -p1
dos2unix *.txt
rm -rf external

%build
%configure \
	--disable-music-mod-modplug-shared \
	--disable-music-mod-mikmod-shared \
	--disable-music-midi-fluidsynth-shared \
	--disable-music-ogg-shared \
	--disable-music-flac-shared \
%if 0%{?sle_version} == 120200 && 0%{?is_opensuse}
	--enable-music-mp3-mpg123-shared \
%else
	--disable-music-mp3-mpg123-shared \
%endif
	--disable-static
make %{?_smp_mflags}

%install
%make_install install-bin
rm -f "%buildroot/%_libdir"/*.la
# We have these debug tools in SDL_mixer-devel already
rm -f "%buildroot/%_bindir"/play*

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING.txt
%doc CHANGES.txt README.txt
%_libdir/libSDL2_mixer-2*.so.*

%files -n libSDL2_mixer-devel
%_includedir/SDL2/
%_libdir/libSDL2_mixer.so
%_libdir/pkgconfig/SDL2_mixer.pc

%changelog
