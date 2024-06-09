#
# spec file for package kf6-qqc2-desktop-style
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


%define qt6_version 6.6.0

%define rname qqc2-desktop-style
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-qqc2-desktop-style
Version:        6.3.0
Release:        0
Summary:        A Qt Quick Controls 2 Style for Desktop UIs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-sonnet-imports >= %{_kf6_bugfix_version}
%requires_eq    qt6-declarative-imports
# plasma6-workspace sets up the env variables so that this theme
# is picked by default. It still works fine without it (no requires),
# but looks better with it. By itself plasma6-workspace does not use
# it (yet), so only install it with qt6-declarative-imports.
Supplements:    (plasma6-workspace and qt6-declarative-imports)
Obsoletes:      qqc2-desktop-style-lang < %{version}

%description
A Qt Quick Controls 2 style engine that uses the desktop style
to draw controls with QStyle.

%package devel
Summary:        Development Files for Qt Quick Controls 2 Desktop Style
Requires:       kf6-qqc2-desktop-style >= %{version}

%description devel
This file contains cmake files to be used by projects that depend on
qqc2-desktop-style.
Usually not needed as it is only a runtime dependency.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-qt

%files
%license LICENSES/*
%doc README.md
%dir %{_kf6_plugindir}/kf6/kirigami
%dir %{_kf6_plugindir}/kf6/kirigami/platform
%{_kf6_plugindir}/kf6/kirigami/platform/org.kde.desktop.so
%{_kf6_qmldir}/org/kde/desktop/
%{_kf6_qmldir}/org/kde/qqc2desktopstyle/

%files lang -f %{name}.lang

%files devel
%{_kf6_cmakedir}/KF6QQC2DesktopStyle/

%changelog
