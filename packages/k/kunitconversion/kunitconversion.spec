#
# spec file for package kunitconversion
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


%define lname   libKF5UnitConversion5
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kunitconversion
Version:        5.82.0
Release:        0
Summary:        Tool for converting physical units
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

%description
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

%package -n %{lname}
Summary:        Converting physical units
Group:          System/GUI/KDE
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

%package devel
Summary:        Converting physical units: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5UnitConversion.so.*

%files devel
%license LICENSES/*
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*.h
%{_kf5_includedir}/*/
%{_kf5_libdir}/cmake/KF5UnitConversion/
%{_kf5_libdir}/libKF5UnitConversion.so
%{_kf5_mkspecsdir}/qt_KUnitConversion.pri

%changelog
