#
# spec file for package qt6-remoteobjects
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
%define tar_name qtremoteobjects-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-remoteobjects%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt6 RemoteObjects Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-remoteobjects-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Bluetooth) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
module to enable information exchange between processes or computers.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 RemoteObjects QML files

%description imports
QML files and plugins for the Qt 6 RemoteObjects module

%package -n libQt6RemoteObjects6
Summary:        Qt 6 RemoteObjects library

%description -n libQt6RemoteObjects6
The Qt 6 RemoteObjects library.

%package devel
Summary:        Qt 6 RemoteObjects library - Development files
Requires:       libQt6RemoteObjects6 = %{version}
Requires:       qt6-remoteobjects-tools = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}

%description devel
Development files for the Qt 6 RemoteObjects library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 RemoteObjects library
Requires:       cmake(Qt6RemoteObjects) = %{real_version}
%requires_eq    qt6-core-private-devel

%description private-devel
This package provides private headers of libQt6RemoteObjects that do not have
any ABI or API guarantees.

%package -n libQt6RemoteObjectsQml6
Summary:        Qt 6 RemoteObjectsQml library

%description -n libQt6RemoteObjectsQml6
The Qt 6 RemoteObjectsQml library.

%package -n qt6-remoteobjectsqml-devel
Summary:        Qt 6 RemoteObjectsQml library - Development files
Requires:       libQt6RemoteObjectsQml6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6RemoteObjects) = %{real_version}

%description -n qt6-remoteobjectsqml-devel
Development files for the Qt 6 RemoteObjectsQml library.

%package -n qt6-remoteobjectsqml-private-devel
Summary:        Non-ABI stable API for the Qt 6 RemoteObjectsQml library
Requires:       cmake(Qt6RemoteObjectsQml) = %{real_version}

%description -n qt6-remoteobjectsqml-private-devel
This package provides private headers of libQt6RemoteObjectsQml that do not have
any ABI or API guarantees.

%package tools
Summary:        Qt 6 RemoteObjects Tools

%description tools
This package contains REPC, a compiler for Qt RemoteObjects API definition files.

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

# repparser has no private headers
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_repparser_private.pri

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

# Unneeded?
rm -r %{buildroot}%{_qt6_mkspecsdir}/features
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6RepParser
rm %{buildroot}%{_qt6_pkgconfigdir}/Qt6RepParser.pc

%ldconfig_scriptlets -n libQt6RemoteObjects6
%ldconfig_scriptlets -n libQt6RemoteObjectsQml6

%files imports
%{_qt6_qmldir}/QtRemoteObjects

%files -n libQt6RemoteObjects6
%license LICENSES/*
%{_qt6_libdir}/libQt6RemoteObjects.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtRemoteObjectsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6RemoteObjects/
%{_qt6_cmakedir}/Qt6RemoteObjectsTools/
%{_qt6_descriptionsdir}/RemoteObjects.json
%{_qt6_descriptionsdir}/RepParser.json
%{_qt6_includedir}/QtRemoteObjects/
%{_qt6_includedir}/QtRepParser/
%{_qt6_libdir}/libQt6RemoteObjects.prl
%{_qt6_libdir}/libQt6RemoteObjects.so
%{_qt6_metatypesdir}/qt6remoteobjects_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_remoteobjects.pri
%{_qt6_mkspecsdir}/modules/qt_lib_repparser.pri
%{_qt6_pkgconfigdir}/Qt6RemoteObjects.pc
%exclude %{_qt6_includedir}/QtRemoteObjects/%{real_version}

%files private-devel
%{_qt6_includedir}/QtRemoteObjects/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_remoteobjects_private.pri

%files -n libQt6RemoteObjectsQml6
%{_qt6_libdir}/libQt6RemoteObjectsQml.so.*

%files -n qt6-remoteobjectsqml-devel
%{_qt6_cmakedir}/Qt6RemoteObjectsQml/
%{_qt6_descriptionsdir}/RemoteObjectsQml.json
%{_qt6_includedir}/QtRemoteObjectsQml/
%{_qt6_libdir}/libQt6RemoteObjectsQml.prl
%{_qt6_libdir}/libQt6RemoteObjectsQml.so
%{_qt6_metatypesdir}/qt6remoteobjectsqml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_remoteobjectsqml.pri
%{_qt6_pkgconfigdir}/Qt6RemoteObjectsQml.pc
%exclude %{_qt6_includedir}/QtRemoteObjectsQml/%{real_version}

%files -n qt6-remoteobjectsqml-private-devel
%{_qt6_includedir}/QtRemoteObjectsQml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_remoteobjectsqml_private.pri

%files tools
%{_qt6_libexecdir}/repc

%endif

%changelog
