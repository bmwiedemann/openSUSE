#
# spec file for package kf6-kirigami
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

%define rname kirigami
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kirigami
Version:        6.3.0
Release:        0
Summary:        Set of QtQuick components
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-qt5compat-imports >= %{qt6_version}

%description
QtQuick plugins to build user interfaces based on the KDE UX guidelines.

%package imports
Summary:        Kirigami QML components
Requires:       kf6-kirigami-imports >= %{version}

%description imports
Kirigami QML and runtime components based on KF6 and Qt6

%package -n libKirigamiPlatform6
Summary:        Set of QtQuick components
Requires:       kf6-kirigami-imports >= %{version}
Recommends:     kf6-kirigami-imports = %{version}

%description -n libKirigamiPlatform6
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Based on Qt Quick Controls 2. This package contains the base shared libraries.

%package devel
Summary:        Development package for kirigami
Requires:       libKirigamiPlatform6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Concurrent) >= %{qt6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}

%description devel
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build

%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libkirigami6 --with-qt --without-mo

%ldconfig_scriptlets -n libKirigamiPlatform6

%files
%{_kf6_debugdir}/kirigami.categories

%files imports
%{_kf6_qmldir}/org/kde/kirigami/

%files -n libKirigamiPlatform6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKirigami.so.*
%{_kf6_libdir}/libKirigamiDelegates.so.*
%{_kf6_libdir}/libKirigamiDialogs.so.*
%{_kf6_libdir}/libKirigamiLayouts.so.*
%{_kf6_libdir}/libKirigamiPlatform.so.*
%{_kf6_libdir}/libKirigamiPrimitives.so.*

%files devel
%doc %{_kf6_qchdir}/KF6KirigamiPlatform.*
%{_kf6_cmakedir}/KF6Kirigami/
%{_kf6_cmakedir}/KF6Kirigami2/
%{_kf6_cmakedir}/KF6KirigamiPlatform/
%dir %{_kf6_includedir}/Kirigami/
%{_kf6_includedir}/Kirigami/Platform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_sharedir}/kdevappwizard/templates/kirigami6.tar.bz2

%files lang -f libkirigami6.lang

%changelog
