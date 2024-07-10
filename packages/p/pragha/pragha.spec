#
# spec file for package pragha
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


Name:           pragha
Version:        1.3.99.1
Release:        0
Summary:        Lightweight Music Player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/pragha-music-player/pragha
Source0:        https://github.com/pragha-music-player/pragha/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source100:      pragha-rpmlintrc
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  rygel-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.31
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(gudev-1.0)
%if 0%{?suse_version} > 1500 || (0%{?suse_version} >= 1500 && 0%{?sle_version} > 150500)
BuildRequires:  pkgconfig(gupnp-1.6)
%else
BuildRequires:  pkgconfig(gupnp-1.2)
%endif
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia) >= 0.90
BuildRequires:  pkgconfig(libclastfm) >= 0.5
BuildRequires:  pkgconfig(libglyr)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(totem-plparser)
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Recommends:     %{name}-lang
Recommends:     %{name}-plugins

%description
A Lightweight Music Player for GNU/Linux, based on Gtk, sqlite, and
completely written in C, constructed to be fast, light, and
simultaneously complete without obstructing the daily work.

Pragha was originally derived of Consonance Music Manager
(http://sites.google.com/site/consonancemanager/), discontinued by the
original author.

Some of the features are:
* Library management using sqlite3.
* Versatile Amarok-style play queue.
* Multiple views.
* OSD support with Libnotify.
* Id3 tag editing.
* mp3, ogg, flac, modplug, wav, asf, wma, mp4, m4a, MonkeyAudio and
  Audio CD support.
* Last.fm scrobbling, get cover art, get artist information, append
  similar songs, love, unlove, etc.
* Playlist management (M3U Exporting).
* DBUS management interface.
* MPRIS2 Support.
* Search/Filterin the current playlist.
* Search lyrics.

%package plugins
Summary:        Plugins for Pragha
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description plugins
This package includes plugins for the Pragha player.

* AcoustID - Get metadata on AcoustID service.
* Ampache - Append music on Ampache server.
* CD-ROM - Play Audio CDs.
* Devices - Management removable devices.
* DLNA Server - Share your playlist on a DLNA server.
* DLNA Renderer - Play music on a DLNA server.
* Global Hotkeys - Control Pragha with multimedia keys.
* Global Hotkeys with gnome-media-keys daemon - Control Pragha with
  gnome-media-keys daemon.
* Koel - Append music on Koel server.
* Last.fm - Scrobbling, love, unlove song and append similar song to get
  related playlists.
* MPRIS2 - Control Pragha with MPRIS2 interface.
* MTP Devices - Management MTP devices.
* Notification - Show notification when change songs.
* Removable Media - Detect removable media and scan it.
* Song Info - Get Artist info, Lyrics and Album arts of yours songs.
* Get radios - Get radios on TuneIn.

%package plugins-devel
Summary:        Development Files for Pragha Plugins
Group:          Development/Libraries/C and C++
Requires:       pkgconfig(libpeas-1.0)
Requires:       pkgconfig(libpeas-gtk-1.0)

%description plugins-devel
This package contains development files needed to develop plugins for Pragha.

%lang_package

%prep
%setup -q

%build
%if 0%{?sle_version} >= 0150200 || (0%{?suse_version} >= 01550 && 0%{?is_opensuse})
export CPPFLAGS='-I/usr/include/gssdp-1.2/ -I/usr/include/gupnp-1.2/ -I/usr/include/libsoup-2.4/'
%else
export CPPFLAGS='-I/usr/include/gssdp-1.0/ -I/usr/include/gupnp-1.0/ -I/usr/include/libsoup-2.4/'
%endif
%configure
%make_build

%install
%make_install

find %{buildroot}%{_libdir}/%{name}/plugins/ -type f -name "*.la" -delete -print

# Remove installed docs -- I will install them myself.
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Install Norwegian Bokmål locale to the right place.
mv -f %{buildroot}%{_datadir}/locale/{no,nb}

# Install Korean locale to the right place.
mv -f %{buildroot}%{_datadir}/locale/{ko_KR,ko}

# Install Castillan locale to the right place.
mv -f %{buildroot}%{_datadir}/locale/{ca_ES,ca}

rm -f %{buildroot}%{_libdir}/pragha/libpragha.la

%fdupes -s %{buildroot}%{_datadir}/icons/hicolor/

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%find_lang %{name}

%files
# FIXME: add AUTHORS to docs if not empty.
%license COPYING
%doc FAQ NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/metainfo/io.github.pragha_music_player.metainfo.xml
%{_datadir}/pixmaps/%{name}/
%{_datadir}/pragha/
%{_mandir}/man?/*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/libpragha.so

%files plugins
%license COPYING
%doc FAQ NEWS README
%dir %{_libdir}/%{name}/plugins/
%dir %{_libdir}/%{name}/plugins/*/
%{_libdir}/%{name}/plugins/*/*.plugin
%{_libdir}/%{name}/plugins/*/*.so*

%files plugins-devel
%license COPYING
%doc NEWS
%{_includedir}/libpragha
%{_libdir}/pkgconfig/libpragha.pc

%files lang -f %{name}.lang

%changelog
