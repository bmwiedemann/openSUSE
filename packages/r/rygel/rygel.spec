#
# spec file for package rygel
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


%define sover      2_8-0
%define apiver     2.8
%define typelibver 2_8

Name:           rygel
Version:        0.43.0
Release:        0
Summary:        UPnP/DLNA home media server for GNOME
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://live.gnome.org/Rygel
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.33.4
BuildRequires:  libunistring-devel
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  vala >= 0.36.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gssdp-1.6)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(gupnp-1.6) >= 1.1
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.12.8
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(gupnp-dlna-gst-2.0) >= 0.9.4
BuildRequires:  pkgconfig(libmediaart-2.0) >= 1.9.0
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.2
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
Requires:       gstreamer-plugins-base
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly
%{?systemd_ordering}

%description
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network. In
technical terms, it is both a UPnP AV MediaServer and MediaRenderer
implemented through a plug-in mechanism. It conforms to DLNA and does
on-the-fly conversion of media to format that client devices are
capable of handling.

%package -n librygel-core-%{sover}
Summary:        Core library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-core-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the core library of rygel.

%package -n librygel-db-%{sover}
Summary:        Database library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-db-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the database library of rygel.

%package -n librygel-renderer-%{sover}
Summary:        Render library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-renderer-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the renderer library of rygel.

%package -n librygel-renderer-gst-%{sover}
Summary:        Gstreamer render library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-renderer-gst-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the renderer library of rygel.

%package -n librygel-ruih-%{sover}
Summary:        Remote User Interface handling library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-ruih-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the ruih library of rygel.

%package -n librygel-server-%{sover}
Summary:        Server library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-server-%{sover}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the server library of rygel.

%package -n typelib-1_0-RygelCore-%{typelibver}
Summary:        GObject introspection files for the Rygel core library
Group:          System/Libraries

%description -n typelib-1_0-RygelCore-%{typelibver}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelRenderer-%{typelibver}
Summary:        GObject introspection files for the Rygel renderer library
Group:          System/Libraries

%description -n typelib-1_0-RygelRenderer-%{typelibver}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelRendererGst-%{typelibver}
Summary:        GObject introspection files for the Rygel RendererGst library
Group:          System/Libraries

%description -n typelib-1_0-RygelRendererGst-%{typelibver}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelServer-%{typelibver}
Summary:        GObject introspection files for the Rygel server library
Group:          System/Libraries

%description -n typelib-1_0-RygelServer-%{typelibver}
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package devel
Summary:        Development files for the Rygel UPnP/DLNA media server
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       librygel-core-%{sover} = %{version}
Requires:       librygel-db-%{sover} = %{version}
Requires:       librygel-renderer-%{sover} = %{version}
Requires:       librygel-renderer-gst-%{sover} = %{version}
Requires:       librygel-ruih-%{sover} = %{version}
Requires:       librygel-server-%{sover} = %{version}
Requires:       typelib-1_0-RygelCore-%{typelibver} = %{version}
Requires:       typelib-1_0-RygelRenderer-%{typelibver} = %{version}
Requires:       typelib-1_0-RygelRendererGst-%{typelibver} = %{version}
Requires:       typelib-1_0-RygelServer-%{typelibver} = %{version}

%description devel
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides development files for rygel.

%package plugin-gstreamer-renderer
Summary:        GStreamer renderer plugin for the Rygel UPnP/DLNA media server
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}

%description plugin-gstreamer-renderer
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides a standalone MediaRenderer plugin, based on the
GStreamer playbin3 element.

%package plugin-tracker
Summary:        Tracker plugin for the Rygel UPnP/DLNA media server
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Requires:       tracker
Supplements:    (%{name} and tracker)

%description plugin-tracker
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides a plugin using tracker to export media found on
the local machine.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dapi-docs=false \
	-Dsystemd-user-units-dir=auto \
	-Dexamples=false \
	-Dtests=false \
	-Dgstreamer=enabled \
	-Dgtk=enabled \
	-Dplugins=external,gst-launch,media-export,mpris,playbin,ruih,tracker3 \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install

%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%ldconfig_scriptlets -n librygel-core-%{sover}
%ldconfig_scriptlets -n librygel-db-%{sover}
%ldconfig_scriptlets -n librygel-renderer-%{sover}
%ldconfig_scriptlets -n librygel-renderer-gst-%{sover}
%ldconfig_scriptlets -n librygel-ruih-%{sover}
%ldconfig_scriptlets -n librygel-server-%{sover}

