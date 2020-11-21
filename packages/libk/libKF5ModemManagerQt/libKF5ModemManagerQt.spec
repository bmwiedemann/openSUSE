#
# spec file for package libKF5ModemManagerQt
#
# Copyright (c) 2020 SUSE LLC
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
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           libKF5ModemManagerQt
Version:        5.75.0
Release:        0
Summary:        Qt wrapper for ModemManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/modemmanager-qt-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/modemmanager-qt-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0

%description
Qt5 wrapper for ModemManager DBus API.

%package devel
Summary:        Development package for the libmm-qt library
Group:          Development/Libraries/KDE
Requires:       libKF5ModemManagerQt%{soversion} = %{version}
Requires:       cmake(Qt5Core) >= 5.12.0
Requires:       cmake(Qt5DBus) >= 5.12.0
Requires:       cmake(Qt5Xml) >= 5.12.0
Requires:       pkgconfig(ModemManager) >= 1.0.0

%description devel
Qt5 wrapper for ModemManager DBus API. Development files.

%package -n libKF5ModemManagerQt%{soversion}
Summary:        Qt wrapper around the ModemManager libraries
Group:          Development/Libraries/KDE

%description -n libKF5ModemManagerQt%{soversion}
Qt5 wrapper for ModemManager DBus API.

%prep
%setup -q -n modemmanager-qt-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -n libKF5ModemManagerQt%{soversion} -p /sbin/ldconfig
%postun -n libKF5ModemManagerQt%{soversion} -p /sbin/ldconfig

%files -n libKF5ModemManagerQt%{soversion}
%license LICENSES/*
%doc README
%{_kf5_debugdir}/modemmanagerqt.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5ModemManagerQt.so.*

%files devel
%license LICENSES/*
%{_kf5_includedir}/*.h
%{_kf5_includedir}/ModemManagerQt/
%{_kf5_libdir}/cmake/KF5ModemManagerQt/
%{_kf5_libdir}/libKF5ModemManagerQt.so

%changelog
