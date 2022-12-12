#
# spec file for package kconfig
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


%define sonum   5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kconfig
Version:        5.101.0
Release:        0
Summary:        Advanced configuration system
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FEATURE-OPENSUSE
Patch0:         kconfig-desktop-translations.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

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

%package -n libKF5ConfigCore%{sonum}
Summary:        System for configuration files
%requires_ge    libQt5Core5
Recommends:     kconf_update5 = %{version}

%description -n libKF5ConfigCore%{sonum}
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves.

%package -n libKF5ConfigGui%{sonum}
Summary:        Widgets hooks for configuration entities
%requires_ge    libKF5ConfigCore5
%requires_ge    libQt5Core5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Xml5

%description -n libKF5ConfigGui%{sonum}
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%package -n libKF5ConfigQml%{sonum}
Summary:        QtQuick bindings for configuration entities
%requires_ge    libKF5ConfigCore5
%requires_ge    libKF5ConfigGui5
%requires_ge    libQt5Core5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Xml5

%description -n libKF5ConfigQml%{sonum}
KConfigQml provides QtQuick bindings to KConfig, which allows using the library with
QML.

%package -n kconf_update5
Summary:        Configuration file access
Requires:       libKF5ConfigCore%{sonum} = %{version}

%description -n kconf_update5
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

This package contains the kconf_update tool.

%package devel
Summary:        KConfig Development files
Requires:       extra-cmake-modules
Requires:       kconf_update5 = %{version}
Requires:       libKF5ConfigCore%{sonum} = %{version}
Requires:       libKF5ConfigGui%{sonum} = %{version}
Requires:       libKF5ConfigQml%{sonum} = %{version}
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5Xml) >= 5.15.0

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

%lang_package -n libKF5ConfigCore%{sonum}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang kconfig5 --with-qt --without-mo

%post -n libKF5ConfigCore%{sonum} -p /sbin/ldconfig
%postun -n libKF5ConfigCore%{sonum} -p /sbin/ldconfig
%post -n libKF5ConfigGui%{sonum} -p /sbin/ldconfig
%postun -n libKF5ConfigGui%{sonum} -p /sbin/ldconfig
%post -n libKF5ConfigQml%{sonum} -p /sbin/ldconfig
%postun -n libKF5ConfigQml%{sonum} -p /sbin/ldconfig

%files -n libKF5ConfigCore%{sonum}-lang -f kconfig5.lang

%files -n libKF5ConfigCore%{sonum}
%license LICENSES/*
%doc README*
%{_kf5_bindir}/k*config5
%{_kf5_debugdir}/kconfig.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5ConfigCore.so.*

%files -n libKF5ConfigGui%{sonum}
%doc README*
%{_kf5_libdir}/libKF5ConfigGui.so.*

%files -n libKF5ConfigQml%{sonum}
%doc README*
%{_kf5_libdir}/libKF5ConfigQml.so.*

%files -n kconf_update5
%doc README*
%dir %{_kf5_libexecdir}
%{_kf5_libexecdir}/kconf_update

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Config/
%{_kf5_libdir}/libKF5ConfigCore.so
%{_kf5_libdir}/libKF5ConfigGui.so
%{_kf5_libdir}/libKF5ConfigQml.so
%{_kf5_libexecdir}/kconfig_compiler_kf5
%{_kf5_mkspecsdir}/qt_KConfigCore.pri
%{_kf5_mkspecsdir}/qt_KConfigGui.pri

%changelog
