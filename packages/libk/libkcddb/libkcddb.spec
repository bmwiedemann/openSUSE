#
# spec file for package libkcddb
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkcddb
Version:        22.12.0
Release:        0
Summary:        CDDB library for KDE Applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      libkcddb5 < %{version}
Provides:       libkcddb5 = %{version}
Obsoletes:      libkcddb16 < %{version}
Provides:       libkcddb16 < %{version}

%description
The KDE Compact Disc DataBase library provides an API for
applications to fetch and submit audio CD
information over the Internet.

%package devel
Summary:        Development files for KDE CDDB library
Requires:       %{name} = %{version}
Requires:       libKF5Cddb5 = %{version}
Obsoletes:      libkcddb5-devel < %{version}
Provides:       libkcddb5-devel = %{version}

%description devel
This package includes the development headers for %{name}.

%package -n libKF5Cddb5
Summary:        CDDB library for KDE Applications
Recommends:     %{name}

%description -n libKF5Cddb5
The KDE Compact Disc DataBase library provides an API for
applications to fetch and submit audio CD
information over the Internet.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -n libKF5Cddb5   -p /sbin/ldconfig
%postun -n libKF5Cddb5 -p /sbin/ldconfig

%files
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_configkcfgdir}/
%{_kf5_debugdir}/libkcddb.categories
%{_kf5_plugindir}/
%{_kf5_servicesdir}/

%files -n libKF5Cddb5
%license LICENSES/*
%{_kf5_libdir}/libKF5Cddb.so.*

%files devel
%{_includedir}/KCddb5/
%{_kf5_cmakedir}/KF5Cddb/
%{_kf5_includedir}/KCddb/
%{_kf5_includedir}/kcddb_version.h
%{_kf5_libdir}/libKF5Cddb.so
%{_kf5_mkspecsdir}/qt_KCddb.pri

%files lang -f %{name}.lang

%changelog
