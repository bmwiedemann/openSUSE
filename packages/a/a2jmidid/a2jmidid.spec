#
# spec file for package a2jmidid
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Michael Csida <krysanto@gmail.com>
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


Name:           a2jmidid
Version:        9
Release:        0
Summary:        A modular multi-system emulator system
License:        GPL-2.0-or-later
URL:            https://github.com/linuxaudio/a2jmidid
Source0:        https://github.com/linuxaudio/a2jmidid/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(jack)

%description
a2jmidid is a daemon for exposing legacy ALSA sequencer applications in JACK
MIDI systems.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot}/%{_bindir} -name 'a2j_control' -exec sed -i "s|#! %{_bindir}/env python3$|#!%{_bindir}/python3|" {} +

%files
%doc README.rst INSTALLATION.rst
%license LICENSE
%{_bindir}/a2j
%{_bindir}/a2j_control
%{_bindir}/a2jmidi_bridge
%{_bindir}/a2jmidid
%{_bindir}/j2amidi_bridge
%{_mandir}/man1/a2j.1%{?ext_man}
%{_mandir}/man1/a2j_control.1%{?ext_man}
%{_mandir}/man1/a2jmidi_bridge.1%{?ext_man}
%{_mandir}/man1/a2jmidid.1%{?ext_man}
%{_mandir}/man1/j2amidi_bridge.1%{?ext_man}
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service

%changelog
