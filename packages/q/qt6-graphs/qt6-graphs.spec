#
# spec file for package qt6-graphs
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
%define tar_name qtgraphs-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-graphs%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        3D visualization module
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick3d-private-devel
BuildRequires:  qt6-quick3druntimerender-private-devel
BuildRequires:  qt6-quickshapes-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6Quick3D) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6QuickWidgets) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt Graphs module enables you to visualize data in 3D as bar, scatter, and
surface graphs.
It's especially useful for visualizing depth maps and large quantities of
rapidly changing data, such as data received from multiple sensors.
The look and feel of graphs can be customized by using themes or by adding
custom items and labels

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Graphs QML files and plugins

%description imports
QML files and plugins from the Qt 6 Graphs module

%package -n libQt6Graphs6
Summary:        Qt 6 Graphs library

%description -n libQt6Graphs6
The Qt Graphs module enables you to visualize data in 3D as bar, scatter, and
surface graphs.
It's especially useful for visualizing depth maps and large quantities of
rapidly changing data, such as data received from multiple sensors.
The look and feel of graphs can be customized by using themes or by adding
custom items and labels

%package -n qt6-graphs-devel
Summary:        Qt 6 Graphs library - Development files
Requires:       libQt6Graphs6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6Quick3D) = %{real_version}
Requires:       cmake(Qt6Quick3DRuntimeRender) = %{real_version}
Requires:       cmake(Qt6QuickWidgets) = %{real_version}

%description -n qt6-graphs-devel
Development files for the Qt 6 Graphs library.

%package -n qt6-graphs-private-devel
Summary:        Non-ABI stable API for the Qt 6 Graphs Library
Requires:       cmake(Qt6Graphs) = %{real_version}
%requires_eq    qt6-quick3d-private-devel
%requires_eq    qt6-quick3druntimerender-private-devel

%description -n qt6-graphs-private-devel
This package provides private headers of libQt6Graphs that do not have any
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

%ldconfig_scriptlets -n libQt6Graphs6

%files imports
%{_qt6_qmldir}/QtGraphs/

%files -n libQt6Graphs6
%license LICENSES/*
%{_qt6_libdir}/libQt6Graphs.so.*

%files -n qt6-graphs-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtGraphsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Graphs/
%{_qt6_descriptionsdir}/Graphs.json
%{_qt6_includedir}/QtGraphs/
%{_qt6_libdir}/libQt6Graphs.prl
%{_qt6_libdir}/libQt6Graphs.so
%{_qt6_metatypesdir}/qt6graphs_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_graphs.pri
%{_qt6_pkgconfigdir}/Qt6Graphs.pc
%exclude %{_qt6_includedir}/QtGraphs/%{real_version}

%files -n qt6-graphs-private-devel
%{_qt6_includedir}/QtGraphs/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_graphs_private.pri

%endif

%changelog
