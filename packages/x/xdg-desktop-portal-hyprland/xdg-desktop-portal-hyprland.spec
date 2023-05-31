#
# spec file for package xdg-desktop-portal-hyprland
#
# Copyright (c) 2023 SUSE LLC
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


%define _protocol_version 0.2
Name:           xdg-desktop-portal-hyprland
Version:        0.4.0
Release:        0
Summary:        Extended xdg-desktop-portal backend for Hyprland
License:        MIT
Group:          System/Libraries
URL:            https://github.com/hyprwm/xdg-desktop-portal-hyprland
Source0:        https://github.com/hyprwm/xdg-desktop-portal-hyprland/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/hyprwm/hyprland-protocols/archive/refs/tags/v%{_protocol_version}.tar.gz#/hyprland-protocols-%{_protocol_version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-wayland
BuildRequires:  qt6-wayland-devel
BuildRequires:  qt6-waylandclient-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  scdoc >= 1.9.7
BuildRequires:  pkgconfig(gbm) >= 21.3
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.62
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
# Screencasting won't work without pipewire, but it's not a hard dependency.
Recommends:     pipewire >= 0.3.41

# Required since the picker uses qt wayland.
# Not a strict requirement as the portal will fallback to slurp
Recommends:     qt6-wayland

Requires:       xdg-desktop-portal

# As this is a fork of XDPW, installing this will conflict with XDPH
Conflicts:      xdg-desktop-portal-wlr

%description
A fork of xdg-desktop-portal backend for wlroots for Hyprland. It supports
other wlroots-based Wayland compositors too with some limitations.

%package -n hyprland-protocols-devel
Summary:        Development files for Hyprland protocols
Group:          Development/Libraries/Other
Version:        0.2
BuildArch:      noarch
Provides:       hyprland-protocols-devel = %{_protocol_version}

%description -n hyprland-protocols-devel
Wayland protocol extensions for interacting or modifying Hyprland.

%prep
%setup -q

# Needed for this portal to work.
tar xvf %{SOURCE1} -C subprojects/hyprland-protocols --strip-components=1

%build
%meson -Dsd-bus-provider=libsystemd
%meson_build
make -C hyprland-share-picker all

%install
%meson_install
install -Dm0755 -t %{buildroot}%{_bindir} hyprland-share-picker/build/hyprland-share-picker

%files
%{-,root,root,-}
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/hyprland-share-picker
%{_libexecdir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal

%files -n hyprland-protocols-devel
%{_datadir}/pkgconfig/hyprland-protocols.pc
%dir %{_datadir}/hyprland-protocols
%dir %{_datadir}/hyprland-protocols/protocols
%{_datadir}/hyprland-protocols/protocols/*

%changelog
