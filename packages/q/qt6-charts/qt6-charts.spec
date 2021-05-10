#
# spec file for package qt6-charts
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
Version:        6.1.0
Release:        0
Summary:        Qt 6 Charts library
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
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
%requires_eq     qt6-core-private-devel

%description devel
Development files for the Qt 6 Charts library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Charts Library
Requires:       cmake(Qt6Charts) = %{real_version}

%description private-devel
This package provides private headers of libQt6Charts that do not have any
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

%post -n libQt6Charts6 -p /sbin/ldconfig
%postun -n libQt6Charts6 -p /sbin/ldconfig

%files imports
%{_qt6_qmldir}/QtCharts/

%files -n libQt6Charts6
%license LICENSE.*
%{_qt6_libdir}/libQt6Charts.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Charts/
%{_qt6_descriptionsdir}/Charts.json
%{_qt6_includedir}/QtCharts/
%{_qt6_libdir}/libQt6Charts.prl
%{_qt6_libdir}/libQt6Charts.so
%{_qt6_mkspecsdir}/modules/qt_lib_charts.pri
%exclude %{_qt6_includedir}/QtCharts/%{real_version}

%files private-devel
%{_qt6_includedir}/QtCharts/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_charts_private.pri

%endif

%changelog
