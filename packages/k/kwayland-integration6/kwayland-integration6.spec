#
# spec file for package kwayland-integration6
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
%define rname kwayland-integration
Name:           kwayland-integration6
Version:        6.1.2
Release:        0
Summary:        Plugin to integrate KF5 KWayland into Plasma 6
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.102.0
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XkbCommonSupport)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
# Newer compiler needed for C++20 on Leap 15
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%endif
# From Plasma 5. In theory coinstallable, but make sure only
# the right one is installed.
Obsoletes:      kwayland-integration < %{version}

%description
Plugin to integrate KF5 KWayland into Plasma 6.

%prep
%autosetup -n %{rname}-%{version}

%build
%if 0%{?suse_version} < 1600
  export CC=gcc-13
  export CXX=g++-13
%endif
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_kf5_plugindir}/
%{_kf5_debugdir}/kwindowsystem.kwayland.categories

%changelog
