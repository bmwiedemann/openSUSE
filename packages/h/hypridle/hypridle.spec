#
# spec file for package hypridle
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


Name:           hypridle
Version:        0.1.5
Release:        0
Summary:        Hyprland's idle daemon
License:        BSD-3-Clause
URL:            https://wiki.hyprland.org/hypr-ecosystem/hypridle
Source0:        %{name}-%{version}.tar.xz
Source1:        hypridle.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
## Added for directory ownership
BuildRequires:  hyprland
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(hyprlang) >= 0.4.2
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Hyprland's idle daemon

* based on the ext-idle-notify-v1 wayland protocol
* support for dbus' loginctl commands (lock / unlock / before-sleep)
* support for dbus' inhibit (used by e.g. firefox / steam)

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm 0644 %{SOURCE1} %buildroot/%_docdir/%name/hypridle.conf.example

%files
%license LICENSE
%doc README.md hypridle.conf.example
%{_bindir}/hypridle
%{_datadir}/hypr/hypridle.conf
%{_userunitdir}/hypridle.service

%changelog
