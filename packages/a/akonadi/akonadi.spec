#
# spec file for package akonadi
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

%define name   akonadi
%bcond_without released
Name:           akonadi
Version:        24.05.1
Release:        0
Summary:        PIM Storage Service
License:        LGPL-2.1-or-later
URL:            https://userbase.kde.org/Akonadi
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  mariadb
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-sql-private-devel >= %{qt6_version}
BuildRequires:  shared-mime-info
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
# SECTION sqlite
Requires:       qt6-sql-sqlite
Requires:       sqlite3
# /SECTION
# SECTION mysql
# Users already using the mysql backend need the backend
Requires:       qt6-sql-mysql
Requires:       mariadb
# /SECTION
Recommends:     kaccounts-integration
Recommends:     kaccounts-providers
# Package was renamed before the 6.0 release
Provides:       akonadi-server = %{version}
Obsoletes:      akonadi-server < %{version}
Obsoletes:      akonadi-server-lang < %{version}
# Sqlite driver was removed, now uses Qt driver
Obsoletes:      akonadi-server-sqlite < %{version}

%description
This package contains the data files of Akonadi, the KDE PIM storage
service.

%package -n libKPim6AkonadiCore6
Summary:        Core Akonadi Server library
Recommends:     akonadi

%description -n libKPim6AkonadiCore6
This package includes the core Akonadi library, the KDE PIM storage service.

%package -n libKPim6AkonadiAgentBase6
Summary:        Akonadi Agent base library
Recommends:     akonadi

%description -n libKPim6AkonadiAgentBase6
This package includes the agent library for Akonadi, the KDE PIM storage service.

%package -n libKPim6AkonadiWidgets6
Summary:        Akonadi Agent base library
Recommends:     akonadi

%description -n libKPim6AkonadiWidgets6
This package provides the basic GUI widgets for Akonadi, the KDE PIM storage service.

%package -n libKPim6AkonadiPrivate6
Summary:        Akonadi Private Server library
Recommends:     akonadi

%description -n libKPim6AkonadiPrivate6
This package includes the Private Akonadi library for Akonadi, the KDE PIM storage service.

%package -n libKPim6AkonadiXml6
Summary:        Akonadi Xml library
Recommends:     akonadi

%description -n libKPim6AkonadiXml6
This package includes the Akonadi Xml library for Akonadi, the KDE PIM storage service.

%package devel
Summary:        Akonadi Framework: Build Environment
Requires:       akonadi = %{version}
# For the kcfg_generate_dbus_interface CMake macro
Requires:       xsltproc
Requires:       libKPim6AkonadiAgentBase6 = %{version}
Requires:       libKPim6AkonadiCore6 = %{version}
Requires:       libKPim6AkonadiWidgets6 = %{version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6ConfigWidgets) >= %{kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KF6ItemModels) >= %{kf6_version}
Requires:       cmake(KF6XmlGui) >= %{kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}
Obsoletes:      akonadi-server-devel < %{version}
Obsoletes:      libakonadiprotocolinternals-devel < %{version}
Provides:       libKF5AkonadiPrivate-devel = %{version}
Obsoletes:      libKF5AkonadiPrivate-devel < %{version}

%description devel
This package contains development files of Akonadi, the KDE PIM storage
service.

%package apparmor
Summary:        AppArmor profiles for Akonadi
Requires:       apparmor-abstractions
Provides:       akonadi-server-apparmor = %{version}
Obsoletes:      akonadi-server-apparmor < %{version}

%description apparmor
This package contains AppArmor profiles for Akonadi.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE -DDATABASE_BACKEND:STRING=SQLITE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n libKPim6AkonadiWidgets6
%ldconfig_scriptlets -n libKPim6AkonadiCore6
%ldconfig_scriptlets -n libKPim6AkonadiAgentBase6
%ldconfig_scriptlets -n libKPim6AkonadiPrivate6
%ldconfig_scriptlets -n libKPim6AkonadiXml6

