#
# spec file for package plasma6-activities
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

%define rname plasma-activities
%bcond_without released
Name:           plasma6-activities
Version:        6.1.2
Release:        0
Summary:        Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package tools
Summary:        Command-line tools for Plasma Activity management
Requires:       libPlasmaActivities6 = %{version}

%description tools
This package provides command-line tools to manipulate Plasma Activities.

%package -n libPlasmaActivities6
Summary:        Library for Plasma Activities support
Requires:       plasma6-activities >= %{version}

%description -n libPlasmaActivities6
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package imports
Summary:        Plasma Activities support
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description imports
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
QML imports.

%package devel
Summary:        Plasma Activities support
Requires:       libPlasmaActivities6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Kactivities provides an API for using and interacting with the Plasma Activities Manager.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=ON

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libPlasmaActivities6

%files
%{_kf6_debugdir}/plasma-activities.categories
%{_kf6_debugdir}/plasma-activities.renamecategories

%files tools
%{_kf6_bindir}/plasma-activities-cli6

%files -n libPlasmaActivities6
%license LICENSES/*
%{_kf6_libdir}/libPlasmaActivities.so.*

%files imports
%{_kf6_qmldir}/org/kde/activities/

%files devel
%doc %{_kf6_qchdir}/PlasmaActivities.*
%{_kf6_cmakedir}/PlasmaActivities/
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_pkgconfigdir}/PlasmaActivities.pc

%changelog
