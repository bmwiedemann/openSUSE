#
# spec file for package qt6-opcua
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
%define tar_name qtopcua-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-opcua%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt wrapper for existing OPC UA stacks
# src/plugins/opcua is GPL-3.0-or-later, rest is dual licensed
# only exception is the open62541 folder which is MPL-2.0
License:        (GPL-2.0-or-later OR LGPL-3.0-only) AND GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        %{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-opcua-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-network-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(openssl)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt API to interact with OPC UA (Open Platform Communications Unified
Architecture) on top of a 3rd party OPC UA stack.

%if !%{qt6_docs_flavor}

%package -n libQt6OpcUa6
Summary:        Qt 6 OpcUa Client Library
Recommends:     qt6-opcua = %{version}
Recommends:     qt6-opcua-imports = %{version}

%description -n libQt6OpcUa6
Qt 6 OpcUa Client Library.

%package devel
Summary:        Qt 6 OpcUa library - Development files
Requires:       libQt6OpcUa6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}

%description devel
Development files for the Qt 6 OpcUa library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 OpcUa library
Requires:       cmake(Qt6OpcUa) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-network-private-devel

%description private-devel
This package provides private headers of libQt6Opcua that do not have any
ABI or API guarantees.

%package imports
Summary:        Qt 6 OpcUa QML files and plugins
Requires:       qt6-opcua = %{version}

%description imports
QML files and plugins from the Qt 6 OpcUa module.

%package -n libQt6DeclarativeOpcua6
Summary:        Qt 6 DeclarativeOpcua library

%description -n libQt6DeclarativeOpcua6
Qt 6 DeclarativeOpcua library.

%package -n qt6-declarativeopcua-private-devel
Summary:        Non-ABI stable API for the Qt 6 DeclarativeOpcua library
Requires:       libQt6DeclarativeOpcua6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6OpcUa) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-declarativeopcua-private-devel
This package provides private headers of libDeclarativeOpcua that do not have
any ABI or API guarantees.

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

%ldconfig_scriptlets -n libQt6DeclarativeOpcua6
%ldconfig_scriptlets -n libQt6OpcUa6

%files
%dir %{_qt6_pluginsdir}/opcua
%{_qt6_pluginsdir}/opcua/libopen62541_backend.so

%files -n libQt6OpcUa6
%license LICENSES/*
%{_qt6_libdir}/libQt6OpcUa.so.*

%files devel
%{_qt6_bindir}/qopcuaxmldatatypes2cpp
%{_qt6_cmakedir}/Qt6/FindOpen62541.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtOpcUaTestsConfig.cmake
%{_qt6_cmakedir}/Qt6OpcUa/
%{_qt6_cmakedir}/Qt6QtOpcUaTools/
%{_qt6_descriptionsdir}/OpcUa.json
%{_qt6_includedir}/QtOpcUa
%{_qt6_libdir}/libQt6OpcUa.prl
%{_qt6_libdir}/libQt6OpcUa.so
%{_qt6_metatypesdir}/qt6opcua_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_opcua.pri
%{_qt6_pkgconfigdir}/Qt6OpcUa.pc
%exclude %{_qt6_includedir}/QtOpcUa/%{real_version}

%files private-devel
%{_qt6_includedir}/QtOpcUa/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_opcua_private.pri

%files imports
%{_qt6_qmldir}/QtOpcUa/

%files -n libQt6DeclarativeOpcua6
%{_qt6_libdir}/libQt6DeclarativeOpcua.so.*

%files -n qt6-declarativeopcua-private-devel
%{_qt6_cmakedir}/Qt6DeclarativeOpcua/
%{_qt6_descriptionsdir}/DeclarativeOpcua.json
%{_qt6_includedir}/QtDeclarativeOpcua/
%{_qt6_libdir}/libQt6DeclarativeOpcua.prl
%{_qt6_libdir}/libQt6DeclarativeOpcua.so
%{_qt6_metatypesdir}/qt6declarativeopcua_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_declarativeopcua.pri
%{_qt6_mkspecsdir}/modules/qt_lib_declarativeopcua_private.pri
%{_qt6_pkgconfigdir}/Qt6DeclarativeOpcua.pc

%endif

%changelog
