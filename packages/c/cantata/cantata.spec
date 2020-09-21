#
# spec file for package cantata
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


Name:           cantata
Version:        2.4.2
Release:        0
Summary:        Client for the Music Player Daemon (MPD)
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/CDrummond/cantata/
Source0:        https://github.com/CDrummond/cantata/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE  fix-translations-with-qt5.diff  -- Make sure that it finds the right lrelease and lconvert binaries with Qt5 (cantata only find the 64bits lrelease).
Patch0:         fix-translations-with-qt5.diff
BuildRequires:  fdupes
BuildRequires:  media-player-info
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(taglib-extras)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(zlib)
Requires:       media-player-info
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     %{name}-lang = %{version}
Recommends:     mpd
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
    -DENABLE_CATEGORIZED_VIEW=OFF
%cmake_build

%install
%cmake_install
%suse_update_desktop_file %{name}

%find_lang %{name} --without-kde --with-qt --all-name --without-mo

%fdupes %{buildroot}

%files
%license LICENSE
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/translations/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%doc AUTHORS ChangeLog README README.md TODO

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations

%changelog
