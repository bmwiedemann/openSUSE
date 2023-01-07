#
# spec file for package grantleetheme
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
Name:           grantleetheme
Version:        22.12.1
Release:        0
Summary:        Grantlee theme support
License:        GPL-2.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
%if %{with released}
%requires_eq    grantlee5
%endif

%description
the grantleetheme library adds Grantlee theme support for PIM applications.

%package -n libKF5GrantleeTheme5
Summary:        GrantleeTheme library for KDE PIM applications
License:        LGPL-2.1-or-later
Requires:       grantleetheme = %{version}

%description -n libKF5GrantleeTheme5
The GrantleeTheme library

%package devel
Summary:        Development package for grantleetheme
License:        LGPL-2.1-or-later
Requires:       libKF5GrantleeTheme5 = %{version}

%description devel
The development package for the grantleetheme library

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%global grantlee_shortver %(rpm -q --queryformat=%%{VERSION} grantlee5 | cut -d . -f 1-2)

%post -n libKF5GrantleeTheme5  -p /sbin/ldconfig
%postun -n libKF5GrantleeTheme5 -p /sbin/ldconfig

%files devel
%{_kf5_cmakedir}/KF5GrantleeTheme/
%{_kf5_includedir}/GrantleeTheme/
%{_kf5_libdir}/libKF5GrantleeTheme.so
%{_kf5_mkspecsdir}/qt_GrantleeTheme.pri

%files
%dir %{_kf5_libdir}/grantlee/
%dir %{_kf5_libdir}/grantlee/%{grantlee_shortver}
%{_kf5_debugdir}/grantleetheme.categories
%{_kf5_debugdir}/grantleetheme.renamecategories
%{_kf5_libdir}/grantlee/%{grantlee_shortver}/kde_grantlee_plugin.so

%files -n libKF5GrantleeTheme5
%license LICENSES/*
%{_kf5_libdir}/libKF5GrantleeTheme.so.*

%files lang -f %{name}.lang

%changelog
