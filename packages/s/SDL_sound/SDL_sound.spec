#
# spec file for package SDL_sound
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           SDL_sound
%define lname	libSDL_sound-1_0-1
Version:        1.0.3
Release:        0
Summary:        Sound Sample Library for SDL (Simple DirectMedia Layer)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://icculus.org/SDL_sound/  

Source:         %name-%version-nompglib.tar.bz2
Source2:        baselibs.conf
Patch0:         %name-%version-nompglib.patch
BuildRequires:  flac-devel
BuildRequires:  libSDL-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  speex-devel
BuildRequires:  pkgconfig(libmodplug)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%package -n %lname
Summary:        Sound Sample Library for SDL (Simple DirectMedia Layer)
Group:          System/Libraries
Provides:       SDL_sound = %version
Obsoletes:      SDL_sound <= %version

%description -n %lname
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%package -n libSDL_sound-devel
Summary:        Development files for the SDL sound sample library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       pkgconfig(sdl)
Provides:       SDL_sound-devel = %version
Obsoletes:      SDL_sound-devel <= %version

%description -n libSDL_sound-devel
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as wav, ogg mp3 and midi. SDL_sound can just
play a file or alternatively decode a file and hand back a single
pointer to the waveform. SDL_sound also can handle channel conversion
on-the-fly and behind-the-scenes.

%prep
%setup -q
%patch0

%build
%configure \
    --disable-static \
    --disable-sdltest \
    --disable-smpeg \
    --disable-mpglib
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n libSDL_sound-1_0-1
%defattr(-,root,root)
%doc CHANGELOG COPYING CREDITS README TODO
%_libdir/lib*.so.*

%files -n libSDL_sound-devel
%defattr(-,root,root)
%_bindir/playsound*
%_includedir/SDL/
%_libdir/lib*.so

%changelog
