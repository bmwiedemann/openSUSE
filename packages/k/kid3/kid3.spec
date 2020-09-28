#
# spec file for package kid3
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


Name:           kid3
Version:        3.8.4
Release:        0
Summary:        Efficient ID3 Tag Editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            https://kid3.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
BuildRequires:  hicolor-icon-theme
BuildRequires:  id3lib-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libxslt-tools
BuildRequires:  python >= 3.6
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  config(docbook-xsl-stylesheets)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  pkgconfig(vorbis)
Requires:       %{name}-core = %{version}
Requires:       libxslt-tools
Requires:       xdg-utils
# kid3 and kid3-qt can exist together on a system but the user will have two packages with the same functionality.
Conflicts:      kid3-qt = %{version}

%description
f you want to easily tag multiple MP3, Ogg/Vorbis, Opus, DSF, FLAC,
MPC, MP4/AAC, MP2, Opus, Speex, TrueAudio, WavPack and WMA files 
(e.g. full albums) without typing the same information again and
again and have control over both ID3v1 and ID3v2 tags,
then Kid3 is the program you are looking for.

With Kid3 you can:
- Edit ID3v1.1 tags
- Edit all ID3v2.3 and ID3v2.4 frames
- Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
- Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2, Speex,
  TrueAudio, WavPack, WMA, AIFF and WAV files
- Edit tags of multiple files, e.g. the artist, album, year and
  genre of all files of an album typically have the same values
  and can be set together.
- Generate tags from filenames
- Generate tags from the contents of tag fields
- Generate filenames from tags
- Rename and create directories from tags
- Generate playlist files
- Automatically convert upper and lower case and replace strings
- Import from freedb2.org, MusicBrainz, Discogs, Amazon and other
  sources of album data
- Export tags as CSV, HTML, playlists, Kover XML and in other formats
- Edit synchronized lyrics and event timing codes,import and export LRC files

This package uses KDE libraries, if you do not use KDE you should use kid3-qt.
For a commandline interface you can use kid3-cli.

%package qt
Summary:        Efficient ID3 Tag Editor
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-core = %{version}
Requires:       xdg-utils
# kid3 and kid3-qt can exist together on a system but the user will have two packages with the same functionality.
Conflicts:      kid3 = %{version}
Obsoletes:      kid3-qt < %{version}

%description qt
With Kid3 you can:
  - Edit ID3v1.1 tags
  - Edit all ID3v2.3 and ID3v2.4 frames
  - Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
  - Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex,
    TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules (MOD,
    S3M, IT, XM).
  - Edit tags of multiple files, e.g. the artist, album, year and genre
    of all files of an album typically have the same values and can be
    set together.
  - Generate tags from filenames
  - Generate tags from the contents of tag fields
  - Generate filenames from tags
  - Generate playlist files
  - Automatic case conversion and string translation
  - Import and export album data
  - Import from gnudb.org, TrackType.org, MusicBrainz, Discogs, Amazon

This package does not use KDE libraries, if you use KDE you should use kid3.
For a commandline interface you can use kid3-cli.

%package cli
Summary:        Efficient ID3 Tag Editor
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-core = %{version}

%description cli
With Kid3 you can:
  - Edit ID3v1.1 tags
  - Edit all ID3v2.3 and ID3v2.4 frames
  - Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
  - Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex,
    TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules (MOD,
    S3M, IT, XM).
  - Edit tags of multiple files, e.g. the artist, album, year and genre
    of all files of an album typically have the same values and can be
    set together.
  - Generate tags from filenames
  - Generate tags from the contents of tag fields
  - Generate filenames from tags
  - Generate playlist files
  - Automatic case conversion and string translation
  - Import and export album data
  - Import from gnudb.org, TrackType.org, MusicBrainz, Discogs, Amazon

This package contains a command line interface for Kid3, for a GUI you can
use kid3-qt or kid3.

%package doc
Summary:        Documentation for %{name}
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name} = %{version}

%description doc
This package provides documentation and help files for %{name}.

%package qt-doc
Summary:        Documentation for %{name}-qt
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-qt = %{version}

%description qt-doc
This package provides documentation and help files for %{name}-qt.

%package  core
Summary:        Efficient ID3 Tag Editor: Libraries and Data
Group:          Productivity/Multimedia/Sound/Utilities
Recommends:     kid3-trans-lang = %{version}

%description  core
This package contains common libraries and data files used by kid3, kid3-qt, and kid3-cli.

%lang_package -n %{name}-core

%prep
%autosetup -p1

%build
options+="-DWITH_LIBDIR=%{_lib}/kid3 -DWITH_PLUGINSDIR=%{_lib}/kid3/plugins "
options+="-DWITH_CHROMAPRINT_FFMPEG=ON -DWITH_FFMPEG=ON -DWITH_GSTREAMER=ON "
options+="-DWITH_DOCDIR=share/doc/packages/kid3-qt "
options+="-DCMAKE_SKIP_RPATH=ON -DWITH_QMLDIR=%{_lib}/qt5/qml/kid3 "
%cmake_kf5 -d build -- $options
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 %make_jobs

%install
%kf5_makeinstall -C build

pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
gzip -dS .svgz kid3.svgz
mv kid3 kid3.svg
popd

%find_lang %{name} %{name}-core.lang --without-kde --with-qt --all-name --without-mo

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat <<EOF >%{buildroot}%{_sysconfdir}/ld.so.conf.d/kid3.conf
%{_libdir}/kid3
EOF

rm %{buildroot}%{_libdir}/kid3/libkid3-*.so

%post core -p /sbin/ldconfig

%postun core -p /sbin/ldconfig

%files
%dir %{_datadir}/metainfo
%{_kf5_bindir}/kid3
%{_kf5_iconsdir}/hicolor/*/apps/kid3.*
%{_kf5_kxmlguidir}/kid3/
%{_kf5_applicationsdir}/org.kde.kid3.desktop
%{_kf5_appstreamdir}/org.kde.kid3.appdata.xml

%files qt
%dir %{_datadir}/metainfo
%{_datadir}/applications/org.kde.kid3-qt.desktop
%{_datadir}/metainfo/org.kde.kid3-qt.appdata.xml
%{_bindir}/kid3-qt
%{_datadir}/icons/hicolor/*/apps/kid3-qt.*
%{_mandir}/man1/kid3-qt.1%{ext_man}
%{_mandir}/*/man1/kid3-qt.1%{ext_man}

%files cli
%{_bindir}/kid3-cli
%{_mandir}/man1/kid3-cli.1%{ext_man}
%{_mandir}/*/man1/kid3-cli.1%{ext_man}

%files core
%doc AUTHORS ChangeLog README
%license COPYING LICENSE
%{_libdir}/kid3/
%{_libdir}/qt5/qml/kid3/
%config %{_sysconfdir}/ld.so.conf.d/kid3.conf
%{_datadir}/dbus-1/interfaces/org.kde.Kid3.xml
%{_mandir}/man1/kid3.1%{ext_man}
%{_mandir}/*/man1/kid3.1%{ext_man}

%files doc
%doc %{_kf5_htmldir}/*/kid3/

%files qt-doc
%{_docdir}/kid3-qt/

%files -n %{name}-core-lang -f %{name}-core.lang
%dir %{_datadir}/kid3
%dir %{_datadir}/kid3/translations

%changelog
