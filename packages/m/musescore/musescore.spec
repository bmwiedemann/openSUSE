#
# spec file for package musescore
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         rname mscore
%define         version_lesser 3.3
%define fontdir %{_datadir}/fonts/%{name}
%define docdir  %{_docdir}/%{name}
Name:           musescore
Version:        3.3.0
Release:        0
Summary:        A WYSIWYG music score typesetter
# Musescore code license is GPL-2.0
# Software in thirdparty is licensed under their own license
# Documentation is CC-SA
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://musescore.org
Source0:        https://github.com/musescore/MuseScore/archive/v%{version_lesser}/MuseScore-%{version_lesser}.tar.gz
Source1:        %{rname}.desktop
# PATCH-FIX-UPSTREAM: see https://github.com/musescore/MuseScore/releases
Patch0:         correct-revision.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake >= 3.0
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-devel
BuildRequires:  libQt5WebKitWidgets-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libpulse-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  libqt5-qtxmlpatterns-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  update-desktop-files
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
%setup -q -n MuseScore-%{version_lesser}
%patch0 -p1

# remove precompiled binary
rm thirdparty/rtf2html/rtf2html

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

# remove executable bit
chmod -x fonts/gootville/readme.txt

%build
%define __builddir build.release
%cmake \
       -DUSE_SYSTEM_FREETYPE="ON" \
       -DBUILD_WEBENGINE="OFF" \
       -DBUILD_CRASH_REPORTER="OFF"
%make_jobs lrelease all

# Put the desktop file in place for the packaging
cp %{SOURCE1} .

%install
%cmake_install

# install fonts
mkdir -p %{buildroot}%{fontdir}
install -p -m 644 fonts/*.ttf %{buildroot}/%{fontdir}

# update desktop file
%suse_update_desktop_file -n %{rname} AudioVideo AudioVideoEditing

# also package additional demos
mkdir -p %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos
install -p -m 644 demos/*.mscz %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos

# collect doc files
install -d -m 755 %{buildroot}%docdir
install -p -m 644 thirdparty/beatroot/COPYING         %{buildroot}%docdir/COPYING.beatroot
install -p -m 644 thirdparty/beatroot/README.txt      %{buildroot}%docdir/README.txt.beatroot
install -p -m 644 thirdparty/intervaltree/README      %{buildroot}%docdir/README.intervaltree
install -p -m 644 thirdparty/kQOAuth/COPYING          %{buildroot}%docdir/COPYING.kQOAuth
install -p -m 644 thirdparty/kQOAuth/README           %{buildroot}%docdir/README.kQOAuth
install -p -m 644 thirdparty/kQOAuth/README.md        %{buildroot}%docdir/README.md.kQOAuth
install -p -m 644 thirdparty/ofqf/README.md           %{buildroot}%docdir/README.md.ofqf
install -p -m 644 thirdparty/rtf2html/ChangeLog       %{buildroot}%docdir/ChangeLog.rtf2html
install -p -m 644 thirdparty/rtf2html/COPYING.LESSER  %{buildroot}%docdir/COPYING.LESSER.rtf2html
install -p -m 644 thirdparty/rtf2html/README          %{buildroot}%docdir/README.rtf2html
install -p -m 644 thirdparty/rtf2html/README.mscore   %{buildroot}%docdir/README.mscore.rtf2html
install -p -m 644 thirdparty/rtf2html/README.ru       %{buildroot}%docdir/README.ru.rtf2html
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
install -p -m 644 zerberus/README                     %{buildroot}%docdir/README.zerberus

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
%doc fonts/README.md
%doc fonts/bravura/bravura-text.md
%doc fonts/bravura/OFL-FAQ.txt
%doc fonts/bravura/OFL.txt
%doc fonts/gootville/readme.txt

%changelog
