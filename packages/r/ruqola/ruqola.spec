#
# spec file for package ruqola
#
# Copyright (c) 2023 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           ruqola
Version:        2.2.0
Release:        0
Summary:        Rocket.chat Client
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ruqola
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        ruqola.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets) >= 1.5.4
BuildRequires:  cmake(KF6TextCustomEditor) >= 1.5.4
BuildRequires:  cmake(KF6TextEditTextToSpeech) >= 1.5.4
BuildRequires:  cmake(KF6TextEmoticonsWidgets) >= 1.5.4
BuildRequires:  cmake(KF6TextTranslator) >= 1.5.4
BuildRequires:  cmake(KF6TextUtils) >= 1.5.4
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.14.1
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Ruqola is a Rocket.Chat client for the KDE desktop.

It supports multi-account, search in room, open close rooms, direct message,
thread, discussions.
RC settings can be changed directly.

It's a native alternative to the official embedded browser type of desktop app
available from Rocket.Chat project.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/ruqola/
# # upstream installs with execute bit, gives a linter warning
%attr(0644,-,-) %{_kf6_applicationsdir}/org.kde.ruqola.desktop
%{_kf6_appstreamdir}/org.kde.ruqola.appdata.xml
%{_kf6_bindir}/ruqola
%{_kf6_debugdir}/ruqola.categories
%{_kf6_debugdir}/ruqola.renamecategories
%{_kf6_iconsdir}/hicolor/*/*/ruqola.png
%{_kf6_libdir}/librocketchatrestapi-qt.so.*
%{_kf6_libdir}/libruqolacore.so.*
%{_kf6_libdir}/libruqolawidgets.so.*
%{_kf6_notificationsdir}/ruqola.notifyrc
%dir %{_kf6_plugindir}/ruqolaplugins
%dir %{_kf6_plugindir}/ruqolaplugins/authentication
%{_kf6_plugindir}/ruqolaplugins/authentication/ruqola_githubauthenticationplugin.so
%{_kf6_plugindir}/ruqolaplugins/authentication/ruqola_gitlabauthenticationplugin.so
%{_kf6_plugindir}/ruqolaplugins/authentication/ruqola_passwordauthenticationplugin.so
%{_kf6_plugindir}/ruqolaplugins/authentication/ruqola_personalaccesstokenauthenticationplugin.so
%dir %{_kf6_plugindir}/ruqolaplugins/textplugins
%{_kf6_plugindir}/ruqolaplugins/textplugins/ruqola_sharetextplugin.so
%{_kf6_plugindir}/ruqolaplugins/textplugins/ruqola_webshortcuttextplugin.so
%dir %{_kf6_sharedir}/messageviewer
%dir %{_kf6_sharedir}/messageviewer/openurlwith
%{_kf6_sharedir}/messageviewer/openurlwith/ruqola.openurl

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ruqola/

%changelog
