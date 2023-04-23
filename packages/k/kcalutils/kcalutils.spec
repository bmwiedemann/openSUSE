#
# spec file for package kcalutils
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


%define kf5_version 5.103.0
%bcond_without released
Name:           kcalutils
Version:        23.04.0
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
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(Qt5Test)
%requires_eq    grantlee5
Conflicts:      libKF5CalendarUtils5 < %{version}

%description
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package -n libKPim5CalendarUtils5
Summary:        Library with utility functions for handling calendar data
%requires_eq    kcalutils

%description  -n libKPim5CalendarUtils5
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package devel
Summary:        Development files for kcalutils
Requires:       libKPim5CalendarUtils5
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5KDELibs4Support) >= %{kf5_version}
Provides:       kcalutils5-devel = %{version}
Obsoletes:      kcalutils5-devel < %{version}

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kcalutils.

%lang_package

%prep
%autosetup -p1 -n kcalutils-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%global grantlee_shortver %(rpm -q --queryformat=%%{VERSION} grantlee5 | cut -d . -f 1-2)

%ldconfig_scriptlets -n libKPim5CalendarUtils5

%files
%license LICENSES/*
%dir %{_kf5_libdir}/grantlee/
%dir %{_kf5_libdir}/grantlee/%{grantlee_shortver}
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/grantlee/%{grantlee_shortver}/kcalendar_grantlee_plugin.so

%files -n libKPim5CalendarUtils5
%{_kf5_libdir}/libKPim5CalendarUtils.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KCalUtils/
%{_kf5_cmakedir}/KF5CalendarUtils/
%{_kf5_cmakedir}/KPim5CalendarUtils/
%{_kf5_libdir}/libKPim5CalendarUtils.so
%{_kf5_mkspecsdir}/qt_KCalUtils.pri

%files lang -f %{name}.lang

%changelog
