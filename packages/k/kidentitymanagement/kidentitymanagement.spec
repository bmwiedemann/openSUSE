#
# spec file for package kidentitymanagement
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.103.0
%bcond_without released
Name:           kidentitymanagement
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries: Identity Management
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Emoticons) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
Conflicts:      libKF5IdentityManagement5 < %{version}
Conflicts:      libKF5IdentityManagementWidgets5 < %{version}

%description
This package provides a library to handle multiple email identities and
associated settings.

%package -n libKPim5IdentityManagement5
Summary:        KDE PIM Libraries: Identity Management - core library
Recommends:     %{name}-lang
%requires_eq    %{name}

%description  -n libKPim5IdentityManagement5
This package provides the core library to handle multiple email identities and
associated settings.

%package -n libKPim5IdentityManagementWidgets5
Summary:        KDE PIM Libraries: Identity Management - widgets library
Recommends:     %{name}-lang
Requires:       libKPim5IdentityManagement5 = %{version}

%description  -n libKPim5IdentityManagementWidgets5
This package provides graphical widgets to handle multiple email identities
and associated settings.

%package devel
Summary:        KDE PIM Libraries: Identity Management - development files
Requires:       libKPim5IdentityManagement5 = %{version}
Requires:       libKPim5IdentityManagementWidgets5 = %{version}
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5TextEditTextToSpeech)
Requires:       cmake(KPim5TextEdit)

%description devel
This package contains necessary include files and libraries needed
to develop applications that make use of multiple email identities.

%lang_package

%prep
%autosetup -p1 -n kidentitymanagement-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libKPim5IdentityManagement5
%ldconfig_scriptlets -n libKPim5IdentityManagementWidgets5

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n libKPim5IdentityManagement5
%{_kf5_libdir}/libKPim5IdentityManagement.so.*

%files -n libKPim5IdentityManagementWidgets5
%{_kf5_libdir}/libKPim5IdentityManagementWidgets.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KIdentityManagement/
%{_includedir}/KPim5/KIdentityManagementWidgets/
%{_kf5_cmakedir}/KF5IdentityManagement/
%{_kf5_cmakedir}/KPim5IdentityManagement/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.pim.IdentityManager.xml
%{_kf5_libdir}/libKPim5IdentityManagement.so
%{_kf5_libdir}/libKPim5IdentityManagementWidgets.so
%{_kf5_mkspecsdir}/qt_KIdentityManagement.pri
%{_kf5_mkspecsdir}/qt_KIdentityManagementWidgets.pri

%files lang -f %{name}.lang

%changelog
