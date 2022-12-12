#
# spec file for package kcmutils
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

# Internal QML import
%global __requires_exclude qmlimport\\(org\\.kde\\.kcmutils\\.private.*\\)

%define lname   libKF5KCMUtils5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kcmutils
Version:        5.101.0
Release:        0
Summary:        Classes to work with KCModules
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
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Declarative) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package -n libKF5KCMUtilsCore5
Summary:        Core library of classes to work with KCModules

%description -n libKF5KCMUtilsCore5
KCMUtils provides various classes to work with KCModules. This package provides the main core library.

%package -n %{lname}
Summary:        Classes to work with KCModules
Obsoletes:      libKF5KCMUtils4

%description -n %{lname}
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package imports
Summary:        QtQuick bindings for classes to work with KCModules
Requires:       %{lname} = %{version}
Requires:       libKF5KCMUtilsCore5 = %{version}

%description imports
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. This package provides QtQuick bindings
for the KCMUtils libraries.

%package devel
Summary:        Build environment for kcmutils, a set of classes to work with KCModules
Requires:       libKF5KCMUtilsCore5 = %{version}
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}

%description devel
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kcmutils5

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%post -n libKF5KCMUtilsCore5 -p /sbin/ldconfig
%postun -n libKF5KCMUtilsCore5 -p /sbin/ldconfig

%files -n %{lname}-lang -f kcmutils5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5KCMUtils.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kcmodule.desktop
%{_kf5_servicetypesdir}/kcmoduleinit.desktop
%{_kf5_debugdir}/kcmutils.categories
%{_kf5_libexecdir}/kcmdesktopfilegenerator

%files -n libKF5KCMUtilsCore5
%{_kf5_libdir}/libKF5KCMUtilsCore.so.*

%files imports
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kcmutils/

%files devel
%{_kf5_libdir}/libKF5KCMUtils.so
%{_kf5_libdir}/libKF5KCMUtilsCore.so
%{_kf5_libdir}/cmake/KF5KCMUtils/
%{_kf5_includedir}/KCMUtils/
%{_kf5_includedir}/KCMUtilsCore/
%{_kf5_mkspecsdir}/qt_KCMUtils.pri

%changelog
