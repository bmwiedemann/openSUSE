#
# spec file for package union6
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.24.0
%define qt6_version 6.9.0

%define rname union
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           union6
Version:        6.7.1
Release:        0
Summary:        Qt style supporting both QtQuick and QtWidgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Breeze) >= %{_plasma6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(cxx-rust-cssparser)
BuildRequires:  cmake(ryml)
Requires:       qt6qmlimport(org.kde.breeze)
Requires:       qt6qmlimport(org.kde.plasma.components)
Requires:       qt6qmlimport(Qt.labs.qmlmodels)
# Marked as runtime dep
Requires:       libKirigamiPlatform6 >= %{kf6_version}

%description
A Qt style supporting both QtQuick and QtWidgets.

%package devel
Summary:        Qt style supporting both QtQuick and QtWidgets
Requires:       %{name} = %{version}

%description devel
A Qt style supporting both QtQuick and QtWidgets.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/union.categories
%{_kf6_libdir}/libUnion.so.6{,.*}
%{_kf6_libdir}/libUnionQuickImpl.so.6{,.*}
%{_kf6_libdir}/libUnionQuickStyle.so.6{,.*}
%{_kf6_qmldir}/org/kde/kirigami/
%{_kf6_qmldir}/org/kde/union/
%{_kf6_sharedir}/union/
%dir %{_kf6_sharedir}/kstyle/
%dir %{_kf6_sharedir}/kstyle/themes/
%{_kf6_sharedir}/kstyle/themes/union.themerc
%{_kf6_pluginsdir}/union/
%dir %{_kf6_pluginsdir}/styles/
%{_kf6_pluginsdir}/styles/UnionWidgetsStyle.so
%dir %{_kf6_pluginsdir}/kf6/kirigami
%dir %{_kf6_pluginsdir}/kf6/kirigami/platform
%{_kf6_pluginsdir}/kf6/kirigami/platform/org.kde.union.so

%files devel
%{_includedir}/union/
%{_kf6_cmakedir}/Union/
%{_kf6_libdir}/libUnion.so
%{_kf6_bindir}/union-ruleinspector

%changelog
