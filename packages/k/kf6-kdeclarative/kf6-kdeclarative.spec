#
# spec file for package kf6-kdeclarative
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

%define rname kdeclarative
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kdeclarative
Version:        6.3.0
Release:        0
Summary:        Integration of QML and KDE workspaces
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
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KDeclarative provides integration of QML and KDE workspaces.

%package -n libKF6CalendarEvents6
Summary:        Integration of QML and KDE workspaces
Recommends:     kf6-kdeclarative-imports = %{version}

%description -n libKF6CalendarEvents6
KDeclarative provides integration of QML and KDE workspaces.

%package imports
Summary:        KDeclarative QML imports
Requires:       kf6-kirigami-imports >= %{_kf6_bugfix_version}

%description imports
KDeclarative provides integration of QML and KDE workspaces.

%package devel
Summary:        Integration of QML and KDE workspaces: Build Environment
Requires:       libKF6CalendarEvents6 = %{version}
Requires:       cmake(KF6Config) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}

%description devel
KDeclarative provides integration of QML and KDE workspaces.
Development files.

%lang_package -n libKF6CalendarEvents6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kdeclarative6

%ldconfig_scriptlets -n libKF6CalendarEvents6

%files -n libKF6CalendarEvents6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6CalendarEvents.so.*

%files imports
%dir %{_kf6_qmldir}/org/kde/private
%{_kf6_qmldir}/org/kde/draganddrop/
%{_kf6_qmldir}/org/kde/graphicaleffects/
%{_kf6_qmldir}/org/kde/kquickcontrols/
%{_kf6_qmldir}/org/kde/kquickcontrolsaddons/
%{_kf6_qmldir}/org/kde/private/kquickcontrols/

%files devel
%doc %{_kf6_qchdir}/KF6Declarative.*
%{_kf6_cmakedir}/KF6Declarative/
%{_kf6_includedir}/KDeclarative/
%{_kf6_libdir}/libKF6CalendarEvents.so

%files -n libKF6CalendarEvents6-lang -f kdeclarative6.lang

%changelog
