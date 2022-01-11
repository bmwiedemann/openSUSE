#
# spec file for package gnome-kiosk
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-kiosk
Version:        41.0
Release:        0
Summary:        Mutter based compositor for kiosks
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-kiosk
Source:         https://download.gnome.org/sources/gnome-kiosk/41/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  mutter-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Requires:       gnome-session

%description
Kiosk provides a desktop enviroment suitable for fixed purpose, or single
application deployments like wall displays and point-of-sale systems.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/gnome-kiosk
%{_bindir}/gnome-kiosk-script
%dir %{_userunitdir}/gnome-session@gnome-kiosk-script.target.d
%{_userunitdir}/gnome-session@gnome-kiosk-script.target.d/session.conf
%{_userunitdir}/org.gnome.Kiosk.Script.service
%{_userunitdir}/org.gnome.Kiosk.target
%{_userunitdir}/org.gnome.Kiosk@wayland.service
%{_userunitdir}/org.gnome.Kiosk@x11.service
%{_datadir}/applications/org.gnome.Kiosk.Script.desktop
%{_datadir}/applications/org.gnome.Kiosk.SearchApp.desktop
%{_datadir}/applications/org.gnome.Kiosk.desktop
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/sessions/gnome-kiosk-script.session
%{_datadir}/gnome-session/sessions/org.gnome.Kiosk.SearchApp.session
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/gnome-kiosk-script-wayland.desktop
%{_datadir}/wayland-sessions/org.gnome.Kiosk.SearchApp.Session.desktop
%{_datadir}/xsessions/gnome-kiosk-script-xorg.desktop
%{_datadir}/xsessions/org.gnome.Kiosk.SearchApp.Session.desktop

%changelog
