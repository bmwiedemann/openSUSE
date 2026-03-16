#
# spec file for package SDL3_mixer
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover	0
Name:           SDL3_mixer
Version:        3.2.0
Release:        0
Summary:        SDL3 sound mixer library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://wiki.libsdl.org/SDL3_mixer
#Git-Clone:     https://github.com/libsdl-org/SDL_mixer
Source:         https://github.com/libsdl-org/SDL_mixer/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Source2:        https://github.com/libsdl-org/SDL_mixer/releases/download/release-%{version}/%{name}-%{version}.tar.gz.sig
# https://www.libsdl.org/signing-keys.php
Source3:        %{name}.keyring
BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig
BuildRequires:  cmake(SDL3) >= 3.4.0
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth) >= 2.2.0
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)

%description
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%package -n lib%{name}%{sover}
Summary:        Simple DirectMedia Layer 3 – Sound mixer library
Group:          System/Libraries
Provides:       SDL3_mixer = %{version}-%{release}

%description -n lib%{name}%{sover}
A multichannel audio mixer. It supports four channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%package devel
Summary:        Development files for the SDL3 sound mixer library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
A multi-channel audio mixer. It supports 4 channels of 16-bit stereo
audio, plus a single channel of music, mixed by the MikMod MOD,
Timidity MIDI, and mpg123 MP3 libraries.

%prep
%autosetup -p1

%build
%cmake \
	-DSDLMIXER_STRICT:BOOL=ON \
	-DSDLMIXER_WERROR:BOOL=ON \
	-DSDLMIXER_INSTALL_MAN:BOOL=ON \
	-DSDLMIXER_EXAMPLES_INSTALL:BOOL=OFF \
	-DSDLMIXER_TESTS_INSTALL:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/licenses/SDL3_mixer/LICENSE.txt

%check
%ctest

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license LICENSE.txt
%{_libdir}/libSDL3_mixer.so.%{sover}{,.*}

%files devel
%license LICENSE.txt
%{_includedir}/SDL3_mixer
%{_libdir}/pkgconfig/sdl3-mixer.pc
%{_libdir}/cmake/SDL3_mixer
%{_libdir}/libSDL3_mixer.so
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man3/*.3type%{?ext_man}

%changelog
