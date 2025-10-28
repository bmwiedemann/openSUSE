#
# spec file for package libopnmidi
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
%define libname libOPNMIDI
Name:           libopnmidi
Version:        1.6.1
Release:        0
Summary:        A software MIDI synthesizer library with OPN2 (YM2612) emulation
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Languages/C and C++
URL:            https://github.com/Wohlstand/%{libname}
Source:         https://github.com/Wohlstand/libopnmidi/archive/refs/tags/v%{version}.tar.gz#/%{libname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
A software MIDI synthesizer library with OPN2 (YM2612) and
OPNA (YM2608) emulation.

%package -n %{libname}%{sover}
Summary:        A software MIDI synthesizer library with OPN2 emulation
Group:          System/Libraries

%description -n %{libname}%{sover}
A software MIDI synthesizer library with OPN2 (YM2612) and
OPNA (YM2608) emulation.

%package -n opnmidi-tools
Summary:        A MIDI player with OPN2 emulation
Group:          Productivity/Multimedia/Sound/Players

%description -n opnmidi-tools
OpnMIDI is a commandline program that plays MIDI files using software
OPN2 emulation.

%package devel
Summary:        Header files for libOPNMIDI
Group:          Development/Libraries/C and C++
Requires:       libOPNMIDI%{sover} = %{version}

%description devel
Development and header files for libOPNMIDI.

%prep
%autosetup -p1 -n %{libname}-%{version}

%build
%cmake \
  -DlibOPNMIDI_STATIC=OFF \
  -DlibOPNMIDI_SHARED=ON \
  -DWITH_MIDIPLAY=ON \
  -DWITH_CPP_EXTRAS=ON
%cmake_build

%install
%cmake_install
rm -Rv %{buildroot}%{_datadir}/doc/

%ldconfig_scriptlets -n %{libname}%{sover}

%files -n %{libname}%{sover}
%license LICENSE LICENSE.GPL-3.txt LICENSE.LGPL-2.1.txt
%{_libdir}/%{libname}.so.%{sover}*

%files -n opnmidi-tools
%{_bindir}/opnmidiplay
%dir %{_datadir}/sounds/wopn
%{_datadir}/sounds/wopn/xg.wopn

%files devel
%doc AUTHORS README.md
%{_includedir}/opnmidi.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/cmake/libOPNMIDI

%changelog
