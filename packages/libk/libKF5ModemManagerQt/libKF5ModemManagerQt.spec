#
# spec file for package libKF5ModemManagerQt
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


%define soversion 6
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           libKF5ModemManagerQt
Version:        5.115.0
Release:        0
Summary:        Qt wrapper for ModemManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source:         modemmanager-qt-%{version}.tar.xz
%if %{with released}
Source1:        modemmanager-qt-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0

%description
Qt5 wrapper for ModemManager DBus API.

%package devel
Summary:        Development package for the libmm-qt library
Requires:       libKF5ModemManagerQt%{soversion} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}
Requires:       cmake(Qt5DBus) >= %{qt5_version}
Requires:       pkgconfig(ModemManager) >= 1.0.0

%description devel
Qt5 wrapper for ModemManager DBus API. Development files.

%package -n libKF5ModemManagerQt%{soversion}
Summary:        Qt wrapper around the ModemManager libraries

%description -n libKF5ModemManagerQt%{soversion}
Qt5 wrapper for ModemManager DBus API.

%prep
%autosetup -p1 -n modemmanager-qt-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libKF5ModemManagerQt%{soversion}

%files -n libKF5ModemManagerQt%{soversion}
%license LICENSES/*
%doc README
%{_kf5_debugdir}/modemmanagerqt.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5ModemManagerQt.so.*

%files devel
%{_kf5_includedir}/ModemManagerQt/
%{_kf5_libdir}/cmake/KF5ModemManagerQt/
%{_kf5_libdir}/libKF5ModemManagerQt.so

%changelog
