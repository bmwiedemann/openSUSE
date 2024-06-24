#
# spec file for package qt6-httpserver
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
%define tar_name qthttpserver-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-httpserver%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt HTTP Server
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-network-private-devel
BuildRequires:  qt6-websockets-private-devel
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6WebSockets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
QHttpServer is a simplified API for QAbstractHttpServer and QHttpServerRouter

%if !%{qt6_docs_flavor}

%package -n libQt6HttpServer6
Summary:        Qt 6 HttpServer library

%description -n libQt6HttpServer6
QHttpServer is a simplified API for QAbstractHttpServer and QHttpServerRouter.

%package -n qt6-httpserver-devel
Summary:        Qt 6 HttpServer library - Development files
Requires:       libQt6HttpServer6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6WebSockets) = %{real_version}

%description -n qt6-httpserver-devel
Development files for the Qt 6 HttpServer library.

%package -n qt6-httpserver-private-devel
Summary:        Non-ABI stable API for the Qt 6 HttpServer Library
Requires:       cmake(Qt6HttpServer) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-network-private-devel
%requires_eq    qt6-websockets-private-devel

%description -n qt6-httpserver-private-devel
This package provides private headers of libQt6HttpServer that do not have any
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

%ldconfig_scriptlets -n libQt6HttpServer6

%files -n libQt6HttpServer6
%license LICENSES/*
%{_qt6_libdir}/libQt6HttpServer.so.*

%files -n qt6-httpserver-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtHttpServerTestsConfig.cmake
%{_qt6_cmakedir}/Qt6HttpServer/
%{_qt6_descriptionsdir}/HttpServer.json
%{_qt6_includedir}/QtHttpServer/
%{_qt6_libdir}/libQt6HttpServer.prl
%{_qt6_libdir}/libQt6HttpServer.so
%{_qt6_metatypesdir}/qt6httpserver_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_httpserver.pri
%{_qt6_pkgconfigdir}/Qt6HttpServer.pc
%exclude %{_qt6_includedir}/QtHttpServer/%{real_version}

%files -n qt6-httpserver-private-devel
%{_qt6_includedir}/QtHttpServer/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_httpserver_private.pri

%endif

%changelog
