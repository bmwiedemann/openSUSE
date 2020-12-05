#
# spec file for package mpvpaper
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mpvpaper
Version:        1.1
Release:        0
Summary:        A video wallpaper program for wlroots based wayland compositors
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/GhostNaN/mpvpaper
Source:         https://github.com/GhostNaN/mpvpaper/archive/%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  mpv-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  wlroots-devel
Requires:       mpv

%description
A video wallpaper program for wlroots based wayland compositors.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/mpvpaper
%{_bindir}/mpvpaper-holder

%changelog
