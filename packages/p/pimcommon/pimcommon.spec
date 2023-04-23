#
# spec file for package pimcommon
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


%define kf5_version 5.99.0
%bcond_without released
Name:           pimcommon
Version:        23.04.0
Release:        0
Summary:        Base package of KDE PIM PimCommon library
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libxslt-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextAutoCorrection)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5IMAP)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Conflicts:      libKF5PimCommon5 < %{version}

%description
This package contains the pimcommon library, used by several KDE PIM
applications.

%package devel
Summary:        Development package for pimcommon
License:        LGPL-2.1-or-later
Requires:       libKF5PimCommon5 = %{version}
Requires:       libKF5PimCommonAkonadi5 = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5KIO)
Requires:       cmake(KF5TextAutoCorrection)
Requires:       cmake(KF5TextGrammarCheck)
Requires:       cmake(KF5TextTranslator)
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KPim5AkonadiContact)
Requires:       cmake(KPim5IMAP)
Requires:       cmake(KPim5TextEdit)

%description devel
The development package for the pimcommon libraries

%package -n libKF5PimCommon5
Summary:        The PimCommon Library
License:        LGPL-2.1-or-later
%requires_eq    %{name}

%description -n libKF5PimCommon5
The PimCommon library

%package -n libKF5PimCommonAkonadi5
Summary:        The PimCommon Akonadi Library
License:        LGPL-2.1-or-later
%requires_eq    %{name}

%description -n libKF5PimCommonAkonadi5
The PimCommon Akonadi library

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libKF5PimCommon5
%ldconfig_scriptlets -n libKF5PimCommonAkonadi5

%files
%license LICENSES/*
%{_kf5_debugdir}/pimcommon.categories
%{_kf5_debugdir}/pimcommon.renamecategories

%files -n libKF5PimCommon5
%{_kf5_libdir}/libKF5PimCommon.so.*

%files -n libKF5PimCommonAkonadi5
%{_kf5_libdir}/libKF5PimCommonAkonadi.so.*

%files devel
%{_kf5_cmakedir}/KF5PimCommon/
%{_kf5_cmakedir}/KF5PimCommonAkonadi/
%dir %{_includedir}/KF5/
%{_includedir}/KF5/PimCommon/
%{_includedir}/KF5/PimCommonAkonadi/
%{_kf5_libdir}/libKF5PimCommon.so
%{_kf5_libdir}/libKF5PimCommonAkonadi.so
%{_kf5_mkspecsdir}/qt_PimCommon.pri
%{_kf5_mkspecsdir}/qt_PimCommonAkonadi.pri
%{_kf5_plugindir}/designer/

%files lang -f %{name}.lang

%changelog
