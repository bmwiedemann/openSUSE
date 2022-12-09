#
# spec file for package akregator
#
# Copyright (c) 2022 SUSE LLC
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


%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           akregator
Version:        22.12.0
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/akregator
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  libkleo
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5WebEngine) >= 5.15.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
Provides:       akregator5 = %{version}
Obsoletes:      akregator5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

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
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.akregator Network RSS-News

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/akregator/
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/kcms
%{_kf5_applicationsdir}/org.kde.akregator.desktop
%{_kf5_appstreamdir}/org.kde.akregator.appdata.xml
%{_kf5_bindir}/akregator*
%{_kf5_configkcfgdir}/akregator.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.akregator.part.xml
%{_kf5_debugdir}/akregator.categories
%{_kf5_debugdir}/akregator.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/akregator*.png
%{_kf5_iconsdir}/hicolor/scalable/apps/akregator.svg
%{_kf5_libdir}/libakregatorinterfaces.so.*
%{_kf5_libdir}/libakregatorprivate.so.*
%{_kf5_notifydir}/akregator.notifyrc
%{_kf5_plugindir}/akregator*.so
%{_kf5_plugindir}/pim5/kontact/
%{_kf5_plugindir}/pim5/kcms/akregator
%{_kf5_sharedir}/akregator/

%files lang -f %{name}.lang

%changelog
