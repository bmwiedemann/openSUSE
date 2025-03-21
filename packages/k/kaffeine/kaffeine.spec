#
# spec file for package kaffeine
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

Name:           kaffeine
Version:        2.0.19git.20250316T013712~afc3f87
Release:        0
Summary:        VLC-based Multimedia Player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kaffeine/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libdvbv5)
BuildRequires:  pkgconfig(libvlc) >= 3.0
Requires:       qt6-sql-sqlite >= %{qt6_version}
Requires:       vlc-noX
Recommends:     vlc-codecs

%description
Kaffeine is a media player.
What makes it different from the others is its support of digital TV (DVB).
Kaffeine has a user-friendly interface so that even first-time users can start
immediately playing their movies: from DVD (including DVD menus, titles,
chapters, etc.), VCD, or a file.

%lang_package

%prep
%autosetup -p1

# Unneeded
sed -i '/scrnsaver/d' src/mediawidget.cpp

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/kaffeine/
%{_kf6_applicationsdir}/org.kde.kaffeine.desktop
%{_kf6_appstreamdir}/org.kde.kaffeine.appdata.xml
%{_kf6_bindir}/kaffeine
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_mandir}/man1/kaffeine.1%{?ext_man}
%dir %{_kf6_sharedir}/kaffeine
%{_kf6_sharedir}/kaffeine/scanfile.dvb
%{_kf6_sharedir}/solid/actions/kaffeine_play_audiocd.desktop
%{_kf6_sharedir}/solid/actions/kaffeine_play_dvd.desktop
%{_kf6_sharedir}/solid/actions/kaffeine_play_videocd.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kaffeine/

%changelog
