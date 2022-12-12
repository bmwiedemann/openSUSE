#
# spec file for package kdnssd-framework
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


%define lname   libKF5DNSSD5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdnssd-framework
Version:        5.101.0
Release:        0
Summary:        Network service discovery using Zeroconf
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         kdnssd-%{version}.tar.xz
%if %{with released}
Source1:        kdnssd-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0

%description
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package -n %{lname}
Summary:        Network service discovery using Zeroconf
%requires_ge    libQt5DBus5
%requires_ge    libQt5Network5
Recommends:     nss-mdns

%description -n %{lname}
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package devel
Summary:        Network service discovery using Zeroconf
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Network) >= 5.15.0

%description devel
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure. Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1 -n kdnssd-%{version}

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kdnssd5 --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f kdnssd5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5DNSSD.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5DNSSD/
%{_kf5_libdir}/libKF5DNSSD.so
%{_kf5_mkspecsdir}/qt_KDNSSD.pri

%changelog
