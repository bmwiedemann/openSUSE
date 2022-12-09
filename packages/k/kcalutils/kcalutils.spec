#
# spec file for package kcalutils
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
Name:           kcalutils
Version:        22.12.0
Release:        0
Summary:        Library with utility functions for handling calendar data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(Qt5Test)
#  Only with stable builds
%if %{with released}
%requires_eq    grantlee5
%endif

%description
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package -n libKF5CalendarUtils5
Summary:        Library with utility functions for handling calendar data
Requires:       %{name} = %{version}

%description  -n libKF5CalendarUtils5
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package devel
Summary:        Development files for kcalutils
Requires:       libKF5CalendarUtils5
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5KDELibs4Support) >= %{kf5_version}
Obsoletes:      kcalutils5-devel < %{version}
Provides:       kcalutils5-devel = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kcalutils.

%lang_package

%prep
%autosetup -p1 -n kcalutils-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%global grantlee_shortver %(rpm -q --queryformat=%%{VERSION} grantlee5 | cut -d . -f 1-2)

%post -n libKF5CalendarUtils5 -p /sbin/ldconfig
%postun -n libKF5CalendarUtils5 -p /sbin/ldconfig

%files -n libKF5CalendarUtils5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5CalendarUtils.so.*

%files devel
%{_kf5_cmakedir}/KF5CalendarUtils/
%{_kf5_includedir}/KCalUtils/
%{_kf5_libdir}/libKF5CalendarUtils.so
%{_kf5_mkspecsdir}/qt_KCalUtils.pri

%files
%dir %{_kf5_libdir}/grantlee/
%dir %{_kf5_libdir}/grantlee/%{grantlee_shortver}
%{_kf5_libdir}/grantlee/%{grantlee_shortver}/kcalendar_grantlee_plugin.so

%files lang -f %{name}.lang

%changelog
