#
# spec file for package akregator
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           akregator
Version:        24.05.2
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/akregator
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Syndication) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(KPim6WebEngineViewer) >= %{kpim6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       akregator5 = %{version}
Obsoletes:      akregator5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Akregator is a news feed reader. It enables you to follow news sites,
blogs and other RSS/Atom-enabled websites without the need to
manually check for updates using a web browser. Akregator is designed
for convenient reading of hundreds of news sources. It comes with
Konqueror integration for adding news feeds and with an internal
browser for news reading.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/akregator/
%{_kf6_applicationsdir}/org.kde.akregator.desktop
%{_kf6_appstreamdir}/org.kde.akregator.appdata.xml
%{_kf6_bindir}/akregator
%{_kf6_bindir}/akregatorstorageexporter
%{_kf6_configkcfgdir}/akregator.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.akregator.part.xml
%{_kf6_debugdir}/akregator.categories
%{_kf6_debugdir}/akregator.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/akregator*.png
%{_kf6_iconsdir}/hicolor/scalable/apps/akregator.svg
%{_kf6_libdir}/libakregatorinterfaces.so.*
%{_kf6_libdir}/libakregatorprivate.so.*
%{_kf6_notificationsdir}/akregator.notifyrc
%{_kf6_plugindir}/akregatorpart.so
%dir %{_kf6_plugindir}/pim6
%{_kf6_plugindir}/pim6/kontact/
%dir %{_kf6_plugindir}/pim6/kcms
%{_kf6_plugindir}/pim6/kcms/akregator/
%{_kf6_sharedir}/akregator/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/akregator/

%changelog
