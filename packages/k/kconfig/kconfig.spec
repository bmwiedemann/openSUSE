#
# spec file for package kconfig
#
# Copyright (c) 2020 SUSE LLC
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
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kconfig
Version:        5.75.0
Release:        0
Summary:        Advanced configuration system
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE
Patch0:         kconfig-desktop-translations.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves. It features:

- centralized definition: define your configuration in an XML file and use
`kconfig_compiler` to generate classes to read and write configuration entries.

- lock-down (kiosk) support.

KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%package -n libKF5ConfigCore%{sonum}
Summary:        System for configuration files
Group:          System/GUI/KDE
%requires_ge    libQt5Core5
Recommends:     kconf_update5 = %{version}
%if %{with lang}
Recommends:     libKF5ConfigCore%{sonum}-lang = %{version}
%endif

%description -n libKF5ConfigCore%{sonum}
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

KConfigCore provides access to the configuration files themselves.

%package -n libKF5ConfigGui%{sonum}
Summary:        Widgets hooks for configuration entities
Group:          System/GUI/KDE
%requires_ge    libKF5ConfigCore5
%requires_ge    libQt5Core5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Xml5

%description -n libKF5ConfigGui%{sonum}
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%package -n kconf_update5
Summary:        Configuration file access
Group:          System/GUI/KDE
Requires:       libKF5ConfigCore%{sonum} = %{version}

%description -n kconf_update5
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

This package contains the kconf_update tool.

%package devel
Summary:        KConfig Development files
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules
Requires:       kconf_update5 = %{version}
Requires:       libKF5ConfigCore%{sonum} = %{version}
Requires:       libKF5ConfigGui%{sonum} = %{version}
Requires:       cmake(Qt5Xml) >= 5.12.0

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

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n libKF5ConfigCore%{sonum} -p /sbin/ldconfig
%postun -n libKF5ConfigCore%{sonum} -p /sbin/ldconfig
%post -n libKF5ConfigGui%{sonum} -p /sbin/ldconfig
%postun -n libKF5ConfigGui%{sonum} -p /sbin/ldconfig

%if %{with lang}
%files -n libKF5ConfigCore%{sonum}-lang -f %{name}5.lang
%endif

%files -n libKF5ConfigCore%{sonum}
%license LICENSES/*
%doc README*
%{_kf5_bindir}/k*config5
%{_kf5_debugdir}/kconfig.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5ConfigCore.so.*

%files -n libKF5ConfigGui%{sonum}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5ConfigGui.so.*

%files -n kconf_update5
%license LICENSES/*
%doc README*
%dir %{_kf5_libexecdir}
%{_kf5_libexecdir}/kconf_update

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Config/
%{_kf5_libdir}/libKF5ConfigCore.so
%{_kf5_libdir}/libKF5ConfigGui.so
%{_kf5_libexecdir}/kconfig_compiler_kf5
%{_kf5_mkspecsdir}/qt_KConfigCore.pri
%{_kf5_mkspecsdir}/qt_KConfigGui.pri

%changelog
