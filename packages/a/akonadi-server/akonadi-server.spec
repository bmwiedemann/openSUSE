#
# spec file for package akonadi-server
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


%define rname   akonadi
%define kf5_version 5.104.0
%bcond_without released
Name:           akonadi-server
Version:        23.04.0
Release:        0
Summary:        PIM Storage Service
License:        LGPL-2.1-or-later
URL:            https://akonadi-project.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       akonadi-server-rpmlintrc
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  mariadb
BuildRequires:  postgresql-devel
BuildRequires:  shared-mime-info
BuildRequires:  sqlite3-devel
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       libqt5-sql-mysql
Requires:       mysql
Recommends:     kaccounts-integration
Recommends:     kaccounts-providers
Suggests:       mariadb
Obsoletes:      akonadi5 < %{version}
Provides:       akonadi5 = %{version}
# Needed for users of unstable repositories
Obsoletes:      akonadi < %{version}
Obsoletes:      akonadi-runtime < %{version}

%description
This package contains the data files of Akonadi, the KDE PIM storage
service.

%package -n libKPim5AkonadiCore5
Summary:        Core Akonadi Server library
Recommends:     %{name}

%description -n libKPim5AkonadiCore5
This package includes the core Akonadi library, the KDE PIM storage service.

%package -n libKPim5AkonadiAgentBase5
Summary:        Akonadi Agent base library
Recommends:     %{name}

%description -n libKPim5AkonadiAgentBase5
This package includes the agent library for Akonadi, the KDE PIM storage service.

%package -n libKPim5AkonadiWidgets5
Summary:        Akonadi Agent base library
Recommends:     %{name}

%description -n libKPim5AkonadiWidgets5
This package provides the basic GUI widgets for Akonadi, the KDE PIM storage service.

%package -n libKPim5AkonadiPrivate5
Summary:        Akonadi Private Server library
Recommends:     %{name}

%description -n libKPim5AkonadiPrivate5
This package includes the Private Akonadi library for Akonadi, the KDE PIM storage service.

%package -n libKPim5AkonadiXml5
Summary:        Akonadi Xml library
Recommends:     %{name}

%description -n libKPim5AkonadiXml5
This package includes the Akonadi Xml library for Akonadi, the KDE PIM storage service.

%package sqlite
Summary:        akonadi server's SQlite plugin
Requires:       %{name} = %{version}
Supplements:    (%{name} and sqlite3)

%description sqlite
Akonadi server's SQlite plugin.

%package devel
Summary:        Akonadi Framework: Build Environment
Requires:       %{name} = %{version}
Requires:       libKPim5AkonadiAgentBase5 = %{version}
Requires:       libKPim5AkonadiCore5 = %{version}
Requires:       libKPim5AkonadiWidgets5 = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5ConfigWidgets)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5ItemModels)
Requires:       cmake(KF5KIO)
Requires:       cmake(KF5XmlGui)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5DBus)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)
Conflicts:      libakonadiprotocolinternals-devel
Obsoletes:      akonadi-devel < %{version}
Provides:       libKF5AkonadiPrivate-devel = %{version}
Obsoletes:      libKF5AkonadiPrivate-devel < %{version}

%description devel
This package contains development files of Akonadi, the KDE PIM storage
service.

%package apparmor
Summary:        AppArmor profiles for Akonadi
Requires:       apparmor-abstractions

