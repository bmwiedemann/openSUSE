#
# spec file for package libKF5NetworkManagerQt
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
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           libKF5NetworkManagerQt
Version:        5.101.0
Release:        0
Summary:        A Qt wrapper for NetworkManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source:         networkmanager-qt-%{version}.tar.xz
%if %{with released}
Source1:        networkmanager-qt-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  pkgconfig(libnm) >= 1.0.0

%description
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%package devel
Summary:        A Qt wrapper for NetworkManager DBus API
Requires:       libKF5NetworkManagerQt%{soversion} = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5Network) >= 5.15.0
Requires:       pkgconfig(libnm) >= 1.0.0

%description devel
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication. Development files.

%package -n libKF5NetworkManagerQt%{soversion}
Summary:        A Qt wrapper for NetworkManager DBus API

%description -n libKF5NetworkManagerQt%{soversion}
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%prep
%autosetup -p1 -n networkmanager-qt-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%post -n libKF5NetworkManagerQt%{soversion} -p /sbin/ldconfig
%postun -n libKF5NetworkManagerQt%{soversion} -p /sbin/ldconfig

%files -n libKF5NetworkManagerQt%{soversion}
%license LICENSES/*
%{_kf5_debugdir}/networkmanagerqt.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5NetworkManagerQt.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5NetworkManagerQt/
%{_kf5_libdir}/libKF5NetworkManagerQt.so

%changelog
