#
# spec file for package frameworkintegration
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


%define lname   libKF5Style5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           frameworkintegration
Version:        5.116.0
Release:        0
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  (cmake(AppStreamQt5) >= 1.0.0 or cmake(AppStreamQt) < 1.0.0)
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{_kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_version}
BuildRequires:  cmake(KF5Package) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(packagekitqt5)

%description
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package -n %{lname}
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Obsoletes:      %{lname}-lang < %{version}
Obsoletes:      libKF5Style4

%description -n %{lname}
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       plasma5-integration-plugin
Conflicts:      %{lname} < 5.6.0

%description plugin
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package devel
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       %{lname} = %{version}
Requires:       cmake(KF5ConfigWidgets) >= %{_kf5_version}
Requires:       cmake(KF5IconThemes) >= %{_kf5_version}

%description devel
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly. Development files

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5Style.so.*

%files plugin
%{_kf5_datadir}/infopage/
%{_kf5_plugindir}/
%{_kf5_libexecdir}/
%{_kf5_notifydir}/

%files devel
%{_kf5_libdir}/libKF5Style.so
%{_kf5_libdir}/cmake/KF5FrameworkIntegration/
%{_kf5_includedir}/KStyle/
%{_kf5_includedir}/FrameworkIntegration/

%changelog
