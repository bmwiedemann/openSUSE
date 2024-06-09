#
# spec file for package kf6-kconfigwidgets
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

%define rname kconfigwidgets
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kconfigwidgets
Version:        6.3.0
Release:        0
Summary:        Widgets for configuration dialogs
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package -n libKF6ConfigWidgets6
Summary:        Widgets for configuration dialogs
Requires:       kf6-kconfigwidgets >= %{version}

%description -n libKF6ConfigWidgets6
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package devel
Summary:        Widgets for configuration dialogs: Build Environment
Requires:       libKF6ConfigWidgets6 = %{version}
Requires:       cmake(KF6Codecs) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Config) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}

%description devel
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings. Development files.

%lang_package -n libKF6ConfigWidgets6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kconfigwidgets6 --with-man --all-name

%ldconfig_scriptlets -n libKF6ConfigWidgets6

%files
%{_kf6_debugdir}/kconfigwidgets.categories
%{_kf6_debugdir}/kconfigwidgets.renamecategories
%{_kf6_sharedir}/locale/*/kf6_entry.desktop

%files -n libKF6ConfigWidgets6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ConfigWidgets.so.*

%files devel
%doc %{_kf6_qchdir}/KF6ConfigWidgets.*
%{_kf6_cmakedir}/KF6ConfigWidgets/
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_plugindir}/designer/kconfigwidgets6widgets.so

%files -n libKF6ConfigWidgets6-lang -f kconfigwidgets6.lang

%changelog
