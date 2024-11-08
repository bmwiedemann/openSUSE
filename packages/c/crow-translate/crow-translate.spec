#
# spec file for package crow-translate
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define  _name  io.crow_translate.CrowTranslate
Name:           crow-translate
Version:        3.1.0
Release:        0
Summary:        A Qt GUI for Google, Yandex and Bing translators
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Frontends
URL:            https://apps.kde.org/crowtranslate
Source0:        https://download.kde.org/stable/crow-translate/%{version}/%{name}-v%{version}.tar.gz
Source1:        https://download.kde.org/stable/crow-translate/%{version}/%{name}-v%{version}.tar.gz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/shatur@key1.asc?ref_type=heads
Source2:        crow-translate.keyring
BuildRequires:  cmake >= 3.16.0
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(tesseract) >= 4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Requires:       gstreamer-plugins-good

%description
A simple and lightweight translator that allows to translate and speak
text using Google, Yandex and Bing written with Qt5.

%lang_package

%prep
%autosetup -p1 -n crow-translate-v%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-qt

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.CrowTranslate.desktop
%{_kf5_appstreamdir}/org.kde.CrowTranslate.metainfo.xml
%{_kf5_bindir}/crow
%{_kf5_iconsdir}/hicolor/*/apps/org.kde.CrowTranslate.*
%{_kf5_iconsdir}/hicolor/*/status/org.kde.CrowTranslate-tray-*.*

%files lang -f %{name}.lang

%changelog
