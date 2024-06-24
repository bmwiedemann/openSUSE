#
# spec file for package qt6-serialport
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
%define tar_name qtserialport-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-serialport%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 SerialPort library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-serialport-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(libudev)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 SerialPort library

%if !%{qt6_docs_flavor}

%package -n libQt6SerialPort6
Summary:        Qt 6 SerialPort library

%description -n libQt6SerialPort6
The Qt SerialPort library provides the basic functionality, which includes
configuring, I/O operations, getting and setting the control signals
of the RS-232 pinouts. This module does not support terminal features
(echo, CR/LF control, text mode, timeouts/delays, or poinout signal
change notification).

%package devel
Summary:        Qt 6 SerialPort library - Development files
Requires:       libQt6SerialPort6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description devel
Development files for the Qt 6 SerialPort library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 SerialPort library
Requires:       cmake(Qt6SerialPort) = %{real_version}
%requires_eq    qt6-core-private-devel

%description private-devel
This package provides private headers of libQt6SerialPort that do not have any
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

%ldconfig_scriptlets -n libQt6SerialPort6

%files -n libQt6SerialPort6
%license LICENSES/*
%{_qt6_libdir}/libQt6SerialPort.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtSerialPortTestsConfig.cmake
%{_qt6_cmakedir}/Qt6SerialPort/
%{_qt6_descriptionsdir}/SerialPort.json
%{_qt6_includedir}/QtSerialPort/
%{_qt6_libdir}/libQt6SerialPort.prl
%{_qt6_libdir}/libQt6SerialPort.so
%{_qt6_metatypesdir}/qt6serialport_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_serialport.pri
%{_qt6_pkgconfigdir}/Qt6SerialPort.pc
%exclude %{_qt6_includedir}/QtSerialPort/%{real_version}/

%files private-devel
%dir %{_qt6_includedir}/QtSerialPort
%{_qt6_includedir}/QtSerialPort/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_serialport_private.pri

%endif

%changelog
