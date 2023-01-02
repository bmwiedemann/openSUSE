#
# spec file for package musescore
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


# Internal QML imports
%global __requires_exclude qmlimport\\((MuseScore|FileIO).*
# Workaround boo#1189991
%define _lto_cflags %{nil}
%define rname   mscore
%define version_lesser 4.0
%define revision 5485621
%define fontdir %{_datadir}/fonts/%{name}
%define docdir  %{_docdir}/%{name}
Name:           musescore
Version:        4.0
Release:        0
Summary:        A WYSIWYG music score typesetter
# Musescore code license is GPL-2.0
# Software in thirdparty is licensed under their own license
# Documentation is CC-SA
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://musescore.org
Source0:        https://github.com/musescore/MuseScore/archive/v%{version}/MuseScore-%{version}.tar.gz
# MuseScore expect to be able to download the latest version of its soundfonts
# They are downloaded from the link conteinde in CMakeLists.text
# They are newer versions than the one included in the MuseScore tarball itself
Source1:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Changelog.md
Source2:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_License.md
Source3:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Readme.md
Source4:        https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General.sf3
Source5:        README.SUSE
# PATCH-FIX-OPENSUSE: openSUSE has qmake-qt5 qmake was reserved for qt4, which is no longer present
Patch0:         use-qtmake-qt5.patch
# PATCH-FIX-UPSTREAM: fix build with jack on linux.
Patch1:         0dde64eef84.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  strip-nondeterminism
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5NetworkAuth)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5QuickTemplates2)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
Requires:       %{name}-fonts = %{version}-%{release}
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
Requires:       ( alsa-plugins-pulse if pulseaudio )
Requires:       ( pipewire-alsa      if pipewire )

%description
MuseScore is a graphical music typesetter. It allows for note entry on a
virtual note sheet. It has an integrated sequencer for immediate playing of the
score. MuseScore can import and export MusicXml and standard MIDI files.

Regarding Muse-Hub and VSTs, you should really read:
%{_docdir}/%{name}/README.SUSE.

%package fonts
Summary:        MuseScore fonts
License:        GPL-3.0-or-later WITH Font-exception-2.0 AND OFL-1.1
Group:          System/X11/Fonts
BuildArch:      noarch

%description fonts
Additional fonts for use by the MuseScore music notation program.

%package devel
Summary:        MuseScore development files
License:        GPL-3.0-or-later WITH Font-exception-2.0 AND OFL-1.1
Group:          Development/Libraries/C and C++

%description devel
MuseScore files, used for plugin development.

%prep
%autosetup -p1 -n MuseScore-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} share/sound/
cp %{SOURCE5} .

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

# fix missing -ldl for Leaps
sed -i 's/\(target_link_libraries(mscore ${LINK_LIB}\)/\1 ${CMAKE_DL_LIBS}/' src/main/CMakeLists.txt

%build
%define __builddir build.release
# TODO:
# find out what those do:
# BUILD_VIDEOEXPORT_MODULE:BOOL=ON
# find out how to enable this
# BUILD_VST:BOOL=ON
# -DBUILD_UPDATE_MODULE:BOOL=OFF triggers bug  https://github.com/musescore/MuseScore/issues/15617
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DMUSESCORE_BUILD_CONFIG=release \
       -DBUILD_UNIT_TESTS=OFF \
       -DUSE_SYSTEM_FREETYPE=ON \
       -DBUILD_JACK:BOOL=ON \
       -DBUILD_UPDATE_MODULE:BOOL=ON \
       -DBUILD_CRASHPAD_CLIENT=OFF \
       -DMUSESCORE_REVISION=%{revision}
%make_jobs

%install
%cmake_install

# don't package staic libs
rm %{buildroot}%{_libdir}/*.a

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
mv fonts/edwin/LICENSE.txt       fonts/edwin/LICENSE.txt.edwin
mv fonts/leland/README.md        fonts/leland/README.md.leland
mv fonts/leland/LICENSE.txt      fonts/leland/LICENSE.txt.leland

# also package additional demos
mkdir -p %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos
install -p -m 644 demos/*.mscz %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos

# Remove opus devel files, they are provided by system
rm -rf %{buildroot}%{_includedir}/opus
# Delete crashpad binary
rm -rf %{buildroot}%{_bindir}/crashpad_handler

# collect doc files
install -d -m 755 %{buildroot}%docdir
install -p -m 644 README.SUSE                         %{buildroot}%docdir/
install -p -m 644 thirdparty/beatroot/COPYING         %{buildroot}%docdir/COPYING.beatroot
install -p -m 644 thirdparty/beatroot/README.txt      %{buildroot}%docdir/README.txt.beatroot
install -p -m 644 thirdparty/dtl/COPYING              %{buildroot}%docdir/COPYING.BSD.dtl
install -p -m 644 thirdparty/freetype/README          %{buildroot}%docdir/README.freetype
install -p -m 644 thirdparty/intervaltree/README      %{buildroot}%docdir/README.intervaltree
install -p -m 644 thirdparty/rtf2html/ChangeLog       %{buildroot}%docdir/ChangeLog.rtf2html
install -p -m 644 thirdparty/rtf2html/COPYING.LESSER  %{buildroot}%docdir/COPYING.LESSER.rtf2html
install -p -m 644 thirdparty/rtf2html/README          %{buildroot}%docdir/README.rtf2html
install -p -m 644 thirdparty/rtf2html/README.mscore   %{buildroot}%docdir/README.mscore.rtf2html
install -p -m 644 thirdparty/rtf2html/README.ru       %{buildroot}%docdir/README.ru.rtf2html
install -p -m 644 thirdparty/singleapp/LGPL_EXCEPTION.txt %{buildroot}%docdir/LGPL_EXCEPTION.txt.singleapp
install -p -m 644 thirdparty/singleapp/LICENSE.GPL3   %{buildroot}%docdir/LICENSE.GPL3.singleapp
install -p -m 644 thirdparty/singleapp/LICENSE.LGPL   %{buildroot}%docdir/LICENSE.LGPL.singleapp
install -p -m 644 thirdparty/singleapp/README.TXT     %{buildroot}%docdir/README.TXT.singleapp

install -p -m 644 tools/bww2mxml/COPYING              %{buildroot}%docdir/COPYING.bww2mxml
install -p -m 644 tools/bww2mxml/README               %{buildroot}%docdir/README.bww2mxml
install -p -m 644 share/sound/README.md               %{buildroot}%docdir/README.md.sound
install -p -m 644 share/instruments/README.md         %{buildroot}%docdir/README.md.instruments
install -p -m 644 share/wallpapers/COPYRIGHT          %{buildroot}%docdir/COPYING.wallpaper

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
%license LICENSE.GPL
%{_bindir}/%{rname}
%{_datadir}/metainfo/org.musescore.MuseScore.appdata.xml
%{_datadir}/applications/org.musescore.MuseScore.desktop
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%dir %{_datadir}/%{rname}-%{version_lesser}
%{_datadir}/%{rname}-%{version_lesser}/*
%{_mandir}/man1/*
%doc README.md README.SUSE
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
%license fonts/campania/LICENSE
%doc fonts/gootville/readme.txt

# see section 'unique names for font docs' above
%doc fonts/edwin/README.md.edwin
%license fonts/edwin/LICENSE.txt.edwin
%doc fonts/leland/README.md.leland
%license fonts/leland/LICENSE.txt.leland

%files devel
%license LICENSE.GPL
%{_includedir}/kddockwidgets
%{_libdir}/cmake

%changelog
