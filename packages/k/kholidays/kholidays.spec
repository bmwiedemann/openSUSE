#
# spec file for package kholidays
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


%define lname   libKF5Holidays5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kholidays
Version:        5.74.0
Release:        0
Summary:        Holiday calculation library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools)
%endif

%description
This package contains a library which helps developers determining when holidays occur.

%package -n %{lname}
Summary:        Holiday API for KDE PIM
Group:          System/GUI/KDE
Recommends:     %{lname}-lang
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}

%description -n %{lname}
This package contains a library which helps developers determining when holidays occur.

%package devel
Summary:        Development files for the KDE PIM Holiday API
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core)

%description devel
This package contains necessary include files and libraries needed
to develop applications depending on the kholidays library

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name --with-qt
  %endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc DESIGN

%files -n %{lname}
%license LICENSES/*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_debugdir}/kholidays.categories
%{_kf5_libdir}/libKF5Holidays.so.*
%{_kf5_qmldir}/org/kde/kholidays/

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5Holidays/
%{_kf5_includedir}/KHolidays/
%{_kf5_includedir}/kholidays_version.h
%{_kf5_libdir}/libKF5Holidays.so
%{_kf5_mkspecsdir}/qt_KHolidays.pri

%if %{with lang}
%files -n %{lname}-lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
