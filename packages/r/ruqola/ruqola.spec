#
# spec file for package ruqola
#
# Copyright (c) 2019-2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ruqola
Version:        1.1~git.20200520
Release:        0
Summary:        Rocket.chat Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://invent.kde.org/network/ruqola
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5MultimediaWidgets) >= 5.12.0
BuildRequires:  cmake(Qt5NetworkAuth) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5WebSockets) >= 5.12.0
BuildRequires:  update-desktop-files
Requires:       kirigami2

%description
Ruqola is a Rocket.Chat client for the KDE desktop.

It supports multi-account, search in room, open close rooms, direct message, thread, discussions.
RC settings can be changed directly.

It's a native alternative to the official embedded browser type of desktop app available from Rocket.Chat project.

Ruqola uses Kirigami components based on QtQuick.

%prep
%autosetup -p1

%build
 %cmake_kf5 -d build
 %cmake_build

%install
 %kf5_makeinstall -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
 %license COPYING*
 %doc README*
 %{_kf5_bindir}/ruqola
 %{_kf5_bindir}/ruqolaqml
 %{_kf5_libdir}/libruqolacore.so.*
 %{_kf5_libdir}/libruqolawidgets.so.*
 %{_kf5_libdir}/librocketchatrestapi-qt5*
 %dir %{_kf5_plugindir}/ruqolaplugins
 %dir %{_kf5_plugindir}/ruqolaplugins/authentication
 %{_kf5_plugindir}/ruqolaplugins/authentication/ruqola_passwordauthenticationplugin.so
 %dir %{_kf5_plugindir}/ruqolaplugins/textplugins
 %{_kf5_plugindir}/ruqolaplugins/textplugins/ruqola_webshortcuttextplugin.so
# upstream installs with execute bit, gives a linter warning
 %attr(0644,-,-) %{_kf5_applicationsdir}/org.kde.ruqola.desktop
 %attr(0644,-,-) %{_kf5_applicationsdir}/org.kde.ruqolaqml.desktop
 %{_kf5_iconsdir}/hicolor/*/*/*.*
 %doc %{_kf5_htmldir}/en/ruqola/
 %{_kf5_notifydir}/ruqola.notifyrc
 %{_kf5_appstreamdir}/org.kde.ruqola.appdata.xml
 %{_kf5_appstreamdir}/org.kde.ruqolaqml.appdata.xml
 %{_kf5_debugdir}/ruqola.categories

%changelog
