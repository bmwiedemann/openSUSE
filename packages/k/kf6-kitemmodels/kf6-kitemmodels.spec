#
# spec file for package kf6-kitemmodels
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

%define rname kitemmodels
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_with python
%bcond_without released
Name:           kf6-kitemmodels
Version:        6.3.0
Release:        0
Summary:        Set of item models extending the Qt model-view framework
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
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KItemModels provides a set of item models extending the Qt model-view framework.

%package -n libKF6ItemModels6
Summary:        Set of item models extending the Qt model-view framework
%requires_ge    libQt6Core6

%description -n libKF6ItemModels6
KItemModels provides a set of item models extending the Qt model-view framework.

%package imports
Summary:        Set of item models extending the Qt model-view framework
Requires:       libKF6ItemModels6 = %{version}

%description imports
KItemModels provides a set of item models extending the Qt model-view framework.
This package provides support to use KItemModels with the QtQuick framework.

%package devel
Summary:        Set of item models extending the Qt model-view framework
Requires:       libKF6ItemModels6 = %{version}

%description devel
KItemModels provides a set of item models extending the Qt model-view framework.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6ItemModels6

%files
%{_kf6_debugdir}/kitemmodels.categories
%{_kf6_debugdir}/kitemmodels.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/kitemmodels/

%files -n libKF6ItemModels6
%license LICENSES/*
%{_kf6_libdir}/libKF6ItemModels.so.*

%files devel
%doc %{_kf6_qchdir}/KF6ItemModels.*
%{_kf6_cmakedir}/KF6ItemModels/
%{_kf6_includedir}/KItemModels/
%{_kf6_libdir}/libKF6ItemModels.so

%changelog
