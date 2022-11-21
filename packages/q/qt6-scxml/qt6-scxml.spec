#
# spec file for package qt6-scxml
#
# Copyright (c) 2022 SUSE LLC
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


%define real_version 6.4.1
%define short_version 6.4
%define short_name qtscxml
%define tar_name qtscxml-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-scxml%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        SCXML (state machine notation) compiler and related tools
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-scxml-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt SCXML module provides functionality to create state machines from SCXML
files.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Scxml QML files and plugins

%description imports
QML files and plugins from the Qt 6 Scxml module

%package -n libQt6Scxml6
Summary:        Qt 6 Scxml library

%description -n libQt6Scxml6
The Qt 6 Scxml library.

%package devel
Summary:        Qt 6 Scxml library - Development files
# ScxmlTools requires the scxmlc executable
Requires:       %{name} = %{version}
Requires:       libQt6Scxml6 = %{version}
Requires:       cmake(Qt6Core)

%description devel
Development files for the Qt 6 Scxml library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Scxml library
Requires:       cmake(Qt6Scxml) = %{real_version}
%requires_eq    qt6-qml-private-devel

%description private-devel
This package provides private headers of libQt6Scxml that do not have any
ABI or API guarantees.

%package -n libQt6ScxmlQml6
Summary:        Qt 6 ScxmlQml library

%description -n libQt6ScxmlQml6
The Qt6 ScxmlQml library.

%package -n qt6-scxmlqml-devel
Summary:        Qt 6 ScxmlQml library - Development files
Requires:       libQt6ScxmlQml6 = %{version}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Scxml) = %{real_version}

%description -n qt6-scxmlqml-devel
Development files for the Qt 6 ScxmlQml library.

%package -n qt6-scxmlqml-private-devel
Summary:        Non-ABI stable API for the Qt 6 ScxmlQml library
Requires:       cmake(Qt6ScxmlQml) = %{real_version}

%description -n qt6-scxmlqml-private-devel
This package provides private headers of libQt6ScxmlQml that do not have any
ABI or API guarantees.

%package -n libQt6StateMachine6
Summary:        Qt 6 StateMachine library

%description -n libQt6StateMachine6
The Qt 6 StateMachine library.

%package -n qt6-statemachine-devel
Summary:        Qt 6 StateMachine library - Development files
Requires:       libQt6StateMachine6 = %{version}
Requires:       cmake(Qt6Gui)

%description -n qt6-statemachine-devel
Development files for the Qt 6 StateMachine library.

%package -n qt6-statemachine-private-devel
Summary:        Non-ABI stable API for the Qt 6 StateMachine library
Requires:       cmake(Qt6StateMachine) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description -n qt6-statemachine-private-devel
This package provides private headers of libQt6StateMachine that do not have any
ABI or API guarantees.

%package -n libQt6StateMachineQml6
Summary:        Qt 6 StateMachineQml library

%description -n libQt6StateMachineQml6
The Qt 6 StateMachineQml library.

%package -n qt6-statemachineqml-devel
Summary:        Qt 6 StateMachineQml library - Development files
Requires:       libQt6StateMachineQml6 = %{version}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6StateMachine)

%description -n qt6-statemachineqml-devel
Development files for the Qt 6 StateMachineQml library.

%package -n qt6-statemachineqml-private-devel
Summary:        Non-ABI stable API for the Qt 6 StateMachineQml library
Requires:       cmake(Qt6StateMachineQml) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description -n qt6-statemachineqml-private-devel
This package provides private headers of libQt6StateMachineQml that do not have any
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
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{Config,ConfigVersion,Targets*}.cmake

%post -n libQt6Scxml6 -p /sbin/ldconfig
%post -n libQt6ScxmlQml6 -p /sbin/ldconfig
%post -n libQt6StateMachine6 -p /sbin/ldconfig
%post -n libQt6StateMachineQml6 -p /sbin/ldconfig
%postun -n libQt6Scxml6 -p /sbin/ldconfig
%postun -n libQt6ScxmlQml6 -p /sbin/ldconfig
%postun -n libQt6StateMachine6 -p /sbin/ldconfig
%postun -n libQt6StateMachineQml6 -p /sbin/ldconfig

