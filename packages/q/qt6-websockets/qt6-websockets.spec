#
# spec file for package qt6-websockets
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
%define tar_name qtwebsockets-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-websockets%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 WebSockets library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-websockets-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-network-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt WebSockets module provides C++ and QML interfaces that enable
Qt applications to act as a server that can process WebSocket
requests, or a client that can consume data received from the server,
or both.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 WebSockets QML files and plugins

%description imports
QML files and plugins from the Qt 6 WebSockets module

%package -n libQt6WebSockets6
Summary:        Qt 6 WebSockets library

%description -n libQt6WebSockets6
The Qt WebSockets module provides C++ and QML interfaces that enable
Qt applications to act as a server that can process WebSocket
requests, or a client that can consume data received from the server,
or both.

%package devel
Summary:        Qt 6 WebSockets library - Development files
Requires:       libQt6WebSockets6 = %{version}
Requires:       cmake(Qt6Network)

%description devel
Development files for the Qt 6 WebSockets library

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 WebSockets library
Requires:       qt6-core-private-devel
Requires:       cmake(Qt6WebSockets) = %{real_version}

%description private-devel
This package provides private headers of libQt6WebSockets that do not have any
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

%post -n libQt6WebSockets6 -p /sbin/ldconfig
%postun -n libQt6WebSockets6 -p /sbin/ldconfig

%files imports
%{_qt6_qmldir}/QtWebSockets/

%files -n libQt6WebSockets6
%license LICENSES/*
%{_qt6_libdir}/libQt6WebSockets.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6WebSockets/
%{_qt6_descriptionsdir}/WebSockets.json
%{_qt6_includedir}/QtWebSockets/
%{_qt6_libdir}/libQt6WebSockets.prl
%{_qt6_libdir}/libQt6WebSockets.so
%{_qt6_metatypesdir}/qt6websockets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_websockets.pri
%{_qt6_pkgconfigdir}/Qt6WebSockets.pc
%exclude %{_qt6_includedir}/QtWebSockets/%{real_version}/

%files private-devel
%{_qt6_includedir}/QtWebSockets/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_websockets_private.pri

%endif

%changelog
