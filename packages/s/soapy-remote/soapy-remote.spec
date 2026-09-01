#
# spec file for package soapy-remote
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-remote
Name:           soapy-remote
Version:        0.5.2
Release:        0
Summary:        Remote device support for Soapy SDR
License:        BSL-1.0
URL:            https://github.com/pothosware/SoapyRemote/wiki
#Git-Clone:     https://github.com/pothosware/SoapyRemote.git
Source:         https://github.com/pothosware/SoapyRemote/archive/%{name}-%{version}.tar.gz
Patch0:         harden_SoapySDRServer.service.patch
# Order after avahi-daemon: upstream's mDNS registration is one-shot and never
# retries, so losing the startup race disables advertisement permanently
Patch1:         SoapySDRServer-order-after-avahi.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR) >= 0.4.0
# Without this upstream only WARNS and silently builds the no-op MDNS stub,
# losing mDNS/DNS-SD discovery
BuildRequires:  pkgconfig(avahi-client)

%description
A Soapy module that supports remote devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        Remote device support for Soapy SDR
# Factory review of the soapy-* modules: libSoapySDR does the dlopen and is
# already covered by the soname dep; this pulls the SoapySDR package proper
# (SoapySDRUtil). Not on -server, which is a standalone daemon linking
# libSoapySDR directly.
Requires:       soapy-sdr
# mDNS browsing needs the daemon; not hard, SSDP discovery works without it and
# upstream opens the client with AVAHI_CLIENT_NO_FAIL
Recommends:     avahi
# soapysdr0.7-module-remote needs to be force dropped
Conflicts:      soapysdr0.7-module-remote
# Add 'Provides/Obsoletes' entries for future updates
Provides:       soapy-remote-module = %{soapy_modver}
Obsoletes:      soapy-remote-module < %{soapy_modver}

%description -n %{soapy_modname}
A Soapy module that supports remote devices within the Soapy API.

%package server
Summary:        Server for remote device support for Soapy SDR
# mDNS advertisement needs the daemon; see the module subpackage
Recommends:     avahi
# The server part was split, a 'Conflicts' line is also needed here.
Conflicts:      soapysdr0.7-module-remote

%description server
A server that supports remote devices for the Soapy SDR.
This package is intended to run on the system the sdr device is
connected to.

%prep
%autosetup -p1 -n SoapyRemote-%{name}-%{version}

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcSoapySDRServer

%check
%ctest

%pre server
%service_add_pre SoapySDRServer.service

%post server
%service_add_post SoapySDRServer.service

%preun server
%service_del_preun SoapySDRServer.service

%postun server
%service_del_postun SoapySDRServer.service

%files -n %{soapy_modname}
%license LICENSE_1_0.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR/
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libremoteSupport.so

%files server
%license LICENSE_1_0.txt
%doc Changelog.txt README.md
%{_bindir}/SoapySDRServer
%{_sbindir}/rcSoapySDRServer
%{_mandir}/man1/SoapySDRServer.1%{?ext_man}
%{_sysctldir}/SoapySDRServer.conf
%{_unitdir}/SoapySDRServer.service

%changelog
