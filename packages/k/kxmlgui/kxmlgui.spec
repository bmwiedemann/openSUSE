#
# spec file for package kxmlgui
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


%define lname   libKF5XmlGui5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kxmlgui
Version:        5.116.0
Release:        0
Summary:        Framework for managing menu and toolbar actions
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{_kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_version}
# Now requires private headers
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{qt5_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5PrintSupport) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiPlugin) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  pkgconfig(x11)

%description
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins.

%package -n %{lname}
Summary:        Framework for managing menu and toolbar actions
Obsoletes:      libKF5XmlGui4

%description -n %{lname}
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins.

%package devel
Summary:        Framework for managing menu and toolbar actions
Requires:       %{lname} = %{version}
Requires:       cmake(KF5Config) >= %{_kf5_version}
Requires:       cmake(KF5ConfigWidgets) >= %{_kf5_version}
Requires:       cmake(Qt5DBus) >= %{qt5_version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}
Requires:       cmake(Qt5Xml) >= %{qt5_version}

%description devel
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

mkdir -p %{buildroot}%{_kf5_sharedir}/kxmlgui5/

%find_lang kxmlgui5

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f kxmlgui5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5XmlGui.so.*
%{_kf5_configdir}/ui/
%{_kf5_libexecdir}/ksendbugmail
%dir %{_kf5_sharedir}/kxmlgui5/
%{_kf5_debugdir}/kxmlgui.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5XmlGui.so
%{_kf5_libdir}/cmake/KF5XmlGui/
%{_kf5_includedir}/KXmlGui/
%{_kf5_mkspecsdir}/qt_KXmlGui.pri
%dir %{_kf5_plugindir}/designer
%{_kf5_plugindir}/designer/kxmlgui5widgets.so

%changelog
