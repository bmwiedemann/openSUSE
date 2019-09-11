#
# spec file for package waybar
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           waybar
Version:        0.7.2
Release:        0
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Alexays/Waybar
Source:         https://github.com/Alexays/Waybar/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gtkmm3-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libinput-devel
BuildRequires:  libsigc++3-devel
BuildRequires:  libudev-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  spdlog-devel
# optional: tray module
BuildRequires:  libdbusmenu-gtk3-devel
# optional: network
BuildRequires:  libnl3-devel
# optional: audio
BuildRequires:  libpulse-devel
# optional: mpd module
BuildRequires:  libmpdclient-devel
# optional: sway integration
Recommends:     sway

%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%setup -q -n Waybar-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar

%changelog
