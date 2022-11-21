#
# spec file for package qt6-connectivity
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
%define tar_name qtconnectivity-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-connectivity%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 connectivity tools and libraries
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-connectivity-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-network-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(libpcsclite)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 connectivity tools and libraries.

%if !%{qt6_docs_flavor}

%package -n libQt6Bluetooth6
Summary:        Qt 6 bluetooth library

%description -n libQt6Bluetooth6
Provides access to Bluetooth hardware.

%package -n libQt6Nfc6
Summary:        Qt 6 NFC library

%description -n libQt6Nfc6
Provides access to NFC hardware.

# TODO: split
%package devel
Summary:        Qt 6 connectivity libraries - Development files
Requires:       libQt6Bluetooth6 = %{version}
Requires:       libQt6Nfc6 = %{version}
# sdoscanner in required by Qt6BluetoothToolsTargets.cmake
Requires:       qt6-connectivity = %{version}
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Network)

%description devel
Development files for the Qt6 connectivity libraries.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 connectivity libraries
Requires:       qt6-core-private-devel
Requires:       cmake(Qt6Bluetooth) = %{real_version}
Requires:       cmake(Qt6Nfc) = %{real_version}

%description private-devel
This package provides private headers of qt6-connectivity that are normally
not used by application development and that do not have any ABI or
API guarantees.
The packages that build against these have to require the exact Qt version.

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

%post -n libQt6Bluetooth6 -p /sbin/ldconfig
%postun -n libQt6Bluetooth6 -p /sbin/ldconfig
%post -n libQt6Nfc6 -p /sbin/ldconfig
%postun -n libQt6Nfc6 -p /sbin/ldconfig

%files
%{_qt6_libexecdir}/sdpscanner

%files -n libQt6Bluetooth6
%license LICENSES/*
%{_qt6_libdir}/libQt6Bluetooth.so.*

%files -n libQt6Nfc6
%license LICENSES/*
%{_qt6_libdir}/libQt6Nfc.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindBlueZ.cmake
%{_qt6_cmakedir}/Qt6/FindPCSCLite.cmake
%{_qt6_cmakedir}/Qt6Bluetooth/
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtConnectivityTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Nfc/
%{_qt6_descriptionsdir}/Bluetooth.json
%{_qt6_descriptionsdir}/Nfc.json
%{_qt6_includedir}/QtBluetooth/
%{_qt6_includedir}/QtNfc/
%{_qt6_libdir}/libQt6Bluetooth.prl
%{_qt6_libdir}/libQt6Bluetooth.so
%{_qt6_libdir}/libQt6Nfc.prl
%{_qt6_libdir}/libQt6Nfc.so
%{_qt6_metatypesdir}/qt6bluetooth*_metatypes.json
%{_qt6_metatypesdir}/qt6nfc_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_bluetooth.pri
%{_qt6_mkspecsdir}/modules/qt_lib_nfc.pri
%{_qt6_pkgconfigdir}/Qt6Bluetooth.pc
%{_qt6_pkgconfigdir}/Qt6Nfc.pc
%exclude %{_qt6_includedir}/QtBluetooth/%{real_version}/
%exclude %{_qt6_includedir}/QtNfc/%{real_version}/

%files private-devel
%dir %{_qt6_includedir}/QtBluetooth
%dir %{_qt6_includedir}/QtNfc
%{_qt6_includedir}/QtBluetooth/%{real_version}/
%{_qt6_includedir}/QtNfc/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_bluetooth_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_nfc_private.pri

%endif

%changelog
