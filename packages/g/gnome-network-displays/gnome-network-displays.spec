#
# spec file for package gnome-network-displays
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


Name:           gnome-network-displays
Version:        0.94.0
Release:        0
Summary:        Miracast implementation for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source:         %{name}-%{version}.tar.zst
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libnm) >= 1.15
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.7
BuildRequires:  pkgconfig(libprotobuf-c) >= 1.0.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
Requires:       gstreamer-plugin-pipewire

%description
This is an experimental implementation of Wi-Fi Display (aka Miracast).

The application will stream the selected monitor if the mutter screencast
portal is available. If it is unavailable, a fallback to X11 based frame
grabbing will happen. As such, it should work fine in almost all setups.

To get audio streaming, you need to change the audio output in pulseaudio
to use the created "Network-Displays" sink.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%meson_test

%files
%license COPYING
%{_bindir}/gnome-network-displays
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/zones
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml
%{_datadir}/applications/org.gnome.NetworkDisplays.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_datadir}/metainfo/org.gnome.NetworkDisplays.appdata.xml

%files lang -f %{name}.lang

%changelog
