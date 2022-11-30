#
# spec file for package kpipewire
#
# Copyright (c) 2022 SUSE LLC
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


%define _sover 5
# Full Plasma 5 version (e.g. 5.9.1)
%{!?_plasma5_bugfix: %global _plasma5_bugfix %{version}}
%bcond_without released
Name:           kpipewire
Version:        5.26.4
Release:        0
Summary:        PipeWire integration for KDE Plasma
License:        LGPL-2.0-only AND LGPL-3.0-only
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kpipewire-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kpipewire-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libQt5Gui-private-headers-devel >= 5.15.0
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CoreAddons) >= 5.98.0
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(wayland-client)

%description
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.

%package -n libKPipeWire%{_sover}
Summary:        PipeWire integration for KDE Plasma - main library
%requires_eq    libQt5Gui

%description -n libKPipeWire%{_sover}
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package contains the main KPipeWire library.

%package -n libKPipeWireRecord%{_sover}
Summary:        PipeWire integration for KDE Plasma - recording support
%requires_eq    libQt5Gui

%description -n libKPipeWireRecord%{_sover}
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package contains the library needed for video and audio capture.

%package imports
Summary:        QtQuick bindings for kpipewire
Requires:       libKPipeWire%{_sover} = %{version}
Requires:       libKPipeWireRecord%{_sover} = %{version}

%description imports
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides QtQuick bindings for the main KPipeWire libraries.

%package devel
Summary:        Development files for kpipewire
Group:          Development/Libraries/KDE
Requires:       %{name}-imports = %{version}
Requires:       libKPipeWire%{_sover} = %{version}
Requires:       libKPipeWireRecord%{_sover} = %{version}

%description devel
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides the development files needed to build applications
which use KPipeWire.

%lang_package -n libKPipeWire%{_sover}

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with released}
    %find_lang kpipewire%{_sover}
  %endif

%check
%ctest

%post -n libKPipeWire%{_sover} -p /sbin/ldconfig
%postun -n libKPipeWire%{_sover} -p /sbin/ldconfig
%post -n libKPipeWireRecord%{_sover} -p /sbin/ldconfig
%postun -n libKPipeWireRecord%{_sover} -p /sbin/ldconfig

%files -n libKPipeWire%{_sover}
%license LICENSES/*
%{_kf5_libdir}/libKPipeWire.so.%{_sover}
%{_kf5_libdir}/libKPipeWire.so.%{_sover}.*
%{_kf5_debugdir}/kpipewire.categories

%files -n libKPipeWireRecord%{_sover}
%{_kf5_libdir}/libKPipeWireRecord.so.%{_sover}
%{_kf5_libdir}/libKPipeWireRecord.so.%{_sover}.*
%{_kf5_debugdir}/kpipewirerecord.categories

%files imports
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/pipewire

%files devel
%{_includedir}/KPipeWire/
%{_kf5_cmakedir}/KPipeWire/
%{_kf5_libdir}/libKPipeWire.so
%{_kf5_libdir}/libKPipeWireRecord.so

%files -n libKPipeWire%{_sover}-lang -f kpipewire%{_sover}.lang

%changelog
