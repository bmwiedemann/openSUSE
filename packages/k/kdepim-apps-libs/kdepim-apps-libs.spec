#
# spec file for package kdepim-apps-libs
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-apps-libs
Version:        20.08.1
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Gui) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains mail related libraries

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary:        Mail related libraries
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       cmake(Grantlee5)
Requires:       cmake(KF5Akonadi)

%description devel
The development package for the kdepim-apps-libs libraries

%files devel
%license COPYING*
%{_kf5_includedir}/
%{_kf5_cmakedir}/KF5KaddressbookImportExport/
%{_kf5_libdir}/cmake/KF5KaddressbookGrantlee/
%{_kf5_libdir}/libKF5KaddressbookGrantlee.so
%{_kf5_libdir}/libKF5KaddressbookImportExport.so
%{_kf5_mkspecsdir}/qt_KaddressbookGrantlee.pri
%{_kf5_mkspecsdir}/qt_KaddressbookImportExport.pri

%files
%license COPYING*
%{_kf5_debugdir}/kdepim-apps-lib.categories
%{_kf5_libdir}/libKF5KaddressbookGrantlee.so.*
%{_kf5_libdir}/libKF5KaddressbookImportExport.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
