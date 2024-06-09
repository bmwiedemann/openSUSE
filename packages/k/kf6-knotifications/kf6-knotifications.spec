#
# spec file for package kf6-knotifications
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


%define qt6_version 6.6.0

%define rname knotifications
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-knotifications
Version:        6.3.0
Release:        0
Summary:        KDE Desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libcanberra)

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

%package -n libKF6Notifications6
Summary:        KDE Desktop notifications
Requires:       kf6-knotifications >= %{version}

%description -n libKF6Notifications6
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package devel
Summary:        KDE Desktop notifications: Build Environment
Requires:       libKF6Notifications6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KNotification is used to notify the user of an event. It covers feedback and
persistent events. Development files.

%lang_package -n libKF6Notifications6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang knotifications6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Notifications6

%files -n libKF6Notifications6-lang -f knotifications6.lang

%files
%{_kf6_debugdir}/knotifications.categories
%{_kf6_debugdir}/knotifications.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/notification/

%files -n libKF6Notifications6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Notifications.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Notifications.*
%{_kf6_cmakedir}/KF6Notifications/
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so

%changelog
