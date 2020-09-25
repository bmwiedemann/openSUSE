#
# spec file for package waybar
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


Name:           waybar
Version:        0.9.4
Release:        0
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Alexays/Waybar
# use this to download tarball. then use `meson subprojects download`
# to get the `date` dependency. and create own tarball
#Source:         https://github.com/Alexays/Waybar/archive/%{version}.tar.gz
Source:         %{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
# optional: man pages
BuildRequires:  scdoc
# optional: tray module
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
# optional: mpd module
BuildRequires:  pkgconfig(libmpdclient)
# optional: network
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
# optional: audio
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
# requires branding
Requires:       %{name}-branding
# optional: sway integration
Recommends:     sway

%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/xdg/waybar/config contains upstream config
#BRAND: /etc/xdg/waybar/style.css contains upstream style

%description branding-upstream
This package provides the upstream look and feel for sway.

%prep
%setup -q -n Waybar-%{version}

%build
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
