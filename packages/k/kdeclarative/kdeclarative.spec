#
# spec file for package kdeclarative
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


%define lname   libKF5Declarative5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdeclarative
Version:        5.101.0
Release:        0
Summary:        Integration of QML and KDE workspaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libepoxy-devel
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Package) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
KDeclarative provides integration of QML and KDE workspaces.

%package -n %{lname}
Summary:        Integration of QML and KDE workspaces
# QQmlPropertyMap leaks private but exported QObjectPrivate symbol
# https://bugreports.qt.io/browse/QTBUG-46433 and https://bugs.launchpad.net/bugs/1426335
%requires_eq    libQt5Core5

%description -n %{lname}
KDeclarative provides integration of QML and KDE workspaces.

%package -n libKF5QuickAddons5
Summary:        Integration of QML and KDE workspaces

%description -n libKF5QuickAddons5
KDeclarative provides integration of QML and KDE workspaces.

%package -n libKF5CalendarEvents5
Summary:        Integration of QML and KDE workspaces

%description -n libKF5CalendarEvents5
KDeclarative provides integration of QML and KDE workspaces.

%package components
Summary:        KDeclarative QML components
Requires:       kirigami2 >= %{_kf5_bugfix_version}

%description components
KDeclarative provides integration of QML and KDE workspaces.

%package tools
Summary:        KDeclarative tools

%description tools
KDeclarative provides integration of QML and KDE workspaces.

%package devel
Summary:        Integration of QML and KDE workspaces: Build Environment
Requires:       %{lname} = %{version}
Requires:       %{name}-components = %{version}
Requires:       extra-cmake-modules
Requires:       libKF5CalendarEvents5 = %{version}
Requires:       libKF5QuickAddons5 = %{version}
Requires:       cmake(KF5Config) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Package) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Qml) >= 5.15.0

%description devel
KDeclarative provides integration of QML and KDE workspaces.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang kdeclarative5

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5QuickAddons5 -p /sbin/ldconfig
%postun -n libKF5QuickAddons5 -p /sbin/ldconfig
%post -n libKF5CalendarEvents5 -p /sbin/ldconfig
%postun -n libKF5CalendarEvents5 -p /sbin/ldconfig

%files -n %{lname}-lang -f kdeclarative5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5Declarative.so.*

%files -n libKF5QuickAddons5
%{_kf5_libdir}/libKF5QuickAddons.so.*

%files -n libKF5CalendarEvents5
%{_kf5_libdir}/libKF5CalendarEvents.so.*

%files components
%{_kf5_libdir}/qt5/qml/

%files tools
%{_kf5_bindir}/kpackagelauncherqml

%files devel
%{_kf5_libdir}/libKF5Declarative.so
%{_kf5_libdir}/libKF5QuickAddons.so
%{_kf5_libdir}/libKF5CalendarEvents.so
%{_kf5_libdir}/cmake/KF5Declarative/
%{_kf5_includedir}/KDeclarative/
%{_kf5_mkspecsdir}/qt_KDeclarative.pri
%{_kf5_mkspecsdir}/qt_QuickAddons.pri

%changelog
