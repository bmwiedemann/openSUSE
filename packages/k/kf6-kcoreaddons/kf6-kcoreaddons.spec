#
# spec file for package kf6-kcoreaddons
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

%define rname kcoreaddons

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
Name:           kf6-kcoreaddons
Version:        6.21.0
Release:        0
Summary:        Utilities for core application functionality and accessing the OS
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
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
Requires:       shared-mime-info >= 1.8

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package imports
Summary:        QML imports for kcoreaddons

%description imports
QML imports for kcoreaddons.

%package -n libKF6CoreAddons6
Summary:        Utilities for core application functionality and accessing the OS
Requires:       kf6-kcoreaddons = %{version}

%description -n libKF6CoreAddons6
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package devel
Summary:        Utilities for core application functionality and accessing the OS
Requires:       libKF6CoreAddons6 = %{version}

%description devel
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more. Development files.

%if %{with kde_python_bindings}
%package -n python3-kf6-kcoreaddons
Summary:        Python bindings for kf6-kcoreaddons

%description -n python3-kf6-kcoreaddons
This package provides Python bindings for kf6-kcoreaddons.
%endif

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# ENABLE_PCH breaks the build locally with 'error: is pie differs in PCH file vs. current file'
%cmake_kf6 \
  -DENABLE_PCH:BOOL=FALSE \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kf6-kcoreaddons --all-name --with-qt --without-mo

%ldconfig_scriptlets -n libKF6CoreAddons6

%files
%{_kf6_appsdir}/mime/packages/kde6.xml
%{_kf6_debugdir}/kcoreaddons.categories
%{_kf6_debugdir}/kcoreaddons.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/coreaddons/

%files -n libKF6CoreAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6CoreAddons.so.*

%files devel
%{_kf6_includedir}/KCoreAddons/
%{_kf6_cmakedir}/KF6CoreAddons/
%dir %{_kf6_datadir}/jsonschema
%{_kf6_datadir}/jsonschema/kpluginmetadata.schema.json
%{_kf6_libdir}/libKF6CoreAddons.so
%{_kf6_pkgconfigdir}/KF6CoreAddons.pc
%if %{with kde_python_bindings}
%dir %{_includedir}/PySide6/
%{_includedir}/PySide6/KCoreAddons/
%endif


%if %{with kde_python_bindings}
%files -n python3-kf6-kcoreaddons
%{mypython_sitearch}/*.so
%{_kf6_sharedir}/PySide6/typesystems/typesystem_kcoreaddons.xml
%endif

%files lang -f kf6-kcoreaddons.lang

%changelog
