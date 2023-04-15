#
# spec file for package xdg-desktop-portal-wlr
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


Name:           xdg-desktop-portal-wlr
Version:        0.7.0
Release:        0
Summary:        An xdg-desktop-portal backend for wlroots
License:        MIT
Group:          System/Libraries
URL:            https://github.com/emersion/xdg-desktop-portal-wlr
Source0:        %{url}/releases/download/v%{version}/xdg-desktop-portal-wlr-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/xdg-desktop-portal-wlr-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/%{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.7
BuildRequires:  pkgconfig(gbm) >= 21.3
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.62
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
# Screencasting won't work without pipewire, but it's not a hard dependency.
Recommends:     pipewire >= 0.3.41
Requires:       xdg-desktop-portal

%description
xdg-desktop-portal backend for wlroots.

Make sure the `XDG_CURRENT_DESKTOP` env var is set in the D-Bus user session
to one of the UseIn values in wlr.portal

%prep
%setup -q

%build
%meson -Dsd-bus-provider=libsystemd
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libexecdir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.wlr.service
%{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_mandir}/man5/%{name}.5.gz

%changelog
