#
# spec file for package kopeninghours
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

%bcond_without released
Name:           kopeninghours
Version:        24.05.2
Release:        0
Summary:        OSM opening hours expression parser and evaluator
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
A library for parsing and evaluating OSM opening hours expressions.

%package imports
Summary:        QML imports for kopeninghours
Requires:       libKOpeningHours1 = %{version}

%description imports
kopeninghours is a library for parsing and evaluating OSM opening hours
expressions.
This package contains QML imports for using kopeninghours in QML apps.

%package -n libKOpeningHours1
Summary:        OSM opening hours expression parser and evaluator
Requires:       kopeninghours >= %{version}

%description -n libKOpeningHours1
A library for parsing and evaluating OSM opening hours expressions.

%package devel
Summary:        Development files for KOpeningHours
Requires:       libKOpeningHours1 = %{version}

%description devel
Include files and libraries needed to build programs that use the KOpeningHours
library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DBUILD_QCH:BOOL=TRUE \
  -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name}

%check
export QT_QPA_PLATFORM=offscreen
%ctest

%ldconfig_scriptlets -n libKOpeningHours1

%files
%{_kf6_debugdir}/org_kde_kopeninghours.categories

%files imports
%{_kf6_qmldir}/org/kde/kopeninghours/

%files -n libKOpeningHours1
%license LICENSES/*
%{_kf6_libdir}/libKOpeningHours.so.*

%files devel
%doc %{_kf6_qchdir}/KOpeningHours.*
%{_includedir}/KOpeningHours/
%{_includedir}/kopeninghours/
%{_includedir}/kopeninghours_version.h
%{_kf6_cmakedir}/KOpeningHours/
%{_kf6_libdir}/libKOpeningHours.so

%files lang -f %{name}.lang

%changelog
