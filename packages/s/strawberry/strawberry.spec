#
# spec file for package strawberry
#
# Copyright (c) 2023 SUSE LLC
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


Name:           strawberry
Version:        1.0.13
Release:        0
Summary:        A music player and music collection organizer
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://www.strawberrymusicplayer.org/
Source:         https://files.strawberrymusicplayer.org/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
%if 0%{?sle_version} == 150400 || 0%{?sle_version} == 150500
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%else
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3) >= 3.9
BuildRequires:  pkgconfig(taglib) >= 1.11.1

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
Requires:       qt6-sql-sqlite
%else
Requires:       libQt5Sql5-sqlite
%endif

%description
Strawberry is a music player and music collection organizer.
It is a fork of Clementine. The name is inspired by the band Strawbs.

Features:
  - Play and organize music
  - Supports WAV, FLAC, WavPack, DSF, DSDIFF, Ogg FLAC, Ogg Vorbis, Ogg Opus, Ogg Speex, MPC, TrueAudio,
    AIFF, MP4, MP3, ASF and Monkey's Audio.
  - Audio CD playback
  - Native desktop notifications
  - Playlists in multiple formats
  - Advanced audio output and device options
  - Edit tags on music files
  - Fetch tags from MusicBrainz
  - Album cover art from Last.fm, Musicbrainz, Discogs, Musixmatch, Deezer, Tidal, Qobuz and Spotify
  - Song lyrics from AudD, Genius, Musixmatch, ChartLyrics, lyrics.ovh and lololyrics.com
  - Support for multiple backends
  - Audio analyzer
  - Equalizer
  - Transfer music to iPod, MTP or mass-storage USB player
  - Scrobbler with support for Last.fm, Libre.fm and ListenBrainz
  - Subsonic streaming support

%prep
%setup -q

%build
%if 0%{?sle_version} == 150400 || 0%{?sle_version} == 150500
export CC="gcc-11"
export CXX="g++-11"
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%cmake -DBUILD_WERROR=OFF \
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
       -DQT_MAJOR_VERSION=6
%else
       -DQT_MAJOR_VERSION=5
%endif
%cmake_build

%install
%cmake_install

%suse_update_desktop_file org.strawberrymusicplayer.strawberry Qt AudioVideo Audio Player

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.strawberrymusicplayer.strawberry.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml

%files
%doc README.md Changelog
%license COPYING
%{_bindir}/strawberry*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/strawberry.*
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-tagreader.1%{?ext_man}

%changelog
