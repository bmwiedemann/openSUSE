#
# spec file for package mediainfo
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2007-2011 The Packman Team
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


Name:           mediainfo
Version:        22.12
Release:        0
Summary:        Audio/video file technical and tag information utility
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://mediaarea.net
Source0:        https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  pkgconfig(libmediainfo) = %{version}
BuildRequires:  pkgconfig(libzen)
BuildRequires:  pkgconfig(zlib)
Provides:       MediaInfo = 0.7.7.8
Obsoletes:      MediaInfo < 0.7.7.8

%description
MediaInfo supplies technical and tag information about a video or
audio file.

It reads the following information:
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

It supports the following containers/codecs:
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%package gui
Summary:        GUI for mediainfo
Group:          Productivity/Multimedia/Other
Provides:       MediaInfo-gui = 0.7.7.8
Obsoletes:      MediaInfo-gui < 0.7.7.8

%description gui
This package contains a Frontend for mediainfo.

MediaInfo supplies technical and tag information about a video or
audio file.

%package -n kf5-mediainfo
Summary:        KF5 extension for mediainfo-gui
Group:          Productivity/Multimedia/Other
Requires:       %{name}-gui
Obsoletes:      kde4-%{name} < %{version}
Provides:       kde4-%{name} = %{version}

%description -n kf5-mediainfo
KF5 context menu extension for mediainfo-gui.

%prep
%setup -q -n MediaInfo
sed -i 's/\r$//' *.html *.txt Release/*.txt
chmod 0644 *.html *.txt Release/*.txt

%build
# build CLI
pushd Project/GNU/CLI
    autoreconf -fiv
    %configure
    make %{?_smp_mflags}
popd

# now build GUI
pushd Project/GNU/GUI
    autoreconf -fiv
    %configure
    make %{?_smp_mflags}
popd

%install
pushd Project/GNU/CLI
%make_install
popd

pushd Project/GNU/GUI
%make_install
popd

# icon
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 Source/Resource/Image/MediaInfo.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/pixmaps/mediainfo-gui.png

rm %{buildroot}%{_datadir}/kde4/services/ServiceMenus/mediainfo-gui.desktop
%suse_update_desktop_file -n %{name}-gui AudioVideo AudioVideoEditing

# these files are just ridicully large:
gzip -n -9 License.html
gzip -n -9 History_*.txt
%fdupes -s %{buildroot}/%{_datadir}

%files
%defattr(-,root,root,-)
%doc Release/ReadMe_CLI_Linux.txt
%doc License.html.gz History_CLI.txt.gz
%{_bindir}/mediainfo

%files gui
%license License.html.gz
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt.gz
%{_bindir}/mediainfo-gui
%dir %{_datadir}/metainfo
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/mediainfo-gui.metainfo.xml

%files -n kf5-mediainfo
%dir %{_kf5_servicesdir}
%dir %{_kf5_servicesdir}/ServiceMenus
%dir %{_datadir}/apps
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_kf5_servicesdir}/ServiceMenus/*.desktop

%changelog