%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/mariadbd_akonadi %{_sysconfdir}/apparmor.d/mysqld_akonadi %{_sysconfdir}/apparmor.d/postgresql_akonadi %{_sysconfdir}/apparmor.d/usr.bin.akonadiserver

%files
%doc AUTHORS
%dir %{_kf6_sysconfdir}/xdg/akonadi
%config %{_kf6_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf
%config %{_kf6_sysconfdir}/xdg/akonadi/mysql-global.conf
%dir %{_kf6_iconsdir}/hicolor/256x256
%dir %{_kf6_iconsdir}/hicolor/256x256/apps
%{_kf6_bindir}/akonadi_agent_launcher
%{_kf6_bindir}/akonadi_agent_server
%{_kf6_bindir}/akonadi_control
%{_kf6_bindir}/akonadi-db-migrator
%{_kf6_bindir}/akonadi_knut_resource
%{_kf6_bindir}/akonadi_rds
%{_kf6_bindir}/akonadictl
%{_kf6_bindir}/akonadiselftest
%{_kf6_bindir}/akonadiserver
%{_kf6_bindir}/akonaditest
%{_kf6_bindir}/asapcat
%{_kf6_configkcfgdir}/resourcebase.kcfg
%dir %{_kf6_datadir}/akonadi/
%{_kf6_datadir}/akonadi/akonadi-xml.xsd
%{_kf6_datadir}/akonadi/kcfg2dbus.xsl
%dir %{_kf6_datadir}/akonadi_knut_resource/
%{_kf6_datadir}/akonadi_knut_resource/knut-template.xml
%{_kf6_debugdir}/akonadi.categories
%{_kf6_debugdir}/akonadi.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/akonadi.png
%{_kf6_iconsdir}/hicolor/scalable/apps/akonadi.svgz
%{_kf6_plugindir}/pim6/akonadi/akonadi_test_searchplugin.so
%dir %{_kf6_sharedir}/akonadi
%dir %{_kf6_sharedir}/akonadi/agents
%{_kf6_sharedir}/akonadi/agents/knutresource.desktop
%{_kf6_sharedir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_kf6_sharedir}/mime/packages/akonadi-mime.xml

%files -n libKPim6AkonadiAgentBase6
%{_kf6_libdir}/libKPim6AkonadiAgentBase.so.*

%files -n libKPim6AkonadiCore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiCore.so.*

%files -n libKPim6AkonadiWidgets6
%{_kf6_libdir}/libKPim6AkonadiWidgets.so.*

%files -n libKPim6AkonadiPrivate6
%{_kf6_libdir}/libKPim6AkonadiPrivate.so.*

%files -n libKPim6AkonadiXml6
%{_kf6_libdir}/libKPim6AkonadiXml.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Akonadi*
%{_includedir}/KPim6/Akonadi/
%{_includedir}/KPim6/AkonadiAgentBase/
%{_includedir}/KPim6/AkonadiCore/
%{_includedir}/KPim6/AkonadiWidgets/
%{_includedir}/KPim6/AkonadiXml/
%{_kf6_bindir}/akonadi2xml
%{_kf6_cmakedir}/KPim6Akonadi/
%{_kf6_dbusinterfacesdir}/org.freedesktop.Akonadi.*.xml
%{_kf6_libdir}/libKPim6AkonadiAgentBase.so
%{_kf6_libdir}/libKPim6AkonadiCore.so
%{_kf6_libdir}/libKPim6AkonadiPrivate.so
%{_kf6_libdir}/libKPim6AkonadiWidgets.so
%{_kf6_libdir}/libKPim6AkonadiXml.so
%dir %{_kf6_plugindir}/designer
%{_kf6_plugindir}/designer/akonadi6widgets.so
%{_kf6_sharedir}/kdevappwizard/templates/akonadiresource.tar.bz2
%{_kf6_sharedir}/kdevappwizard/templates/akonadiserializer.tar.bz2

%files apparmor
%config(noreplace) %{_sysconfdir}/apparmor.d/mariadbd_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/mysqld_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/postgresql_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.akonadiserver

%files lang -f %{name}.lang

%changelog
