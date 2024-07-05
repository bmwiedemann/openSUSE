#
# spec file for package kaccounts-integration
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
Name:           kaccounts-integration
Version:        24.05.2
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(SignOnQt6)
Requires:       signon-kwallet-extension
Recommends:     kaccounts-providers

%description
Small system to administer web accounts for the sites and services across the
Plasma desktop, including: Google, Facebook, Owncloud, IMAP, Jabber and others.

%package -n libkaccounts6-2
Summary:        KDE Accounts Providers - System Library
Recommends:     kaccounts-integration

%description -n libkaccounts6-2
Small system to administer web accounts for the sites and services across the
Plasma desktop, including: Google, Facebook, Owncloud, IMAP, Jabber and others.

%package devel
Summary:        KDE Accounts Providers - Development Files
# Used in KAccountsMacros.cmake
Requires:       intltool
Requires:       libkaccounts6-2 = %{version}
Requires:       cmake(AccountsQt6)
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(SignOnQt6)
Requires:       pkgconfig(libaccounts-glib)

%description devel
Small system to administer web accounts for the sites and services across the
Plasma desktop, including: Google, Facebook, Owncloud, IMAP, Jabber and others.
This package provides development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libkaccounts6-2

%files
%{_kf6_applicationsdir}/kcm_kaccounts.desktop
%dir %{_kf6_plugindir}/kaccounts
%dir %{_kf6_plugindir}/kaccounts/daemonplugins
%{_kf6_plugindir}/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%{_kf6_plugindir}/kf6/kded/kded_accounts.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_kf6_qmldir}/org/kde/kaccounts/

%files -n libkaccounts6-2
%license LICENSES/*
%{_kf6_libdir}/libkaccounts6.so.*

%files devel
%{_includedir}/KAccounts6/
%{_kf6_cmakedir}/KAccounts6/
%{_kf6_libdir}/libkaccounts6.so

%files lang -f %{name}.lang

%changelog
