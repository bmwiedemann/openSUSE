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


%define rname  libkcddb

%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           libkcddb-qt6
Version:        25.08.3
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

%description
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package -n libKCddb5
Summary:        CDDB library for KDE Applications
Recommends:     libkcddb-qt6 >= %{version}

%description -n libKCddb5
The KDE Compact Disc DataBase library provides an API for applications to fetch
and submit audio CD information over the Internet.

%package devel
Summary:        Development files for KDE CDDB library
Requires:       libKCddb5 = %{version}

%description devel
This package includes the development headers for libkcddb.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n libKCddb5

%files
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/kcm_cddb.desktop
%{_kf6_configkcfgdir}/libkcddb5.kcfg
%{_kf6_debugdir}/libkcddb.categories
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so

%files -n libKCddb5
%license LICENSES/*
%{_kf6_libdir}/libKCddb6.so.*

%files devel
%{_includedir}/KCddb6/
%{_kf6_cmakedir}/KCddb6/
%{_kf6_libdir}/libKCddb6.so
%{_kf6_mkspecsdir}/qt_KCddb.pri

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
