#
# spec file for package libadlmidi
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2019-2020, Martin Hauke <mardnh@gmx.de>
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
%define libname libADLMIDI
Name:           libadlmidi
%define hyphver 1.5.0.1-1
Version:        1.5.0.1.1
Release:        0
Summary:        A software MIDI synthesizer library with OPL3 emulation
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Languages/C and C++
URL:            https://github.com/Wohlstand/%{libname}
Source:         %{URL}/archive/v%{hyphver}.tar.gz#/%{libname}-%{hyphver}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
A software MIDI synthesizer library with OPL3 emulation (FM synthesis).
The library is based on the ADLMIDI, a multiplatform MIDI player with OPL3 emulation:
https://bisqwit.iki.fi/source/adlmidi.html

%package -n %{libname}%{sover}
Summary:        A Software MIDI Synthesizer library with OPL3 (YMF262) emulator
Group:          System/Libraries

%description -n %{libname}%{sover}
A software MIDI synthesizer library with OPL3 emulation (FM synthesis).
The library is based on the ADLMIDI, a multiplatform MIDI player with OPL3 emulation:
https://bisqwit.iki.fi/source/adlmidi.html

%package -n adlmidi-tools
Summary:        A MIDI player with OPL3 emulation
Group:          Productivity/Multimedia/Sound/Players

%description -n adlmidi-tools
AdlMIDI is a commandline program that plays MIDI files using software
OPL3 emulation (FM synthesis).

%package devel
Summary:        Header files for libADLMIDI
Group:          Development/Libraries/C and C++
Requires:       libADLMIDI%{sover} = %{version}

%description devel
Development and header files for libADLMIDI.

%prep
%setup -q -n %{libname}-%{hyphver}

%build
%cmake \
  -DlibADLMIDI_STATIC=OFF \
  -DlibADLMIDI_SHARED=ON \
  -DlibADLMIDI_SHARED=ON \
  -DWITH_MIDIPLAY=ON \
  -DWITH_CPP_EXTRAS=ON \
  -DWITH_ADLMIDI2=ON
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc/

%post   -n libADLMIDI%{sover} -p /sbin/ldconfig
%postun -n libADLMIDI%{sover} -p /sbin/ldconfig

%files -n %{libname}%{sover}
%license LICENSE LICENSE.GPL-3.txt LICENSE.LGPL-2.1.txt
%{_libdir}/%{libname}.so.%{sover}*

%files -n adlmidi-tools
%{_bindir}/adlmidi2
%{_bindir}/adlmidiplay

%files devel
%doc AUTHORS README.md
%{_includedir}/adlmidi.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
