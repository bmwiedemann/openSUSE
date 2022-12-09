#
# spec file for package libkmahjongg
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
Name:           libkmahjongg
Version:        22.12.0
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  xz
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}

%description
This package contains data which is required by KDE games.

%package -n libKF5KMahjongglib5
Summary:        Library for Mahjongg tiles
License:        LGPL-2.1-or-later
Requires:       libkmahjongg

%description -n libKF5KMahjongglib5
This package contains the library for Mahjongg tiles.

%package devel
Summary:        Library for Mahjongg tiles: Build Environment
License:        LGPL-2.1-or-later
Requires:       libKF5KMahjongglib5 = %{version}
Obsoletes:      %{name}-kf5-devel < %{version}
Provides:       %{name}-kf5-devel = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop games that uses Mahjongg tiles.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes -s %{buildroot}

%post -n libKF5KMahjongglib5 -p /sbin/ldconfig
%postun -n libKF5KMahjongglib5 -p /sbin/ldconfig

%files
%doc README
%{_kf5_debugdir}/libkmahjongg.categories
%{_kf5_sharedir}/kmahjongglib/

%files -n libKF5KMahjongglib5
%license LICENSES/*
%doc README
%{_kf5_libdir}/libKF5KMahjongglib.so.*

%files devel
%doc README
%{_kf5_cmakedir}/KF5KMahjongglib
%{_kf5_includedir}/KMahjongg/
%{_kf5_libdir}/libKF5KMahjongglib.so

%files lang -f %{name}.lang

%changelog
