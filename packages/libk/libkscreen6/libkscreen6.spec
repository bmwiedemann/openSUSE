#
# spec file for package libkscreen6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%bcond_without released
%define rname libkscreen
%define sover   8
Name:           libkscreen6
Version:        6.1.2
Release:        0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plasma screen management library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)

%description
Dynamic display management library for KDE

%package -n libKF6ScreenDpms%{sover}
Summary:        Plasma screen management library
Requires:       libKF6Screen%{sover} = %{version}

%description -n libKF6ScreenDpms%{sover}
Energy saving display management library for KDE

%package plugin
Summary:        Plasma screen management library
Requires:       libKF6Screen%{sover} = %{version}
Requires:       libKF6ScreenDpms%{sover} = %{version}
Provides:       libkscreen2-plugin = %{version}
Obsoletes:      libkscreen2-plugin < %{version}

%description plugin
Plugins for dynamic display management in Plasma

%package devel
Summary:        Plasma screen management library (development package)
Requires:       libKF6Screen%{sover} = %{version}
Requires:       libKF6ScreenDpms%{sover} = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Development files belonging to libkscreen, dynamic display management in Plasma

%package -n libKF6Screen%{sover}
Summary:        Plasma screen management library
Recommends:     libKF6ScreenDpms%{sover}
Recommends:     libkscreen6-plugin

%description -n libKF6Screen%{sover}
Shared library for dynamic display management in Plasma

%lang_package -n libKF6Screen%{sover}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libkscreen6 --with-qt --all-name --without-mo

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Screen%{sover}
%ldconfig_scriptlets -n libKF6ScreenDpms%{sover}

%post plugin
%{systemd_user_post plasma-kscreen.service}

%preun plugin
%{systemd_user_preun plasma-kscreen.service}

%postun plugin
%{systemd_user_postun plasma-kscreen.service}

%files plugin
%{_kf6_bindir}/kscreen-doctor
%{_kf6_plugindir}/kf6/kscreen/
%{_kf6_libexecdir}/kscreen_backend_launcher
%{_kf6_sharedir}/dbus-1/services/org.kde.kscreen.service
%{_kf6_debugdir}/libkscreen.categories
%{_userunitdir}/plasma-kscreen.service
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kscreen-doctor

%files -n libKF6Screen%{sover}
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Screen.so.%{sover}
%{_kf6_libdir}/libKF6Screen.so.*

%files -n libKF6ScreenDpms%{sover}
%{_kf6_libdir}/libKF6ScreenDpms.so.%{sover}
%{_kf6_libdir}/libKF6ScreenDpms.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Screen.*
%{_kf6_includedir}/kscreen_version.h
%{_kf6_includedir}/KScreen/
%{_kf6_libdir}/cmake/KF6Screen/
%{_kf6_libdir}/libKF6Screen.so
%{_kf6_libdir}/libKF6ScreenDpms.so
%{_kf6_libdir}/pkgconfig/KF6Screen.pc

%files -n libKF6Screen%{sover}-lang -f libkscreen6.lang

%changelog
