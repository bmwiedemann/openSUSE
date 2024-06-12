#
# spec file for package musescore
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
%global __requires_exclude qmlimport\\((MuseScore|FileIO).*
# Workaround boo#1189991
%define _lto_cflags %{nil}
%define rname   mscore
%define version_lesser 4.3
%define fontdir %{_datadir}/fonts/%{name}
%define docdir  %{_docdir}/%{name}
Name:           musescore
Version:        4.3.2
Release:        0
Summary:        A WYSIWYG music score typesetter
# Licenses in MuseScore are a mess. To help other maintainers I give the following overview:
# Musescore code license is GPL-3.0 with font exception (see LICENSE.rtf in top dir)
# although some files mention GPL-2.0, probably for historical reasons
# Software in thirdparty is licensed under their own license
# thirdparty/beatroot: GPL 2.0 or later
# thirdparty/dr_libs: Public Domain OR MIT no attribution
# thirdparty/dtl: BSD
# thirdparty/flac: BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.2-only
# thirdparty/fluidsytn: LGPL-2.1
# thirdparty/freetype): FTL (we use system freetype)
# thirdparty/google_crashpad_client: Apache 2.0 (we don't build with this)
# thirdparty/googletest: BSD 3
# thirdparty/invaltree: MIT
# thirdparty/kddockwidgets: GPL-2.0-only OR GPL-3.0-only
# thirdparty/lame: LGPL 2
# thirdparty/opus and opusenc: BSD 3
# thirdparty/rtf2html: LGPL-2.1
# thirdparty/singleapp: the actual code has BSD 3 (although GPL and LGPL are included)
# thirdparty/stb: MIT
# the soundfont we musescore uses (see below) is BSD 3
License:        Apache-2.0 AND BSD-3-Clause AND FTL AND GPL-2.0-only AND GPL-3.0-only WITH Font-exception-2.0 AND GPL-2.0-or-later AND GFDL-1.2-only AND LGPL-2.0-only AND LGPL-2.1-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://musescore.org
Source0:        https://github.com/musescore/MuseScore/archive/refs/tags/v%{version}.tar.gz#/MuseScore-%{version}.tar.gz
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

BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} < 1560 && 0%{?sle_version} <= 150600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
%ifarch ppc64 ppc64le
# PPC builds often have memory issues, limit the number of parallel jobs
BuildRequires:  memory-constraints
%endif
BuildRequires:  pkgconfig
BuildRequires:  strip-nondeterminism
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
# For the following arch build fails in the crashpad client,
# Maybe repairable? Disabled until a solution is found by someone.
ExcludeArch:    aarch64 ppc64 ppc64le

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

## fix missing -ldl for Leaps
# comment out because error
#TODO: check if still needed
#sed -i 's/\(target_link_libraries(mscore ${LINK_LIB}\)/\1 ${CMAKE_DL_LIBS}/' src/main/CMakeLists.txt

%build
# Limit memory / threads on PowerPC to avoid memory issues
%ifarch ppc64 ppc64le
%limit_build -m 2000
%endif

%if 0%{?suse_version} < 1560 && 0%{?sle_version} <= 150600
export CC=gcc-12
export CXX=g++-12
%endif

%define __builddir build.release
# TODO:
# find out what those do:
# BUILD_VIDEOEXPORT_MODULE:BOOL=ON
# find out how to enable this
# BUILD_VST:BOOL=ON
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DMUSESCORE_BUILD_CONFIGURATION=app \
       -DMUSESCORE_BUILD_MODE=release \
       -DMUE_BUILD_UNIT_TESTS=OFF \
       -DMUE_COMPILE_USE_SYSTEM_FREETYPE=ON \
       -DMUE_ENABLE_AUDIO_JACK=OFF \
       -DMUE_BUILD_UPDATE_MODULE=OFF \
       -DMUE_BUILD_CRASHPAD_CLIENT=OFF \
       -Wno-dev
%cmake_build

%install
%cmake_install

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

# collect doc files
install -d -m 755 %{buildroot}%docdir
install -p -m 644 README.SUSE                         %{buildroot}%docdir/
install -p -m 644 thirdparty/beatroot/COPYING         %{buildroot}%docdir/COPYING.beatroot
install -p -m 644 thirdparty/beatroot/README.txt      %{buildroot}%docdir/README.txt.beatroot
install -p -m 644 thirdparty/dtl/COPYING              %{buildroot}%docdir/COPYING.BSD.dtl
install -p -m 644 src/framework/draw/thirdparty/freetype/freetype-2.13.1/README          %{buildroot}%docdir/README.freetype
install -p -m 644 thirdparty/intervaltree/README      %{buildroot}%docdir/README.intervaltree
install -p -m 644 thirdparty/rtf2html/ChangeLog       %{buildroot}%docdir/ChangeLog.rtf2html
install -p -m 644 thirdparty/rtf2html/COPYING.LESSER  %{buildroot}%docdir/COPYING.LESSER.rtf2html
install -p -m 644 thirdparty/rtf2html/README          %{buildroot}%docdir/README.rtf2html
install -p -m 644 thirdparty/rtf2html/README.mscore   %{buildroot}%docdir/README.mscore.rtf2html
install -p -m 644 thirdparty/rtf2html/README.ru       %{buildroot}%docdir/README.ru.rtf2html

install -p -m 644 tools/bww2mxml/COPYING              %{buildroot}%docdir/COPYING.bww2mxml
install -p -m 644 tools/bww2mxml/README               %{buildroot}%docdir/README.bww2mxml
install -p -m 644 share/sound/README.md               %{buildroot}%docdir/README.md.sound
install -p -m 644 share/instruments/README.md         %{buildroot}%docdir/README.md.instruments
install -p -m 644 share/wallpapers/COPYRIGHT          %{buildroot}%docdir/COPYING.wallpaper

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE.txt
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
%exclude %{_includedir}/
%exclude %{_libdir}/

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

%changelog
