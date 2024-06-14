#
# spec file for package kget
#
# Copyright (c) 2024 SUSE LLC
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
Name:           kget
Version:        24.05.1
Release:        0
Summary:        Download Manager
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kget
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  cmake(Gpgmepp) >= 1.7.0
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KTorrent6)
BuildRequires:  cmake(QGpgmeQt6) >= 1.7.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
# As of 2023-12-16 does not build
# BuildRequires:  pkgconfig(libmms)
Obsoletes:      kget5 < %{version}
Provides:       kget5 = %{version}

%description
An advanced download manager by KDE

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%{kf6_build}

%install
%{kf6_install}

%find_lang %{name} --with-man --all-name --with-html

%ldconfig_scriptlets

%files
%license COPYING COPYING.DOC
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/kget/
%{_kf6_applicationsdir}/org.kde.kget.desktop
%{_kf6_appstreamdir}/org.kde.kget.appdata.xml
%{_kf6_bindir}/kget
%{_kf6_configkcfgdir}/kget*.kcfg
%{_kf6_debugdir}/kget.categories
%{_kf6_iconsdir}/hicolor/*/apps/kget.*
%{_kf6_libdir}/libkgetcore.so*
%{_kf6_notificationsdir}/kget.notifyrc
%dir %{_kf6_plugindir}/kget_kcms/
%{_kf6_plugindir}/kget_kcms/kcm_kget*.so
%{_kf6_plugindir}/kget/
%{_kf6_sharedir}/dbus-1/services/org.kde.kget.service
%{_kf6_sharedir}/kget/
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/kget_download.desktop
%{_kf6_sharedir}/kio/servicemenus/kget_plugin.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kget

%changelog
