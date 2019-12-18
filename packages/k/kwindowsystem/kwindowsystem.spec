#
# spec file for package kwindowsystem
#
# Copyright (c) 2019 SUSE LLC
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
%define _tar_path 5.65
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kwindowsystem
Version:        5.65.0
Release:        0
Summary:        KDE Access to window manager
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Test) >= 5.11.0
BuildRequires:  cmake(Qt5Widgets) >= 5.11.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.11.0
%endif

%description
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package -n %{lname}
Summary:        KDE Access to window manager
Group:          System/GUI/KDE
%requires_ge    libQt5Widgets5
%requires_ge    libQt5X11Extras5
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package devel
Summary:        KDE Access to window manager: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.11.0
Requires:       cmake(Qt5Widgets) >= 5.11.0
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
%setup -q

%build
  %cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5WindowSystem.so.*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/org.kde.kwindowsystem.platforms
%{_kf5_plugindir}/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemWaylandPlugin.so
%{_kf5_plugindir}/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemX11Plugin.so
%{_kf5_debugdir}/kwindowsystem.categories

%files devel
%{_kf5_libdir}/libKF5WindowSystem.so
%{_kf5_libdir}/cmake/KF5WindowSystem/
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KWindowSystem.pri

%changelog
