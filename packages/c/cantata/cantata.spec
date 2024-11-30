#
# spec file for package cantata
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


Name:           cantata
Version:        3.3.0
Release:        0
Summary:        Client for the Music Player Daemon (MPD)
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/nullobsi/cantata/
Source:         https://github.com/nullobsi/cantata/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  media-player-info
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(zlib)
Requires:       media-player-info
Requires:       mpd
Requires:       qt6-sql-sqlite
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme
%lang_package

%description
Cantata is a graphical client for MPD, supporting the following features:
 * Multiple MPD collections.
 * Customisable layout.
 * Songs grouped by album in play queue.
 * Context view to show artist, album, and song information of
   current track.
 * Tag editor.
 * File organizer - use tags to organize files and folders.
 * Ability to calculate ReplyGain tags
 * Dynamic playlists.
 * Online services; Jamendo, Magnatune, SoundCloud, and Podcasts.
 * Radio stream support - with the ability to search for streams via
   TuneIn, ShoutCast, or Dirble.
 * USB-Mass-Storage and MTP device support
 * Audio CD ripping and playback
 * Playback of non-MPD songs - via simple in-built HTTP server if
   connected to MPD via a standard socket, otherwise filepath is sent
   to MPD.
 * MPRISv2 DBUS interface.
 * Basic support for touch-style interface (views are made
   'flickable').
 * Scrobbling.
 * Ratings support.

Cantata started off as a fork of QtMPC, however, the code (and user
interface) is now very different to that of QtMPC. For more detailed
information, please refer to the main README.

%prep
%autosetup -p1

%build
%cmake -DENABLE_REMOTE_DEVICES=OFF \
    -DENABLE_CATEGORIZED_VIEW=OFF \
    -DBUILD_PLUGIN_DEBUG=OFF
%cmake_build

%install
%cmake_install

%find_lang %{name} --without-kde --with-qt --all-name --without-mo

%fdupes %{buildroot}

%files
%license LICENSE
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_libexecdir}/Cantata/*
%{_datadir}/Cantata/icons/*
%{_datadir}/Cantata/scripts/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/scalable/apps/dog.unix.cantata.Cantata.svg
%{_datadir}/icons/hicolor/symbolic/apps/dog.unix.cantata.Cantata-symbolic.svg
%{_datadir}/icons/hicolor/*x*/apps/dog.unix.cantata.Cantata.png
%dir %{_libexecdir}/Cantata
%dir %{_datadir}/Cantata
%dir %{_datadir}/Cantata/icons
%dir %{_datadir}/Cantata/scripts

%files lang -f %{name}.lang
%dir %{_datadir}/Cantata/translations
%{_datadir}/Cantata/translations/*

%changelog
