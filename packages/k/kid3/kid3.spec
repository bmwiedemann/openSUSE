#
# spec file for package kid3
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


# Internal QML imports
%global __requires_exclude qmlimport\\(Kid3.*
%if 0%{?suse_version} > 1500
%define qt_version 6
%else
%define qt_version 5
%endif

Name:           kid3
Version:        3.9.6
Release:        0
Summary:        Efficient ID3 Tag Editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://kid3.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  id3lib-devel
BuildRequires:  kf%{qt_version}-filesystem
BuildRequires:  libxslt-tools
BuildRequires:  python3 >= 3.6
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF%{qt_version}DocTools)
BuildRequires:  cmake(KF%{qt_version}KIO)
BuildRequires:  cmake(Qt%{qt_version}Core)
BuildRequires:  cmake(Qt%{qt_version}DBus)
BuildRequires:  cmake(Qt%{qt_version}Gui)
BuildRequires:  cmake(Qt%{qt_version}LinguistTools)
BuildRequires:  cmake(Qt%{qt_version}Multimedia)
BuildRequires:  cmake(Qt%{qt_version}Network)
BuildRequires:  cmake(Qt%{qt_version}Qml)
BuildRequires:  cmake(Qt%{qt_version}Quick)
BuildRequires:  cmake(Qt%{qt_version}Test)
BuildRequires:  cmake(Qt%{qt_version}UiTools)
BuildRequires:  cmake(Qt%{qt_version}Widgets)
BuildRequires:  cmake(Qt%{qt_version}Xml)
BuildRequires:  config(docbook-xsl-stylesheets)
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
export LC_ALL=en_US.UTF-8
options+="-DWITH_LIBDIR=%{_lib}/kid3 -DWITH_PLUGINSDIR=%{_lib}/kid3/plugins "
options+="-DWITH_CHROMAPRINT_FFMPEG=ON -DWITH_FFMPEG=ON -DWITH_GSTREAMER=ON "
options+="-DWITH_DOCDIR=share/doc/packages/kid3-qt "
options+="-DCMAKE_SKIP_RPATH=ON -DWITH_QMLDIR=%{_lib}/qt%{qt_version}/qml/kid3 "
%if %{qt_version} == 6
%{cmake_kf6} -DBUILD_WITH_QT6=ON $options
%{kf6_build}
%else
%cmake_kf5 -d build -- $options
%make_jobs
%endif

%install
%if %{qt_version} == 6
%{kf6_install}
%else
%kf5_makeinstall -C build
%endif

pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
gzip -dS .svgz kid3.svgz
mv kid3 kid3.svg
popd

chmod 644 %{buildroot}%{_kf5_applicationsdir}/org.kde.kid3.desktop

%find_lang %{name} %{name}-core.lang --without-kde --with-qt --all-name --without-mo

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat <<EOF >%{buildroot}%{_sysconfdir}/ld.so.conf.d/kid3.conf
%{_libdir}/kid3
EOF

%post core -p /sbin/ldconfig

%postun core -p /sbin/ldconfig

%files
%dir %{_datadir}/metainfo
%{expand:%{_kf%{qt_version}_bindir}}/kid3
%{expand:%{_kf%{qt_version}_iconsdir}}/hicolor/*/apps/kid3.*
%{expand:%{_kf%{qt_version}_kxmlguidir}}/kid3/
%{expand:%{_kf%{qt_version}_applicationsdir}}/org.kde.kid3.desktop
%{expand:%{_kf%{qt_version}_appstreamdir}}/org.kde.kid3.appdata.xml

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
%{_libdir}/qt%{qt_version}/qml/kid3/
%config %{_sysconfdir}/ld.so.conf.d/kid3.conf
%{_datadir}/dbus-1/interfaces/org.kde.Kid3.xml
%{_mandir}/man1/kid3.1%{ext_man}
%{_mandir}/*/man1/kid3.1%{ext_man}

%files doc
%doc %{expand:%{_kf%{qt_version}_htmldir}}/*/kid3/

%files qt-doc
%{_docdir}/kid3-qt/

%files -n %{name}-core-lang -f %{name}-core.lang
%dir %{_datadir}/kid3
%dir %{_datadir}/kid3/translations

%changelog
