#
# spec file for package qt6-qt5compat
#
# Copyright (c) 2023 SUSE LLC
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


%define real_version 6.7.2
%define short_version 6.7
%define tar_name qt5compat-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-qt5compat%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Unsupported Qt 5 APIs for Qt 6
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-qt5compat-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-shadertools-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6Xml) = %{real_version}
BuildRequires:  pkgconfig(icu-i18n)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt 6 Compat library provides unsupported Qt 5 APIs which can be useful
while porting Qt 5 code.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Core 5 Compat QML files and plugins

%description imports
QML files and plugins from the Qt 6 Core5Compat module.
This package shall be used while porting away from qtgraphicaleffects.

%package -n libQt6Core5Compat6
Summary:        Qt 6 Core 5 Compat library

%description -n libQt6Core5Compat6
The Qt 6 Core 5 Compat library

%package devel
Summary:        Qt 6 Core 5 Compat library - Development files
Requires:       libQt6Core5Compat6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description devel
Development files for the Qt 6 Core 5 Compat library

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Qt5 Compat library
Requires:       cmake(Qt6Core5Compat) = %{real_version}
%requires_eq    qt6-core-private-devel

%description private-devel
This package provides private headers of libQt6Core5Compat that do not have any
ABI or API guarantees.

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%fdupes %{buildroot}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%ldconfig_scriptlets -n libQt6Core5Compat6

%files imports
%{_qt6_qmldir}/Qt5Compat/

%files -n libQt6Core5Compat6
%license LICENSES/*
%{_qt6_libdir}/libQt6Core5Compat.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapIconv.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/Qt5CompatTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Core5Compat/
%{_qt6_descriptionsdir}/Core5Compat.json
%{_qt6_includedir}/QtCore5Compat/
%{_qt6_libdir}/libQt6Core5Compat.prl
%{_qt6_libdir}/libQt6Core5Compat.so
%{_qt6_metatypesdir}/qt6core5compat_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_core5compat.pri
%{_qt6_pkgconfigdir}/Qt6Core5Compat.pc
%exclude %{_qt6_includedir}/QtCore5Compat/%{real_version}

%files private-devel
%{_qt6_includedir}/QtCore5Compat/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_core5compat_private.pri

%endif

%changelog
