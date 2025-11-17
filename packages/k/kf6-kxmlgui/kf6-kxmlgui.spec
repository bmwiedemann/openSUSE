#
# spec file for package kf6-kxmlgui
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define rname kxmlgui

%bcond_without kde_python_bindings
%if %{with kde_python_bindings}
%if 0%{suse_version} > 1500
%define pythons %{primary_python}
%else
%{?sle15_python_module_pythons}
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}
%endif

# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kxmlgui
Version:        6.20.0
Release:        0
Summary:        Framework for managing menu and toolbar actions
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{_kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
# SECTION bindings
%if %{with kde_python_bindings}
BuildRequires:  %{mypython}-build
BuildRequires:  %{mypython}-devel >= 3.9
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)
%endif
# /SECTION

%description
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins.

%package -n libKF6XmlGui6
Summary:        Framework for managing menu and toolbar actions
Requires:       kf6-kxmlgui >= %{version}

%description -n libKF6XmlGui6
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins.

%package devel
Summary:        Framework for managing menu and toolbar actions
Requires:       libKF6XmlGui6 = %{version}
Requires:       cmake(KF6Config) >= %{_kf6_version}
Requires:       cmake(KF6ConfigWidgets) >= %{_kf6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description devel
libkxmlgui provides a framework for managing menu and toolbar actions in an
abstract way. The actions are configured through a XML description and hooks
in the application code. The framework supports merging of multiple
description for example for integrating actions from plugins. Development files.

%if %{with kde_python_bindings}
%package -n python3-kf6-kxmlgui
Summary:        Python interface for kf6-kxmlgui

%description -n python3-kf6-kxmlgui
This package provides a python interface for kf6-kxmlgui.
%endif

%lang_package -n libKF6XmlGui6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kxmlgui6

%ldconfig_scriptlets -n libKF6XmlGui6

%files
%{_kf6_debugdir}/kxmlgui.categories
%{_kf6_debugdir}/kxmlgui.renamecategories

%files -n libKF6XmlGui6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6XmlGui.so.*

%files devel
%{_kf6_cmakedir}/KF6XmlGui/
%{_kf6_includedir}/KXmlGui/
%{_kf6_libdir}/libKF6XmlGui.so
%{_kf6_plugindir}/designer/kxmlgui6widgets.so

%if %{with kde_python_bindings}
%files -n python3-kf6-kxmlgui
%{mypython_sitearch}/*.so
%endif

%files -n libKF6XmlGui6-lang -f kxmlgui6.lang

%changelog
