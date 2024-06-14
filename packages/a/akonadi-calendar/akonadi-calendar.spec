#
# spec file for package akonadi-calendar
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           akonadi-calendar
Version:        24.05.1
Release:        0
Summary:        Akonadi calendar integration
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageComposer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This library provides calendar integration for Akonadi based Applications.

%package -n libKPim6AkonadiCalendar6
Summary:        KDE PIM Libraries: AkonadiCalendar
Requires:       akonadi-calendar >= %{version}
Obsoletes:      libKF5AkonadiCalendar5 < %{version}
Obsoletes:      libKPim5AkonadiCalendar5 < %{version}
Obsoletes:      libKPim5AkonadiCalendar5-lang < %{version}
# Renamed
Obsoletes:      akonadi-calendar-lang <= 23.04.0

%description -n libKPim6AkonadiCalendar6
This library provides calendar integration for Akonadi based Applications.

%package -n akonadi-plugin-calendar
Summary:        Akonadi calendar integration - serializer plugin
Requires:       libKPim6AkonadiCalendar6 = %{version}

%description -n akonadi-plugin-calendar
This package provides plugins required by PIM applications to read and write calendar data.

%package -n kalendarac
Summary:        Reminder daemon client
# Moved from kalendar 1.0.0 to akonadi-calendar
Obsoletes:      kalendar = 1.0.0

%description -n kalendarac
Kalendarac is a reminder daemon client for calendar events.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim6AkonadiCalendar6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6WidgetsAddons) >= %{kf6_version}
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
Obsoletes:      akonadi-calendar-devel < %{version}
Obsoletes:      akonadi5-calendar-devel < %{version}
Provides:       akonadi5-calendar-devel = %{version}

%description devel
Development package for akonadi-calendar.

%lang_package -n libKPim6AkonadiCalendar6

%prep
%autosetup -p1 -n akonadi-calendar-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6AkonadiCalendar6 --all-name

%ldconfig_scriptlets -n libKPim6AkonadiCalendar6

%files
%license LICENSES/*
%{_kf6_debugdir}/akonadi-calendar.categories
%{_kf6_debugdir}/akonadi-calendar.renamecategories

%files -n libKPim6AkonadiCalendar6
%{_kf6_libdir}/libKPim6AkonadiCalendar.so.*

%files -n akonadi-plugin-calendar
%{_kf6_plugindir}/akonadi_serializer_kcalcore.so
%dir %{_kf6_plugindir}/kf6/org.kde.kcalendarcore.calendars
%{_kf6_plugindir}/kf6/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so
%dir %{_kf6_sharedir}/akonadi
%dir %{_kf6_sharedir}/akonadi/plugins
%dir %{_kf6_sharedir}/akonadi/plugins/serializer
%{_kf6_sharedir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop

%files -n kalendarac
%{_kf6_bindir}/kalendarac
%{_kf6_configdir}/autostart/org.kde.kalendarac.desktop
%{_kf6_debugdir}/org_kde_kalendarac.categories
%{_kf6_notificationsdir}/kalendarac.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.kde.kalendarac.service

%files devel
%doc %{_kf6_qchdir}/KPim6AkonadiCalendar.*
%{_includedir}/KPim6/AkonadiCalendar/
%{_kf6_cmakedir}/KPim6AkonadiCalendar/
%{_kf6_libdir}/libKPim6AkonadiCalendar.so

%files -n libKPim6AkonadiCalendar6-lang -f libKPim6AkonadiCalendar6.lang

%changelog
