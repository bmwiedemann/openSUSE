#
# spec file for package kwayland-integration
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
Name:           kwayland-integration
Version:        5.20.2
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
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwayland-integration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5GuiAddons) >= 5.60.0
BuildRequires:  cmake(KF5IdleTime) >= 5.24.0
BuildRequires:  cmake(KF5Wayland) >= 5.24.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.24.0
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0

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
%license COPYING*
%{_kf5_plugindir}/
%{_kf5_debugdir}/kwindowsystem.kwayland.categories

%changelog
