#
# spec file for package akonadi-calendar
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
Name:           akonadi-calendar
Version:        22.12.0
Release:        0
Summary:        Akonadi calendar integration
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Test)

%description
This library provides calendar integration for Akonadi based Applications.

%package -n libKF5AkonadiCalendar5
Summary:        KDE PIM Libraries: AkonadiCalendar
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5AkonadiCalendar5
This library provides calendar integration for Akonadi based Applications.

%package -n akonadi-plugin-calendar
Summary:        Akonadi calendar integration - serializer plugin
Requires:       libKF5AkonadiCalendar5 = %{version}

%description -n akonadi-plugin-calendar
This package provides plugins required by PIM applications to read and write calendar data.

%package -n kalendarac
Summary:        Reminder daemon client
# Moved from kalendar 1.0.0 to akonadi-calendar
Conflicts:      kalendar = 1.0.0

%description -n kalendarac
Kalendarac is a reminder daemon client for calendar events.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKF5AkonadiCalendar5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5WidgetsAddons)
Obsoletes:      akonadi5-calendar-devel < %{version}
Provides:       akonadi5-calendar-devel = %{version}

%description devel
Development package for akonadi-calendar.

%lang_package

%prep
%autosetup -p1 -n akonadi-calendar-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5AkonadiCalendar5 -p /sbin/ldconfig
%postun -n libKF5AkonadiCalendar5 -p /sbin/ldconfig

%files -n libKF5AkonadiCalendar5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5AkonadiCalendar.so.*
%exclude %{_kf5_debugdir}/org_kde_kalendarac.categories

%files -n akonadi-plugin-calendar
%{_kf5_plugindir}/akonadi_serializer_kcalcore.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/org.kde.kcalendarcore.calendars
%{_kf5_plugindir}/kf5/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop

%files -n kalendarac
%{_kf5_bindir}/kalendarac
%{_kf5_configdir}/autostart/org.kde.kalendarac.desktop
%{_kf5_debugdir}/org_kde_kalendarac.categories
%{_kf5_notifydir}/kalendarac.notifyrc
%{_kf5_sharedir}/dbus-1/services/org.kde.kalendarac.service

%files devel
%{_kf5_cmakedir}/KF5AkonadiCalendar/
%{_kf5_includedir}/AkonadiCalendar/
%{_kf5_libdir}/libKF5AkonadiCalendar.so
%{_kf5_mkspecsdir}/qt_AkonadiCalendar.pri

%files lang -f %{name}.lang

%changelog
