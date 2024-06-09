#
# spec file for package kf6-kconfig
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

%define rname kconfig
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kconfig
Version:        6.3.0
Release:        0
Summary:        Advanced configuration system
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       kf6-kconfig-rpmlintrc
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
KConfig provides an advanced configuration system. It is made of three parts:
KConfigCore, KConfigGui and KConfigQml.

KConfigCore provides access to the configuration files themselves. It features:

- centralized definition: define your configuration in an XML file and use
`kconfig_compiler` to generate classes to read and write configuration entries.

- lock-down (kiosk) support.

KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

KConfigQml provides QtQuick bindings to KConfig, allowing it to be used with QML.

%package imports
Summary:        QML imports for kconfig
%requires_eq    libQt6Quick6
Supplements:    (libKF6ConfigCore6 and libQt6Quick6)

%description imports
QML imports for kconfig.

%package -n libKF6ConfigCore6
Summary:        System for configuration files
Requires:       kf6-kconfig >= %{version}
Recommends:     kconf_update6 = %{version}

%description -n libKF6ConfigCore6
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves.

%package -n libKF6ConfigGui6
Summary:        Widgets hooks for configuration entities
Requires:       libKF6ConfigCore6 = %{version}

%description -n libKF6ConfigGui6
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%package -n libKF6ConfigQml6
Summary:        QtQuick bindings for configuration entities
Requires:       libKF6ConfigCore6 = %{version}
Requires:       libKF6ConfigGui6 = %{version}

%description -n libKF6ConfigQml6
KConfigQml provides QtQuick bindings to KConfig, which allows using the library with
QML.

%package -n kconf_update6
Summary:        Configuration file access
Requires:       libKF6ConfigCore6 = %{version}

%description -n kconf_update6
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

This package contains the kconf_update tool.

%package devel
Summary:        KConfig Development files
Requires:       kconf_update6 = %{version}
Requires:       libKF6ConfigCore6 = %{version}
Requires:       libKF6ConfigGui6 = %{version}
Requires:       libKF6ConfigQml6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description devel
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves. It features:

- centralized definition: define your configuration in an XML file and use
`kconfig_compiler` to generate classes to read and write configuration entries.

- lock-down (kiosk) support.

KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files. Development files.

%lang_package -n libKF6ConfigCore6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kconfig6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6ConfigCore6
%ldconfig_scriptlets -n libKF6ConfigGui6
%ldconfig_scriptlets -n libKF6ConfigQml6

%files
%{_kf6_bindir}/kreadconfig6
%{_kf6_bindir}/kwriteconfig6
%{_kf6_debugdir}/kconfig.categories
%{_kf6_debugdir}/kconfig.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/config/

%files -n libKF6ConfigCore6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ConfigCore.so.*

%files -n libKF6ConfigGui6
%{_kf6_libdir}/libKF6ConfigGui.so.*

%files -n libKF6ConfigQml6
%{_kf6_libdir}/libKF6ConfigQml.so.*

%files -n kconf_update6
%{_kf6_libexecdir}/kconf_update

%files devel
%doc %{_kf6_qchdir}/KF6Config.*
%{_kf6_includedir}/KConfig/
%{_kf6_includedir}/KConfigCore/
%{_kf6_includedir}/KConfigGui/
%{_kf6_includedir}/KConfigQml/
%{_kf6_cmakedir}/KF6Config/
%{_kf6_libdir}/libKF6ConfigCore.so
%{_kf6_libdir}/libKF6ConfigGui.so
%{_kf6_libdir}/libKF6ConfigQml.so
%{_kf6_libexecdir}/kconfig_compiler_kf6

%files -n libKF6ConfigCore6-lang -f kconfig6.lang

%changelog
