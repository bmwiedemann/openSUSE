#
# spec file for package kactivities-stats
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


%define lname   libKF5ActivitiesStats1
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           kactivities-stats
Version:        5.101.0
Release:        0
Summary:        KDE Plasma Activities support
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         kactivities-stats-%{version}.tar.xz
%if %{with released}
Source1:        kactivities-stats-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Sql) >= 5.15.0

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package -n %{lname}
Summary:        Library for KDE's Plasma Activities support

%description -n %{lname}
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package devel
Summary:        KDE Plasma Activities support
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules >= 1.7.0
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%prep
%autosetup -p1 -n kactivities-stats-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5ActivitiesStats.so.*
%{_kf5_debugdir}/kactivities-stats.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5ActivitiesStats.so
%{_kf5_libdir}/cmake/KF5ActivitiesStats/
%{_kf5_includedir}/KActivitiesStats/
%{_kf5_libdir}/pkgconfig/libKActivitiesStats.pc
%{_kf5_mkspecsdir}/qt_KActivitiesStats.pri

%changelog
