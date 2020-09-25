#
# spec file for package grilo-plugins
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


%define plugin_dir %(pkg-config --variable plugindir grilo-0.3)
Name:           grilo-plugins
Version:        0.3.12
Release:        0
Summary:        Media and metadata plugins for the Grilo framework
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://live.gnome.org/Grilo
Source0:        https://download.gnome.org/sources/grilo-plugins/0.3/%{name}-%{version}.tar.xz

BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  gperf
BuildRequires:  intltool >= 0.40.0
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(goa-1.0) >= 3.17.91
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gom-1.0) >= 0.4
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.10
BuildRequires:  pkgconfig(grilo-net-0.3) >= 0.3.10
BuildRequires:  pkgconfig(grilo-pls-0.3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgdata) >= 0.9.1
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua) >= 5.3.0
BuildRequires:  pkgconfig(oauth)
BuildRequires:  pkgconfig(rest-0.7) >= 0.7.90
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(totem-plparser) >= 3.4.1
BuildRequires:  pkgconfig(tracker-sparql-3.0) >= 2.99
# Recommend gupnp-plugin-dleyna (UPnP support)
Recommends:     gupnp-plugin-dleyna
%ifarch armv7hl i586
BuildRequires:  gstreamer1(element-chromaprint)
%else
BuildRequires:  gstreamer1(element-chromaprint)()(64bit)
%endif
BuildRequires:  pkgconfig(libdmapsharing-4.0) >= 3.9.9

%description
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides plugins for accessing content from various media
providers, including podcasts, Apple trailers, Flickr,
Jamendo, Vimeo, YouTube.

%package -n grilo-plugin-tracker
Summary:        Tracker plugin for the Grilo framework
Group:          Productivity/Multimedia/Other
Supplements:    packageand(grilo-plugins:tracker)

%description -n grilo-plugin-tracker
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%package -n grilo-plugin-dleyna
Summary:        DLNA (dLeyna) plugin for the Grilo media framework
# grilo-plugin-upnp was renamed to dleyna (based on the switch from libupnp to dleyna)
# the plugin interacts with dLeyna on dbus using com.intel.dleyna-server
Group:          Productivity/Multimedia/Other
Requires:       dbus(com.intel.dleyna-server)
Obsoletes:      grilo-plugin-upnp < %{version}
Provides:       grilo-plugin-upnp = %{version}

%description -n grilo-plugin-dleyna
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides a plugin for accessing content from a DLNA
(dLeyna) provider.

%package -n grilo-plugin-youtube
Summary:        Youtube plugin for the Grilo media framework
Group:          Productivity/Multimedia/Other
Supplements:    packageand(grilo-plugins:libgdata)

%description -n grilo-plugin-youtube
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides a plugin for accessing content from Youtube.

%package devel
Summary:        Development files for Grilo plugins
Group:          Development/Libraries/GNOME
Requires:       grilo-plugin-dleyna = %{version}
Requires:       grilo-plugin-tracker = %{version}
Requires:       grilo-plugin-youtube = %{version}
Requires:       grilo-plugins = %{version}

%description devel
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides the development files.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/help

%check
# Temp disable make check for PPC arches as they fail - boo#915682 filed.
%ifnarch ppc64 || ppc64le
# Make check disabled - it fails without network access.
#make check
%endif

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/help/C/grilo-plugins/
# Explicitly list plugins
%{plugin_dir}/libgrlbookmarks.so
%{plugin_dir}/libgrlchromaprint.so
%{plugin_dir}/libgrldaap.so
%{plugin_dir}/libgrldpap.so
%{plugin_dir}/libgrlfilesystem.so
%{plugin_dir}/libgrlflickr.so
%{plugin_dir}/libgrlfreebox.so
%{plugin_dir}/libgrlgravatar.so
%{plugin_dir}/libgrljamendo.so
%{plugin_dir}/libgrlmagnatune.so
%{plugin_dir}/libgrllocalmetadata.so
%{plugin_dir}/libgrlmetadatastore.so
%{plugin_dir}/libgrlopensubtitles.so
%{plugin_dir}/libgrlopticalmedia.so
%{plugin_dir}/libgrlpodcasts.so
%{plugin_dir}/libgrlraitv.so
%{plugin_dir}/libgrlshoutcast.so
%{plugin_dir}/libgrlthetvdb.so
%{plugin_dir}/libgrltmdb.so
%{plugin_dir}/libgrlvimeo.so
%{plugin_dir}/libgrlluafactory.so
%dir %{_datadir}/grilo-plugins
%dir %{_datadir}/grilo-plugins/grl-lua-factory
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-acoustid.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz-coverart.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-lastfm-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-steam-store.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-theaudiodb-cover.lua

%files lang -f %{name}.lang

%files -n grilo-plugin-tracker
%{plugin_dir}/libgrltracker3.so

%files -n grilo-plugin-dleyna
%{plugin_dir}/libgrldleyna.so

%files -n grilo-plugin-youtube
%{plugin_dir}/libgrlyoutube.so

%files devel
%{_datadir}/help/*/examples/
%{_libdir}/pkgconfig/grilo-plugins-0.3.pc

%changelog
