#
# spec file for package kpipewire6
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


%global kf6_version 6.0.0
%define qt6_version 6.6.0

%define _sover 6
%define rname kpipewire
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kpipewire6
Version:        6.1.2
Release:        0
Summary:        PipeWire integration for KDE Plasma
License:        LGPL-2.0-only AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)

%description
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.

%package -n libKPipeWire%{_sover}
Summary:        PipeWire integration for KDE Plasma - main library

%description -n libKPipeWire%{_sover}
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package contains the main KPipeWire library.

%package -n libKPipeWireRecord%{_sover}
Summary:        PipeWire integration for KDE Plasma - recording support

%description -n libKPipeWireRecord%{_sover}
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package contains the library needed for video and audio capture.

%package -n libKPipeWireDmaBuf%{_sover}
Summary:        PipeWire integration for KDE Plasma - DMA-BUF support

%description -n libKPipeWireDmaBuf%{_sover}
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides a helper for downloading DMA-BUF textures for CPU processing.

%package imports
Summary:        QtQuick bindings for kpipewire6
Requires:       libKPipeWire%{_sover} = %{version}
Requires:       libKPipeWireDmaBuf%{_sover} = %{version}
Requires:       libKPipeWireRecord%{_sover} = %{version}

%description imports
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides QtQuick bindings for the main KPipeWire libraries.

%package devel
Summary:        Development files for kpipewire6
Requires:       kpipewire6-imports = %{version}
Requires:       libKPipeWire%{_sover} = %{version}
Requires:       libKPipeWireDmaBuf%{_sover} = %{version}
Requires:       libKPipeWireRecord%{_sover} = %{version}
Requires:       pkgconfig(epoxy)
Requires:       pkgconfig(libpipewire-0.3)
Conflicts:      kpipewire-devel

%description devel
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides the development files needed to build applications
which use KPipeWire.

%lang_package -n libKPipeWire%{_sover}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kpipewire6

%check
# Test fails since 03201bb6. A running pipewire is required
# %%ctest

%ldconfig_scriptlets -n libKPipeWire%{_sover}
%ldconfig_scriptlets -n libKPipeWireRecord%{_sover}
%ldconfig_scriptlets -n libKPipeWireDmaBuf%{_sover}

%files -n libKPipeWire%{_sover}
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKPipeWire.so.*
%{_kf6_debugdir}/kpipewire.categories

%files -n libKPipeWireRecord%{_sover}
%{_kf6_libdir}/libKPipeWireRecord.so.*
%{_kf6_debugdir}/kpipewirerecord.categories

%files -n libKPipeWireDmaBuf%{_sover}
%{_kf6_libdir}/libKPipeWireDmaBuf.so.*

%files imports
%{_kf6_qmldir}/org/kde/pipewire/

%files devel
%{_includedir}/KPipeWire/
%{_kf6_cmakedir}/KPipeWire/
%{_kf6_libdir}/libKPipeWire.so
%{_kf6_libdir}/libKPipeWireRecord.so
%{_kf6_libdir}/libKPipeWireDmaBuf.so

%files -n libKPipeWire%{_sover}-lang -f kpipewire6.lang

%changelog
