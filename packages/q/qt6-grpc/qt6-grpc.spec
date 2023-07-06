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


%define real_version 6.5.1
%define short_version 6.5
%define short_name qtgrpc
%define tar_name qtgrpc-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-grpc%{?pkg_suffix}
Version:        6.5.1
Release:        0
Summary:        gRPC and Protobuf generator and bindings for Qt framework
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-include-of-std-set.patch
Patch1:         0002-Remove-protobuf-logging.h-include.patch
Patch2:         0003-Add-missing-memory-include.patch
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickControls2) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  pkgconfig(libprotobuf-c)
# qtgrpc is not compatible with protobuf 23 and protobuf-c is not compatible with 22 either
BuildRequires:  pkgconfig(protobuf) < 22
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

%ldconfig_scriptlets -n libQt6Grpc6
%ldconfig_scriptlets -n libQt6Protobuf6

%files -n libQt6Grpc6
%license LICENSES/*
%{_qt6_libdir}/libQt6Grpc.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindWrapgRPC.cmake
%{_qt6_cmakedir}/Qt6/FindWrapgRPCPlugin.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Grpc/
%{_qt6_cmakedir}/Qt6GrpcTools/
%{_qt6_descriptionsdir}/Grpc.json
%{_qt6_includedir}/QtGrpc/
%{_qt6_libdir}/libQt6Grpc.prl
%{_qt6_libdir}/libQt6Grpc.so
%{_qt6_libexecdir}/qtgrpcgen
%{_qt6_metatypesdir}/qt6grpc_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_grpc.pri
%{_qt6_pkgconfigdir}/Qt6Grpc.pc
%exclude %{_qt6_includedir}/QtGrpc/%{real_version}

%files private-devel
%{_qt6_includedir}/QtGrpc/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_grpc_private.pri

%files -n libQt6Protobuf6
%license LICENSES/*
%{_qt6_libdir}/libQt6Protobuf.so.*

%files -n qt6-protobuf-devel
%{_qt6_cmakedir}/Qt6/FindWrapProtobuf.cmake
%{_qt6_cmakedir}/Qt6/FindWrapProtoc.cmake
%{_qt6_cmakedir}/Qt6Protobuf/
%{_qt6_cmakedir}/Qt6ProtobufTools/
%{_qt6_descriptionsdir}/Protobuf.json
%{_qt6_includedir}/QtProtobuf/
%{_qt6_libdir}/libQt6Protobuf.prl
%{_qt6_libdir}/libQt6Protobuf.so
%{_qt6_libexecdir}/qtprotobufgen
%{_qt6_metatypesdir}/qt6protobuf_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_protobuf.pri
%{_qt6_pkgconfigdir}/Qt6Protobuf.pc
%exclude %{_qt6_includedir}/QtProtobuf/%{real_version}

%files -n qt6-protobuf-private-devel
%{_qt6_includedir}/QtProtobuf/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_protobuf_private.pri

%endif

%changelog
