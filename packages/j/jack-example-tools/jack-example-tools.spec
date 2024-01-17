#
# spec file for package jack-example-tools
#
# Copyright (c) 2022 SUSE LLC
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


Name:           jack-example-tools
Version:        1
Release:        0
Summary:        Official examples and tools from the JACK project
License:        GPL-2.0
Group:          System/Sound Daemons
URL:            https://jackaudio.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         fix-readline-support-leap.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jack
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack) >= 1.9.20
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
# In order to have a transparent transition to the splitted packages
Provides:       jack:/usr/bin/jack_connect

%description
JACK is system for handling real-time, low latency audio
(and MIDI). It runs on GNU/Linux, Solaris, FreeBSD, OS X and
Windows (and can be ported to other POSIX-conformant
platforms). It can connect a number of different
applications to an audio device, as well as allowing them to
share audio between themselves. 

This package contains the the official JACK example clients
and tools.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%meson -Dzalsa=disabled
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}%{_docdir}

%files
%doc CHANGELOG.md README*
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/jack/jack_inprocess.so
%{_libdir}/jack/jack_internal_metro.so
%{_libdir}/jack/jack_intime.so


%changelog
