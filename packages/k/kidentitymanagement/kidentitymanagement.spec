#
# spec file for package kidentitymanagement
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           kidentitymanagement
Version:        24.05.1
Release:        0
Summary:        KDE PIM Libraries: Identity Management
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6TextEdit) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This package provides a library to handle multiple email identities and
associated settings.

%package -n libKPim6IdentityManagementCore6
Summary:        KDE PIM Libraries: Identity Management - core library
Recommends:     kidentitymanagement-lang
Requires:       kidentitymanagement >= %{version}
Obsoletes:      libKF5IdentityManagement5 < %{version}
Obsoletes:      libKPim5IdentityManagement5 < %{version}

%description  -n libKPim6IdentityManagementCore6
This package provides the core library to handle multiple email identities and
associated settings.

%package -n libKPim6IdentityManagementWidgets6
Summary:        KDE PIM Libraries: Identity Management - widgets library
Recommends:     kidentitymanagement-lang
Requires:       libKPim6IdentityManagementCore6 = %{version}
Obsoletes:      libKPim5IdentityManagementWidgets5 < %{version}

%description  -n libKPim6IdentityManagementWidgets6
This package provides graphical widgets to handle multiple email identities
and associated settings.

%package -n libKPim6IdentityManagementQuick6
Summary:        KDE PIM Libraries: Identity Management - QtQuick library
Requires:       libKPim6IdentityManagementCore6 = %{version}

%description -n libKPim6IdentityManagementQuick6
This package provides a shared library to build QtQuick interfaces for 
PIM identity management.

%package imports
Summary:        QML imports for using kidentitymanagement
Requires:       libKPim6IdentityManagementCore6 = %{version}
Requires:       libKPim6IdentityManagementQuick6 = %{version}

%description imports
QML imports for using kidentitymanagement.

%package devel
Summary:        KDE PIM Libraries: Identity Management - development files
Requires:       libKPim6IdentityManagementCore6 = %{version}
Requires:       libKPim6IdentityManagementWidgets6 = %{version}
Requires:       libKPim6IdentityManagementQuick6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KPim6TextEdit) >= %{kpim6_version}

%description devel
This package contains necessary include files and libraries needed
to develop applications that make use of multiple email identities.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6IdentityManagementCore6
%ldconfig_scriptlets -n libKPim6IdentityManagementWidgets6
%ldconfig_scriptlets -n libKPim6IdentityManagementQuick6

%files
%{_kf6_debugdir}/kidentitymanagement.categories
%{_kf6_debugdir}/kidentitymanagement.renamecategories

%files -n libKPim6IdentityManagementCore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6IdentityManagementCore.so.*

%files -n libKPim6IdentityManagementWidgets6
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so.*

%files -n libKPim6IdentityManagementQuick6
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so.*

%files imports
%{_kf6_qmldir}/org/kde/kidentitymanagement/

%files devel
%doc %{_kf6_qchdir}/KPim6IdentityManagement*.*
%{_includedir}/KPim6/KIdentityManagementCore/
%{_includedir}/KPim6/KIdentityManagementQuick/
%{_includedir}/KPim6/KIdentityManagementWidgets/
%{_kf6_cmakedir}/KPim6IdentityManagementCore/
%{_kf6_cmakedir}/KPim6IdentityManagementQuick/
%{_kf6_cmakedir}/KPim6IdentityManagementWidgets/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.pim.IdentityManager.xml
%{_kf6_libdir}/libKPim6IdentityManagementCore.so
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so

%files lang -f %{name}.lang

%changelog
