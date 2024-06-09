#
# spec file for package kf6-krunner
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

%define rname krunner
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-krunner
Version:        6.3.0
Release:        0
Summary:        KDE Framework for providing different actions given a string query
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
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ItemModels) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KDE Framework for providing different actions given a string query.

%package -n libKF6Runner6
Summary:        KDE Framework for providing different actions given a string query
Requires:       kf6-krunner >= %{version}

%description -n libKF6Runner6
KDE Framework for providing different actions given a string query.

%package devel
Summary:        KDE Framework for providing different actions given a string query
Requires:       libKF6Runner6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
Files needed for developing custom runners or frontends.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Runner6

%files
%{_kf6_debugdir}/krunner.categories
%{_kf6_debugdir}/krunner.renamecategories

%files -n libKF6Runner6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Runner.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Runner.*
%{_kf6_cmakedir}/KF6Runner/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.krunner1.xml
%{_kf6_includedir}/KRunner/
%{_kf6_libdir}/libKF6Runner.so
%{_kf6_sharedir}/kdevappwizard/

%changelog
