#
# spec file for package solid
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


%define lname   libKF5Solid5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           solid
Version:        5.116.0
Release:        0
Summary:        KDE Desktop hardware abstraction
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  bison
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(mount)
%if %{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(libplist-2.0)
%else
BuildRequires:  pkgconfig(libplist)
%endif
BuildRequires:  pkgconfig(libudev)

%description
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package -n %{lname}
Summary:        KDE Desktop hardware abstraction
Recommends:     %{name}-imports = %{version}
Recommends:     %{name}-tools = %{version}
Recommends:     media-player-info
Recommends:     udisks2
Obsoletes:      libKF5Solid4

%description -n %{lname}
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package tools
Summary:        KDE Desktop hardware abstraction

%description tools
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
CLI utilities.

%package imports
Summary:        KDE Desktop hardware abstraction

%description imports
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
QML imports.

%package devel
Summary:        KDE Desktop hardware abstraction: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DWITH_NEW_SOLID_JOB=ON -DWITH_NEW_POWER_ASYNC_API=ON -DWITH_NEW_POWER_ASYNC_FREEDESKTOP=ON -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang solid5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f solid5.lang

%files -n %{lname}
%license LICENSES/*
%{_kf5_debugdir}/solid.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Solid.so.5
%{_kf5_libdir}/libKF5Solid.so.5.*

%files tools
%{_kf5_bindir}/solid-hardware5
%{_kf5_bindir}/solid-power

%files imports
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/solid/

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Solid/
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_mkspecsdir}/qt_Solid.pri

%changelog
