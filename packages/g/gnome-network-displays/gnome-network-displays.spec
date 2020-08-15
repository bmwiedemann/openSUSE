#
# spec file for package gnome-network-displays
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


Name:           gnome-network-displays
Version:        0.90.3
Release:        0
Summary:        Miracast implementation for GNOME
Group:          Productivity/Networking/Other
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/GNOME/%{name}
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  update-desktop-files

%description
This is an experimental implementation of Wi-Fi Display (aka Miracast).
The application will stream the selected monitor if the mutter screencast
portal is available. If it is unavailable, a fallback to X11 based frame
grabbing will happen. As such, it should work fine in almost all setups.
To get audio streaming, you need to change the audio output in pulseaudio
to use the created "Network-Displays" sink.

%lang_package

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r org.gnome.NetworkDisplays "Network;RemoteAccess"
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/metainfo/*.appdata.xml

%files lang -f %{name}.lang

%changelog
