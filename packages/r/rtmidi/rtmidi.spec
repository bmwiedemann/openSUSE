#
# spec file for package rtmidi
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Packman Team <packman@links2linux.de>
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


%define sover   7
Name:           rtmidi
Version:        6.0.0
Release:        0
Summary:        C++ library for realtime MIDI input/ouput
License:        MIT
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:        https://www.music.mcgill.ca/~gary/rtmidi/release/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pkgconfig.patch avvissu@yandex.ru
Patch0:         rtmidi-6.0.0-pkgconfig.patch
# PATCH-FIX-OPENSUSE set proper .cmake files path, lower cmake version for Leap (3.24 is required for Android)
Patch1:         rtmidi-cmake.patch
# PATCH-FIX-UPSTREAM ALSA: Avoid listing ports that are usually from 3rd.party
Patch2:         ALSA-Avoid-listing-ports-that-are-usually-from-3rd-party.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
RtMidi is a set of C++ classes (RtMidiIn, RtMidiOut and API-specific
classes) that provides a common API (Application Programming Interface) for
realtime MIDI input/output across ALSA & JACK.

%package -n     lib%{name}%{sover}
Summary:        C++ library for realtime MIDI input/ouput
Group:          System/Libraries

%description -n lib%{name}%{sover}
RtMidi is a set of C++ classes (RtMidiIn, RtMidiOut and API-specific
classes) that provides a common API (Application Programming Interface) for
realtime MIDI input/output across ALSA & JACK.

This package provides the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(jack)

%description    devel
C++ library for realtime MIDI input/ouput.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q
%autopatch -p1

%build

# generate rtmidi-config for compatibility
%configure --disable-static \
    --with-jack \
    --with-alsa

%cmake
%cmake_build

%install
%cmake_install
install -Dm0755 %{name}-config %{buildroot}%{_bindir}/%{name}-config
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%license README.md
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%changelog
