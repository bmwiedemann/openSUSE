#
# spec file for package kf6-kquickcharts
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

%define rname kquickcharts
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kquickcharts
Version:        6.3.0
Release:        0
Summary:        Set of charts for QtQuick applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{_kf6_bugfix_version}
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package devel
Summary:        Header files for kquickcharts, a set of charts for QtQuick applications
Requires:       kf6-kquickcharts >= %{version}

%description devel
Development files for KQuickCharts, a set of charts that can be used from QtQuick
applications.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kquickcharts.categories
%{_kf6_libdir}/libQuickCharts.so.*
%{_kf6_libdir}/libQuickChartsControls.so.*
%{_kf6_qmldir}/org/kde/quickcharts/

%files devel
%{_kf6_cmakedir}/KF6QuickCharts/
%{_kf6_libdir}/libQuickCharts.so
%{_kf6_libdir}/libQuickChartsControls.so

%changelog
