#
# spec file for package ksanecore
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           ksanecore
Version:        24.05.2
Release:        0
Summary:        Qt interface for the SANE library for scanner hardware
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         fix-scanner-search-crash.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  sane-backends-devel
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%package -n libKSaneCore6-1
Summary:        Qt interface for the SANE library for scanner hardware
# Same translation catalog name
Conflicts:      libKSaneCore1-lang
Obsoletes:      ksanecore-lang < %{version}

%description -n libKSaneCore6-1
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%package devel
Summary:        Development files for KSaneCore, a Qt library for scanner hardware
Requires:       libKSaneCore6-1 = %{version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.
This package contains the development files required to use KSaneCore in other
applications.

%lang_package -n libKSaneCore6-1

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKSaneCore6-1

%files -n libKSaneCore6-1
%license LICENSES/*
%{_kf6_libdir}/libKSaneCore6.so.*

%files devel
%{_includedir}/KSaneCore6/
%{_kf6_cmakedir}/KSaneCore6/
%{_kf6_libdir}/libKSaneCore6.so

%files -n libKSaneCore6-1-lang -f %{name}.lang

%changelog
