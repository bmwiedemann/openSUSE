#
# spec file for package kf6-kcoreaddons
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

%define rname kcoreaddons
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kcoreaddons
Version:        6.3.0
Release:        0
Summary:        Utilities for core application functionality and accessing the OS
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
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
Requires:       shared-mime-info >= 1.8

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package imports
Summary:        QML imports for kcoreaddons

%description imports
QML imports for kcoreaddons.

%package -n libKF6CoreAddons6
Summary:        Utilities for core application functionality and accessing the OS
Requires:       kf6-kcoreaddons = %{version}

%description -n libKF6CoreAddons6
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package devel
Summary:        Utilities for core application functionality and accessing the OS
Requires:       libKF6CoreAddons6 = %{version}

%description devel
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more. Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# ENABLE_PCH breaks the build locally with 'error: is pie differs in PCH file vs. current file'
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE -DENABLE_PCH:BOOL=FALSE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kf6-kcoreaddons --all-name --with-qt --without-mo

%ldconfig_scriptlets -n libKF6CoreAddons6

%files
%{_kf6_appsdir}/mime/packages/kde6.xml
%{_kf6_debugdir}/kcoreaddons.categories
%{_kf6_debugdir}/kcoreaddons.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/coreaddons/

%files -n libKF6CoreAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6CoreAddons.so.*

%files devel
%doc %{_kf6_qchdir}/KF6CoreAddons.*
%{_kf6_includedir}/KCoreAddons/
%{_kf6_cmakedir}/KF6CoreAddons/
%dir %{_kf6_datadir}/jsonschema
%{_kf6_datadir}/jsonschema/kpluginmetadata.schema.json
%{_kf6_libdir}/libKF6CoreAddons.so

%files lang -f kf6-kcoreaddons.lang

%changelog
