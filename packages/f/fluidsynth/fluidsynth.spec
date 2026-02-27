#
# spec file for package fluidsynth
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define gcem_hash 012ae73c6d0a2cb09ffe86475f5c6fba3926e200

%define sover   3
Name:           fluidsynth
Version:        2.5.3
Release:        0
Summary:        A Real-Time Software Synthesizer That Uses Soundfont(tm)
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://www.fluidsynth.org/
#Git-Clone:     https://github.com/FluidSynth/fluidsynth.git
Source0:        https://github.com/FluidSynth/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        https://github.com/kthohr/gcem/archive/%{gcem_hash}.tar.gz#/gcem-%{gcem_hash}.tar.gz
Source1000:     baselibs.conf
BuildRequires:  cmake >= 3.13.0
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndfile)
Recommends:     fluid-soundfont-gm
%{?systemd_ordering}

%description
FluidSynth (formerly IIWU Synth) is a real-time software synthesizer
based on the SoundFont(tm) 2 specifications. It can read MIDI events
from the MIDI input device and render them to the audio device. It
can also play MIDI files.

%package devel
Summary:        Development package for the fluidsynth library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libfluidsynth%{sover} = %{version}
Provides:       libfluidsynth-devel = %{version}

%description devel
This package contains the files needed to compile programs that use the
fluidsynth library.

%package -n libfluidsynth%{sover}
Summary:        Library for Fluidsynth
Group:          System/Libraries

%description -n libfluidsynth%{sover}
This package contains the shared library for Fluidsynth.

%prep
%autosetup -p1
tar -C gcem --strip-components=1 -x -f %{SOURCE2}

%build
%cmake \
    -Dosal=cpp11 \
    -Denable-dbus=0 \
    -DFLUID_DAEMON_ENV_FILE=%{_fillupdir}/sysconfig.%{name} \
    -DDEFAULT_SOUNDFONT=/usr/share/sounds/sf2/FluidR3_GM.sf2
%cmake_build

# FIXME: check on s390x seems broken, disable checksing for now
%ifnarch s390x
%check
# depending on the distribution being built for, cmake
# may or may not create a 'build' subdirectory
%cmake
# cannot call ctest as the unit tests need to be compiled yet
%cmake_build check
%endif

%install
%cmake_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm0644 build/fluidsynth.service %{buildroot}%{_userunitdir}/%{name}.service
mkdir %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%systemd_user_pre %{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%ldconfig_scriptlets -n libfluidsynth%{sover}

%files
%license LICENSE
%doc AUTHORS ChangeLog.old README.md THANKS TODO
%{_bindir}/%{name}
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_sbindir}/rc%{name}
%{_userunitdir}/%{name}.service

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/%{name}/
%{_libdir}/cmake/%{name}/*.cmake

%files -n libfluidsynth%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
