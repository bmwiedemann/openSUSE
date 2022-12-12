#
# spec file for package kpeople5
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


%define rname kpeople
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kpeople5
Version:        5.101.0
Release:        0
Summary:        Library for access to contacts and identity holders
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Sql) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
A library that provides access to all contacts and the people who hold them.

%package devel
Summary:        Library for access to contacts and identity holders
Requires:       %{name} = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
A library that provides access to all contacts and the people who hold them.
Development files for kpeople5.

%lang_package

%prep
%autosetup -p1 -n kpeople-%{version}

%build
%cmake_kf5 -d build -- -DENABLE_EXAMPLES=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%license LICENSES/*
%{_kf5_debugdir}/kpeople.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5People*.so.*
%{_kf5_qmldir}/

%files devel
%{_kf5_libdir}/libKF5People*.so
%{_kf5_libdir}/cmake/KF5People/
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KPeople.pri
%{_kf5_mkspecsdir}/qt_KPeopleWidgets.pri

%changelog
