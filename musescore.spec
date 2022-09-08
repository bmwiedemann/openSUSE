#
# spec file for package musescore
#
# Copyright (c) 2022 SUSE LLC
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


%ifarch ppc64 ppc64le
%define qtwebengine 0
%else
%define qtwebengine 1
%endif

# Internal QML imports
%global __requires_exclude qmlimport\\((MuseScore|FileIO).*

%define         rname mscore
%define         version_lesser 3.6
%define         revision 3224f34
%define fontdir %{_datadir}/fonts/%{name}
%define docdir  %{_docdir}/%{name}
Name:           musescore
Version:        3.6.2
Release:        0
Summary:        A WYSIWYG music score typesetter
# Musescore code license is GPL-2.0
# Software in thirdparty is licensed under their own license
# Documentation is CC-SA
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://musescore.org
Source0:        https://github.com/musescore/MuseScore/archive/v%{version}/MuseScore-%{version}.tar.gz
Source1:        %{rname}.desktop
# MuseScore expect to be able to download the latest version of its soundfonts
# They are downloaded from the link conteinde in CMakeLists.text
# They are newer versions than the one included in the MuseScore tarball itself
Source2:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Changelog.md
Source3:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_License.md
Source4:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Readme.md
Source5:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General.sf3
# PATCH-FIX-OPENSUSE: openSUSE has qmake-qt5 qmake was reserved for qt4, which is no longer present
Patch0:         use-qtmake-qt5.patch
# PATCH-FIX-OPENSUSE: don't install qtwebengine files, they are not needed
Patch1:         use-system-qtwebengine-files.patch
# PATCH-FIX-OPENSUSE: don't use webview in startcentre (boo#1181604)
Patch2:         no-webview-in-startcentre.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Help5
BuildRequires:  libQt5QuickTemplates2-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  strip-nondeterminism
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
%if %qtwebengine
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
%endif
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
Requires:       %{name}-fonts = %{version}-%{release}
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2

%description
MuseScore is a graphical music typesetter. It allows for note entry on a
virtual note sheet. It has an integrated sequencer for immediate playing of the
score. MuseScore can import and export MusicXml and standard MIDI files.

%package fonts
Summary:        MuseScore fonts
License:        GPL-3.0-or-later WITH Font-exception-2.0 AND OFL-1.1
Group:          System/X11/Fonts
BuildArch:      noarch

%description fonts
Additional fonts for use by the MuseScore music notation program.

%prep
%autosetup -p1 -n MuseScore-%{version}
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} share/sound/

# fix EOL encoding
sed 's/\r$//' fonts/bravura/OFL-FAQ.txt > tmpfile
touch -r fonts/bravura/OFL-FAQ.txt tmpfile
mv -f tmpfile fonts/bravura/OFL-FAQ.txt

sed 's/\r$//' thirdparty/rtf2html/README > tmpfile
touch -r thirdparty/rtf2html/README tmpfile
mv -f tmpfile thirdparty/rtf2html/README

sed 's/\r$//' thirdparty/rtf2html/README.ru > tmpfile
touch -r thirdparty/rtf2html/README.ru tmpfile
mv -f tmpfile thirdparty/rtf2html/README.ru

sed 's/\r$//' thirdparty/portmidi/README.txt > tmpfile
touch -r thirdparty/portmidi/README.txt tmpfile
mv -f tmpfile thirdparty/portmidi/README.txt

%build
%define __builddir build.release
%cmake \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DMUSESCORE_BUILD_CONFIG=release \
       -DUSE_SYSTEM_FREETYPE="ON" \
%if %qtwebengine
       -DBUILD_WEBENGINE="ON" \
%else
       -DBUILD_WEBENGINE="OFF" \
%endif
       -DBUILD_TELEMETRY_MODULE=OFF \
       -DMUSESCORE_REVISION=%{revision}
%make_jobs lrelease all

# Put the desktop file in place for the packaging
cp %{SOURCE1} .

