#
# spec file for package wildmidi
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2007-2016 Hans de Goede <j.w.r.degoede@hhs.nl>
# Copyright (c) 2016 Pauline Emily <vilene@posteo.net>
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


%define soname  libWildMidi2
Name:           wildmidi
Version:        0.4.5
Release:        0
Summary:        Softsynth midi player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://www.mindwerks.net/projects/wildmidi
Source:         https://github.com/Mindwerks/wildmidi/archive/%{name}-%{version}.tar.gz
Source1:        %{name}.cfg
BuildRequires:  cmake >= 3.1
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openal)
Requires:       %{soname} = %{version}

%description
WildMidi is a software midi player which has a core softsynth library that can
be used with other applications.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     %{soname}
Summary:        WildMidi Midi Wavetable Synth Lib
License:        LGPL-3.0-or-later
Group:          System/Libraries
Requires:       timidity

%description -n %{soname}
This package contains the WildMidi core softsynth library. The library is
designed to process a midi file and stream out the stereo audio data
through a buffer which an external program can then process further.

%prep
%setup -q -n %{name}-%{name}-%{version}
dos2unix -c ascii COPYING

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

install -d %{buildroot}%{_sysconfdir}/wildmidi
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/wildmidi

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files
%license COPYING docs/license/GPLv3.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files devel
%{_includedir}/%{name}_lib.h
%{_libdir}/libWildMidi.so
%{_libdir}/pkgconfig/wildmidi.pc
%{_libdir}/cmake/WildMidi
%{_mandir}/man3/WildMidi_*.3%{?ext_man}

%files -n %{soname}
%license docs/license/LGPLv3.txt
%{_libdir}/libWildMidi.so.*
%{_mandir}/man5/%{name}.cfg.5%{?ext_man}
%config(noreplace) %{_sysconfdir}/wildmidi

%changelog
