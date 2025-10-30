#
# spec file for package musescore
#
# Copyright (c) 2025 SUSE LLC and contributors
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

# we do not generate proper provides for those controls and without excluding them from the requires list we can not install the package
%global __requires_exclude ^.*qml.*(Muse|MuseScore|FileIO).*$
# Workaround boo#1189991
%define _lto_cflags %{nil}
%define rname   mscore
%define version_lesser 4.6
%define fontdir %{_datadir}/fonts/%{name}
%define docdir  %{_docdir}/%{name}
Name:           musescore
Version:        4.6.3
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
Patch1:         musescore-fix-build-against-qt-6-10.patch
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} < 1560 && 0%{?sle_version} <= 150600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
%ifarch ppc64 ppc64le
# PPC builds often have memory issues, limit the number of parallel jobs
BuildRequires:  memory-constraints
%endif

# Qt tools want an UTF-8 locale
BuildRequires:  glibc-locale-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  strip-nondeterminism
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6QuickTemplates2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(tinyxml2)
BuildRequires:  pkgconfig(alsa)
# it could use this but our flac doesnt provide the cmake file and the finder in MuseScore does not find it just via pkgconfig
# BuildRequires:  pkgconfig(flac)
# it looks for it but then doesnt find it.
# BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jack)
# it looks for it but then doesnt find it.
# BuildRequires:  pkgconfig(lame)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
Requires:       %{name}-fonts = %{version}-%{release}
Requires:       qt6-qt5compat-imports
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
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
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
# it tries to use it but the finder apparently needs the cmake file
# TODO: -DMUE_COMPILE_USE_SYSTEM_FLAC:BOOL=ON \
%cmake \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DMUSESCORE_BUILD_CONFIGURATION=app \
       -DMUSE_APP_BUILD_MODE=release \
       -DMUE_BUILD_UNIT_TESTS=OFF \
       -DMUE_COMPILE_USE_SYSTEM_FREETYPE:BOOL=ON \
       -DMUE_COMPILE_USE_SYSTEM_HARFBUZZ:BOOL=ON \
       -DMUE_COMPILE_USE_SYSTEM_OPUS:BOOL=ON \
       -DMUE_COMPILE_USE_SYSTEM_OPUSENC:BOOL=ON \
       -DMUE_COMPILE_USE_SYSTEM_TINYXML:BOOL=ON \
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
install -p -m 644 fonts/*/*.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/bravura/BravuraText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/campania/Campania.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/edwin/*.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/gootville/GootvilleText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/leland/LelandText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/musejazz/MuseJazzText.otf %{buildroot}/%{fontdir}
install -p -m 644 fonts/petaluma/PetalumaText.otf %{buildroot}/%{fontdir}

for i in fonts/*/*.md fonts/*/LICENSE* ; do
  d=$(basename $(dirname $i)) ;
  cp ${i} $(basename $i).font.${d} ;
done

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
%license LICEN?E*.font.*
%doc fonts/gootville/readme.txt

# see section 'unique names for font docs' above
%doc README.md.font.*

%changelog
