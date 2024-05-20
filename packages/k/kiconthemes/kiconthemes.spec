#
# spec file for package kiconthemes
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   libKF5IconThemes5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kiconthemes
Version:        5.116.0
Release:        0
Summary:        Icon GUI utilities
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Archive) >= %{_kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiPlugin) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{qt5_version}

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package -n %{lname}
Summary:        Icon GUI utilities
%requires_eq libQt5Core5
%if %pkg_vcmp cmake(Qt5Core) >= %{qt5_version}
# Used as fallback icon theme starting with Qt 5.12
Recommends:     breeze5-icons
%endif


%description -n %{lname}
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package devel
Summary:        Icon GUI utilities: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}

%description devel
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kiconthemes5

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f kiconthemes5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5IconThemes.so.*
%dir %{_kf5_plugindir}/iconengines
%{_kf5_plugindir}/iconengines/KIconEnginePlugin.so
%{_kf5_debugdir}/kiconthemes.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%dir %{_kf5_plugindir}/designer
%{_kf5_bindir}/kiconfinder5
%{_kf5_libdir}/libKF5IconThemes.so
%{_kf5_libdir}/cmake/KF5IconThemes/
%{_kf5_includedir}/KIconThemes
%{_kf5_plugindir}/designer/kiconthemes5widgets.so
%{_kf5_mkspecsdir}/qt_KIconThemes.pri

%changelog
