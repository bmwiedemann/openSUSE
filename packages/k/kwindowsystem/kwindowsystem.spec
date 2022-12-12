#
# spec file for package kwindowsystem
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


%define lname   libKF5WindowSystem5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwindowsystem
Version:        5.101.0
Release:        0
Summary:        KDE Access to window manager
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)

%description
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package -n %{lname}
Summary:        KDE Access to window manager
%requires_ge    libQt5Widgets5
%requires_ge    libQt5X11Extras5

%description -n %{lname}
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package devel
Summary:        KDE Access to window manager: Build Environment
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0
Requires:       cmake(Qt5Widgets) >= 5.15.0
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcb)

%description devel
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang kwindowsystem5 --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f kwindowsystem5.lang

%files -n %{lname}
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kwindowsystem
%{_kf5_debugdir}/kwindowsystem.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5WindowSystem.so.*
%{_kf5_plugindir}/kf5/kwindowsystem/KF5WindowSystemX11Plugin.so

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5WindowSystem/
%{_kf5_libdir}/libKF5WindowSystem.so
%{_kf5_mkspecsdir}/qt_KWindowSystem.pri

%changelog
