#
# spec file for package kdesvn
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


Name:           kdesvn
Version:        2.1.0
Release:        0
Summary:        KDE Subversion Client
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kdesvn
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  subversion-devel
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
# needed for the database
Requires:       libQt5Sql5-sqlite
Provides:       kde4-kdesvn = %{version}
Obsoletes:      kde4-kdesvn < %{version}
Obsoletes:      libsvnqt7 < %{version}

%description
kdesvn is a GUI client for subversion repositories.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name --with-man

%{kf5_find_htmldocs}

%fdupes %{buildroot}%{_datadir}

%files -f %{name}.lang
%license COPYING COPYING.OpenSSL
%doc AUTHORS ChangeLog
%doc %lang(en) %{_kf5_htmldir}/en/kdesvn/
%doc %lang(en) %{_kf5_mandir}/man1/kdesvn.1%{?ext_man}
%doc %lang(en) %{_kf5_mandir}/man1/kdesvnaskpass.1%{?ext_man}
%{_kf5_applicationsdir}/org.kde.kdesvn.desktop
%{_kf5_appstreamdir}/org.kde.kdesvn.appdata.xml
%{_kf5_bindir}/kdesvn
%{_kf5_bindir}/kdesvnaskpass
%{_kf5_configkcfgdir}/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.kdesvnd.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kdesvn/
%{_kf5_plugindir}/kdesvnpart.so
%{_kf5_plugindir}/kf5/kded/kdesvnd.so
%{_kf5_plugindir}/kio_ksvn.so
%{_kf5_servicesdir}/*.desktop
%{_kf5_servicesdir}/*.protocol
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_sharedir}/dbus-1/services/org.kde.kdesvnd.service
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kdesvn/

%changelog
