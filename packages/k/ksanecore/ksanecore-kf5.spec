#
# spec file for package ksanecore-kf5
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


%define kf5_version 5.90.0
%define qt5_version 5.15.2

%define rname ksanecore
%bcond_without released
Name:           ksanecore-kf5
Version:        24.05.1
Release:        0
Summary:        Qt interface for the SANE library for scanner hardware
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  pkgconfig(sane-backends)

%description
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%package -n libKSaneCore1
Summary:        Qt interface for the SANE library for scanner hardware
Obsoletes:      ksanecore-lang < %{version}

%description -n libKSaneCore1
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.

%package devel
Summary:        Development files for KSaneCore, a Qt library for scanner hardware
Requires:       libKSaneCore1 = %{version}
Requires:       cmake(Qt5Gui) >= %{qt5_version}

%description devel
KSaneCore is a Qt-based interface for SANE library to control scanner hardware.
This package contains the development files required to use KSaneCore in other
applications.

%lang_package -n libKSaneCore1

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libKSaneCore1

%files -n libKSaneCore1
%license LICENSES/*
%{_kf5_libdir}/libKSaneCore.so.*

%files devel
%{_includedir}/KSaneCore/
%{_kf5_cmakedir}/KSaneCore/
%{_kf5_libdir}/libKSaneCore.so

%files -n libKSaneCore1-lang -f %{name}.lang

%changelog
