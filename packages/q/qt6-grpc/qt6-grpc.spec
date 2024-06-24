#
# spec file for package qt6-grpc
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
%define short_name qtgrpc
%define tar_name qtgrpc-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
# protobuf and absl packages in Leap 15.5 are incompatible, qtgrpcgen and
# protobuf types libraries can't be built (https://bugzilla.suse.com/show_bug.cgi?id=1222343)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150500
%define with_usable_protobuf 1
%else
%define with_usable_protobuf 0
%endif

Name:           qt6-grpc%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        gRPC and Protobuf generator and bindings for Qt framework
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel = %{version}
BuildRequires:  qt6-network-private-devel = %{version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6QmlNetwork) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickControls2) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(protobuf)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
gRPC and Protobuf generator and bindings for Qt framework.

%if !%{qt6_docs_flavor}
%package -n libQt6Grpc6
Summary:        Qt 6 Grpc library

%description -n libQt6Grpc6
The Qt 6 Grpc library.

%package devel
Summary:        Qt 6 Grpc library - Development files
Requires:       libQt6Grpc6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6Protobuf) = %{real_version}
Requires:       pkgconfig(grpc++)

%description devel
Development files for the Qt 6 Grpc library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Grpc Library
Requires:       cmake(Qt6Grpc) = %{real_version}

%description private-devel
This package provides private headers of libQt6Grpc that do not have any
ABI or API guarantees.

%package imports
Summary:        Qt 6 Grpc QML files and plugins

%description imports
QML files and plugins from the Qt 6 Grpc module.

%package -n libQt6Protobuf6
Summary:        Qt 6 Protobuf library

%description -n libQt6Protobuf6
The Qt 6 Protobuf library.

%package -n qt6-protobuf-devel
Summary:        Qt 6 Protobuf library - Development files
Requires:       libQt6Protobuf6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       pkgconfig(protobuf)

%description -n qt6-protobuf-devel
Development files for the Qt 6 Protobuf library.

%package -n qt6-protobuf-private-devel
Summary:        Non-ABI stable API for the Qt 6 Protobuf Library
Requires:       cmake(Qt6Protobuf) = %{real_version}

%description -n qt6-protobuf-private-devel
This package provides private headers of libQt6Protobuf that do not have any
ABI or API guarantees.

%if %{with_usable_protobuf}
%{qt6_examples_package}
%endif

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

%ldconfig_scriptlets -n libQt6Grpc6
%ldconfig_scriptlets -n libQt6Protobuf6

%files imports
%{_qt6_qmldir}/QtGrpc/

