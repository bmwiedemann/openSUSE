#
# spec file for package knotifications
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


%define lname   libKF5Notifications5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           knotifications
Version:        5.116.0
Release:        0
Summary:        KDE Desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(x11)

%description
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package imports
Summary:        KDE Desktop notifications - QML files

%description imports
KNotification is used to notify the user of an event. It covers feedback and
persistent events.
This package contains files that allow using knotification in QtQuick based
applications.

%package -n %{lname}
Summary:        KDE Desktop notifications

%description -n %{lname}
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package devel
Summary:        KDE Desktop notifications: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5DBus) >= %{qt5_version}
Requires:       cmake(Qt5TextToSpeech) >= %{qt5_version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}

%description devel
KNotification is used to notify the user of an event. It covers feedback and
persistent events. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang knotifications5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f knotifications5.lang

%files imports
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/notification/

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Notifications.so.*
%{_kf5_debugdir}/knotifications.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5Notifications.so
%{_kf5_libdir}/cmake/KF5Notifications/
%{_kf5_includedir}/KNotifications/
%{_kf5_mkspecsdir}/qt_KNotifications.pri
%{_kf5_dbusinterfacesdir}/kf5_org.kde.StatusNotifierItem.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.StatusNotifierWatcher.xml

%changelog
