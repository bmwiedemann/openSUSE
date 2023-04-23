#
# spec file for package eventviews
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


%bcond_without released
%define libname libKPim5EventViews5
Name:           eventviews
Version:        23.04.0
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
BuildRequires:  cmake(KGantt)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%package -n %{libname}
Summary:        Eventviews Library
License:        LGPL-2.1-or-later
Requires:       eventviews
# Renamed
Obsoletes:      eventviews-lang <= 23.04.0

%description -n %{libname}
This internal library implements a GUI framework for viewing various
calendar events in agenda, list, month view or timeline fashion.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KPim5AkonadiCalendar)
Requires:       cmake(KPim5CalendarSupport)
Requires:       cmake(KPim5CalendarUtils)

%description devel
The development package for the eventviews libraries

%lang_package -n %{libname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%{_kf5_debugdir}/eventviews.categories
%{_kf5_debugdir}/eventviews.renamecategories

%files -n %{libname}
%{_kf5_libdir}/libKPim5EventViews.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/EventViews/
%{_kf5_cmakedir}/KF5EventViews/
%{_kf5_cmakedir}/KPim5EventViews/
%{_kf5_libdir}/libKPim5EventViews.so
%{_kf5_mkspecsdir}/qt_EventViews.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
