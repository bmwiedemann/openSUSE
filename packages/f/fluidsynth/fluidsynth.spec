#
# spec file for package fluidsynth
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


%define sover   2
Name:           fluidsynth
Version:        2.1.5
Release:        0
Summary:        A Real-Time Software Synthesizer That Uses Soundfont(tm)
License:        LGPL-2.1-or-later
URL:            http://www.fluidsynth.org
Source0:        https://github.com/FluidSynth/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.service
Source1000:     baselibs.conf
BuildRequires:  cmake >= 3.1.0
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libinstpatch-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
Requires:       fluid-soundfont-gm
Requires(pre):  %fillup_prereq
Requires(pre):  group(audio)
Requires(pre):  shadow
%{?systemd_requires}

%description
FluidSynth (formerly IIWU Synth) is a real-time software synthesizer
based on the SoundFont(tm) 2 specifications. It can read MIDI events
from the MIDI input device and render them to the audio device. It
can also play MIDI files.

%package devel
Summary:        Development package for the fluidsynth library
Requires:       glibc-devel
Requires:       libfluidsynth%{sover} = %{version}
Provides:       libfluidsynth-devel = %{version}

%description devel
This package contains the files needed to compile programs that use the
fluidsynth library.

%package -n libfluidsynth%{sover}
Summary:        Library for Fluidsynth

%description -n libfluidsynth%{sover}
This package contains the shared library for Fluidsynth.

%prep
%autosetup

%build
%cmake \
    -DFLUID_DAEMON_ENV_FILE=%{_fillupdir}/sysconfig.%{name} \
    -Denable-lash=0
%make_jobs

%check
# depending on the distribution being built for, cmake
# may or may not create a 'build' subdirectory
%cmake
# cannot call ctest as the unit tests need to be compiled yet
%make_build check

%install
%cmake_install
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
mkdir %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
getent passwd %{name} >/dev/null || useradd -rc 'FluidSynth GM daemon' -s /bin/false -d %{_localstatedir}/lib/%{name} -g audio %{name}
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post -n libfluidsynth%{sover} -p /sbin/ldconfig
%postun -n libfluidsynth%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md THANKS TODO
%dir %attr(-,%{name},audio) %{_localstatedir}/lib/%{name}
%{_bindir}/%{name}
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n libfluidsynth%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
