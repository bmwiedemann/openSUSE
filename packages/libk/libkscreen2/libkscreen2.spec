#
# spec file for package libkscreen2
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


%bcond_without released
%define sover   8
%define lname   libKF5Screen%{sover}
Name:           libkscreen2
Version:        5.27.11
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE's screen management library
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/libkscreen-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/libkscreen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)

%description
Dynamic display management library for KDE

%package -n libKF5ScreenDpms%{sover}
Summary:        KDE's screen management library
Group:          System/GUI/KDE
Requires:       %{lname} = %{version}

%description -n libKF5ScreenDpms%{sover}
Energy saving display management library for KDE

%package plugin
Summary:        KDE's screen management library
Group:          System/GUI/KDE
Requires:       %{lname} = %{version}
Requires:       libKF5ScreenDpms%{sover} = %{version}
# Existed in KDE:Unstable:Frameworks for a short time
Provides:       %{name}-zsh-completion = %{version}
Obsoletes:      %{name}-zsh-completion < %{version}

%description plugin
Plugins for dynamic display management in KDE

%package devel
Summary:        KDE's screen management library (development package)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libKF5ScreenDpms%{sover} = %{version}
Requires:       cmake(Qt5Core)

%description devel
Development files belonging to libkscreen, dynamic display management in KDE

%package -n %{lname}
Summary:        KDE's screen management library
Group:          System/GUI/KDE
Recommends:     %{name}-plugin
Recommends:     libKF5ScreenDpms%{sover}

%description -n %{lname}
Shared library for dynamic display management in KDE

%lang_package -n %{lname}

%prep
%autosetup -p1 -n libkscreen-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %find_lang libkscreen5 --with-qt --all-name --without-mo
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%post -n libKF5ScreenDpms%{sover} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig
%postun -n libKF5ScreenDpms%{sover} -p /sbin/ldconfig

%post plugin
%{systemd_user_post plasma-kscreen.service}

%preun plugin
%{systemd_user_preun plasma-kscreen.service}

%postun plugin
%{systemd_user_postun plasma-kscreen.service}

%files plugin
%license LICENSES/*
%{_kf5_bindir}/kscreen-doctor
%{_kf5_plugindir}/
%{_kf5_libexecdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kscreen.service
%{_kf5_debugdir}/libkscreen.categories
%{_userunitdir}/plasma-kscreen.service
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kscreen-doctor

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Screen.so.%{sover}
%{_kf5_libdir}/libKF5Screen.so.*

%files -n libKF5ScreenDpms%{sover}
%{_kf5_libdir}/libKF5ScreenDpms.so.%{sover}
%{_kf5_libdir}/libKF5ScreenDpms.so.*

%files -n %{lname}-lang -f libkscreen5.lang

%files devel
%license LICENSES/*
%{_kf5_libdir}/libKF5Screen.so
%{_kf5_libdir}/libKF5ScreenDpms.so
%{_kf5_libdir}/cmake/KF5Screen/
%{_kf5_libdir}/pkgconfig/kscreen2.pc
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KScreen.pri

%changelog
