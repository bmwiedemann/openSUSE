#
# spec file for package qqc2-breeze-style6
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

%define rname qqc2-breeze-style

%bcond_without released
Name:           qqc2-breeze-style6
Version:        6.1.1
Release:        0
Summary:        Breeze Style for Qt Quick
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTemplates2) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
A Qt Quick Controls 2 style engine that uses the desktop style to draw controls
with QStyle.

%package devel
Summary:        Development Files for the Breeze Qt Quick Controls 2 Style
Requires:       %{name} = %{version}
Requires:       kf6-extra-cmake-modules >= %{kf6_version}

%description devel
This file contains cmake files to be used by projects that depend on
qqc2-breeze-style6.
Usually not needed as it is only a runtime dependency.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/kf6/kirigami/
%dir %{_kf6_plugindir}/kf6/kirigami/platform
%{_kf6_qmldir}/org/kde/breeze/
%{_kf6_plugindir}/kf6/kirigami/platform/org.kde.breeze.so

%files devel
%{_kf6_cmakedir}/QQC2BreezeStyle/

%changelog
