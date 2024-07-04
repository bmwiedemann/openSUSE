#
# spec file for package plasma6-activities-stats
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%define rname   plasma-activities-stats
%bcond_without released
Name:           plasma6-activities-stats
Version:        6.1.2
Release:        0
Summary:        KDE Plasma Activities support
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package -n libPlasmaActivitiesStats1
Summary:        Library for KDE's Plasma Activities support
Requires:       plasma6-activities-stats >= %{version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description -n libPlasmaActivitiesStats1
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package devel
Summary:        KDE Plasma Activities support
Requires:       libPlasmaActivitiesStats1 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libPlasmaActivitiesStats1

%files
%{_kf6_debugdir}/plasma-activities-stats.categories
%{_kf6_debugdir}/plasma-activities-stats.renamecategories

%files -n libPlasmaActivitiesStats1
%license LICENSES/*
%{_kf6_libdir}/libPlasmaActivitiesStats.so.*

%files devel
%doc %{_kf6_qchdir}/PlasmaActivitiesStats.*
%{_includedir}/PlasmaActivitiesStats/
%{_kf6_cmakedir}/PlasmaActivitiesStats/
%{_kf6_libdir}/libPlasmaActivitiesStats.so
%{_kf6_pkgconfigdir}/PlasmaActivitiesStats.pc

%changelog
