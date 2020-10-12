#
# spec file for package kalarmcal
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


%define kf5_version 5.63.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kalarmcal
Version:        20.08.2
Release:        0
Summary:        Library for handling kalarm calendar data
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This library provides access to and handling of kalarm calendar data.

%package -n libKF5AlarmCalendar5
Summary:        Library for handling kalarm calendar data
Group:          System/Libraries
Requires:       %{name} = %{version}

%description  -n libKF5AlarmCalendar5
This library provides access to and handling of kalarm calendar data.

%package -n akonadi-plugin-kalarmcal
Summary:        Plugin to read and write calendar-related alarm data
Group:          System/Libraries
Requires:       libKF5AlarmCalendar5 = %{version}

%description -n akonadi-plugin-kalarmcal
This package provides plugins for KDE PIM needed to read and write calendar-related notification data.

%package devel
Summary:        Development files for kalarmcal
Group:          Development/Libraries/KDE
Requires:       libKF5AlarmCalendar5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Holidays)
Requires:       cmake(KF5IdentityManagement)

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kalarmcal.

%lang_package

%prep
%setup -q -n kalarmcal-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AlarmCalendar5 -p /sbin/ldconfig
%postun -n libKF5AlarmCalendar5 -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README DESIGN.html
%{_kf5_debugdir}/kalarmcal.categories
%{_kf5_debugdir}/kalarmcal.renamecategories

%files -n libKF5AlarmCalendar5
%license LICENSES/*
%doc README DESIGN.html
%{_kf5_libdir}/libKF5AlarmCalendar.so.*

%files -n akonadi-plugin-kalarmcal
%{_kf5_plugindir}/akonadi_serializer_kalarm.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_kalarm.desktop

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5AlarmCalendar/
%{_kf5_libdir}/libKF5AlarmCalendar.so
%{_kf5_includedir}/KAlarmCal/
%{_kf5_includedir}/kalarmcal_version.h
%{_kf5_mkspecsdir}/qt_KAlarmCal.pri

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
