#
# spec file for package qt6-datavis3d
#
# Copyright (c) 2020 SUSE LLC
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


%define real_version 6.1.0
%define short_version 6.1
%define short_name qtdatavis3d
%define tar_name qtdatavis3d-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-datavis3d%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Qt 6 data visualization framework 
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-datavis3d-rpmlintrc
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Data Visualization module provides multiple graph types to visualize data
in 3D space both with C++ and Qt Quick 2.

%if !%{qt6_docs_flavor}

%package -n qt6-datavisualization-imports
Summary:        Qt 6 DataVisualization QML files and plugins

%description -n qt6-datavisualization-imports
QML files and plugins from the Qt 6 DataVisualization module.

%package -n libQt6DataVisualization6
Summary:        Qt 6 DataVisualization library

%description -n libQt6DataVisualization6
The Qt 6 DataVisualization library.

%package -n qt6-datavisualization-devel
Summary:        Qt 6 DataVisualization library - Development files
Requires:       libQt6DataVisualization6 = %{version}

%description -n qt6-datavisualization-devel
Development files for the Qt 6 DataVisualization library.

%package -n qt6-datavisualization-private-devel
Summary:        Non-ABI stable API for the Qt 6 DataVisualization Library
Requires:       cmake(Qt6DataVisualization) = %{real_version}

%description -n qt6-datavisualization-private-devel
This package provides private headers of libQt6DataVisualization that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt6DataVisualization6 -p /sbin/ldconfig
%postun -n libQt6DataVisualization6 -p /sbin/ldconfig

%files -n qt6-datavisualization-imports
%{_qt6_qmldir}/QtDataVisualization/

%files -n libQt6DataVisualization6
%license LICENSE.*
%{_qt6_libdir}/libQt6DataVisualization.so.*

%files -n qt6-datavisualization-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtDataVisualizationTestsConfig.cmake
%{_qt6_cmakedir}/Qt6DataVisualization/
%{_qt6_descriptionsdir}/DataVisualization.json
%{_qt6_includedir}/QtDataVisualization/
%{_qt6_libdir}/libQt6DataVisualization.prl
%{_qt6_libdir}/libQt6DataVisualization.so
%{_qt6_mkspecsdir}/modules/qt_lib_datavisualization.pri
%exclude %{_qt6_includedir}/QtDataVisualization/%{real_version}

%files -n qt6-datavisualization-private-devel
%{_qt6_includedir}/QtDataVisualization/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_datavisualization_private.pri

%endif

%changelog
