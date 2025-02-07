#
# spec file for package kweathercore
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kweathercore
Version:        24.12.2
Release:        0
Summary:        Library to facilitate retrieval of weather information
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  doxygen
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package -n libKWeatherCore6
Summary:        Library to facilitate retrieval of weather information

%description -n libKWeatherCore6
Shared objects for kweathercore.
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package devel
Summary:        Development headers for kweathercore
Requires:       libKWeatherCore6 = %{version}

%description devel
Required headers to build components based on kweathercore.

%lang_package -n libKWeatherCore6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKWeatherCore6

%files -n libKWeatherCore6
%license LICENSES/*
%{_kf6_libdir}/libKWeatherCore.so.*

%files devel
%doc %{_kf6_qchdir}/KWeatherCore.*
%{_includedir}/KWeatherCore/
%{_includedir}/kweathercore_version.h
%{_kf6_cmakedir}/KWeatherCore/
%{_kf6_libdir}/libKWeatherCore.so
%{_kf6_mkspecsdir}/qt_KWeatherCore.pri

%files -n libKWeatherCore6-lang -f %{name}.lang

%changelog