%files
%license COPYING
%doc AUTHORS NEWS
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_userunitdir}/rygel.service
%{_bindir}/rygel
%{_bindir}/rygel-preferences
%{_datadir}/rygel/
%{_datadir}/applications/rygel.desktop
%{_datadir}/applications/rygel-preferences.desktop
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mx-extract
%{_mandir}/*/*
# Plugins that we ship by default because they don't have a dependency and can
# be useful to most people
%dir %{_libdir}/rygel-%{apiver}/
%dir %{_libdir}/rygel-%{apiver}/engines/
%dir %{_libdir}/rygel-%{apiver}/plugins/
%{_libdir}/rygel-%{apiver}/engines/librygel-media-engine-gst.so
%{_libdir}/rygel-%{apiver}/engines/librygel-media-engine-simple.so
%{_libdir}/rygel-%{apiver}/engines/media-engine-gst.plugin
%{_libdir}/rygel-%{apiver}/engines/media-engine-simple.plugin
# external applications implementing D-Bus MediaServer spec
%{_libdir}/rygel-%{apiver}/plugins/librygel-external.so
%{_libdir}/rygel-%{apiver}/plugins/external.plugin
# GStreamer pipelines in the config
%{_libdir}/rygel-%{apiver}/plugins/librygel-gst-launch.so
%{_libdir}/rygel-%{apiver}/plugins/gst-launch.plugin
# folders and files in the config
%{_libdir}/rygel-%{apiver}/plugins/librygel-media-export.so
%{_libdir}/rygel-%{apiver}/plugins/media-export.plugin
# media players implementing MPRIS2 D-Bus interface
%{_libdir}/rygel-%{apiver}/plugins/librygel-mpris.so
%{_libdir}/rygel-%{apiver}/plugins/mpris.plugin
# ruih plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-ruih.so
%{_libdir}/rygel-%{apiver}/plugins/ruih.plugin

%files -n librygel-core-%{sover}
%{_libdir}/librygel-core-%{apiver}.so.*

%files -n librygel-db-%{sover}
%{_libdir}/librygel-db-%{apiver}.so.*

%files -n librygel-renderer-%{sover}
%{_libdir}/librygel-renderer-%{apiver}.so.*

%files -n librygel-renderer-gst-%{sover}
%{_libdir}/librygel-renderer-gst-%{apiver}.so.*

%files -n librygel-ruih-%{sover}
%{_libdir}/librygel-ruih-%{apiver}.so.*

%files -n librygel-server-%{sover}
%{_libdir}/librygel-server-%{apiver}.so.*

%files -n typelib-1_0-RygelCore-%{typelibver}
%{_libdir}/girepository-1.0/RygelCore-%{apiver}.typelib

%files -n typelib-1_0-RygelRenderer-%{typelibver}
%{_libdir}/girepository-1.0/RygelRenderer-%{apiver}.typelib

%files -n typelib-1_0-RygelRendererGst-%{typelibver}
%{_libdir}/girepository-1.0/RygelRendererGst-%{apiver}.typelib

%files -n typelib-1_0-RygelServer-%{typelibver}
%{_libdir}/girepository-1.0/RygelServer-%{apiver}.typelib

%files devel
%{_includedir}/rygel-%{apiver}/
%{_libdir}/librygel-core-%{apiver}.so
%{_libdir}/librygel-db-%{apiver}.so
%{_libdir}/librygel-renderer-%{apiver}.so
%{_libdir}/librygel-renderer-gst-%{apiver}.so
%{_libdir}/librygel-server-%{apiver}.so
%{_libdir}/librygel-ruih-%{apiver}.so
%{_libdir}/pkgconfig/rygel-core-%{apiver}.pc
%{_libdir}/pkgconfig/rygel-renderer-%{apiver}.pc
%{_libdir}/pkgconfig/rygel-renderer-gst-%{apiver}.pc
%{_libdir}/pkgconfig/rygel-ruih-%{apiver}.pc
%{_libdir}/pkgconfig/rygel-server-%{apiver}.pc
%{_datadir}/gir-1.0/RygelCore-%{apiver}.gir
%{_datadir}/gir-1.0/RygelRenderer-%{apiver}.gir
%{_datadir}/gir-1.0/RygelRendererGst-%{apiver}.gir
%{_datadir}/gir-1.0/RygelServer-%{apiver}.gir
%{_datadir}/vala/vapi/rygel-core-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-core-%{apiver}.vapi
%{_datadir}/vala/vapi/rygel-db-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-db-%{apiver}.vapi
%{_datadir}/vala/vapi/rygel-renderer-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-renderer-%{apiver}.vapi
%{_datadir}/vala/vapi/rygel-renderer-gst-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-renderer-gst-%{apiver}.vapi
%{_datadir}/vala/vapi/rygel-ruih-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-ruih-%{apiver}.vapi
%{_datadir}/vala/vapi/rygel-server-%{apiver}.deps
%{_datadir}/vala/vapi/rygel-server-%{apiver}.vapi

%files plugin-gstreamer-renderer
%{_libdir}/rygel-%{apiver}/plugins/librygel-playbin.so
%{_libdir}/rygel-%{apiver}/plugins/playbin.plugin

%files plugin-tracker
%{_libdir}/rygel-%{apiver}/plugins/librygel-tracker3.so
%{_libdir}/rygel-%{apiver}/plugins/tracker3.plugin

%files lang -f %{name}.lang

%changelog
