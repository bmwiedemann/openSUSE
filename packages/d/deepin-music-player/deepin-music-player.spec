#
# spec file for package deepin-music-player
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013-2021 Hillwood Yang <hillwood@opensuse.org>
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-music-player
Version:        6.2.18
Release:        0
Summary:        Deepin Music Player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/linuxdeepin/deepin-music
Source0:        https://github.com/linuxdeepin/deepin-music/archive/%{version}/deepin-music-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Fix-library-link.patch hillwood@opensuse.org - Fix library link
Patch0:         Fix-library-link.patch
# PATCH-FIX-UPSTRAM update-taglib-interface.patch hillwood@opensuse.org - fix build on new taglib
Patch1:         update-taglib-interface.patch
# PATCH-FIX-UPSTRAM fix-c++17.patch hillwood@opensuse.org - ICU 75 needs c++17
Patch2:         fix-c++17.patch
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
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
BuildRequires:  pkgconfig(dbusextended-qt5)
BuildRequires:  pkgconfig(dframeworkdbus)
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
BuildRequires:  pkgconfig(mpris-qt5)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(udisks2-qt5)
BuildRequires:  pkgconfig(xext)
%if 0%{?suse_version} <= 1500
BuildRequires:  qtdbusextended-devel < 3.1.2
BuildRequires:  qtmpris-devel < 3.1.2
%endif
Requires:       qt5integration
Provides:       deepin-music
Requires:       vlc
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Music Player is a music player backed by gstreamer, with
customizable UI, and featuring music search by Pinyin and Quanpin. It
supports colorful lyrics, online audio support and a "mini mode".

%lang_package

%prep
%autosetup -p1 -n deepin-music-%{version}
sed -i 's/Exec=deepin-music/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-music/g' \
src/music-player/data/deepin-music.desktop
sed -i '/CMAKE_INSTALL_VOICE_LIBDIR/s|/usr/lib|${CMAKE_INSTALL_LIBDIR}|' \
src/libmusic-plugin/CMakeLists.txt

%build
%cmake -DVERSION=%{version}-%{distribution} \
       -DAPP_VERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install

find %{buildroot} -type f -name "*.a" -delete -print

# openSUSE does not provide deepin-aiassistant, the deepin-aiassistant plugin is invaild
rm -rf %{buildroot}%{_libdir}/deepin-aiassistant

%suse_update_desktop_file -r deepin-music Audio Player
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/deepin-music
%{_datadir}/applications/deepin-music.desktop
%{_datadir}/icons/hicolor/scalable/apps/deepin-music.svg
%{_datadir}/deepin-manual/manual-assets/application/deepin-music
# %dir %{_libdir}/deepin-aiassistant
# %dir %{_libdir}/deepin-aiassistant/serivce-plugins
# %{_libdir}/deepin-aiassistant/serivce-plugins/libmusic-plugin.so

%files lang
%defattr(-,root,root,-)
%{_datadir}/deepin-music

%changelog
