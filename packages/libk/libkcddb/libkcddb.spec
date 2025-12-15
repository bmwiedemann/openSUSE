#
# spec file for package libkcddb
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf5_version 5.92.0
%define qt5_version 5.15.2
# For KDE unstable applications repository
%define rversion 25.04.3
%bcond_without released
Name:           libkcddb
Version:        25.04.3
Release:        0
Summary:        CDDB library for KDE Applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{rversion}/src/%{name}-%{rversion}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{rversion}/src/%{name}-%{rversion}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
Provides:       libkcddb5 = %{rversion}
Obsoletes:      libkcddb5 < %{rversion}
Provides:       libkcddb16 = %{rversion}
Obsoletes:      libkcddb16 < %{rversion}

%description
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package -n libKF5Cddb5
Summary:        CDDB library for KDE Applications
Recommends:     %{name} >= %{rversion}

%description -n libKF5Cddb5
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package devel
Summary:        Development files for KDE CDDB library
Requires:       libKF5Cddb5 = %{rversion}
Provides:       libkcddb5-devel = %{rversion}
Obsoletes:      libkcddb5-devel < %{rversion}

%description devel
This package includes the development headers for libkcddb.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{rversion}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n libKF5Cddb5

%files
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/kcm_cddb.desktop
%{_kf5_configkcfgdir}/libkcddb5.kcfg
%{_kf5_debugdir}/libkcddb.categories
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so

%files -n libKF5Cddb5
%license LICENSES/*
%{_kf5_libdir}/libKF5Cddb.so.*

%files devel
%{_includedir}/KCddb5/
%{_kf5_cmakedir}/KF5Cddb/
%{_kf5_includedir}/KCddb/
%{_kf5_libdir}/libKF5Cddb.so
%{_kf5_mkspecsdir}/qt_KCddb.pri

%files lang -f %{name}.lang
%exclude %{_kf5_htmldir}/en/*/

%changelog