%install
%cmake_install
strip-nondeterminism -t zip %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/workspaces/*.workspace

# install fonts
mkdir -p %{buildroot}%{fontdir}
install -p -m 644 fonts/*.ttf %{buildroot}/%{fontdir}
install -p -m 644 fonts/*/*.ttf %{buildroot}/%{fontdir}
install -p -m 644 fonts/bravura/BravuraText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/campania/Campania.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/edwin/*.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/gootville/GootvilleText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/leland/LelandText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/musejazz/MuseJazzText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/petaluma/PetalumaText.otf %{buildroot}/%{fontdir}

# unique names for font docs
mv fonts/edwin/README.md         fonts/edwin/README.md.edwin
mv fonts/edwin/GPL_LICENSE.txt   fonts/edwin/GPL_LICENSE.txt.edwin
mv fonts/edwin/LICENSE.txt       fonts/edwin/LICENSE.txt.edwin
mv fonts/leland/README.md        fonts/leland/README.md.leland
mv fonts/leland/LICENSE.txt      fonts/leland/LICENSE.txt.leland

# update desktop file
%suse_update_desktop_file -n %{rname} AudioVideo AudioVideoEditing

# also package additional demos
mkdir -p %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos
install -p -m 644 demos/*.mscz %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos

# collect doc files
install -d -m 755 %{buildroot}%docdir
install -p -m 644 thirdparty/beatroot/COPYING         %{buildroot}%docdir/COPYING.beatroot
install -p -m 644 thirdparty/beatroot/README.txt      %{buildroot}%docdir/README.txt.beatroot
install -p -m 644 thirdparty/dtl/COPYING              %{buildroot}%docdir/COPYING.BSD.dtl
install -p -m 644 thirdparty/freetype/README          %{buildroot}%docdir/README.freetype
install -p -m 644 thirdparty/intervaltree/README      %{buildroot}%docdir/README.intervaltree
install -p -m 644 thirdparty/ofqf/README.md           %{buildroot}%docdir/README.md.ofqf
install -p -m 644 thirdparty/rtf2html/ChangeLog       %{buildroot}%docdir/ChangeLog.rtf2html
install -p -m 644 thirdparty/rtf2html/COPYING.LESSER  %{buildroot}%docdir/COPYING.LESSER.rtf2html
install -p -m 644 thirdparty/rtf2html/README          %{buildroot}%docdir/README.rtf2html
install -p -m 644 thirdparty/rtf2html/README.mscore   %{buildroot}%docdir/README.mscore.rtf2html
install -p -m 644 thirdparty/rtf2html/README.ru       %{buildroot}%docdir/README.ru.rtf2html
install -p -m 644 thirdparty/portmidi/README.txt      %{buildroot}%docdir/README.txt.portmidi
install -p -m 644 thirdparty/portmidi/license.txt     %{buildroot}%docdir/license.txt.portmidi
install -p -m 644 thirdparty/qt-google-analytics/README.md         %{buildroot}%docdir/README.md.qt-google-analytics
install -p -m 644 thirdparty/qt-google-analytics/LICENSE.txt       %{buildroot}%docdir/LICENSE.qt-google-analytics
install -p -m 644 thirdparty/singleapp/LGPL_EXCEPTION.txt %{buildroot}%docdir/LGPL_EXCEPTION.txt.singleapp
install -p -m 644 thirdparty/singleapp/LICENSE.GPL3   %{buildroot}%docdir/LICENSE.GPL3.singleapp
install -p -m 644 thirdparty/singleapp/LICENSE.LGPL   %{buildroot}%docdir/LICENSE.LGPL.singleapp
install -p -m 644 thirdparty/singleapp/README.TXT     %{buildroot}%docdir/README.TXT.singleapp

# aeolus not included in this build
#install -p -m 644 aeolus/AUTHORS                     %%{buildroot}%%{docdir}/AUTHORS.aeolus
#install -p -m 644 aeolus/COPYING                     %%{buildroot}%%{docdir}/COPYING.aeolus
#install -p -m 644 aeolus/README                      %%{buildroot}%%{docdir}/README.aeolus
#install -p -m 644 aeolus/README.mscore               %%{buildroot}%%{docdir}/README.mscore.aeolus
#install -p -m 644 aeolus/README.mscore1              %%{buildroot}%%{docdir}/README.mscore1.aeolus

install -p -m 644 bww2mxml/COPYING                    %{buildroot}%docdir/COPYING.bww2mxml
install -p -m 644 bww2mxml/README                     %{buildroot}%docdir/README.bww2mxml
install -p -m 644 effects/chorus/COPYING              %{buildroot}%docdir/COPYING.chorus
install -p -m 644 effects/chorus/README               %{buildroot}%docdir/README.chorus
install -p -m 644 effects/compressor/README           %{buildroot}%docdir/README.compressor
install -p -m 644 share/sound/README.md               %{buildroot}%docdir/README.md.sound
install -p -m 644 share/locale/README.md              %{buildroot}%docdir/README.md.locale
install -p -m 644 share/instruments/README.md         %{buildroot}%docdir/README.md.instruments
install -p -m 644 share/wallpaper/COPYRIGHT           %{buildroot}%docdir/COPYING.wallpaper

%fdupes %{buildroot}/%{_prefix}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post
%endif

%if 0%{?suse_version} < 1500
%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif

%files
%{_bindir}/%{name}
%{_bindir}/%{rname}
%{_datadir}/metainfo/org.musescore.MuseScore.appdata.xml
%{_datadir}/applications/%{rname}.desktop
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%dir %{_datadir}/%{rname}-%{version_lesser}
%{_datadir}/%{rname}-%{version_lesser}/*
%{_mandir}/man1/*
%doc README.md
%license LICENSE.GPL
%dir %docdir
%doc %docdir/*

%files fonts
%dir %{fontdir}
%{fontdir}/*.ttf
%{fontdir}/*.otf
%doc fonts/README.md
%doc fonts/bravura/bravura-text.md
%doc fonts/bravura/OFL-FAQ.txt
%doc fonts/bravura/OFL.txt
%doc fonts/campania/LICENSE
%doc fonts/gootville/readme.txt

# see section 'unique names for font docs' above
%doc fonts/edwin/README.md.edwin
%doc fonts/edwin/GPL_LICENSE.txt.edwin
%doc fonts/edwin/LICENSE.txt.edwin
%doc fonts/leland/README.md.leland
%doc fonts/leland/LICENSE.txt.leland

%changelog
