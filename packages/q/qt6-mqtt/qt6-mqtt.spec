#
# spec file for package qt6-mqtt
#
# Copyright (c) 2024 SUSE LLC
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
%define tar_name qtmqtt-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-mqtt%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Module to implement MQTT protocol version 3.1 and 3.1.1
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source0:        %{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-mqtt-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6WebSockets) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 Module to implement MQTT (Message Queuing Telemetry Transport) protocol
version 3.1 and 3.1.1 in Qt applications.

%if !%{qt6_docs_flavor}

%package -n libQt6Mqtt6
Summary:        Qt 6 MQTT library

%description -n libQt6Mqtt6
Qt library to implement MQTT protocol version 3.1 and 3.1.1

%package devel
Summary:        Qt 6 Mqtt library - Development files
Requires:       libQt6Mqtt6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}

%description devel
Development files for the Qt 6 Mqtt library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Mqtt library
Requires:       cmake(Qt6Mqtt) = %{real_version}

%description private-devel
This package provides private headers of libQt6Mqtt that do not have any
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

%fdupes %{buildroot}%{_qt6_includedir}

%ldconfig_scriptlets -n libQt6Mqtt6

%files -n libQt6Mqtt6
%license LICENSES/*
%{_qt6_libdir}/libQt6Mqtt.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Mqtt/
%{_qt6_descriptionsdir}/Mqtt.json
%{_qt6_includedir}/QtMqtt
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_metatypesdir}/qt6mqtt_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_mqtt.pri
%{_qt6_pkgconfigdir}/Qt6Mqtt.pc
%exclude %{_qt6_includedir}/QtMqtt/%{real_version}

%files private-devel
%{_qt6_includedir}/QtMqtt/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_mqtt_private.pri

%endif

%changelog
