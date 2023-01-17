#
# spec file for package swaybg
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


Name:           swaybg
Version:        1.2.0
Release:        0
Summary:        Wallpaper tool for Wayland compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/swaybg
Source0:        https://github.com/swaywm/swaybg/releases/download/v%{version}/swaybg-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  wlroots-devel >= 0.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
swaybg is a wallpaper utility for Wayland compositors. It is compatible with any Wayland compositor which implements the following Wayland protocols:
wlr-layer-shell, xdg-output, xdg-shell.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%meson

%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1%{?ext_man}

%changelog
