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


%bcond_without released
Name:           ruqola
Version:        1.9.1
Release:        0
Summary:        Rocket.chat Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://invent.kde.org/network/ruqola
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
# PATCH-FIX-UPSTREAM: Fix build error with Qt 6.4
Patch0:         allow_build_without_deprecated_method.patch
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons) >= 5.91.0
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia) >= 5.15.2
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5WebSockets)

%description
Ruqola is a Rocket.Chat client for the KDE desktop.

It supports multi-account, search in room, open close rooms, direct message, thread, discussions.
RC settings can be changed directly.

It's a native alternative to the official embedded browser type of desktop app available from Rocket.Chat project.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%if %{with released}
%find_lang %{name}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc README*
%{_kf5_bindir}/ruqola
%{_kf5_libdir}/libruqolacore.so.*
%{_kf5_libdir}/libruqolawidgets.so.*
%{_kf5_libdir}/librocketchatrestapi-qt5*
%{_kf5_libdir}/libruqola-*
%dir %{_kf5_plugindir}/ruqolaplugins
%dir %{_kf5_plugindir}/ruqolaplugins/authentication
%{_kf5_plugindir}/ruqolaplugins/authentication/ruqola_passwordauthenticationplugin.so
%dir %{_kf5_plugindir}/kf5/ruqola-translator
%{_kf5_plugindir}/kf5/ruqola-translator/*
%dir %{_kf5_plugindir}/ruqolaplugins/textplugins
%{_kf5_plugindir}/ruqolaplugins/textplugins/ruqola_*.so
# upstream installs with execute bit, gives a linter warning
%attr(0644,-,-) %{_kf5_applicationsdir}/org.kde.ruqola.desktop
%{_kf5_iconsdir}/hicolor/*/*/*.*
%doc %{_kf5_htmldir}/en/ruqola/
%{_kf5_notifydir}/ruqola.notifyrc
%{_kf5_appstreamdir}/org.kde.ruqola.appdata.xml
%{_kf5_debugdir}/ruqola.categories
%{_kf5_debugdir}/ruqola.renamecategories

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
