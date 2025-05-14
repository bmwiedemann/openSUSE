#
# spec file for package kf6-kunitconversion
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


%define qt6_version 6.7.0

%define rname kunitconversion

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

# Full KF6 version (e.g. 6.14.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kunitconversion
Version:        6.14.0
Release:        0
Summary:        Tool for converting physical units
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
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
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
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

%package -n libKF6UnitConversion6
Summary:        Converting physical units
Requires:       kf6-kunitconversion >= %{version}

%description -n libKF6UnitConversion6
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

%package devel
Summary:        Converting physical units: Build Environment
Requires:       libKF6UnitConversion6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).
Development files.

%if %{with kde_python_bindings}
%package -n python3-kf6-kunitconversion
Summary:        Python interface for kf6-kunitconversion

%description -n python3-kf6-kunitconversion
This package provides a python interface for kf6-kunitconversion.
%endif

%lang_package -n libKF6UnitConversion6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_QCH:BOOL=TRUE \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kunitconversion6

%ldconfig_scriptlets -n libKF6UnitConversion6

%files
%{_kf6_debugdir}/kunitconversion.categories

%files -n libKF6UnitConversion6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6UnitConversion.so.*

%files devel
%doc %{_kf6_qchdir}/KF6UnitConversion.*
%{_kf6_includedir}/KUnitConversion/
%{_kf6_cmakedir}/KF6UnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so

%if %{with kde_python_bindings}
%files -n python3-kf6-kunitconversion
%{mypython_sitearch}/*.so
%endif

%files -n libKF6UnitConversion6-lang -f kunitconversion6.lang

%changelog
