#
# spec file for package kcalutils
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           kcalutils
Version:        24.05.1
Release:        0
Summary:        Library with utility functions for handling calendar data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Conflicts:      libKF6CalendarUtils5 < %{version}

%description
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package -n libKPim6CalendarUtils6
Summary:        Library with utility functions for handling calendar data
Requires:       kcalutils = %{version}
Obsoletes:      libKF5CalendarUtils5 < %{version}
Obsoletes:      libKPim5CalendarUtils5 < %{version}

%description  -n libKPim6CalendarUtils6
This library provides a set of utility functions that help
applications access and use calendar data via the KCalCore library.

%package devel
Summary:        Development files for kcalutils
Requires:       libKPim6CalendarUtils6
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Provides:       kcalutils5-devel = %{version}
Obsoletes:      kcalutils5-devel < %{version}

%description devel
This package contains necessary include files and libraries needed
to develop applications wanting to use kcalutils.

%lang_package

%prep
%autosetup -p1 -n kcalutils-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6CalendarUtils6

%files
%license LICENSES/*
%{_kf6_debugdir}/kcalutils.categories
%{_kf6_debugdir}/kcalutils.renamecategories
%dir %{_kf6_plugindir}/kf6/ktexttemplate
%{_kf6_plugindir}/kf6/ktexttemplate/kcalendar_grantlee_plugin.so

%files -n libKPim6CalendarUtils6
%{_kf6_libdir}/libKPim6CalendarUtils.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6CalendarUtils.*
%{_includedir}/KPim6/KCalUtils/
%{_kf6_cmakedir}/KPim6CalendarUtils/
%{_kf6_libdir}/libKPim6CalendarUtils.so

%files lang -f %{name}.lang

%changelog
