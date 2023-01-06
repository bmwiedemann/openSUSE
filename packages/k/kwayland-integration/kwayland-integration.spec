#
# spec file for package kwayland-integration
#
# Copyright (c) 2023 SUSE LLC
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
Name:           kwayland-integration
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Integration plugins for various KDE frameworks for wayland windowing system
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kwayland-integration-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwayland-integration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5XkbCommonSupport)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
Provides integration plugins for various KDE frameworks for the wayland windowing system.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_kf5_plugindir}/
%{_kf5_debugdir}/kwindowsystem.kwayland.categories

%changelog
