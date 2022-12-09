#
# spec file for package kaccounts-integration
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


%define sover 2
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kaccounts-integration
Version:        22.12.0
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     kaccounts-providers

%description
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package -n libkaccounts%{sover}
Summary:        KDE Accounts Providers - System Library
Recommends:     %{name}

%description -n libkaccounts%{sover}
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package devel
Summary:        KDE Accounts Providers - Development Files
Requires:       libkaccounts%{sover} = %{version}
Requires:       libsignon-qt5-devel
Requires:       cmake(AccountsQt5)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(Qt5Core)
Requires:       pkgconfig(libaccounts-glib)
# Used in KAccountsMacros.cmake
Requires:       intltool

%description devel
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others. Devel files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post   -n libkaccounts%{sover} -p /sbin/ldconfig
%postun -n libkaccounts%{sover} -p /sbin/ldconfig

%files
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_sharedir}/kpackage/kcms/kcm_kaccounts/

%files -n libkaccounts%{sover}
%license LICENSES/*
%{_kf5_libdir}/libkaccounts.so.*

%files devel
%{_kf5_cmakedir}/KAccounts/
%{_kf5_libdir}/libkaccounts.so
%{_kf5_prefix}/include/KAccounts/

%files lang -f %{name}.lang

%changelog
