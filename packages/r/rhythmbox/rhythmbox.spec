#
# spec file for package rhythmbox
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rhythmbox
Version:        3.4.8
Release:        0
Summary:        GNOME Music Management Application
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://wiki.gnome.org/Apps/Rhythmbox
Source0:        https://download.gnome.org/sources/rhythmbox/3.4/%{name}-%{version}.tar.xz
Source1:        %{name}-remote-control.xml
Source2:        daap-server.xml

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  lirc-devel
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.18.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.11.02
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libbrasero-media3)
BuildRequires:  pkgconfig(libdmapsharing-4.0)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0) >= 0.7.3
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 0.7.3
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.7
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(totem-plparser) >= 3.2.0
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
# For python plugins
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Recommends:     gstreamer-plugins-ugly
Recommends:     media-player-info

%description
Music Management application with support for ripping audio-CD's,
playback of Ogg Vorbis and MP3 and burning of CD-ROMs.

%package devel
Summary:        GNOME Music Management Application -- Development Files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Music Management application with support for ripping audio-CD's,
playback of Ogg Vorbis and MP3 and burning of CD-ROMs.

This package contains the development requirements to extend rhythmbox.

%lang_package

%prep
%autosetup -p1

%build
export MOZILLA_PLUGINDIR=%{_libdir}/browser-plugins
export PYTHON=%{_bindir}/python3
%meson \
	-D tests=disabled \
	-D daap=enabled \
	%{nil}
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/firewalld/services/

%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
# Disabled as it pulls old webkit, needs fixing upstream
rm -rf %{buildroot}/%{_libdir}/rhythmbox/plugins/context
# Remove zeitgeist plugin: no longer maintained
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/rbzeitgeist/
%fdupes -s %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog DOCUMENTERS MAINTAINERS MAINTAINERS.old NEWS README.md THANKS
%doc %{_datadir}/help/C/rhythmbox/
%{_bindir}/rhythmbox
%{_bindir}/rhythmbox-client
%dir %{_datadir}/metainfo
%{_datadir}/applications/org.gnome.Rhythmbox3.desktop
%{_datadir}/applications/org.gnome.Rhythmbox3.device.desktop
%{_datadir}/metainfo/org.gnome.Rhythmbox3.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Rhythmbox3.service
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Rhythmbox*.svg
%{_datadir}/rhythmbox/
%{_libdir}/girepository-1.0/MPID-3.0.typelib
%{_libdir}/girepository-1.0/RB-3.0.typelib
%{_libdir}/librhythmbox-core.so.*
%dir %{_libdir}/rhythmbox
%dir %{_libdir}/rhythmbox/plugins
%{_libdir}/rhythmbox/plugins/android/
%{_libdir}/rhythmbox/plugins/artsearch/
%{_libdir}/rhythmbox/plugins/audiocd/
%{_libdir}/rhythmbox/plugins/audioscrobbler/
%{_libdir}/rhythmbox/plugins/cd-recorder/
# Disabled as it pulls old webkit, needs fixing upstream
#{_libdir}/rhythmbox/plugins/context/
%{_libdir}/rhythmbox/plugins/daap/
%{_libdir}/rhythmbox/plugins/dbus-media-server/
%{_libdir}/rhythmbox/plugins/fmradio/
%{_libdir}/rhythmbox/plugins/generic-player/
%{_libdir}/rhythmbox/plugins/grilo/
%{_libdir}/rhythmbox/plugins/im-status/
%{_libdir}/rhythmbox/plugins/ipod/
%{_libdir}/rhythmbox/plugins/iradio/
%{_libdir}/rhythmbox/plugins/listenbrainz/
%{_libdir}/rhythmbox/plugins/lyrics/
%{_libdir}/rhythmbox/plugins/magnatune/
%{_libdir}/rhythmbox/plugins/mpris/
%{_libdir}/rhythmbox/plugins/mtpdevice/
%{_libdir}/rhythmbox/plugins/notification/
%{_libdir}/rhythmbox/plugins/power-manager/
%{_libdir}/rhythmbox/plugins/python-console/
%{_libdir}/rhythmbox/plugins/rb/
%{_libdir}/rhythmbox/plugins/rblirc/
%{_libdir}/rhythmbox/plugins/replaygain/
%{_libdir}/rhythmbox/plugins/webremote/
%{_libexecdir}/rhythmbox-metadata
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/*.xml
%{_mandir}/man1/rhythmbox.1%{ext_man}
%{_mandir}/man1/rhythmbox-client.1%{ext_man}

%files devel
%{_datadir}/gir-1.0/*.gir
%{_includedir}/rhythmbox/
%{_libdir}/pkgconfig/rhythmbox.pc
%{_libdir}/librhythmbox-core.so
%{_datadir}/vala/vapi/rb.vapi
%{_datadir}/vala/vapi/rhythmdb.vapi

%files lang -f %{name}.lang

%changelog
