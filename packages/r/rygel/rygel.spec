#
# spec file for package rygel
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


Name:           rygel
Version:        0.38.1
Release:        0
Summary:        UPnP/DLNA home media server for GNOME
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://live.gnome.org/Rygel
Source0:        https://download.gnome.org/sources/rygel/0.38/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.33.4
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.36.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gssdp-1.2) >= 1.1
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(gupnp-1.2) >= 1.1
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.12.8
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(gupnp-dlna-gst-2.0) >= 0.9.4
BuildRequires:  pkgconfig(libmediaart-2.0) >= 1.9.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.44.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.44.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tracker-sparql-2.0)
Requires:       gstreamer-plugins-base
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly
# plugin-zdf-mediathek was removed in 0.31.1
Obsoletes:      plugin-zdf-mediathek
%{?systemd_ordering}

%description
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network. In
technical terms, it is both a UPnP AV MediaServer and MediaRenderer
implemented through a plug-in mechanism. It conforms to DLNA and does
on-the-fly conversion of media to format that client devices are
capable of handling.

%package -n librygel-core-2_6-2
Summary:        Core library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-core-2_6-2
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the core library of rygel.

%package -n librygel-db-2_6-2
Summary:        Database library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-db-2_6-2
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the database library of rygel.

%package -n librygel-renderer-2_6-2
Summary:        Render library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-renderer-2_6-2
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the renderer library of rygel.

%package -n librygel-renderer-gst-2_6-2
Summary:        Gstreamer render library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-renderer-gst-2_6-2
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the renderer library of rygel.

%package -n librygel-ruih-2_0-1
Summary:        Remote User Interface handling library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-ruih-2_0-1
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the ruih library of rygel.

%package -n librygel-server-2_6-2
Summary:        Server library for the Rygel UPnP/DLNA media server
Group:          System/Libraries

%description -n librygel-server-2_6-2
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides the server library of rygel.

%package -n typelib-1_0-RygelCore-2_6
Summary:        GObject introspection files for the Rygel core library
Group:          System/Libraries

%description -n typelib-1_0-RygelCore-2_6
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelRenderer-2_6
Summary:        GObject introspection files for the Rygel renderer library
Group:          System/Libraries

%description -n typelib-1_0-RygelRenderer-2_6
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelRendererGst-2_6
Summary:        GObject introspection files for the Rygel RendererGst library
Group:          System/Libraries

%description -n typelib-1_0-RygelRendererGst-2_6
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package -n typelib-1_0-RygelServer-2_6
Summary:        GObject introspection files for the Rygel server library
Group:          System/Libraries

%description -n typelib-1_0-RygelServer-2_6
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

%package devel
Summary:        Development files for the Rygel UPnP/DLNA media server
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       librygel-core-2_6-2 = %{version}
Requires:       librygel-db-2_6-2 = %{version}
Requires:       librygel-renderer-2_6-2 = %{version}
Requires:       librygel-renderer-gst-2_6-2 = %{version}
Requires:       librygel-ruih-2_0-1 = %{version}
Requires:       librygel-server-2_6-2 = %{version}
Requires:       typelib-1_0-RygelCore-2_6 = %{version}
Requires:       typelib-1_0-RygelRenderer-2_6 = %{version}
Requires:       typelib-1_0-RygelRendererGst-2_6 = %{version}
Requires:       typelib-1_0-RygelServer-2_6 = %{version}

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
GStreamer playbin2 element.

%package plugin-tracker
Summary:        Tracker plugin for the Rygel UPnP/DLNA media server
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Requires:       tracker
Supplements:    packageand(%{name}:tracker)

%description plugin-tracker
Rygel is a home media server that allows sharing audio, video,
pictures, and control of media player on your home network.

This package provides a plugin using tracker to export media found on
the local machine.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-tracker-plugin \
    --enable-media-export-plugin \
    --enable-external-plugin \
    --enable-gst-launch-plugin
%make_build

# Future use
#%%meson \
#	-Dapi-docs=false \
#	-Dsystemd-user-units-dir=auto \
#	-Dexamples=false \
#	-Dtests=false \
#	-Dgstreamer=true \
#	-Dgtk=true \
#	%%{nil}
#%%meson_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Future use
#%%meson_install

%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file rygel
%suse_update_desktop_file rygel-preferences X-SuSE-ControlCenter-Personal
%find_lang %{name} %{?no_lang_C}

