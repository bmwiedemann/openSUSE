#
# spec file for package purpose
#
# Copyright (c) 2021 SUSE LLC
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


# Used by optional plugins
%global __requires_exclude qmlimport\\((Ubuntu\\.OnlineAccounts|org\\.kde\\.kdeconnect).*

%define lname   libKF5Purpose5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           purpose
Version:        5.101.0
Release:        0
Summary:        Framework to integrate services and actions in applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  intltool
BuildRequires:  kf5-filesystem
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(AccountsQt5)
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
Requires:       kdeclarative-components >= %{_kf5_bugfix_version}
Requires:       libKF5QuickAddons5 >= %{_kf5_bugfix_version}
Requires:       libqt5-qtquickcontrols2
Suggests:       kdeconnect-kde

%description
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package -n %{lname}
Summary:        Framework to integrate services and actions - core library
Recommends:     %{name}

%description -n %{lname}
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

This package contains the core library files of the package.

%package -n libKF5PurposeWidgets5
Summary:        Framework to integrate services and actions - GUI library
Recommends:     %{name}

%description -n libKF5PurposeWidgets5
This framework offers the possibility to create integrate services and actions
on any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

This package contains the library files of the package needed to use GUI widgets.

%package devel
Summary:        Framework to integrate services and actions - Build Environment
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       libKF5PurposeWidgets5 = %{version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}

%description devel
This package contains development files needed to build applications which rely on the purpose framework.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang libpurpose_quick %{name}.lang
%find_lang libpurpose_widgets %{name}.lang
%find_lang purpose-fileitemaction %{name}.lang
%find_lang purpose_barcode %{name}.lang
%find_lang purpose_bluetooth %{name}.lang
%find_lang purpose_imgur %{name}.lang
%find_lang purpose_kdeconnect %{name}.lang
%find_lang purpose_kdeconnectsms %{name}.lang
%find_lang purpose_ktp-sendfile %{name}.lang
%find_lang purpose_nextcloud %{name}.lang
%find_lang purpose_pastebin %{name}.lang
%find_lang purpose_phabricator %{name}.lang
%find_lang purpose_reviewboard %{name}.lang
%find_lang purpose_saveas %{name}.lang
%find_lang purpose_youtube %{name}.lang

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5PurposeWidgets5 -p /sbin/ldconfig
%postun -n libKF5PurposeWidgets5 -p /sbin/ldconfig
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files lang -f %{name}.lang

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Purpose.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n libKF5PurposeWidgets5
%{_kf5_libdir}/libKF5PurposeWidgets.so.*

%files
%{_kf5_libdir}/libPhabricatorHelpers.so.*
%{_kf5_libdir}/libReviewboardHelpers.so.*
%{_kf5_libexecdir}/
%{_kf5_sharedir}/purpose/
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_iconsdir}/hicolor/*/actions/kipiplugin_youtube.*
%{_kf5_iconsdir}/hicolor/*/apps/phabricator-purpose.*
%{_kf5_iconsdir}/hicolor/*/apps/reviewboard-purpose.*
%{_kf5_sharedir}/accounts/

%files devel
%{_kf5_libdir}/libKF5Purpose.so
%{_kf5_libdir}/libKF5PurposeWidgets.so
%{_kf5_libdir}/cmake/KDEExperimentalPurpose/
%{_kf5_includedir}/
%dir %{_kf5_cmakedir}/KF5Purpose
%{_kf5_cmakedir}/KF5Purpose/*.cmake

%changelog