%description apparmor
This package contains AppArmor profiles for Akonadi.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE -DQT_PLUGINS_DIR=%{_kf5_plugindir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets

%ldconfig_scriptlets -n libKPim5AkonadiWidgets5
%ldconfig_scriptlets -n libKPim5AkonadiCore5
%ldconfig_scriptlets -n libKPim5AkonadiAgentBase5
%ldconfig_scriptlets -n libKPim5AkonadiPrivate5
%ldconfig_scriptlets -n libKPim5AkonadiXml5

%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/mariadbd_akonadi %{_sysconfdir}/apparmor.d/mysqld_akonadi %{_sysconfdir}/apparmor.d/postgresql_akonadi %{_sysconfdir}/apparmor.d/usr.bin.akonadiserver

%files
%doc AUTHORS
%config %{_kf5_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf
%config %{_kf5_sysconfdir}/xdg/akonadi/mysql-global.conf
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_sysconfdir}/xdg/akonadi
%dir %{_kf5_plugindir}/pim5
%{_datadir}/akonadi/
%{_datadir}/kf5/akonadi/
%{_datadir}/kf5/akonadi_knut_resource/
%{_kf5_bindir}/akonadi_*
%{_kf5_bindir}/akonadictl
%{_kf5_bindir}/akonadiselftest
%{_kf5_bindir}/akonadiserver
%{_kf5_bindir}/akonaditest
%{_kf5_bindir}/asapcat
%{_kf5_configkcfgdir}/resourcebase.kcfg
%{_kf5_debugdir}/akonadi.*categories
%{_kf5_iconsdir}/hicolor/*/apps/akonadi.png
%{_kf5_iconsdir}/hicolor/scalable/apps/akonadi.svgz
%{_kf5_plugindir}/pim5/akonadi/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_kf5_sharedir}/mime/packages/akonadi-mime.xml

%files -n libKPim5AkonadiAgentBase5
%{_kf5_libdir}/libKPim5AkonadiAgentBase.so.*

%files -n libKPim5AkonadiCore5
%license LICENSES/*
%{_kf5_libdir}/libKPim5AkonadiCore.so.*

%files -n libKPim5AkonadiWidgets5
%{_kf5_libdir}/libKPim5AkonadiWidgets.so.*

%files -n libKPim5AkonadiPrivate5
%{_kf5_libdir}/libKPim5AkonadiPrivate.so.*

%files -n libKPim5AkonadiXml5
%{_kf5_libdir}/libKPim5AkonadiXml.so.*

%files sqlite
%{_kf5_plugindir}/sqldrivers/

%files devel
%dir %{_includedir}/KPim5
%dir %{_kf5_sharedir}/kdevappwizard
%dir %{_kf5_sharedir}/kdevappwizard/templates
%{_includedir}/KPim5/Akonadi/
%{_includedir}/KPim5/AkonadiAgentBase/
%{_includedir}/KPim5/AkonadiCore/
%{_includedir}/KPim5/AkonadiWidgets/
%{_includedir}/KPim5/AkonadiXml/
%{_kf5_bindir}/akonadi2xml
%{_kf5_cmakedir}/KF5Akonadi/
%{_kf5_cmakedir}/KPim5Akonadi/
%{_kf5_dbusinterfacesdir}/org.freedesktop.Akonadi.*.xml
%{_kf5_libdir}/libKPim5AkonadiAgentBase.so
%{_kf5_libdir}/libKPim5AkonadiCore.so
%{_kf5_libdir}/libKPim5AkonadiPrivate.so
%{_kf5_libdir}/libKPim5AkonadiWidgets.so
%{_kf5_libdir}/libKPim5AkonadiXml.so
%{_kf5_mkspecsdir}/qt_AkonadiAgentBase.pri
%{_kf5_mkspecsdir}/qt_AkonadiCore.pri
%{_kf5_mkspecsdir}/qt_AkonadiWidgets.pri
%{_kf5_mkspecsdir}/qt_AkonadiXml.pri
%{_kf5_plugindir}/designer/
%{_kf5_sharedir}/kdevappwizard/templates/akonadiresource.tar.bz2
%{_kf5_sharedir}/kdevappwizard/templates/akonadiserializer.tar.bz2

%files apparmor
%config(noreplace) %{_sysconfdir}/apparmor.d/mariadbd_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/mysqld_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/postgresql_akonadi
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.akonadiserver

%files lang -f %{name}.lang

%changelog
