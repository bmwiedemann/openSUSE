#
# spec file for package kf6-kcmutils
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

%define rname kcmutils
# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kcmutils\\.private.*\\)

# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kcmutils
Version:        6.3.0
Release:        0
Summary:        Classes to work with KCModules
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
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6XmlGui) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package -n libKF6KCMUtils6
Summary:        Classes to work with KCModules
Requires:       kf6-kcmutils >= %{version}

%description -n libKF6KCMUtils6
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package -n libKF6KCMUtilsCore6
Summary:        Core library of classes to work with KCModules

%description -n libKF6KCMUtilsCore6
KCMUtils provides various classes to work with KCModules. This package provides
the main core library.

%package -n libKF6KCMUtilsQuick6
Summary:        Classes to work with KCModules

%description -n libKF6KCMUtilsQuick6
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package imports
Summary:        QtQuick bindings for classes to work with KCModules
Requires:       libKF6KCMUtils6 = %{version}
Requires:       libKF6KCMUtilsCore6 = %{version}
Requires:       libKF6KCMUtilsQuick6 = %{version}

%description imports
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. This package provides QtQuick bindings
for the KCMUtils libraries.

%package devel
Summary:        Build environment for kcmutils, a set of classes to work with KCModules
Requires:       libKF6KCMUtils6 = %{version}
Requires:       libKF6KCMUtilsCore6 = %{version}
Requires:       libKF6KCMUtilsQuick6 = %{version}
Requires:       cmake(KF6ConfigWidgets) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}

%description devel
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. Development files.

%lang_package
%lang_package -n libKF6KCMUtils6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kcmutils6
%find_lang kcmshell6

%ldconfig_scriptlets -n libKF6KCMUtils6
%ldconfig_scriptlets -n libKF6KCMUtilsCore6
%ldconfig_scriptlets -n libKF6KCMUtilsQuick6

%files
%doc README.md
%{_kf6_bindir}/kcmshell6
%{_kf6_debugdir}/kcmutils.categories
%{_kf6_libexecdir}/kcmdesktopfilegenerator

%files -n libKF6KCMUtils6
%{_kf6_libdir}/libKF6KCMUtils.so.*

%files -n libKF6KCMUtilsCore6
%license LICENSES/*
%{_kf6_libdir}/libKF6KCMUtilsCore.so.*

%files -n libKF6KCMUtilsQuick6
%{_kf6_libdir}/libKF6KCMUtilsQuick.so.*

%files imports
%{_kf6_qmldir}/org/kde/kcmutils/

%files devel
%doc %{_kf6_qchdir}/KF6KCMUtils.*
%{_kf6_cmakedir}/KF6KCMUtils/
%{_kf6_includedir}/KCMUtils/
%{_kf6_includedir}/KCMUtilsCore/
%{_kf6_includedir}/KCMUtilsQuick/
%{_kf6_libdir}/libKF6KCMUtils.so
%{_kf6_libdir}/libKF6KCMUtilsCore.so
%{_kf6_libdir}/libKF6KCMUtilsQuick.so

%files lang -f kcmshell6.lang

%files -n libKF6KCMUtils6-lang -f kcmutils6.lang

%changelog
