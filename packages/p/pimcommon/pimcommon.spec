#
# spec file for package pimcommon
#
# Copyright (c) 2022 SUSE LLC
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
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           pimcommon
Version:        22.12.1
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
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

%description
This package contains the pimcommon library, used by several KDE PIM
applications.

%package devel
Summary:        Development package for pimcommon
License:        LGPL-2.1-or-later
Requires:       libKF5PimCommon5 = %{version}
Requires:       libKF5PimCommonAkonadi5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiContact)
Requires:       cmake(KF5Config)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IMAP)
Requires:       cmake(KF5KIO)
Requires:       cmake(KF5PimTextEdit)

%description devel
The development package for the pimcommon libraries

%package -n libKF5PimCommon5
Summary:        The PimCommon Library
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}

%description -n libKF5PimCommon5
The PimCommon library

%package -n libKF5PimCommonAutoCorrection5
Summary:        Text autocorrection library for PimCommon
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}

%description -n libKF5PimCommonAutoCorrection5
This package provides a library for text autocorrection as part
of the PIM libraries by KDE.

%package -n libKF5PimCommonAkonadi5
Summary:        The PimCommon Akonadi Library
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}

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

%post -n libKF5PimCommon5  -p /sbin/ldconfig
%postun -n libKF5PimCommon5 -p /sbin/ldconfig
%post -n libKF5PimCommonAutoCorrection5  -p /sbin/ldconfig
%postun -n libKF5PimCommonAutoCorrection5 -p /sbin/ldconfig
%post -n libKF5PimCommonAkonadi5  -p /sbin/ldconfig
%postun -n libKF5PimCommonAkonadi5 -p /sbin/ldconfig

%files
%{_kf5_debugdir}/pimcommon.categories
%{_kf5_debugdir}/pimcommon.renamecategories

%files devel
%{_kf5_cmakedir}/KF5PimCommon/
%{_kf5_cmakedir}/KF5PimCommonAutoCorrection/
%{_kf5_cmakedir}/KF5PimCommonAkonadi/
%{_kf5_includedir}/PimCommon/
%{_kf5_includedir}/PimCommonAutoCorrection/
%{_kf5_includedir}/PimCommonAkonadi
%{_kf5_libdir}/libKF5PimCommon.so
%{_kf5_libdir}/libKF5PimCommonAkonadi.so
%{_kf5_libdir}/libKF5PimCommonAutoCorrection.so
%{_kf5_mkspecsdir}/qt_PimCommon.pri
%{_kf5_mkspecsdir}/qt_PimCommonAutoCorrection.pri
%{_kf5_mkspecsdir}/qt_PimCommonAkonadi.pri
%{_kf5_plugindir}/designer/

%files -n libKF5PimCommon5
%license LICENSES/*
%{_libdir}/libKF5PimCommon.so.*

%files -n libKF5PimCommonAutoCorrection5
%{_libdir}/libKF5PimCommonAutoCorrection.so.*

%files -n libKF5PimCommonAkonadi5
%{_libdir}/libKF5PimCommonAkonadi.so.*

%files lang -f %{name}.lang

%changelog
