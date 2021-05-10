#
# spec file for package kitemmodels
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


%define lname   libKF5ItemModels5
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_with python
# Only needed for the package signature condition
%bcond_without lang
Name:           kitemmodels
Version:        5.82.0
Release:        0
Summary:        Set of item models extending the Qt model-view framework
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
%if %{with python}
BuildRequires:  python3-clang
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-qt5-utils
BuildRequires:  python3-sip-devel
%endif

%description
KItemModels provides a set of item models extending the Qt model-view framework.

%package -n %{lname}
Summary:        Set of item models extending the Qt model-view framework
Group:          System/GUI/KDE
%requires_ge    libQt5Core5

%description -n %{lname}
KItemModels provides a set of item models extending the Qt model-view framework.

%package imports
Summary:        Set of item models extending the Qt model-view framework
Group:          System/GUI/KDE
Requires:       %{lname} = %{version}

%description imports
KItemModels provides a set of item models extending the Qt model-view framework. This package
provides support to use KItemModels with the QtQuick framework.

%package devel
Summary:        Set of item models extending the Qt model-view framework
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
KItemModels provides a set of item models extending the Qt model-view framework.
Development files.

%if %{with python}
%package -n python-%{name}
Summary:        Set of item models extending the Qt model-view framework
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
%requires_python3_sip_api

%description -n python-%{name}
KItemModels provides a set of item models extending the Qt model-view framework.
Python bindings.
%endif

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
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5ItemModels.so.*

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5ItemModels/
%{_kf5_libdir}/libKF5ItemModels.so
%{_kf5_mkspecsdir}/qt_KItemModels.pri

%files imports
%license LICENSES/*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%dir %{_kf5_qmldir}/org/kde/kitemmodels
%{_kf5_qmldir}/org/kde/kitemmodels/libitemmodelsplugin.so
%{_kf5_qmldir}/org/kde/kitemmodels/qmldir

%if %{with python}
%files -n python-%{name}
%license LICENSES/*
%{python3_sitearch}/PyKF5
%{_datadir}/sip/PyKF5/
%endif

%changelog
