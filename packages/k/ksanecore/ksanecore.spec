#
# spec file for package ksanecore
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


%define _so 1
%define lname libKSaneCore
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ksanecore
Version:        22.12.1
Release:        0
Summary:        Qt interface for the SANE library for scanner hardware
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  sane-backends-devel
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)

%description
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%package devel
Summary:        Development files for KSaneCore, a Qt library for scanner hardware
Requires:       %{lname}%{_so} = %{version}
Requires:       pkgconfig
Requires:       sane-backends-devel
Requires:       cmake(KF5Wallet)
Requires:       cmake(KF5WidgetsAddons)
Requires:       cmake(Qt5Gui)

%description devel
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.
This package contains the development files required to use KSaneCore in other
applications.

%package -n %{lname}%{_so}
Summary:        Qt interface for the SANE library for scanner hardware
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n %{lname}%{_so}
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n %{lname}%{_so} -p /sbin/ldconfig
%postun -n %{lname}%{_so} -p /sbin/ldconfig

%files -n %{lname}%{_so}
%license LICENSES/*
%{_kf5_libdir}/%{lname}.so.*

%files devel
%{_kf5_cmakedir}/KSaneCore/
%{_includedir}/KSaneCore/
%{_kf5_libdir}/%{lname}.so

%files lang -f %{name}.lang

%changelog
