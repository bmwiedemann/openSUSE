#
# spec file for package kldap
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kldap
Version:        24.05.2
Release:        0
Summary:        Library to assist working with LDAP directories
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  openldap2-devel
# Voluntarily omitted, QCH doc is sufficient
# BuildRequires:  cmake(KF6DocTools) >= %%{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKPim6LdapCore6
Summary:        KDE PIM Libraries: LDAP support
Requires:       kldap >= %{version}

%description  -n libKPim6LdapCore6
This package provides LDAP support for KDE PIM applications

%package -n libKPim6LdapWidgets6
Summary:        KDE PIM Libraries: LDAP support
Requires:       kldap >= %{version}

%description  -n libKPim6LdapWidgets6
This package provides LDAP support for KDE PIM applications

%package devel
Summary:        Development files for kldap
Requires:       libKPim6LdapCore6 = %{version}
Requires:       libKPim6LdapWidgets6 = %{version}

%description devel
This package contains necessary include files and libraries needed
to add LDAP support to applications.

%lang_package

%prep
%autosetup -p1 -n kldap-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6LdapCore6
%ldconfig_scriptlets -n libKPim6LdapWidgets6

%files
%{_kf6_debugdir}/kldap.categories
%{_kf6_debugdir}/kldap.renamecategories
%{_kf6_plugindir}/kf6/kio/ldap.so

%files -n libKPim6LdapCore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6LdapCore.so.*

%files -n libKPim6LdapWidgets6
%license LICENSES/*
%{_kf6_libdir}/libKPim6LdapWidgets.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Ldap*.*
%{_includedir}/KPim6/KLDAPCore/
%{_includedir}/KPim6/KLDAPWidgets/
%{_kf6_cmakedir}/KPim6LdapCore/
%{_kf6_cmakedir}/KPim6LdapWidgets/
%{_kf6_libdir}/libKPim6LdapCore.so
%{_kf6_libdir}/libKPim6LdapWidgets.so

%files lang -f %{name}.lang

%changelog
