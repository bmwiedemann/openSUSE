#
# spec file for package gnome-network-displays
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


Name:           gnome-network-displays
Version:        0.90.5
Release:        0
Summary:        Miracast implementation for GNOME
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://gitlab.gnome.org/GNOME/%{name}
Source:         https://download.gnome.org/sources/%{name}/0.90/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
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
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/metainfo/*.appdata.xml
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/zones
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml

%files lang -f %{name}.lang

%changelog
