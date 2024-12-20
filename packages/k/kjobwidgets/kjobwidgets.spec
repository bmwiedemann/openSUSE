#
# spec file for package kjobwidgets
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


%define lname   libKF5JobWidgets5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kjobwidgets
Version:        5.116.0
Release:        0
Summary:        Widgets for showing progress of asynchronous jobs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  pkgconfig(x11)

%description
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package -n %{lname}
Summary:        Widgets for showing progress of asynchronous jobs

%description -n %{lname}
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package devel
Summary:        Widgets for showing progress of asynchronous jobs
Requires:       %{lname} = %{version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}

%description devel
KJobWIdgets provides widgets for showing progress of asynchronous jobs.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kjobwidgets5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f kjobwidgets5.lang

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5JobWidgets.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5JobWidgets.so
%{_kf5_libdir}/cmake/KF5JobWidgets/
%{_kf5_includedir}/KJobWidgets
%{_kf5_mkspecsdir}/qt_KJobWidgets.pri
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobView.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobViewServer.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.JobViewV2.xml

%changelog
