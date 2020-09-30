#
# spec file for package clementine
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


%define rev b49afcc5b73162fba903095c5d85046804c9a283

%bcond_without git

%if 0%{?suse_version} > 1500
%bcond_without manpage
%else
%bcond_with manpage
%endif
%bcond_without qt5
%define gname Clementine

Name:           clementine
Version:        1.3.99
Release:        0
Summary:        A music player inspired by Amarok 1.4
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://clementine-player.org/
%if %{without git}
#Source:         https://github.com/clementine-player/%%{gname}/archive/%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
%else
Source0:        https://github.com/clementine-player/Clementine/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# PATCH-FEATURE-UPSTREAM uudisks2-support-for-devicemanager.patch
Patch1:         clementine-udisks-headers.patch
# Patch fix factory build, add -fPIC to moodbar build
Patch2:         clementine-moodbar-fpic.patch
# PATCH-FIX-OPENSUSE clementine-hidden-systray-icon.patch davejplater@gmail.com -- sys tray icon is hidden on some plasma5 systems.
Patch4:         clementine-hidden-systray-icon.patch
# PATCH-FEATURE-OPENSUSE
Patch6:         use_system_qxtglobalshortcut.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  update-desktop-files
%if %{with qt5}
#BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libmygpo-qt5)
BuildRequires:  pkgconfig(qxtglobalshortcut)
#BuildRequires:  pkgconfig(QxtCore-qt5)
%else
BuildRequires:  liblastfm-devel
BuildRequires:  libqxt-devel
BuildRequires:  pkgconfig(QJson)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtSql)
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib) > 1.11.1
Requires:       libtag1 >= 1.8
%if %{without qt5}
Recommends:     sni-qt
%else
Recommends:     projectM-data
%endif
# clementine-kde was last used in openSUSE 12.2.
# plasma_runner was dropped in Clementine 1.1.0.
Provides:       %{name}-kde = %{version}
Obsoletes:      %{name}-kde < %{version}

%description
Clementine is a music player and library organiser.
It is inspired by Amarok 1.4, focusing on a fast and easy-to-use
interface for searching and playing your music.

Features:

 * Search and play your local music library.
 * Play audio CDs.
 * Edit tags on audio files and organise your music.
 * Native desktop notifications.
 * Tabbed playlists, import and export M3U, XSPF, PLS and ASX.
 * Create smart playlists and dynamic playlists.
 * Download missing album cover art from Last.fm, MusicBrainz and Discogs.
 * Lyrics and artist biographies and photos.
 * Copy music to your iPod, iPhone, MTP or mass-storage USB player.
 * Queue manager.
 * Search and play songs you've uploaded to Box, Dropbox, Google Drive, and OneDrive
 * Listen to internet radio from Spotify, Grooveshark, SomaFM, Magnatune, Jamendo,
 SKY.fm, Digitally Imported, JAZZRADIO.com, Icecast and Subsonic servers.

%prep
%if %{without git}
%setup -q -n %{gname}-%{version}
%else
%setup -q -n %{gname}-%{rev}
%endif
%autopatch -p1

# NOTE: Build using system versions of libraries.
rm -rvf 3rdparty/taglib
rm -rvf 3rdparty/SPMediaKeyTap

%build
%ifarch %{arm} aarch64
%define _lto_cflags %{nil}
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing -ggdb"
export CXXFLAGS="$CFLAGS"
%cmake \
  -DBUILD_WERROR=OFF                   \
  -DUSE_SYSTEM_QTSINGLEAPPLICATION=OFF \
  -DUSE_SYSTEM_TAGLIB=ON               \
  -DUSE_SYSTEM_PROJECTM=ON             \
  -DBUNDLE_PROJECTM_PRESETS=OFF        \
%if %{with qt5}
  -DUSE_SYSTEM_QXT=ON                 \
%else
  -DUSE_SYSTEM_QXT=ON                  \
%endif
  -DENABLE_MOODBAR=ON                  \
  -DENABLE_DBUS=ON
make %{?_smp_mflags}

%install
%cmake_install

%if %{with manpage}
# Generate a man page with help2man.
mkdir -p %{buildroot}%{_mandir}/man1/
pushd %{buildroot}%{_mandir}/man1/
cp -f %{buildroot}%{_bindir}/%{name} ./
help2man --version-string="%{version}" -N -o %{name}.1 ./%{name}
rm -f %{name}
popd
%endif

%suse_update_desktop_file clementine Qt AudioVideo Audio Player

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc Changelog README.md
%license COPYING
%{_bindir}/clementine*
%{_datadir}/applications/clementine.desktop
%{_datadir}/icons/hicolor/*/apps/clementine.*
%if %{with manpage}
%{_mandir}/man1/%{name}.1%{?ext_man}
%endif
%if %{with qt5}
%{_datadir}/metainfo/
%{_datadir}/kservices5/
%else
%dir %{_datadir}/appdata/
%{_datadir}/appdata/clementine.appdata.xml
%dir %{_datadir}/kde4/
%dir %{_datadir}/kde4/services/
%{_datadir}/kde4/services/clementine-*.protocol
%endif

%changelog
