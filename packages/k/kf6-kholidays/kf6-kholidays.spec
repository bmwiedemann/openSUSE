#
# spec file for package kf6-kholidays
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

%define rname kholidays
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kholidays
Version:        6.3.0
Release:        0
Summary:        Holiday calculation library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This package contains a library which helps developers determining when holidays occur.

%package imports
Summary:        QML imports for the KDE Holidays Franework

%description imports
QML imports for the KDE Holidays Franework.

%package -n libKF6Holidays6
Summary:        Holiday API for KDE PIM
Requires:       kf6-kholidays >= %{version}

%description -n libKF6Holidays6
This package contains a library which helps developers determining when holidays occur.

%package devel
Summary:        Development files for the KDE PIM Holiday API
Requires:       libKF6Holidays6 = %{version}
Requires:       cmake(Qt6Core)

%description devel
This package contains necessary include files and libraries needed
to develop applications depending on the kholidays library

%lang_package -n libKF6Holidays6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libkholidays6 --with-man --all-name --with-qt

%ldconfig_scriptlets -n libKF6Holidays6

%files
%{_kf6_debugdir}/kholidays.categories

%files imports
%{_kf6_qmldir}/org/kde/kholidays/

%files -n libKF6Holidays6
%license LICENSES/*
%doc DESIGN README.md
%{_kf6_libdir}/libKF6Holidays.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Holidays.*
%{_kf6_cmakedir}/KF6Holidays/
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/libKF6Holidays.so

%files -n libKF6Holidays6-lang -f libkholidays6.lang

%changelog
