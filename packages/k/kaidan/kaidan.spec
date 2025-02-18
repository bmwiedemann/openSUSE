#
# spec file for package kaidan
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

Name:           kaidan
Version:        0.11.0
Release:        0
Summary:        A XMPP client based on KDE Framework
License:        AML AND GPL-3.0-or-later AND SUSE-GPL-3.0+-with-openssl-exception AND MIT AND CC-BY-SA-4.0
URL:            https://www.kaidan.im
Source0:        https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kaidan.keyring
# PATCH-FIX-UPSTREAM: https://invent.kde.org/network/kaidan/-/merge_requests/1328
Patch0:         drop_quick_compiler_option.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{qt6_version}
# Both Qt 5 and Qt 6 flavors use the same cmake config name, use the -devel package name
# BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  kquickimageeditor6-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-declarative-tools >= %{qt6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 1.4.0
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(QXmppQt6) >= 1.9.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Location) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(ZXing) >= 1.0.8
BuildRequires:  pkgconfig(icu-uc) >= 61.0
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-prison-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 1.4.0
Requires:       kquickimageeditor6-imports
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-location >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
Requires:       qt6-positioning-imports >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Kaidan is a simple Jabber/XMPP client providing a user-interface using
Kirigami and QtQuick. The back-end of Kaidan is entirely written in C++
using the qxmpp XMPP client library and Qt 6.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-qt

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md NEWS.md
%dir %{_kf6_sharedir}/kaidan
%{_kf6_applicationsdir}/im.kaidan.kaidan.desktop
%{_kf6_appstreamdir}/im.kaidan.kaidan.appdata.xml
%{_kf6_bindir}/kaidan
%{_kf6_debugdir}/kaidan.categories
%{_kf6_iconsdir}/hicolor/*/apps/kaidan.*
%{_kf6_notificationsdir}/kaidan.notifyrc
%{_kf6_sharedir}/kaidan/images
%{_kf6_sharedir}/kaidan/providers*

%files lang -f %{name}.lang

%changelog
