#
# spec file for package kaccounts-integration-kf5
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


%define kf5_version 5.97.0
%define qt5_version 5.15.2

%define rname kaccounts-integration
%define sover 2
%bcond_without released
Name:           kaccounts-integration-kf5
Version:        24.05.1
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Source0:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
%if 0%{?suse_version} < 1550
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(QCoro5)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(SignOnQt5)
BuildRequires:  pkgconfig(libaccounts-glib)
# kaccounts-integration 23.08.4 is the last packaged version supporting KF5/Qt5
Provides:       kaccounts-integration = 23.08.4
Obsoletes:      kaccounts-integration < 23.08.4
Recommends:     kaccounts-integration-lang
# kaccounts-providers isn't meant to be flavored
Recommends:     kaccounts-providers

%description
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package -n libkaccounts%{sover}
Summary:        KDE Accounts Providers - System Library

%description -n libkaccounts%{sover}
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package devel
Summary:        KDE Accounts Providers - Development Files
Requires:       libkaccounts%{sover} = %{version}
Requires:       cmake(AccountsQt5)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(Qt5Core)
Requires:       cmake(SignOnQt5)
Requires:       pkgconfig(libaccounts-glib)
# Used in KAccountsMacros.cmake
Requires:       intltool

%description devel
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others. Devel files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-13
%endif

%cmake_kf5 -d build -- -DKF6_COMPAT_BUILD:BOOL=TRUE

%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libkaccounts%{sover}

%files
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/kaccounts/

%files -n libkaccounts%{sover}
%license LICENSES/*
%{_kf5_libdir}/libkaccounts.so.*

%files devel
%{_includedir}/KAccounts/
%{_kf5_cmakedir}/KAccounts/
%{_kf5_libdir}/libkaccounts.so

%changelog
