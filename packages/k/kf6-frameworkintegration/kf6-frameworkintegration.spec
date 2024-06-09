#
# spec file for package kf6-frameworkintegration
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

%define rname frameworkintegration
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-frameworkintegration
Version:        6.3.0
Release:        0
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6NewStuff) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Package) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)

%description
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package -n libKF6Style6
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace

%description -n libKF6Style6
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       plasma6-integration-plugin

%description plugin
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package devel
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       libKF6Style6 = %{version}
Requires:       cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6IconThemes) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}

%description devel
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly. Development files

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Style6

%files -n libKF6Style6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Style.so.*

%files plugin
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler
%{_kf6_libexecdir}/kpackagehandlers/knshandler
%{_kf6_notificationsdir}/plasma_workspace.notifyrc
%{_kf6_plugindir}/kf6/FrameworkIntegrationPlugin.so

%files devel
%{_kf6_cmakedir}/KF6FrameworkIntegration/
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/libKF6Style.so

%changelog
