#
# spec file for package qt6-charts
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
%define short_name qtcharts
%define tar_name qtcharts-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-charts%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Charts library
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-charts-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Multimedia) = %{real_version}
BuildRequires:  cmake(Qt6OpenGL) = %{real_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
A collection of components that can be used to create charts.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Charts QML files and plugins

%description imports
QML files and plugins from the Qt 6 Charts module.

%package -n libQt6Charts6
Summary:        Qt 6 Charts library

%description -n libQt6Charts6
The Qt 6 Charts library.

%package devel
Summary:        Qt 6 Charts library - Development files
Requires:       libQt6Charts6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6OpenGLWidgets) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description devel
Development files for the Qt 6 Charts library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Charts Library
Requires:       cmake(Qt6Charts) = %{real_version}

%description private-devel
This package provides private headers of libQt6Charts that do not have any
ABI or API guarantees.

%package -n libQt6ChartsQml6
Summary:        Qt 6 ChartsQml library

%description -n libQt6ChartsQml6
The Qt 6 ChartsQml library.

%package -n qt6-chartsqml-devel
Summary:        Qt 6 ChartsQml library - Development files
Requires:       libQt6ChartsQml6 = %{version}
Requires:       cmake(Qt6Charts) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-chartsqml-devel
Development files for the Qt 6 ChartsQml library.

%package -n qt6-chartsqml-private-devel
Summary:        Non-ABI stable API for the Qt 6 ChartsQml Library
Requires:       cmake(Qt6ChartsQml) = %{real_version}

%description -n qt6-chartsqml-private-devel
This package provides private headers of libQt6ChartsQml that do not have any
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

%ldconfig_scriptlets -n libQt6Charts6
%ldconfig_scriptlets -n libQt6ChartsQml6

%files imports
%{_qt6_qmldir}/QtCharts/

%files -n libQt6Charts6
%license LICENSES/*
%{_qt6_libdir}/libQt6Charts.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Charts/
%{_qt6_descriptionsdir}/Charts.json
%{_qt6_includedir}/QtCharts/
%{_qt6_libdir}/libQt6Charts.prl
%{_qt6_libdir}/libQt6Charts.so
%{_qt6_metatypesdir}/qt6charts_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_charts.pri
%{_qt6_pkgconfigdir}/Qt6Charts.pc
%exclude %{_qt6_includedir}/QtCharts/%{real_version}

%files private-devel
%{_qt6_includedir}/QtCharts/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_charts_private.pri

%files -n libQt6ChartsQml6
%{_qt6_libdir}/libQt6ChartsQml.so.*

%files -n qt6-chartsqml-devel
%{_qt6_cmakedir}/Qt6ChartsQml/
%{_qt6_descriptionsdir}/ChartsQml.json
%{_qt6_includedir}/QtChartsQml/
%{_qt6_libdir}/libQt6ChartsQml.prl
%{_qt6_libdir}/libQt6ChartsQml.so
%{_qt6_metatypesdir}/qt6chartsqml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_chartsqml.pri
%{_qt6_pkgconfigdir}/Qt6ChartsQml.pc
%exclude %{_qt6_includedir}/QtChartsQml/%{real_version}

%files -n qt6-chartsqml-private-devel
%{_qt6_includedir}/QtChartsQml/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_chartsqml_private.pri

%endif

%changelog
