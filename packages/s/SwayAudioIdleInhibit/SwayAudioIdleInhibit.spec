#
# spec file for package SwayAudioIdleInhibit
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.1.1
Release:        0
Summary:        Prevents swayidle from sleeping while outputting or receiving audio
License:        GPL-3.0-or-later
URL:            https://github.com/ErikReider/SwayAudioIdleInhibit
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pipewire-devel
BuildRequires:  systemd-devel
Requires:       pipewire-pulseaudio

%description
Prevents swayidle from sleeping while any application is outputting or receiving audio. Should work with all Wayland desktops that support the zwp_idle_inhibit_manager_v1 protocol but only tested in Sway
This only works for Pulseaudio / Pipewire Pulse

%prep
%autosetup -a0 -p0

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