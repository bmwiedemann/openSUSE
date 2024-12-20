#
# spec file for package kconfigwidgets
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libKF5ConfigWidgets5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kconfigwidgets
Version:        5.116.0
Release:        0
Summary:        Widgets for configuration dialogs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Auth) >= %{_kf5_version}
BuildRequires:  cmake(KF5Codecs) >= %{_kf5_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiPlugin) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package -n %{lname}
Summary:        Widgets for configuration dialogs
Conflicts:      kdelibs4support < 5.3.0
Obsoletes:      libKF5ConfigWidgets4

%description -n %{lname}
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package devel
Summary:        Widgets for configuration dialogs: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(KF5Auth) >= %{_kf5_version}
Requires:       cmake(KF5Codecs) >= %{_kf5_version}
Requires:       cmake(KF5Config) >= %{_kf5_version}
Requires:       cmake(KF5WidgetsAddons) >= %{_kf5_version}

%description devel
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DWITH_KAUTH=1
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f %{name}.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5ConfigWidgets.so.*
%{_kf5_sharedir}/locale/*/kf5_entry.desktop
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5ConfigWidgets.so
%{_kf5_libdir}/cmake/KF5ConfigWidgets/
%dir %{_kf5_plugindir}/designer
%{_kf5_plugindir}/designer/kconfigwidgets5widgets.so
%{_kf5_includedir}/KConfigWidgets
%{_kf5_bindir}/preparetips5
%{_kf5_mandir}/man1/preparetips5.*
%{_kf5_mkspecsdir}/qt_KConfigWidgets.pri

%changelog
