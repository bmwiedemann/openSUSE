#
# spec file for package kf6-kplotting
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

%define rname kplotting
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kplotting
Version:        6.3.0
Release:        0
Summary:        KDE Data plotting library
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
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KPlotWidget is a QWidget-derived class that provides a virtual base
class for data plotting. The idea behind KPlotWidget is that a
developer only has to specify information in "data units", i.e. the
natural units of the data being plotted. KPlotWidget automatically
converts everything to screen pixel units.

%package -n libKF6Plotting6
Summary:        KDE Data plotting library

%description -n libKF6Plotting6
KPlotWidget is a QWidget-derived class that provides a virtual base
class for data plotting. The idea behind KPlotWidget is that a
developer only has to specify information in "data units", i.e. the
natural units of the data being plotted. KPlotWidget automatically
converts everything to screen pixel units.

%package devel
Summary:        Build environment for the KDE data plotting library
Requires:       libKF6Plotting6 = %{version}

%description devel
Development files for KPlotWidget, which is a QWidget-derived class
that provides a virtual base class for data plotting.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Plotting6

%files -n libKF6Plotting6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Plotting.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Plotting.*
%{_kf6_includedir}/KPlotting/
%{_kf6_cmakedir}/KF6Plotting/
%{_kf6_libdir}/libKF6Plotting.so
%{_kf6_plugindir}/designer/kplotting6widgets.so

%changelog
