#
# spec file for package hyprpaper
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
Name:           hyprpaper
Summary:        Wayland wallpaper utility with IPC controls
Version:        0.7.0
Release:        0
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpaper
Source0:        https://github.com/hyprwm/hyprpaper/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang) >= 0.2.0
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots) >= 0.16.0
BuildRequires:  pkgconfig(xwaylandproto)

%description
Hyprpaper is a wallpaper utility for Hyprland.
It supports IPC controls for Hyprland and various
image formats.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/hyprpaper
%license LICENSE

%changelog
