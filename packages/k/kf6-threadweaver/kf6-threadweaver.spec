#
# spec file for package kf6-threadweaver
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname threadweaver
# Full KF6 version (e.g. 6.19.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-threadweaver
Version:        6.19.0
Release:        0
Summary:        KDE Helper for multithreaded programming
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
ThreadWeaver is a helper for multithreaded programming. It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between jobs
and ThreadWeaver will work out the most efficient way of dividing the work
between threads within a set of resource limits.

%package -n libKF6ThreadWeaver6
Summary:        KDE Helper for multithreaded programming

%description -n libKF6ThreadWeaver6
ThreadWeaver is a helper for multithreaded programming. It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between jobs
and ThreadWeaver will work out the most efficient way of dividing the work
between threads within a set of resource limits.

%package devel
Summary:        KDE Helper for multithreaded programming
Requires:       libKF6ThreadWeaver6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Development files for the KF6 ThreadWeaver library.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6ThreadWeaver6

%files -n libKF6ThreadWeaver6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ThreadWeaver.so.*

%files devel
%{_kf6_cmakedir}/KF6ThreadWeaver/
%{_kf6_includedir}/ThreadWeaver/
%{_kf6_libdir}/libKF6ThreadWeaver.so

%changelog
