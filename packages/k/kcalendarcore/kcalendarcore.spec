#
# spec file for package kcalendarcore
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kcalendarcore
Version:        5.101.0
Release:        0
Summary:        Library to access and handle calendar data
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(LibIcal) >= 3.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

%package -n libKF5CalendarCore5
Summary:        Library to access to and handle calendar data

%description  -n libKF5CalendarCore5
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

%package devel
Summary:        Development files for kcalendarcore, a library to handle calendar data
Requires:       libKF5CalendarCore5 = %{version}
Requires:       cmake(LibIcal) >= 3.0
# kcalcore-devel version was 19.11.70 in the unstable repo, 19.08.1 in stable
Provides:       kcalcore-devel
Obsoletes:      kcalcore-devel < 19.12
# kcalcore5 was provided/obsoleted by kcalcore
Provides:       kcalcore5-devel
Obsoletes:      kcalcore5-devel < 19.12

%description devel
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP. This package contains the headers necessary to
develop applications making use of KCalendarCore.

%prep
%autosetup -p1

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}%{_kf5_includedir}

%post -n libKF5CalendarCore5 -p /sbin/ldconfig
%postun -n libKF5CalendarCore5 -p /sbin/ldconfig

%files -n libKF5CalendarCore5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5CalendarCore.so.*

%files devel
%{_kf5_cmakedir}/KF5CalendarCore/
%{_kf5_includedir}/KCalendarCore/
%{_kf5_includedir}/kcalcore_version.h
%{_kf5_libdir}/libKF5CalendarCore.so
%{_kf5_libdir}/pkgconfig/KF5CalendarCore.pc
%{_kf5_mkspecsdir}/qt_KCalendarCore.pri

%changelog
