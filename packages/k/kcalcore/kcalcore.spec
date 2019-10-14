#
# spec file for package kcalcore
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.19.0
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kcalcore
Version:        19.08.2
Release:        0
Summary:        KDE PIM Libraries: KCalCore
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Revert-GIT_SILENT-increase-version.patch
BuildRequires:  bison
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kdelibs4support-devel >= %{kf5_version}
BuildRequires:  libical-devel >= 1.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0

%description
This package contains the KCalCore library for KDE PIM applications.

%package -n libKF5CalendarCore5
Summary:        KDE PIM Libraries: KCalCore
Group:          Development/Libraries/KDE

%description  -n libKF5CalendarCore5
The core library for the KDE PIM Calendar

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       kdelibs4support-devel >= %{kf5_version}
Requires:       libKF5CalendarCore5 = %{version}
Requires:       libical-devel >= 0.42
Obsoletes:      kcalcore5-devel < %{version}
Provides:       kcalcore5-devel = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%prep
%autosetup -p1 -n kcalcore-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build

%post -n libKF5CalendarCore5 -p /sbin/ldconfig
%postun -n libKF5CalendarCore5 -p /sbin/ldconfig

%files -n libKF5CalendarCore5
%license COPYING*
%{_kf5_libdir}/libKF5CalendarCore.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5CalendarCore/
%{_kf5_includedir}/KCalendarCore/
%{_kf5_includedir}/kcalcore_version.h
%{_kf5_includedir}/kcalendarcore_version.h
%{_kf5_libdir}/libKF5CalendarCore.so
%{_kf5_mkspecsdir}/qt_KCalendarCore.pri

%changelog
