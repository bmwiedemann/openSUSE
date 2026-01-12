#
# spec file for package hyprpaper
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


Name:           hyprpaper
Version:        0.8.1
Release:        0
Summary:        Wayland wallpaper utility with IPC controls
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpaper
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang) >= 0.2.0
BuildRequires:  pkgconfig(hyprtoolkit) >= 0.5.2
BuildRequires:  pkgconfig(hyprutils) >= 0.2.0
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprwire)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots-0.18) >= 0.18.0
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
%license LICENSE
%{_bindir}/hyprpaper
%{_userunitdir}/hyprpaper.service

%changelog
