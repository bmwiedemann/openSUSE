#
# spec file for package kalarmcal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kalarmcal
Version:        19.08.1
Release:        0
Summary:        Library for handling kalarm calendar data
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kholidays-devel
BuildRequires:  kidentitymanagement-devel >= %{_kapp_version}
BuildRequires:  cmake(Qt5Test)
Recommends:     %{name}-lang

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
Requires:       akonadi-server-devel >= %{_kapp_version}
Requires:       kcalcore-devel >= %{_kapp_version}
Requires:       kholidays-devel
Requires:       kidentitymanagement-devel >= %{_kapp_version}
Requires:       libKF5AlarmCalendar5 = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kalarmcal.

%lang_package

%prep
%setup -q -n kalarmcal-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AlarmCalendar5 -p /sbin/ldconfig
%postun -n libKF5AlarmCalendar5 -p /sbin/ldconfig

%files
%license COPYING.LIB
%doc README DESIGN.html
%{_kf5_debugdir}/kalarmcal.categories
%{_kf5_debugdir}/kalarmcal.renamecategories

%files -n libKF5AlarmCalendar5
%license COPYING.LIB
%doc README DESIGN.html
%{_kf5_libdir}/libKF5AlarmCalendar.so.*

%files -n akonadi-plugin-kalarmcal
%{_kf5_plugindir}/akonadi_serializer_kalarm.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_kalarm.desktop

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5AlarmCalendar/
%{_kf5_libdir}/libKF5AlarmCalendar.so
%{_kf5_includedir}/KAlarmCal/
%{_kf5_includedir}/kalarmcal_version.h
%{_kf5_mkspecsdir}/qt_KAlarmCal.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
