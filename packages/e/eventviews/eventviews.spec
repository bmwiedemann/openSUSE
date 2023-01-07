#
# spec file for package eventviews
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           eventviews
Version:        22.12.1
Release:        0
Summary:        Eventviews Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KChart)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)

%description
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%package -n libKF5EventViews5
Summary:        Eventviews Library
License:        LGPL-2.1-or-later
Requires:       %{name}

%description -n libKF5EventViews5
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Requires:       libKF5EventViews5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiCalendar)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CalendarSupport)
Requires:       cmake(KF5CalendarUtils)

%description devel
The development package for the eventviews libraries

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post  -n libKF5EventViews5 -p /sbin/ldconfig
%postun -n libKF5EventViews5 -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_debugdir}/eventviews.categories
%{_kf5_debugdir}/eventviews.renamecategories

%files devel
%{_kf5_cmakedir}/KF5EventViews/
%{_kf5_includedir}/EventViews/
%{_kf5_libdir}/libKF5EventViews.so
%{_kf5_mkspecsdir}/qt_EventViews.pri

%files -n libKF5EventViews5
%{_kf5_libdir}/libKF5EventViews.so.*

%files lang -f %{name}.lang

%changelog
