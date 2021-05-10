#
# spec file for package bluez-qt
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


%define sonum   6
%define _libname KF5BluezQt
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           bluez-qt
Version:        5.82.0
Release:        0
Summary:        Async Bluez wrapper library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  pkgconfig(udev)

%description
Async Bluez wrapper library.

%package -n lib%{_libname}%{sonum}
Summary:        Async Bluez wrapper library - development files
Group:          System/GUI/KDE

# KUF only due to version number overlapping
Obsoletes:      lib%{_libname}5

%description -n lib%{_libname}%{sonum}
Async Bluez wrapper library.

%package imports
Summary:        Async Bluez wrapper library
Group:          System/GUI/KDE
%requires_ge    libQtQuick5
Supplements:    packageand(lib%{_libname}%{sonum}:libQtQuick5)

%description imports
Async Bluez wrapper library.
QML imports.

%package udev
Summary:        bluez-qt integration with udev
Group:          System/Base
Requires:       udev

%description udev
Async Bluez wrapper library.
Udev rules.

%package devel
Summary:        Async Bluez wrapper library - development files
Group:          Development/Libraries/C and C++
Requires:       lib%{_libname}%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
Development files for QBluez Async Bluez wrapper library.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DUDEV_RULES_INSTALL_DIR="%{_udevrulesdir}"
%cmake_build

%install
%kf5_makeinstall -C build
  %fdupes -s %{buildroot}

%post -n lib%{_libname}%{sonum} -p /sbin/ldconfig
%postun -n lib%{_libname}%{sonum} -p /sbin/ldconfig

%files -n lib%{_libname}%{sonum}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/bluezqt.categories
%{_kf5_debugdir}/bluezqt.renamecategories
%{_libqt5_libdir}/lib%{_libname}*.so.*

%files imports
%license LICENSES/*
%doc README*
%{_kf5_qmldir}/

%files udev
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/%{_libname}/
%{_kf5_libdir}/lib%{_libname}*.so
%{_kf5_mkspecsdir}/qt_BluezQt.pri

%changelog
