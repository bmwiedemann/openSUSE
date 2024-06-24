#
# spec file for package qt6-serialbus
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
%define tar_name qtserialbus-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-serialbus
Version:        6.7.2
Release:        0
Summary:        Qt 6 SerialBus library
License:        LGPL-3.0-only OR GPL-2.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-serialbus-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6SerialPort) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 SerialBus library.

%if !%{qt6_docs_flavor}

%package -n libQt6SerialBus6
Summary:        Qt 6 SerialBus library

%description -n libQt6SerialBus6
The Qt SerialBus API provides classes and functions to access the
various industrial serial buses and protocols, such as CAN, ModBus,
and others.

%package devel
Summary:        Qt 6 SerialBus library - Development files
Requires:       qt6-serialbus = %{version}
Requires:       libQt6SerialBus6 = %{version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6SerialPort) = %{real_version}

%description devel
Development files for the Qt 6 SerialBus library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 SerialBus library
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6SerialBus) = %{real_version}
Requires:       cmake(Qt6SerialPort) = %{real_version}
%requires_eq    qt6-core-private-devel

%description private-devel
This package provides private headers of libQt6SerialBus that do not have any
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

%fdupes %{buildroot}

# CMake files are not needed for plugins
rm %{buildroot}%{_qt6_cmakedir}/Qt6SerialBus/*Plugin*.cmake

%{qt6_link_executables}

%ldconfig_scriptlets -n libQt6SerialBus6

%files
%{_bindir}/canbusutil6
%{_qt6_bindir}/canbusutil
%{_qt6_pluginsdir}/canbus/

%files -n libQt6SerialBus6
%license LICENSES/*
%{_qt6_libdir}/libQt6SerialBus.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtSerialBusTestsConfig.cmake
%{_qt6_cmakedir}/Qt6SerialBus/
%{_qt6_descriptionsdir}/SerialBus.json
%{_qt6_includedir}/QtSerialBus/
%{_qt6_libdir}/libQt6SerialBus.prl
%{_qt6_libdir}/libQt6SerialBus.so
%{_qt6_metatypesdir}/qt6serialbus_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_serialbus.pri
%{_qt6_pkgconfigdir}/Qt6SerialBus.pc
%exclude %{_qt6_includedir}/QtSerialBus/%{real_version}/

%files private-devel
%dir %{_qt6_includedir}/QtSerialBus
%{_qt6_includedir}/QtSerialBus/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_serialbus_private.pri

%endif

%changelog
