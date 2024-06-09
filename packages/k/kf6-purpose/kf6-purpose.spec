#
# spec file for package kf6-purpose
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


# Internal QML imports
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.purpose|org\\.kde\\.kdeconnect|SSO\\.OnlineAccounts).*

%define qt6_version 6.6.0

%define rname purpose
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-purpose
Version:        6.3.0
Release:        0
Summary:        Framework to integrate services and actions in applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Kirigami) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       accounts-qml-module
Requires:       kf6-kdeclarative-imports >= %{_kf6_bugfix_version}
Requires:       kf6-kirigami-imports >= %{_kf6_bugfix_version}
Requires:       kf6-prison-imports >= %{_kf6_bugfix_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       purpose-services >= %{version}

%description
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package services
Summary:        Online services for purpose
Provides:       purpose-services = %{version}
Obsoletes:      purpose-services < %{version}

%description services
This package adds online services to kf6-purpose and are needed to connect to
Google and Nextcloud servers.

%package -n libKF6Purpose6
Summary:        Framework to integrate services and actions - core library
Requires:       kf6-purpose >= %{version}

%description -n libKF6Purpose6
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

This package contains the core library files of the package.

%package -n libKF6PurposeWidgets6
Summary:        Framework to integrate services and actions - GUI library
Recommends:     kf6-purpose >= %{version}

%description -n libKF6PurposeWidgets6
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

This package contains the library files of the package needed to use GUI widgets.

%package devel
Summary:        Framework to integrate services and actions - Build Environment
Requires:       libKF6Purpose6 = %{version}
Requires:       libKF6PurposeWidgets6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}

%description devel
This package contains development files needed to build applications which rely on the purpose framework.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%define _lto_cflags %{nil}

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kf6-purpose --all-name

%ldconfig_scriptlets -n libKF6Purpose6
%ldconfig_scriptlets -n libKF6PurposeWidgets6

%files -n libKF6Purpose6
%{_kf6_libdir}/libKF6Purpose.so.*

%files -n libKF6PurposeWidgets6
%{_kf6_libdir}/libKF6PurposeWidgets.so.*

%files
%license LICENSES/*
%doc README.md
%{_kf6_datadir}/purpose/
%{_kf6_debugdir}/purpose.categories
%{_kf6_debugdir}/purpose.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/phabricator-purpose6.png
%{_kf6_iconsdir}/hicolor/*/apps/reviewboard-purpose6.png
%{_kf6_libexecdir}/purposeprocess
%{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/purpose/
%{_kf6_qmldir}/org/kde/purpose/

%files services
%dir %{_kf6_sharedir}/accounts
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde
%{_kf6_sharedir}/accounts/services/kde/google-youtube.service
%{_kf6_sharedir}/accounts/services/kde/nextcloud-upload.service

%files devel
%{_kf6_cmakedir}/KF6Purpose/
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so

%files lang -f kf6-purpose.lang

%changelog
