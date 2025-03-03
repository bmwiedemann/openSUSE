#
# spec file for package kactivities5
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libKF5Activities5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kactivities5
Version:        5.116.0
Release:        0
Summary:        KDE Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         kactivities-%{version}.tar.xz
%if %{with released}
Source1:        kactivities-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package tools
Summary:        Command-line tools for Plasma Activity management
Requires:       %{lname} = %{version}

%description tools
This package provides command-line tools to manipulate Plasma Activities.

%package -n %{lname}
Summary:        Library for KDE's Plasma Activities support

%description -n %{lname}
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package imports
Summary:        KDE Plasma Activities support

%description imports
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
QML imports.

%package devel
Summary:        KDE Plasma Activities support
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%prep
%autosetup -p1 -n kactivities-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files tools
%{_bindir}/kactivities-cli

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Activities.so.*
%{_kf5_debugdir}/kactivities.categories
%{_kf5_debugdir}/kactivities.renamecategories

%files imports
%{_kf5_qmldir}/

%files devel
%{_kf5_libdir}/libKF5Activities.so
%{_kf5_libdir}/cmake/KF5Activities/
%{_kf5_includedir}/KActivities/
%{_kf5_libdir}/pkgconfig/libKActivities.pc
%{_kf5_mkspecsdir}/qt_KActivities.pri

%changelog