%post -n librygel-core-2_6-2 -p /sbin/ldconfig
%postun -n librygel-core-2_6-2 -p /sbin/ldconfig
%post -n librygel-db-2_6-2 -p /sbin/ldconfig
%postun -n librygel-db-2_6-2 -p /sbin/ldconfig
%post -n librygel-renderer-2_6-2 -p /sbin/ldconfig
%postun -n librygel-renderer-2_6-2 -p /sbin/ldconfig
%post -n librygel-renderer-gst-2_6-2 -p /sbin/ldconfig
%postun -n librygel-renderer-gst-2_6-2 -p /sbin/ldconfig
%post -n librygel-ruih-2_0-1 -p /sbin/ldconfig
%postun -n librygel-ruih-2_0-1 -p /sbin/ldconfig
%post -n librygel-server-2_6-2 -p /sbin/ldconfig
%postun -n librygel-server-2_6-2 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS TODO NEWS
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
%dir %{_libdir}/rygel-2.6/
%dir %{_libdir}/rygel-2.6/engines/
%dir %{_libdir}/rygel-2.6/plugins/
%{_libdir}/rygel-2.6/engines/librygel-media-engine-gst.so
%{_libdir}/rygel-2.6/engines/librygel-media-engine-simple.so
%{_libdir}/rygel-2.6/engines/media-engine-gst.plugin
%{_libdir}/rygel-2.6/engines/media-engine-simple.plugin
# external applications implementing D-Bus MediaServer spec
%{_libdir}/rygel-2.6/plugins/librygel-external.so
%{_libdir}/rygel-2.6/plugins/external.plugin
# GStreamer pipelines in the config
%{_libdir}/rygel-2.6/plugins/librygel-gst-launch.so
%{_libdir}/rygel-2.6/plugins/gst-launch.plugin
# LightweightMediaScanner
%{_libdir}/rygel-2.6/plugins/librygel-lms.so
%{_libdir}/rygel-2.6/plugins/lms.plugin
# folders and files in the config
%{_libdir}/rygel-2.6/plugins/librygel-media-export.so
%{_libdir}/rygel-2.6/plugins/media-export.plugin
# media players implementing MPRIS2 D-Bus interface
%{_libdir}/rygel-2.6/plugins/librygel-mpris.so
%{_libdir}/rygel-2.6/plugins/mpris.plugin
# ruih plugin
%{_libdir}/rygel-2.6/plugins/librygel-ruih.so
%{_libdir}/rygel-2.6/plugins/ruih.plugin

%files -n librygel-core-2_6-2
%{_libdir}/librygel-core-2.6.so.*

%files -n librygel-db-2_6-2
%{_libdir}/librygel-db-2.6.so.*

%files -n librygel-renderer-2_6-2
%{_libdir}/librygel-renderer-2.6.so.*

%files -n librygel-renderer-gst-2_6-2
%{_libdir}/librygel-renderer-gst-2.6.so.*

%files -n librygel-ruih-2_0-1
%{_libdir}/librygel-ruih-2.0.so.*

%files -n librygel-server-2_6-2
%{_libdir}/librygel-server-2.6.so.*

%files -n typelib-1_0-RygelCore-2_6
%{_libdir}/girepository-1.0/RygelCore-2.6.typelib

%files -n typelib-1_0-RygelRenderer-2_6
%{_libdir}/girepository-1.0/RygelRenderer-2.6.typelib

%files -n typelib-1_0-RygelRendererGst-2_6
%{_libdir}/girepository-1.0/RygelRendererGst-2.6.typelib

%files -n typelib-1_0-RygelServer-2_6
%{_libdir}/girepository-1.0/RygelServer-2.6.typelib

%files devel
%{_includedir}/rygel-2.6/
%{_libdir}/librygel-core-2.6.so
%{_libdir}/librygel-db-2.6.so
%{_libdir}/librygel-renderer-2.6.so
%{_libdir}/librygel-renderer-gst-2.6.so
%{_libdir}/librygel-server-2.6.so
%{_libdir}/librygel-ruih-2.0.so
%{_libdir}/pkgconfig/rygel-core-2.6.pc
%{_libdir}/pkgconfig/rygel-renderer-2.6.pc
%{_libdir}/pkgconfig/rygel-renderer-gst-2.6.pc
%{_libdir}/pkgconfig/rygel-ruih-2.0.pc
%{_libdir}/pkgconfig/rygel-server-2.6.pc
%{_datadir}/gir-1.0/RygelCore-2.6.gir
%{_datadir}/gir-1.0/RygelRenderer-2.6.gir
%{_datadir}/gir-1.0/RygelRendererGst-2.6.gir
%{_datadir}/gir-1.0/RygelServer-2.6.gir
%{_datadir}/vala/vapi/rygel-core-2.6.deps
%{_datadir}/vala/vapi/rygel-core-2.6.vapi
%{_datadir}/vala/vapi/rygel-db-2.6.deps
%{_datadir}/vala/vapi/rygel-db-2.6.vapi
%{_datadir}/vala/vapi/rygel-renderer-2.6.deps
%{_datadir}/vala/vapi/rygel-renderer-2.6.vapi
%{_datadir}/vala/vapi/rygel-renderer-gst-2.6.deps
%{_datadir}/vala/vapi/rygel-renderer-gst-2.6.vapi
%{_datadir}/vala/vapi/rygel-ruih-2.0.deps
%{_datadir}/vala/vapi/rygel-ruih-2.0.vapi
%{_datadir}/vala/vapi/rygel-server-2.6.deps
%{_datadir}/vala/vapi/rygel-server-2.6.vapi

%files plugin-gstreamer-renderer
%{_libdir}/rygel-2.6/plugins/librygel-playbin.so
%{_libdir}/rygel-2.6/plugins/playbin.plugin

%files plugin-tracker
%{_libdir}/rygel-2.6/plugins/librygel-tracker.so
%{_libdir}/rygel-2.6/plugins/tracker.plugin

%files lang -f %{name}.lang

%changelog