%files
%dir %{_qt6_pluginsdir}/scxmldatamodel/
%{_qt6_libexecdir}/qscxmlc
%{_qt6_pluginsdir}/scxmldatamodel/libqscxmlecmascriptdatamodel.so

%files imports
%dir %{_qt6_qmldir}/QtQml
%{_qt6_qmldir}/QtQml/StateMachine/
%{_qt6_qmldir}/QtScxml/

%files -n libQt6Scxml6
%license LICENSES/*
%{_qt6_libdir}/libQt6Scxml.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtScxmlTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Scxml/
%{_qt6_cmakedir}/Qt6ScxmlTools/
%{_qt6_descriptionsdir}/Scxml.json
%{_qt6_includedir}/QtScxml/
%{_qt6_libdir}/libQt6Scxml.prl
%{_qt6_libdir}/libQt6Scxml.so
%{_qt6_metatypesdir}/qt6scxml_*_metatypes.json
%{_qt6_mkspecsdir}/features/qscxmlc.prf
%{_qt6_mkspecsdir}/modules/qt_lib_scxml.pri
%{_qt6_pkgconfigdir}/Qt6Scxml.pc
%exclude %{_qt6_includedir}/QtScxml/%{real_version}

%files private-devel
%{_qt6_includedir}/QtScxml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_scxml_private.pri

%files -n libQt6ScxmlQml6
%{_qt6_libdir}/libQt6ScxmlQml.so.*

%files -n qt6-scxmlqml-devel
%{_qt6_cmakedir}/Qt6ScxmlQml/
%{_qt6_descriptionsdir}/ScxmlQml.json
%{_qt6_includedir}/QtScxmlQml/
%{_qt6_libdir}/libQt6ScxmlQml.prl
%{_qt6_libdir}/libQt6ScxmlQml.so
%{_qt6_metatypesdir}/qt6scxmlqml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_scxmlqml.pri
%{_qt6_pkgconfigdir}/Qt6ScxmlQml.pc
%exclude %{_qt6_includedir}/QtScxmlQml/%{real_version}

%files -n qt6-scxmlqml-private-devel
%{_qt6_includedir}/QtScxmlQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_scxmlqml_private.pri

%files -n libQt6StateMachine6
%{_qt6_libdir}/libQt6StateMachine.so.*

%files -n qt6-statemachine-devel
%{_qt6_cmakedir}/Qt6StateMachine/
%{_qt6_descriptionsdir}/StateMachine.json
%{_qt6_includedir}/QtStateMachine/
%{_qt6_libdir}/libQt6StateMachine.prl
%{_qt6_libdir}/libQt6StateMachine.so
%{_qt6_metatypesdir}/qt6statemachine_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_statemachine.pri
%{_qt6_pkgconfigdir}/Qt6StateMachine.pc
%exclude %{_qt6_includedir}/QtStateMachine/%{real_version}

%files -n qt6-statemachine-private-devel
%{_qt6_includedir}/QtStateMachine/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_statemachine_private.pri

%files -n libQt6StateMachineQml6
%{_qt6_libdir}/libQt6StateMachineQml.so.*

%files -n qt6-statemachineqml-devel
%{_qt6_cmakedir}/Qt6StateMachineQml/
%{_qt6_descriptionsdir}/StateMachineQml.json
%{_qt6_includedir}/QtStateMachineQml/
%{_qt6_libdir}/libQt6StateMachineQml.prl
%{_qt6_libdir}/libQt6StateMachineQml.so
%{_qt6_metatypesdir}/qt6statemachineqml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_statemachineqml.pri
%{_qt6_pkgconfigdir}/Qt6StateMachineQml.pc
%exclude %{_qt6_includedir}/QtStateMachineQml/%{real_version}

%files -n qt6-statemachineqml-private-devel
%{_qt6_includedir}/QtStateMachineQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_statemachineqml_private.pri

%endif

%changelog
