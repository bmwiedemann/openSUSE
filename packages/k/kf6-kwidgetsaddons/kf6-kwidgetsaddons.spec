#
# spec file for package kf6-kwidgetsaddons
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

%define rname kwidgetsaddons
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kwidgetsaddons
Version:        6.3.0
Release:        0
Summary:        Large set of desktop widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%package -n libKF6WidgetsAddons6
Summary:        Large set of desktop widgets
Requires:       kf6-kwidgetsaddons >= %{version}

%description -n libKF6WidgetsAddons6
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%package devel
Summary:        Large set of desktop widgets: Build Environment
Requires:       libKF6WidgetsAddons6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%lang_package -n libKF6WidgetsAddons6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kwidgetsaddons6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6WidgetsAddons6

%files
%{_kf6_debugdir}/kwidgetsaddons.categories

%files -n libKF6WidgetsAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6WidgetsAddons.so.*

%files devel
%doc %{_kf6_qchdir}/KF6WidgetsAddons.*
%{_kf6_cmakedir}/KF6WidgetsAddons/
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_plugindir}/designer/kwidgetsaddons6widgets.so

%files -n libKF6WidgetsAddons6-lang -f kwidgetsaddons6.lang

%changelog
