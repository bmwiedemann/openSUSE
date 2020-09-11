#
# spec file for package kget
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           kget
Version:        20.08.1
Release:        0
Summary:        Download Manager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  gpgme-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  libktorrent-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  sqlite-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      kget5 < %{version}
Provides:       kget5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
An advanced download manager by KDE

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  %suse_update_desktop_file -r org.kde.kget         System   TrayIcon

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC
%doc README
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/kget/
%{_kf5_applicationsdir}/org.kde.kget.desktop
%{_kf5_bindir}/kget
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kget.*
%{_kf5_libdir}/libkgetcore.so*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kget.service
%{_kf5_sharedir}/dolphinpart/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kget/
%{_kf5_sharedir}/khtml/
%{_kf5_sharedir}/kwebkitpart/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_appstreamdir}/org.kde.kget.appdata.xml
%{_kf5_debugdir}/kget.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
