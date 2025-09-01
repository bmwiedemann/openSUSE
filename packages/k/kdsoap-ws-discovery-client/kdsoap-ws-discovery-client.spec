#
# spec file for package kdsoap-ws-discovery-client
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global sover 0
%define qt6_version 6.5.0
%bcond_without released
Name:           kdsoap-ws-discovery-client
Version:        0.4.0
Release:        0
Summary:        WS-discovery client library
License:        GPL-3.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kdsoap-ws-discovery-client.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This package provides a client for the Web Services Dynamic Discovery
(WS-Discovery) protocol, used to discover services on a local network.

%package -n libKDSoapWSDiscoveryClient%{sover}
Summary:        WS-discovery client library

%description -n libKDSoapWSDiscoveryClient%{sover}
This package contains the main library implementing a client for the
Web Services Dynamic Discovery (WS-Discovery) protocol, used to discover
services on a local network.

%package devel
Summary:        Development files for kdsoap-ws-discovery-client
Requires:       libKDSoapWSDiscoveryClient%{sover} = %{version}
Requires:       cmake(KDSoap-qt6)

%description devel
Development files for kdsoap-ws-discovery-client, a client for the
WS-discovery protocol.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE -DBUILD_QCH:BOOL=TRUE

%{kf6_build}

%install
%{kf6_install}
%fdupes %{buildroot}

%ldconfig_scriptlets -n libKDSoapWSDiscoveryClient%{sover}

%files -n libKDSoapWSDiscoveryClient%{sover}
%license LICENSES/*
%{_kf6_libdir}/libKDSoapWSDiscoveryClient.so.%{sover}
%{_kf6_libdir}/libKDSoapWSDiscoveryClient.so.*.*

%files devel
%doc %{_kf6_sharedir}/doc/KDSoapWSDiscoveryClient/
%doc %{_kf6_qchdir}/KDSoapWSDiscoveryClient.*
%{_kf6_cmakedir}/KDSoapWSDiscoveryClient
%{_includedir}/KDSoapWSDiscoveryClient
%{_kf6_libdir}/libKDSoapWSDiscoveryClient.so

%changelog
