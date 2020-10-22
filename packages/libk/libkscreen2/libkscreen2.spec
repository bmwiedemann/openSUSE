#
# spec file for package libkscreen2
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


%bcond_without lang
%define lname   libKF5Screen7
Name:           libkscreen2
Version:        5.20.1
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE's screen management library
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         libkscreen-%{version}.tar.xz
%if %{with lang}
Source1:        libkscreen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qt5Core) >= 5.11.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)

%description
Dynamic display management library for KDE

%package plugin
Summary:        KDE's screen management library
Group:          System/GUI/KDE
Requires:       %{lname} = %{version}

%description plugin
Plugins for dynamic display management in KDE

%package devel
Summary:        KDE's screen management library (development package)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= 5.11.0

%description devel
Development files belonging to libkscreen, dynamic display management in KDE

%package -n %{lname}
Summary:        KDE's screen management library
Group:          System/GUI/KDE
Recommends:     %{name}-plugin

%description -n %{lname}
Shared library for dynamic display management in KDE

%prep
%setup -q -n libkscreen-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes -s %{buildroot}

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files plugin
%license COPYING*
%{_kf5_bindir}/kscreen-doctor
%{_kf5_plugindir}/
%{_kf5_libexecdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kscreen.service
%{_kf5_debugdir}/libkscreen.categories

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5Screen.so.*

%files devel
%license COPYING*
%{_kf5_libdir}/libKF5Screen.so
%{_kf5_libdir}/cmake/KF5Screen/
%{_kf5_libdir}/pkgconfig/kscreen2.pc
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KScreen.pri

%changelog
