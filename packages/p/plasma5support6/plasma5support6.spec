#
# spec file for package plasma5support6
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

%define rname plasma5support
# Full KF6 version (e.g. 6.0.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
# Note: despite being in the plasma namespace upstream, the build system follows the frameworks conventions
Name:           plasma5support6
Version:        6.1.1
Release:        0
Summary:        KF6 Porting aid
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Notifications) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Package) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6XmlGui) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KSysGuard) >= 6
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Support components for porting from KF5/Qt5 to KF6/Qt6.

%package -n libPlasma5Support6
Summary:        plasma5support library
Requires:       plasma5support6 >= %{version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description -n libPlasma5Support6
The plasma5support library.

%package devel
Summary:        Development Files for the plasma5support framework
Requires:       libPlasma5Support6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Service) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
Development Files for the plasma5support framework.

%lang_package -n libPlasma5Support6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libPlasma5Support6

%files
%{_kf6_debugdir}/plasma5support.categories
%{_kf6_debugdir}/plasma5support.renamecategories
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_qmldir}/org/kde/plasma/plasma5support/
%{_kf6_sharedir}/plasma5support/
%dir %{_kf6_plugindir}/plasma5support
%dir %{_kf6_plugindir}/plasma5support/dataengine
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_devicenotifications.so
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_keystate.so

%files -n libPlasma5Support6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libPlasma5Support.so.*

%files devel
%doc %{_kf6_qchdir}/Plasma5Support.*
%{_kf6_cmakedir}/Plasma5Support/
%{_includedir}/Plasma5Support/
%{_kf6_libdir}/libPlasma5Support.so

%files -n libPlasma5Support6-lang -f %{name}.lang

%changelog
