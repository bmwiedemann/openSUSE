#
# spec file for package ktnef
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktnef
Version:        20.08.1
Release:        0
Summary:        KDE PIM Libraries: TNEF support
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(Qt5Test)
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKF5Tnef5
Summary:        KDE PIM Libraries: TNEF Support
Group:          System/Libraries

%description  -n libKF5Tnef5
This package contains the TNEF support library for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       libKF5Tnef5 = %{version}
Requires:       cmake(KF5CalendarCore)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n ktnef-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5Tnef5 -p /sbin/ldconfig
%postun -n libKF5Tnef5 -p /sbin/ldconfig

%files -n libKF5Tnef5
%license LICENSES/*
%{_kf5_libdir}/libKF5Tnef.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5Tnef/
%{_kf5_includedir}/KTNEF/
%{_kf5_includedir}/ktnef_version.h
%{_kf5_libdir}/libKF5Tnef.so
%{_kf5_mkspecsdir}/qt_KTNef.pri

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
