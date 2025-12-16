#
# spec file for package kf6-kwidgetsaddons
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

%define rname kwidgetsaddons

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

# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kwidgetsaddons
Version:        6.21.0
Release:        0
Summary:        Large set of desktop widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
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
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%package -n libKF6WidgetsAddons6
Summary:        Large set of desktop widgets
Requires:       kf6-kwidgetsaddons >= %{version}

%description -n libKF6WidgetsAddons6
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%package devel
Summary:        Large set of desktop widgets: Build Environment
Requires:       libKF6WidgetsAddons6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module.

%if %{with kde_python_bindings}
%package -n python3-kf6-kwidgetsaddons
Summary:        Python interface for kf6-kwidgetsaddons

%description -n python3-kf6-kwidgetsaddons
This package provides a python interface for kf6-kwidgetsaddons.
%endif

%lang_package -n libKF6WidgetsAddons6

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

%find_lang kwidgetsaddons6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6WidgetsAddons6

%files
%{_kf6_debugdir}/kwidgetsaddons.categories

%files -n libKF6WidgetsAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6WidgetsAddons.so.*

%files devel
%{_kf6_cmakedir}/KF6WidgetsAddons/
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_plugindir}/designer/kwidgetsaddons6widgets.so

%if %{with kde_python_bindings}
%files -n python3-kf6-kwidgetsaddons
%{mypython_sitearch}/*.so
%endif

%files -n libKF6WidgetsAddons6-lang -f kwidgetsaddons6.lang

%changelog
