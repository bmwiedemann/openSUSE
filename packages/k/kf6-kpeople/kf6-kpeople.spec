#
# spec file for package kf6-kpeople
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


%define qt6_version 6.6.0

%define rname kpeople
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kpeople
Version:        6.3.0
Release:        0
Summary:        Library for access to contacts and identity holders
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
A library that provides access to all contacts and the people who hold them.

%package imports
Summary:        QML imports for kpeople
Requires:       libKF6People6 = %{version}

%description imports
This package provides support to use KPeople with the QtQuick framework.

%package -n libKF6People6
Summary:        Library for access to contacts and identity holders
Requires:       kf6-kpeople >= %{version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description -n libKF6People6
A library that provides access to all contacts and the people who hold them.

%package devel
Summary:        Library for access to contacts and identity holders
Requires:       libKF6People6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
A library that provides access to all contacts and the people who hold them.
Development files for kpeople.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE \
           -DENABLE_EXAMPLES:BOOL=FALSE

%kf6_build

%install
%kf6_install

%find_lang kpeople6

%ldconfig_scriptlets -n libKF6People6

%files
%{_kf6_debugdir}/kpeople.categories
%{_kf6_debugdir}/kpeople.renamecategories
%dir %{_kf6_plugindir}/kpeople/
%dir %{_kf6_plugindir}/kpeople/datasource/
%{_kf6_plugindir}/kpeople/datasource/KPeopleVCard.so

%files imports
%{_kf6_qmldir}/org/kde/people/

%files -n libKF6People6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6People.so.*
%{_kf6_libdir}/libKF6PeopleBackend.so.*
%{_kf6_libdir}/libKF6PeopleWidgets.so.*

%files devel
%doc %{_kf6_qchdir}/KF6People.*
%{_kf6_cmakedir}/KF6People/
%{_kf6_includedir}/KPeople/
%{_kf6_libdir}/libKF6People.so
%{_kf6_libdir}/libKF6PeopleBackend.so
%{_kf6_libdir}/libKF6PeopleWidgets.so

%files lang -f kpeople6.lang

%changelog
