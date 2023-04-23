#
# spec file for package kldap
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
%define libname libKPim5Ldap5
Name:           kldap
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  openldap2-devel
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KPim5Mbox)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Test)

%description
This package contains additional libraries for KDE PIM applications.

%package -n %{libname}
Summary:        KDE PIM Libraries: LDAP support
Requires:       %{name} = %{version}

%description  -n %{libname}
This package provides LDAP support for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       %{libname} = %{version}
Requires:       openldap2-devel
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n kldap-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%ldconfig_scriptlets -n %{libname}

%files
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%{_kf5_debugdir}/kldap.categories
%{_kf5_debugdir}/kldap.renamecategories
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kio
%{_kf5_plugindir}/kf5/kio/ldap.so

%files -n %{libname}
%license LICENSES/*
%{_kf5_libdir}/libKPim5Ldap.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KLDAP/
%{_kf5_cmakedir}/KF5Ldap/
%{_kf5_cmakedir}/KPim5Ldap/
%{_kf5_libdir}/libKPim5Ldap.so
%{_kf5_mkspecsdir}/qt_Ldap.pri

%files lang -f %{name}.lang

%changelog
