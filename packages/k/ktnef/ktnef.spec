#
# spec file for package ktnef
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.103.0
%define libname libKPim5Tnef5
%bcond_without released
Name:           ktnef
Version:        23.04.0
Release:        0
Summary:        TNEF support
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This package contains additional libraries for KDE PIM applications.

%package common
Summary:        Files requires by libKPim5Tnef5
Conflicts:      libKF5Tnef5 < %{version}

%description common
Files that can't be in the libKPim5Tnef5 package anymore.

%package -n %{libname}
Summary:        TNEF Support
%requires_eq    ktnef-common

%description  -n %{libname}
This package contains the TNEF support library for KDE PIM applications

%package devel
Summary:        Development files for libKPim5Tnef5
Requires:       %{libname} = %{version}
Requires:       cmake(KF5CalendarCore)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n ktnef-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files common
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n %{libname}
%{_kf5_libdir}/libKPim5Tnef.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KTNEF/
%{_kf5_cmakedir}/KF5Tnef/
%{_kf5_cmakedir}/KPim5Tnef/
%{_kf5_libdir}/libKPim5Tnef.so
%{_kf5_mkspecsdir}/qt_KTNef.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
