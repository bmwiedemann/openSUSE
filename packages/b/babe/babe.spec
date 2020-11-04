#
# spec file for package babe
#
# Copyright (c) 2020 SUSE LLC
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


Name:           babe
Version:        1.2.1
Release:        0
Summary:        A Qt music player with support for favorites
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://babe.kde.org
Source:         http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Always-use-local-CMake-modules-first.patch
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libtag-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config) >= 5.24.0
BuildRequires:  cmake(KF5I18n) >= 5.24.0
BuildRequires:  cmake(KF5Notifications) >= 5.24.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.5.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.5.0
BuildRequires:  pkgconfig(Qt5WebSockets) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.5.0

%description
Babe is a music collection organizer. Playlists can be created for
organizing music, and they can be filtered by artist, title, album,
genre, date and location. It can link to, and bookmark YouTube music
videos into the local collection by using a Chromium extension.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %suse_update_desktop_file -r org.kde.babe Qt KDE AudioVideo Audio Player

%files
%license COPYING*
%doc README*
%{_kf5_bindir}/babe
%{_kf5_applicationsdir}/org.kde.babe.desktop
%{_kf5_iconsdir}/hicolor/*/apps/babe.*
%{_kf5_appstreamdir}/org.kde.babe.appdata.xml

%changelog
