#
# spec file for package SwayAudioIdleInhibit
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


Name:           SwayAudioIdleInhibit
Version:        0.2.0
Release:        0
Summary:        Prevents swayidle from sleeping while outputting or receiving audio
License:        GPL-3.0-or-later
URL:            https://github.com/ErikReider/SwayAudioIdleInhibit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse) >= 15.0
BuildRequires:  pkgconfig(libsystemd)
Requires:       pipewire-pulseaudio

%description
Prevents swayidle/hypridle from sleeping while any application is outputting
or receiving audio. Uses systemd/elogind idle inhibit. Only works with
PulseAudio / PipeWire Pulse.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/sway-audio-idle-inhibit

%changelog
