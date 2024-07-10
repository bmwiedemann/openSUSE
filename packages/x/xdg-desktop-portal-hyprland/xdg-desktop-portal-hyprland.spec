#
# spec file for package xdg-desktop-portal-hyprland
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


%global __builder ninja

Name:           xdg-desktop-portal-hyprland
Version:        1.3.2
Release:        0
Summary:        Extended xdg-desktop-portal backend for Hyprland
License:        MIT
Group:          System/Libraries
URL:            https://github.com/hyprwm/xdg-desktop-portal-hyprland
Source0:        https://github.com/hyprwm/xdg-desktop-portal-hyprland/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         https://github.com/hyprwm/xdg-desktop-portal-hyprland/commit/c5b30938710d6c599f3f5cd99a3ffac35381fb0f.patch#/fix-compilation-with-pw.patch
BuildRequires:  cmake
# Seems some of the C and CXX flags are CLANG specific
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  hyprland-protocols-devel
BuildRequires:  ninja
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-wayland
BuildRequires:  qt6-wayland-devel
BuildRequires:  qt6-waylandclient-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  scdoc >= 1.9.7
BuildRequires:  util-linux
BuildRequires:  pkgconfig(gbm) >= 21.3
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wlroots) >= 0.17.0

# Screencasting won't work without pipewire, but it's not a hard dependency.
Recommends:     pipewire >= 0.3.41

# Required since the picker uses qt wayland.
# Not a strict requirement as the portal will fallback to slurp
Recommends:     qt6-wayland
Requires:       xdg-desktop-portal

%description
A fork of xdg-desktop-portal backend for wlroots for Hyprland. It supports
other wlroots-based Wayland compositors too with some limitations.

%prep
%autosetup -p1
pushd subprojects
rm -rfv hyprland-protocols sdbus-cpp
popd

%build
%cmake \
	-DCMAKE_C_COMPILER="clang" \
	-DCMAKE_CXX_COMPILER="clang++"
%cmake_build

%install
%cmake_install

%pre
%systemd_user_pre %{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%{-,root,root,-}
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/hyprland-share-picker
%{_libexecdir}/%{name}
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal
%{_userunitdir}/%{name}.service

%changelog
