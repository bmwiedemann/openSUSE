#
# spec file for package kf6-kiconthemes
#
# Copyright (c) 2025 SUSE LLC
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


%define qt6_version 6.8.0

%define rname kiconthemes
# Full KF6 version (e.g. 6.15.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kiconthemes
Version:        6.15.0
Release:        0
Summary:        Icon GUI utilities
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6BreezeIcons) >= %{_kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package imports
Summary:        QML Imports for kiconthemes

%description imports
QML Bindings for the kiconthemes framework.

%package -n libKF6IconThemes6
Summary:        Icon GUI utilities
Requires:       kf6-kiconthemes >= %{version}
Recommends:     breeze6-icons

%description -n libKF6IconThemes6
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package -n libKF6IconWidgets6
Summary:        Icon GUI utilities
Requires:       kf6-kiconthemes >= %{version}
Recommends:     breeze6-icons

%description -n libKF6IconWidgets6
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package devel
Summary:        Icon GUI utilities: Build Environment
Requires:       libKF6IconThemes6 = %{version}
Requires:       libKF6IconWidgets6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks. Development files.

%lang_package -n libKF6IconThemes6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kiconthemes6

%ldconfig_scriptlets -n libKF6IconThemes6
%ldconfig_scriptlets -n libKF6IconWidgets6

%files
%{_kf6_debugdir}/kiconthemes.categories
%{_kf6_debugdir}/kiconthemes.renamecategories
%dir %{_kf6_plugindir}/kiconthemes6/
%dir %{_kf6_plugindir}/kiconthemes6/iconengines
%{_kf6_plugindir}/kiconthemes6/iconengines/KIconEnginePlugin.so

%files imports
%{_kf6_qmldir}/org/kde/iconthemes/

%files -n libKF6IconThemes6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6IconThemes.so.*

%files -n libKF6IconWidgets6
%{_kf6_libdir}/libKF6IconWidgets.so.*

%files devel
%{_kf6_bindir}/kiconfinder6
%{_kf6_cmakedir}/KF6IconThemes/
%{_kf6_includedir}/KIconThemes/
%{_kf6_includedir}/KIconWidgets/
%{_kf6_libdir}/libKF6IconThemes.so
%{_kf6_libdir}/libKF6IconWidgets.so
%{_kf6_plugindir}/designer/kiconthemes6widgets.so

%files -n libKF6IconThemes6-lang -f kiconthemes6.lang

%changelog
