#
# spec file for package noctalia-shell
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           noctalia-shell
Version:        4.7.7
Release:        0
Summary:        A sleek and minimal desktop shell for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/noctalia-dev/noctalia/tree/legacy-v4
Source0:        %{name}-%{version}.tar.zst
Source99:       %{name}-rpmlintrc
Patch0:         001-setting-gate-automatic-network-requests.patch

BuildRequires:  zstd

%if 0%{?suse_version} == 1600
Requires:       ffmpeg >= 7
%else
Requires:       ffmpeg-8
%endif
Requires:       noctalia-qs
Requires:       ImageMagick
Requires:       brightnessctl
Requires:       python3

Recommends:     wlr-randr
Recommends:     cliphist
Recommends:     ddcutil
Recommends:     inter-fonts
Recommends:     inter-variable-fonts
Recommends:     power-profiles-daemon
Recommends:     upower
Recommends:     wlsunset
Recommends:     xdg-desktop-portal

Suggests:       evolution-data-server

BuildArch:      noarch

%description
Noctalia is a minimal desktop shell for Wayland, built on Quickshell
(QtQuick/QML). It provides a status bar, dock, panels, notifications,
lock screen, idle management, OSD, desktop widgets, wallpaper
management, and multi-monitor support, while intentionally staying
out of compositor responsibilities.

Native support is provided for Niri, Hyprland, Sway, Scroll, Labwc
and MangoWC. Launch with:

    qs -c noctalia-shell

%prep
%autosetup -p1
sed -i 's/"autoNetworkEnabled": true/"autoNetworkEnabled": false/' Assets/settings-default.json
find . -type f \( -name "*.sh" \) -exec sed -i '1s|^#! *%{_bindir}/env -S bash|#!/bin/bash|' {} +
find . -type f \( -name "*.sh" \) -exec sed -i '1s|^#! *%{_bindir}/env bash|#!/bin/bash|' {} +
find . -type f \( -name "*.py" \) -exec sed -i '1s|^#! *%{_bindir}/env python3|#!%{_bindir}/python3|' {} +

%build
chmod 0755 Scripts/python/src/network/bluetooth-pair.py
chmod 0755 Scripts/python/src/theming/gtk-refresh.py
chmod 0755 Scripts/python/src/theming/migrate-colorschemes.py
chmod 0755 Scripts/python/src/theming/template-processor.py
chmod 0755 Scripts/python/src/theming/vscode-helper.py

%install
install -d -m 0755 %{buildroot}%{_datadir}/quickshell/noctalia-shell
cp -a ./* "%{buildroot}%{_datadir}/quickshell/noctalia-shell/"
# README and LICENSE are shipped via %%doc / %%license
rm -f %{buildroot}%{_datadir}/quickshell/noctalia-shell/README.md
rm -f %{buildroot}%{_datadir}/quickshell/noctalia-shell/LICENSE

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/quickshell
%{_datadir}/quickshell/noctalia-shell/

%changelog

