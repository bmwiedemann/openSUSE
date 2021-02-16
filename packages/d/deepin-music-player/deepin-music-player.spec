#
# spec file for package deepin-music-player
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2013-2020 Hillwood Yang <hillwood@opensuse.org>
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


Name:           deepin-music-player
Version:        6.0.1.91
Release:        0
Summary:        Deepin Music Player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/linuxdeepin/deepin-music
Source0:        https://github.com/linuxdeepin/deepin-music/archive/%{version}/deepin-music-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Fix-library-link.patch hillwood@opensuse.org - Fix library link
Patch0:         Fix-library-link.patch
# PATCH-FIX-UPSTREAM deepin-music-Qt-5_15.patch  hillwood@opensuse.org - Support Qt 5.15+
Patch1:         deepin-music-Qt-5_15.patch 
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Network-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xext)
Requires:       qt5integration
Provides:       deepin-music
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Music Player is a music player backed by gstreamer, with
customizable UI, and featuring music search by Pinyin and Quanpin. It
supports colorful lyrics, online audio support and a "mini mode".

%lang_package

%prep
%autosetup -p1 -n deepin-music-%{version}
sed -i 's/Exec=deepin-music/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-music/g' \
music/music-player/data/deepin-music.desktop

%build
%cmake
%make_build

%install
%cmake_install

find %{buildroot} -type f -name "*.a" -delete -print

%suse_update_desktop_file -r deepin-music Player AudioVideo
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE COPYING
%{_bindir}/deepin-music
%{_datadir}/applications/deepin-music.desktop
%{_datadir}/icons/hicolor/scalable/apps/deepin-music.svg

%files lang
%defattr(-,root,root,-)
%{_datadir}/deepin-music

%changelog
