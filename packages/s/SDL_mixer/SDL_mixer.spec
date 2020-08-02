#
# spec file for package SDL_mixer
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           SDL_mixer
%define lname	libSDL_mixer-1_2-0
Version:        1.2.12
Release:        0
Summary:        SDL sound mixer library
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://libsdl.org/projects/SDL_mixer/release-1.2.html

Source:         http://libsdl.org/projects/SDL_mixer/release/%name-%version.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM: http://hg.libsdl.org/SDL_mixer/rev/56cad6484b04
Patch1:         mikmod1.patch
# PATCH-FIX-UPSTREAM: http://hg.libsdl.org/SDL_mixer/rev/2ebb0d016f27
Patch2:         mikmod2.patch
# PATCH-FIX-UPSTREAM: http://hg.libsdl.org/SDL_mixer/rev/2d713670db9b
Patch3:         double-free-crash.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug) >= 0.8.7
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbis)

%description
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the popular MikMod MOD,
Timidity MIDI, and SMPEG MP3 libraries.

%package -n %lname
Summary:        Simple DirectMedia Layer – Sound mixer library
Group:          System/Libraries
Provides:       SDL_mixer = %version
Obsoletes:      SDL_mixer < %version
# bug437293
%ifarch ppc64
Obsoletes:      SDL_mixer-64bit
%endif

%description -n %lname
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the popular MikMod MOD,
Timidity MIDI, and SMPEG MP3 libraries.

%package -n libSDL_mixer-devel
Summary:        Development files for the SDL sound mixer library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       SDL_mixer-devel = %version
Obsoletes:      SDL_mixer-devel < %version
# bug437293
%ifarch ppc64
Obsoletes:      SDL_mixer-devel-64bit
%endif

%description -n libSDL_mixer-devel
A multi-channel audio mixer. It supports 4 channels of 16-bit stereo
audio, plus a single channel of music, mixed by the popular MikMod MOD,
Timidity MIDI, and SMPEG MP3 libraries.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
# remove unneccessary files from upstream tarball [bnc#508180] to clean up source RPM
rm libmikmod-3.1.12.zip
rm Watcom-OS2.zip
rm -rf VisualC
rm -rf Xcode
rm -rf Xcode-iOS

%build
%configure --disable-music-mod-shared --disable-music-ogg-shared \
	--disable-music-flac-shared --enable-music-mod-modplug \
	--disable-static
make %{?_smp_mflags}

%install
%make_install install-bin
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc README CHANGES COPYING
%_libdir/libSDL_mixer-1*.so.*

%files -n libSDL_mixer-devel
%defattr(-,root,root)
%_bindir/play*
%_includedir/SDL/
%_libdir/libSDL_mixer.so
%_libdir/pkgconfig/SDL_mixer.pc

%changelog