%files -n libQt6Grpc6
%license LICENSES/*
%{_qt6_libdir}/libQt6Grpc.so.*
%{_qt6_libdir}/libQt6GrpcQuick.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapgRPC.cmake
%{_qt6_cmakedir}/Qt6/FindWrapgRPCPlugin.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Grpc/
%{_qt6_cmakedir}/Qt6GrpcQuick/
%if %{with_usable_protobuf}
%{_qt6_cmakedir}/Qt6GrpcTools/
%endif
%{_qt6_descriptionsdir}/Grpc.json
%{_qt6_descriptionsdir}/GrpcQuick.json
%{_qt6_includedir}/QtGrpc/
%{_qt6_includedir}/QtGrpcQuick/
%{_qt6_libdir}/libQt6Grpc.prl
%{_qt6_libdir}/libQt6Grpc.so
%{_qt6_libdir}/libQt6GrpcQuick.prl
%{_qt6_libdir}/libQt6GrpcQuick.so
%if %{with_usable_protobuf}
%{_qt6_libexecdir}/qtgrpcgen
%endif
%{_qt6_metatypesdir}/qt6grpc_*_metatypes.json
%{_qt6_metatypesdir}/qt6grpcquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_grpc.pri
%{_qt6_mkspecsdir}/modules/qt_lib_grpcquick.pri
%{_qt6_pkgconfigdir}/Qt6Grpc.pc
%{_qt6_pkgconfigdir}/Qt6GrpcQuick.pc
%exclude %{_qt6_includedir}/QtGrpc/%{real_version}
%exclude %{_qt6_includedir}/QtGrpcQuick/%{real_version}

%files private-devel
%{_qt6_includedir}/QtGrpc/%{real_version}
%{_qt6_includedir}/QtGrpcQuick/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_grpc_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_grpcquick_private.pri

%files -n libQt6Protobuf6
%license LICENSES/*
%{_qt6_libdir}/libQt6Protobuf.so.*
%if %{with_usable_protobuf}
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so.*
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so.*
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so.*
%endif

%files -n qt6-protobuf-devel
%{_qt6_cmakedir}/Qt6/FindWrapProtobuf.cmake
%{_qt6_cmakedir}/Qt6/FindWrapProtoc.cmake
%{_qt6_cmakedir}/Qt6Protobuf/
%if %{with_usable_protobuf}
%{_qt6_cmakedir}/Qt6ProtobufQtCoreTypes/
%{_qt6_cmakedir}/Qt6ProtobufQtGuiTypes/
%{_qt6_cmakedir}/Qt6ProtobufWellKnownTypes/
%{_qt6_cmakedir}/Qt6ProtobufTools/
%endif
%{_qt6_descriptionsdir}/Protobuf.json
%if %{with_usable_protobuf}
%{_qt6_descriptionsdir}/ProtobufQtCoreTypes.json
%{_qt6_descriptionsdir}/ProtobufQtGuiTypes.json
%{_qt6_descriptionsdir}/ProtobufWellKnownTypes.json
%endif
%{_qt6_includedir}/QtProtobuf/
%if %{with_usable_protobuf}
%{_qt6_includedir}/QtProtobufQtCoreTypes/
%{_qt6_includedir}/QtProtobufQtGuiTypes/
%{_qt6_includedir}/QtProtobufWellKnownTypes/
%endif
%{_qt6_libdir}/libQt6Protobuf.prl
%{_qt6_libdir}/libQt6Protobuf.so
%if %{with_usable_protobuf}
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.prl
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so
%{_qt6_libexecdir}/qtprotobufgen
%endif
%{_qt6_metatypesdir}/qt6protobuf_*_metatypes.json
%if %{with_usable_protobuf}
%{_qt6_metatypesdir}/qt6protobufqtcoretypes_*_metatypes.json
%{_qt6_metatypesdir}/qt6protobufqtguitypes_*_metatypes.json
%{_qt6_metatypesdir}/qt6protobufwellknowntypes_*_metatypes.json
%endif
%{_qt6_mkspecsdir}/modules/qt_lib_protobuf.pri
%if %{with_usable_protobuf}
%{_qt6_mkspecsdir}/modules/qt_lib_protobufqtcoretypes.pri
%{_qt6_mkspecsdir}/modules/qt_lib_protobufqtguitypes.pri
%{_qt6_mkspecsdir}/modules/qt_lib_protobufwellknowntypes.pri
%endif
%{_qt6_pkgconfigdir}/Qt6Protobuf.pc
%if %{with_usable_protobuf}
%{_qt6_pkgconfigdir}/Qt6ProtobufQtCoreTypes.pc
%{_qt6_pkgconfigdir}/Qt6ProtobufQtGuiTypes.pc
%{_qt6_pkgconfigdir}/Qt6ProtobufWellKnownTypes.pc
%endif
%exclude %{_qt6_includedir}/QtProtobuf/%{real_version}

%files -n qt6-protobuf-private-devel
%{_qt6_includedir}/QtProtobuf/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_protobuf_private.pri
%if %{with_usable_protobuf}
%{_qt6_mkspecsdir}/modules/qt_lib_protobufqtcoretypes_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_protobufqtguitypes_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_protobufwellknowntypes_private.pri
%endif

%endif

%changelog
