#
# spec file for package kf6-ksvg
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

%define rname ksvg
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-ksvg
Version:        6.3.0
Release:        0
Summary:        Components for handling SVGs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{_kf6_bugfix_version}

%description
Components for handling SVGs

%package imports
Summary:        QML Components for ksvg

%description imports
This package contains QML imports for SVG handling.

%package -n libKF6Svg6
Summary:        ksvg library
Requires:       kf6-ksvg >= %{version}
Recommends:     kf6-ksvg-imports = %{version}

%description -n libKF6Svg6
The ksvg library.

%package devel
Summary:        Development Files for the ksvg framework
Requires:       libKF6Svg6 = %{version}

%description devel
Development Files for the ksvg framework.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKF6Svg6

%files
%{_kf6_debugdir}/ksvg.categories

%files imports
%{_kf6_qmldir}/org/kde/ksvg/

%files -n libKF6Svg6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Svg.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Svg.*
%{_kf6_cmakedir}/KF6Svg/
%{_kf6_includedir}/KSvg/
%{_kf6_libdir}/libKF6Svg.so

%changelog
