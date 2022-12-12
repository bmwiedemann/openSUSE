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
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           threadweaver
Version:        5.101.0
Release:        0
Summary:        KDE Helper for multithreaded programming
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

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
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0

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

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

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
