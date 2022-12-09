#
# spec file for package kpmcore
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
%global sover 12
Name:           kpmcore
Version:        22.12.0
Release:        0
Summary:        KDE Partition Manager core library
License:        GPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CoreAddons) >= 5.73
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(blkid) >= 2.33.2

%description
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

%package devel
Summary:        Development package for KDE Partition Manager core library
Requires:       libkpmcore%{sover} = %{version}

%description devel
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Development package for kpmcore.

%package -n libkpmcore%{sover}
Summary:        KDE Partition Manager core library
Requires:       %{name} >= %{version}

%description -n libkpmcore%{sover}
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Main kpmcore library.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang kpmcore --all-name

%post -n libkpmcore%{sover} -p /sbin/ldconfig
%postun -n libkpmcore%{sover} -p /sbin/ldconfig

%files
%{_kf5_dbuspolicydir}/org.kde.kpmcore.*.conf
%{_kf5_plugindir}/kpmcore/
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy
%{_libexecdir}/kpmcore_externalcommand

%files -n libkpmcore%{sover}
%license LICENSES/*
%{_kf5_libdir}/libkpmcore.so.%{sover}
%{_kf5_libdir}/libkpmcore.so.*

%files devel
%{_includedir}/kpmcore/
%{_kf5_cmakedir}/KPMcore/
%{_kf5_libdir}/libkpmcore.so

%files lang -f %{name}.lang

%changelog
