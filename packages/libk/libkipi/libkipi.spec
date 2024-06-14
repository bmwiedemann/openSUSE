#
# spec file for package libkipi
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


%define _soversion 32_0_0
%bcond_without released
Name:           libkipi
Version:        24.05.1
Release:        0
Summary:        KDE Image Plugin Interface
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)

%description
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%package -n libKF5Kipi%{_soversion}
Summary:        KDE Image Plug-In Interface
Requires:       libkipi-data >= %{version}
Recommends:     kipi-plugins

%description -n libKF5Kipi%{_soversion}
This package provides a generic KDE image plug-in interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%package data
Summary:        KDE Image Plug-In Interface - data files
Conflicts:      libKF5Kipi30_0_0

%description data
This package contains data files needed by the KDE image plug-in library.

%package devel
Summary:        KDE Image Plugin Interface
Requires:       libKF5Kipi%{_soversion} = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5Service)
Requires:       cmake(KF5XmlGui)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Gui)
Requires:       cmake(Qt5Widgets)
Obsoletes:      libkipi-kf5-devel < %{version}
Provides:       libkipi-kf5-devel = %{version}

%description devel
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets -n libKF5Kipi%{_soversion}

%files -n libKF5Kipi%{_soversion}
%{_kf5_libdir}/libKF5Kipi.so.*

%files data
%{_kf5_iconsdir}/hicolor/*/apps/kipi.png
%{_kf5_servicetypesdir}/kipiplugin.desktop
%{_kf5_debugdir}/kipi.categories

%files devel
%license LICENSES/*
%doc README
%{_kf5_cmakedir}/KF5Kipi/
%{_kf5_includedir}/KIPI/
%{_kf5_libdir}/libKF5Kipi.so

%changelog
