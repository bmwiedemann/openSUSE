#
# spec file for package kweathercore
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


%define soversion 5
%bcond_without  released
Name:           kweathercore
Version:        0.7
Release:        0
Summary:        Library to facilitate retrieval of weather information
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  doxygen
BuildRequires:  libqt5-qttools-qhelpgenerator
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)

%description
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package -n libKF5KWeatherCore%{soversion}
Summary:        Library to facilitate retrieval of weather information

%description -n libKF5KWeatherCore%{soversion}
Shared objects for kweathercore.
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package devel
Summary:        Development headers for kweathercore
Requires:       libKF5KWeatherCore%{soversion} = %{version}

%description devel
Required headers to build components based on kweathercore.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_QCH=ON

%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libKF5KWeatherCore%{soversion}

%files -n libKF5KWeatherCore%{soversion}
%license LICENSES/*
%{_kf5_libdir}/libKF5KWeatherCore.so.*

%files devel
%{_kf5_cmakedir}/KF5KWeatherCore/
%{_kf5_includedir}/KWeatherCore/
%{_kf5_includedir}/kweathercore_version.h
%{_kf5_libdir}/libKF5KWeatherCore.so
%{_kf5_mkspecsdir}/qt_KWeatherCore.pri
%{_kf5_sharedir}/doc/qch/

%changelog
