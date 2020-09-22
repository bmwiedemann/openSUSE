#
# spec file for package paho-mqtt-c
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 1
Name:           paho-mqtt-c
Version:        1.3.5
Release:        0
Summary:        MQTT C Client
License:        EPL-1.0 AND BSD-3-Clause
URL:            https://eclipse.org/paho/clients/c/
Source:         https://github.com/eclipse/paho.mqtt.c/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  openssl-devel
Patch1:         cmake-libdir.patch
Requires:       openssl

%description
The Paho MQTT C Client is a fully featured MQTT client written in ANSI standard C.

%package -n libpaho-mqtt%{sover}
Summary:        Library implementing the MQTT client

%description  -n libpaho-mqtt%{sover}
The Paho MQTT C Client is a fully featured MQTT client written in ANSI standard C.
C was chosen rather than C++ to maximize portability. A C++ API over this library is also available in Paho.

%package -n libpaho-mqtt-devel
Summary:        Development files for MQTT C Client library
Requires:       libpaho-mqtt%{sover} = %{version}

%description -n libpaho-mqtt-devel
Development files for the the Paho MQTT C Client.

%prep
%setup -q -n paho.mqtt.c-%{version}
%patch1 -p1

%build
%cmake -DPAHO_WITH_SSL=TRUE -DPAHO_BUILD_DOCUMENTATION=FALSE -DPAHO_BUILD_SAMPLES=FALSE -DPAHO_ENABLE_TESTING=FALSE -DPAHO_ENABLE_CPACK=FALSE ..
%make_jobs

%install
%cmake_install
# fix samples path
mkdir -p %{buildroot}%{_docdir}/libpaho-mqtt-devel/samples
mv %{buildroot}%{_datadir}/doc/"Eclipse Paho C"/* %{buildroot}%{_docdir}/libpaho-mqtt-devel/samples
%fdupes -s %{buildroot}/%{_docdir}

%post -n libpaho-mqtt%{sover} -p /sbin/ldconfig
%postun -n libpaho-mqtt%{sover} -p /sbin/ldconfig

%files -n libpaho-mqtt%{sover}
%license LICENSE edl-v10 epl-v20
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.1

%files -n libpaho-mqtt-devel
%doc README.md
%{_bindir}/MQTTVersion
%{_includedir}/*
%{_libdir}/*.so
%{_docdir}/*
%{_libdir}/cmake/*

%changelog
