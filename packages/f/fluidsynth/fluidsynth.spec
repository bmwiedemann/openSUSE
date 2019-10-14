#
# spec file for package fluidsynth
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# fix build for older distros and architectures where _fillupdir is
# not yet defined by using the old path as recommended by
# https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros#.25_fillupdir
%if ! %{defined _fillupdir}
 %define _fillupdir /var/adm/fillup-templates
%endif

Name:           fluidsynth
Version:        2.0.7
Release:        0
Summary:        A Real-Time Software Synthesizer That Uses Soundfont(tm)
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Midi
Url:            http://www.fluidsynth.org/
Source:         https://github.com/FluidSynth/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1000:     baselibs.conf
BuildRequires:  cmake >= 3.1.0
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sndfile)
%if 0%{?suse_version}
%{?systemd_requires}
PreReq:         %fillup_prereq
%endif

%description
FluidSynth (formerly IIWU Synth) is a real-time software synthesizer
based on the SoundFont(tm) 2 specifications. It can read MIDI events
from the MIDI input device and render them to the audio device. It
can also play MIDI files.

%package devel
Summary:        Development package for the fluidsynth library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libfluidsynth2 = %{version}
Provides:       libfluidsynth-devel = %{version}

%description devel
This package contains the files needed to compile programs that use the
fluidsynth library.

%package -n libfluidsynth2
Summary:        Library for Fluidsynth
Group:          System/Libraries

%description -n libfluidsynth2
This package contains the shared library for Fluidsynth.

%prep
%setup -q

%build
%cmake \
    -DFLUID_DAEMON_ENV_FILE=%{_fillupdir}/sysconfig.%{name} \
    -Denable-lash=0
make %{?_smp_mflags}

%check
# depending on the distribution being built for, cmake
# may or may not create a 'build' subdirectory
%cmake
# cannot call ctest as the unit tests need to be compiled yet
make check

%install
%if 0%{?suse_version}
%cmake_install
%else
%cmake
DESTDIR=$RPM_BUILD_ROOT make install
%endif

%if 0%{?suse_version}

# manually install systemd service files
install -Dm 644 build/fluidsynth.conf %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dm 644 build/fluidsynth.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%endif

%post -n libfluidsynth2 -p /sbin/ldconfig
%postun -n libfluidsynth2 -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README.md THANKS TODO
%{_mandir}/man?/*
%{_bindir}/*
%if 0%{?suse_version}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%endif

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files -n libfluidsynth2
%{_libdir}/lib*.so.*

%changelog
