#
# spec file for package threadweaver
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


%define lname   libKF5ThreadWeaver5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           threadweaver
Version:        5.116.0
Release:        0
Summary:        KDE Helper for multithreaded programming
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-UPSTREAM -- cmake 4 compat
Patch0:         threadweaver-cmake4.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}

%description
ThreadWeaver is a helper for multithreaded programming.  It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between the jobs
and ThreadWeaver will work out the most efficient way of dividing the work between
threads within a set of resource limits.

%package -n %{lname}
Summary:        KDE Helper for multithreaded programming
%requires_ge    libQt5Core5

%description -n %{lname}
ThreadWeaver is a helper for multithreaded programming.  It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between the jobs
and ThreadWeaver will work out the most efficient way of dividing the work between
threads within a set of resource limits.

%package devel
Summary:        KDE Helper for multithreaded programming
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
ThreadWeaver is a helper for multithreaded programming.  It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between the jobs
and ThreadWeaver will work out the most efficient way of dividing the work between
threads within a set of resource limits. Development files.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5ThreadWeaver.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5ThreadWeaver/
%{_kf5_libdir}/libKF5ThreadWeaver.so
%{_kf5_mkspecsdir}/qt_ThreadWeaver.pri

%changelog
