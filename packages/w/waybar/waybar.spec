#
# spec file for package waybar
#
# Copyright (c) 2022 SUSE LLC
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


Name:           waybar
Version:        0.9.16
Release:        0
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Alexays/Waybar
Source0:        %{name}-%{version}.tar.gz
Patch0:         0000-replace-gethostbyname-getaddrinfo.patch
BuildRequires:  cmake
%if 0%{?sle_version} >= 150400
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++ >= 8
%endif
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
# test dependency
BuildRequires:  pkgconfig(catch2) >= 3.0
BuildRequires:  sndio-devel >= 1.7.0
# date module
BuildRequires:  hhdate-devel
# optional: man pages
BuildRequires:  scdoc
# optional: tray module
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(upower-glib)
# optional: mpd module
BuildRequires:  pkgconfig(libmpdclient)
# optional: network
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
# optional: audio
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.4)
BuildRequires:  pkgconfig(xkbregistry)
# requires branding
# NOTE: unversioned branding is required to avoid issues like bsc#1205950
Requires:       %{name}-branding
# optional: sway integration
Recommends:     sway

%description
A customizable Wayland bar for Sway and Wlroots based compositors.
It comes with modules for pipewire, alsa, backlight, and bluetooth.
Other modules can be found in the manpages of Waybar.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/xdg/waybar/config contains upstream config
#BRAND: /etc/xdg/waybar/style.css contains upstream style

%description branding-upstream
This package provides the upstream look and feel for sway.

%prep
%autosetup -p1 -n waybar-%{version}

%build
%if 0%{?sle_version} >= 150400
export CXX=g++-11
%endif
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/waybar
%{_mandir}/man?/%{name}*
%{_prefix}/lib/systemd/user/waybar.service

%files branding-upstream
%dir %{_sysconfdir}/xdg/waybar
%config(noreplace) %{_sysconfdir}/xdg/waybar/config
%config(noreplace) %{_sysconfdir}/xdg/waybar/style.css

%changelog
