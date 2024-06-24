#
# spec file for package qt6-sensors
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
%define short_name qtsensors
%define tar_name qtsensors-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-sensors%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt Sensors API to access sensor hardware
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-sensors-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6DBus) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  cmake(Qt6Xml) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%else
# boo#1188098
Requires:       (iio-sensor-proxy if systemd)
%endif

%description
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces. The Qt Sensors API also provides a motion gesture recognition API
for devices.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Sensors QML files and plugins

%description imports
QML files and plugins from the Qt 6 Sensors module

%package -n libQt6Sensors6
Summary:        Qt 6 Sensors library

%description -n libQt6Sensors6
The Qt 6 Sensors library.

%package devel
Summary:        Qt 6 Sensors library - Development files
Requires:       libQt6Sensors6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description devel
Development files for the Qt 6 Sensors library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Sensors library
Requires:       cmake(Qt6Sensors) = %{real_version}
%requires_eq    qt6-core-private-devel

%description private-devel
This package provides private headers of libQt6Sensors that do not have any
ABI or API guarantees.

%package -n libQt6SensorsQuick6
Summary:        Qt 6 SensorsQuick library

%description -n libQt6SensorsQuick6
The Qt6 SensorsQuick library.

%package -n qt6-sensorsquick-devel
Summary:        Qt 6 SensorsQuick library - Development files
Requires:       libQt6SensorsQuick6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Sensors) = %{real_version}

%description -n qt6-sensorsquick-devel
Development files for the Qt 6 SensorsQuick library.

%package -n qt6-sensorsquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 SensorsQuick library
Requires:       cmake(Qt6SensorsQuick) = %{real_version}

%description -n qt6-sensorsquick-private-devel
This package provides private headers of libQt6SensorsQuick that do not have any
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

%ldconfig_scriptlets -n libQt6Sensors6
%ldconfig_scriptlets -n libQt6SensorsQuick6

%files
%{_qt6_pluginsdir}/sensors/

%files imports
%{_qt6_qmldir}/QtSensors/

%files -n libQt6Sensors6
%license LICENSES/*
%{_qt6_libdir}/libQt6Sensors.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindSensorfw.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Sensors/
%{_qt6_descriptionsdir}/Sensors.json
%{_qt6_includedir}/QtSensors/
%{_qt6_libdir}/libQt6Sensors.prl
%{_qt6_libdir}/libQt6Sensors.so
%{_qt6_metatypesdir}/qt6sensors_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_sensors.pri
%{_qt6_pkgconfigdir}/Qt6Sensors.pc
%exclude %{_qt6_includedir}/QtSensors/%{real_version}

%files private-devel
%{_qt6_includedir}/QtSensors/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_sensors_private.pri

%files -n libQt6SensorsQuick6
%{_qt6_libdir}/libQt6SensorsQuick.so.*

%files -n qt6-sensorsquick-devel
%{_qt6_cmakedir}/Qt6SensorsQuick/
%{_qt6_descriptionsdir}/SensorsQuick.json
%{_qt6_includedir}/QtSensorsQuick/
%{_qt6_libdir}/libQt6SensorsQuick.prl
%{_qt6_libdir}/libQt6SensorsQuick.so
%{_qt6_metatypesdir}/qt6sensorsquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_sensorsquick.pri
%{_qt6_pkgconfigdir}/Qt6SensorsQuick.pc
%exclude %{_qt6_includedir}/QtSensorsQuick/%{real_version}

%files -n qt6-sensorsquick-private-devel
%{_qt6_includedir}/QtSensorsQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_sensorsquick_private.pri

%endif

%changelog
