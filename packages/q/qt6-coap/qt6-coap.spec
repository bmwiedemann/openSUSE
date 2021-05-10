#
# spec file for package qt6-coap
#
# Copyright (c) 2021 SUSE LLC
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


%define real_version 6.1.0
%define short_version 6.1
%define tar_name qtcoap
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-coap%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Qt 6 CoAP client module 
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         %{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-coap-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt 6 library to implement a CoAP (Constrained Application Protocol) client.

%if !%{qt6_docs_flavor}

%package -n libQt6Coap6
Summary:        Qt 6 CoAP Client Library

%description -n libQt6Coap6
Qt 6 library to implement a CoAP client.

%package devel
Summary:        Qt 6 CoAP library - Development files
Requires:       libQt6Coap6 = %{version}

%description devel
Development files for the Qt 6 CoAP library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 CoAP library
Requires:       cmake(Qt6Coap) = %{real_version}

%description private-devel
This package provides private headers of libQt6Coap that do not have any
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

%post -n libQt6Coap6 -p /sbin/ldconfig
%postun -n libQt6Coap6 -p /sbin/ldconfig

%files -n libQt6Coap6
%license LICENSE.*
%{_qt6_libdir}/libQt6Coap.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtCoapTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Coap/
%{_qt6_descriptionsdir}/Coap.json
%{_qt6_includedir}/QtCoap
%{_qt6_libdir}/libQt6Coap.prl
%{_qt6_libdir}/libQt6Coap.so
%{_qt6_mkspecsdir}/modules/qt_lib_coap.pri
%exclude %{_qt6_includedir}/QtCoap/%{real_version}

%files private-devel
%{_qt6_includedir}/QtCoap/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_coap_private.pri

%endif

%changelog
