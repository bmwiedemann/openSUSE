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
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kiconthemes
Version:        5.82.0
Release:        0
Summary:        Icon GUI utilities
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:        baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Svg) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package -n %{lname}
Summary:        Icon GUI utilities
Group:          System/GUI/KDE
Recommends:     %{lname}-lang = %{version}
%if %pkg_vcmp cmake(Qt5Core) >= 5.12.0
# Used as fallback icon theme starting with Qt 5.12
Recommends:     breeze5-icons
%endif

%description -n %{lname}
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package devel
Summary:        Icon GUI utilities: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Widgets) >= 5.15.0

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

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5IconThemes.so.*
%dir %{_kf5_plugindir}/iconengines
%{_kf5_plugindir}/iconengines/KIconEnginePlugin.so
%{_kf5_debugdir}/kiconthemes.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_bindir}/kiconfinder5
%{_kf5_libdir}/libKF5IconThemes.so
%{_kf5_libdir}/cmake/KF5IconThemes/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%dir %{_kf5_plugindir}/designer
%{_kf5_plugindir}/designer/kiconthemes5widgets.so
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KIconThemes.pri

%changelog
