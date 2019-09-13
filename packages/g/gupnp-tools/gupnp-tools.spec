#
# spec file for package gupnp-tools
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gupnp-tools
Version:        0.10.0
Release:        0
Summary:        UPnP tools to test and debug UPnP devices and control points
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/gupnp-tools/0.10/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.24
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-2.0) >= 2.24
BuildRequires:  pkgconfig(gssdp-1.2) >= 1.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gupnp-1.2) >= 1.1
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.5.5
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(uuid)
Recommends:     %{name}-lang

%description
GUPnP Tools are free replacements of Intel UPnP tools that use GUPnP.
They provides the following client and server side tools which enable
one to easily test and debug one's UPnP devices and control points:

  * Universal Control Point: a tool that enables one to discover UPnP
    devices and services, retrieve information about them, subscribe to events
    and invoke actions.

  * Network Light: a virtual light bulb that allows control points to
    switch it on and off, change its dimming level and query its current
    status. It also provides a simple UI to control all the network lights
    available on the network.

  * AV Control Point: a simple media player UI that enables one to
    discover and play multimedia contents available on a network. It is
    strictly a control point and therefore does not have any playback
    capabilities of it's own and relies on external UPnP MediaRenderer devices
    for actual playback.

  * Upload: a simple commandline utility that uploads files to known
    MediaServers. Use Universal Control Point for discovering the
    MediaServers.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r gupnp-av-cp GTK Network System Monitor
%suse_update_desktop_file -r gupnp-network-light GTK Network System Monitor
%suse_update_desktop_file -r gupnp-universal-cp GTK Network System Monitor
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/

%files lang -f %{name}.lang

%changelog
