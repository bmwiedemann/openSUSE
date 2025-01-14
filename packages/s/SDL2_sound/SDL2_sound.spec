#
# spec file for package SDL2_sound
#
# Copyright (c) 2025 SUSE LLC
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


Name:           SDL2_sound
%define lname	libSDL2_sound2
Version:        2.0.4
Release:        0
Summary:        Sound Sample Library for SDL (Simple DirectMedia Layer)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://icculus.org/SDL_sound/

Source:         https://github.com/icculus/SDL_sound/archive/refs/tags/v%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig(sdl2)
Provides:       bundled(dr_flac) = 0.12.42
Provides:       bundled(dr_mp3) = 0.6.38
Provides:       bundled(libmodplug)
Provides:       bundled(stb_vorbis) = 1.22

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%package -n %lname
Summary:        Sound Sample Library for SDL (Simple DirectMedia Layer)
Group:          System/Libraries

%description -n %lname
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%package devel
Summary:        Development files for the SDL sound sample library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       pkgconfig(sdl2)
Conflicts:      SDL_sound-devel

%description devel
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%prep
%autosetup -n SDL_sound-%version -p1

%build
%cmake -DSDLSOUND_BUILD_STATIC:BOOL=OFF
%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE.txt
%_libdir/lib*.so.*

%files devel
%_bindir/playsound*
%_includedir/SDL2/
%_libdir/cmake/
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
