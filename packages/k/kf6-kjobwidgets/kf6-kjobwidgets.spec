#
# spec file for package kf6-kjobwidgets
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


%define qt6_version 6.6.0

%define rname kjobwidgets
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kjobwidgets
Version:        6.3.0
Release:        0
Summary:        Widgets for showing progress of asynchronous jobs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package -n libKF6JobWidgets6
Summary:        Widgets for showing progress of asynchronous jobs
Requires:       kf6-kjobwidgets >= %{version}

%description -n libKF6JobWidgets6
KJobWIdgets provides widgets for showing progress of asynchronous jobs.

%package devel
Summary:        Widgets for showing progress of asynchronous jobs
Requires:       libKF6JobWidgets6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KJobWIdgets provides widgets for showing progress of asynchronous jobs.
Development files.

%lang_package -n libKF6JobWidgets6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kjobwidgets6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6JobWidgets6

%files
%{_kf6_debugdir}/kjobwidgets.categories
%{_kf6_debugdir}/kjobwidgets.renamecategories

%files -n libKF6JobWidgets6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6JobWidgets.so.*

%files devel
%doc %{_kf6_qchdir}/KF6JobWidgets.*
%{_kf6_cmakedir}/KF6JobWidgets/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobView.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobViewServer.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.JobViewV2.xml
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so

%files -n libKF6JobWidgets6-lang -f kjobwidgets6.lang

%changelog
