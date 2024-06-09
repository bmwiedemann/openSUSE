#
# spec file for package kf6-kdnssd
#
# Copyright (c) 2024 SUSE LLC
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


%define qt6_version 6.6.0

%define rname kdnssd
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kdnssd
Version:        6.3.0
Release:        0
Summary:        Network service discovery using Zeroconf
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package -n libKF6DNSSD6
Summary:        Network service discovery using Zeroconf
Recommends:     nss-mdns

%description -n libKF6DNSSD6
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package devel
Summary:        Network service discovery using Zeroconf
Requires:       libKF6DNSSD6 = %{version}

%description devel
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure. Development files.

%lang_package -n libKF6DNSSD6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kdnssd6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6DNSSD6

%files -n libKF6DNSSD6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6DNSSD.so.*

%files devel
%doc %{_kf6_qchdir}/KF6DNSSD.*
%{_kf6_cmakedir}/KF6DNSSD/
%{_kf6_includedir}/KDNSSD/
%{_kf6_libdir}/libKF6DNSSD.so

%files -n libKF6DNSSD6-lang -f kdnssd6.lang

%changelog
