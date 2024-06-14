#
# spec file for package libkcddb
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


%define rname  libkcddb
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define library_name libKCddb5
%define so_suffix -5
%else
%define qt5 1
%define kf5_version 5.92.0
%define qt5_version 5.15.2
%define library_name libKF5Cddb5
%define so_suffix 5
%endif

%bcond_without released
Name:           libkcddb%{?pkg_suffix}
Version:        24.05.1
Release:        0
Summary:        CDDB library for KDE Applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmusicbrainz5)
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# FIXME upstream bug, conflicting kcfg and desktop files
Conflicts:      libkcddb
Obsoletes:      libkcddb-lang
%else
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
Provides:       libkcddb5 = %{version}
Obsoletes:      libkcddb5 < %{version}
Provides:       libkcddb16 = %{version}
Obsoletes:      libkcddb16 < %{version}
%endif

%description
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package -n %{library_name}
Summary:        CDDB library for KDE Applications
Recommends:     %{name} >= %{version}

%description -n %{library_name}
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package devel
Summary:        Development files for KDE CDDB library
Requires:       %{library_name} = %{version}
%if 0%{?qt5}
Provides:       libkcddb5-devel = %{version}
Obsoletes:      libkcddb5-devel < %{version}
%endif

%description devel
This package includes the development headers for libkcddb.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE
%kf6_build
%else
%cmake_kf5 -d build
%cmake_build
%endif

%install
%if 0%{?qt6}
%kf6_install
%else
%kf5_makeinstall -C build
%endif

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n %{library_name}

%files
%if 0%{?qt6}
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/kcm_cddb.desktop
%{_kf6_configkcfgdir}/libkcddb5.kcfg
%{_kf6_debugdir}/libkcddb.categories
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%else
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/kcm_cddb.desktop
%{_kf5_configkcfgdir}/libkcddb5.kcfg
%{_kf5_debugdir}/libkcddb.categories
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%endif

%files -n %{library_name}
%license LICENSES/*
%if 0%{?qt6}
%{_kf6_libdir}/libKCddb6.so.*
%else
%{_kf5_libdir}/libKF5Cddb.so.*
%endif

%files devel
%if 0%{?qt6}
%{_includedir}/KCddb6/
%{_kf6_cmakedir}/KCddb6/
%{_kf6_libdir}/libKCddb6.so
%{_kf6_mkspecsdir}/qt_KCddb.pri
%else
%{_includedir}/KCddb5/
%{_kf5_cmakedir}/KF5Cddb/
%{_kf5_includedir}/KCddb/
%{_kf5_libdir}/libKF5Cddb.so
%{_kf5_mkspecsdir}/qt_KCddb.pri
%endif

%files lang -f %{name}.lang
%if 0%{?qt6}
%exclude %{_kf6_htmldir}/en/*/
%else
%exclude %{_kf5_htmldir}/en/*/
%endif

%changelog
