#
# spec file for package ipmitool
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


Name:           ipmitool
Version:        1.8.18+git20200916.1245aaa387dc
Release:        0
Summary:        Utility for IPMI Control
License:        BSD-3-Clause
Group:          System/Management
URL:            https://github.com/ipmitool/ipmitool
Source:         %{name}-%{version}.tar.xz
Source1:        ipmievd.service
Source2:        ipmievd.sysconf
Source3:        enterprise-numbers
Patch1:         0001-Enhance-fwum-output.patch
Patch2:         0002-Fix-file-permissions.patch
Patch3:         0003-Cleanup-and-compiler-issues-only-no-functional-chang.patch
Patch4:         0004-Adjust-SUSE-paths.patch
Patch5:         0005-HPM-x-compatibility-message-is-DEBUG-only.patch
Patch6:         0006-Make-IANA-PEN-download-configurable-fix-uninitalized.patch
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
# Taken over from freeipmi.spec:
# Necessary as only those archs implement iopl and friends (#368541)
%ifarch %{ix86} x86_64 ia64 alpha aarch64
BuildRequires:  freeipmi-devel
%endif
%{?systemd_requires}

%description
This package contains a utility for interfacing with devices that
support the Intelligent Platform Management Interface specification.
IPMI is an open standard for machine health, inventory, and remote
power control.

This utility can communicate with IPMI-enabled devices through either a
kernel driver such as OpenIPMI or over the RMCP LAN protocol defined in
the IPMI specification.  IPMIv2 adds support for encrypted LAN
communications and remote Serial-over-LAN functionality.

It provides commands for reading the Sensor Data Repository (SDR) and
displaying sensor values, displaying the contents of the System Event
Log (SEL), printing Field Replaceable Unit (FRU) information, reading
and setting LAN configuration, and chassis power control.

%package bmc-snmp-proxy
Summary:        SNMP configuration to include the BMC's SNMP agent
Group:          System/Management
Requires:       net-snmp, ipmitool >= %{version}
BuildArch:      noarch

%description bmc-snmp-proxy
Given a host with BMC, this package would extend system configuration
of net-snmp to include redirections to BMC based SNMP.

%prep
%setup -q
%autopatch -p1

%build
cp %{SOURCE3} lib
autoreconf -fiv
# file-security: enables more security checks on files
%configure               \
  --enable-file-security \
  --enable-intf-usb
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/ipmitool

install -D -m 644 %{SOURCE3}  %{buildroot}%{_datadir}/misc/enterprise-numbers

# exchange-bmc-os-info service
install -D -m 0755 contrib/exchange-bmc-os-info.init.redhat %{buildroot}/%{_sbindir}/exchange-bmc-os-info
install -D -m 0644 contrib/exchange-bmc-os-info.service.redhat %{buildroot}%{_unitdir}/exchange-bmc-os-info.service
install -D -m 0644 contrib/exchange-bmc-os-info.sysconf %{buildroot}/%{_sysconfdir}/exchange-bmc-os-info
ln -sf service %{buildroot}%{_sbindir}/rcexchange-bmc-os-info

# ipmievd service
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/ipmievd.service
install -D -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/ipmievd
ln -sf service %{buildroot}%{_sbindir}/rcipmievd

# bmc-snmp-proxy
install -D -m 755 contrib/bmc-snmp-proxy         %{buildroot}/%{_sbindir}/bmc-snmp-proxy
install -D -m 644 contrib/bmc-snmp-proxy.service %{buildroot}%{_unitdir}/bmc-snmp-proxy.service
install -D -m 755 contrib/bmc-snmp-proxy.sysconf %{buildroot}/%{_sysconfdir}/bmc-snmp-proxy
ln -sf service %{buildroot}%{_sbindir}/rcbmc-snmp-proxy

%pre
%service_add_pre exchange-bmc-os-info.service ipmievd.service

%post
%service_add_post exchange-bmc-os-info.service ipmievd.service

%preun
%service_del_preun exchange-bmc-os-info.service ipmievd.service

%postun
%service_del_postun exchange-bmc-os-info.service ipmievd.service

%pre bmc-snmp-proxy
%service_add_pre bmc-snmp-proxy.service

%post bmc-snmp-proxy
%service_add_post bmc-snmp-proxy.service exchange-bmc-os-info.service ipmievd.service

%preun bmc-snmp-proxy
%service_del_preun bmc-snmp-proxy.service exchange-bmc-os-info.service ipmievd.service

%postun bmc-snmp-proxy
%service_del_postun bmc-snmp-proxy.service exchange-bmc-os-info.service ipmievd.service

%files
%doc AUTHORS README ChangeLog
%license COPYING
%{_datadir}/ipmitool
%attr(755,root,root) %{_bindir}/ipmitool
%attr(755,root,root) %{_sbindir}/ipmievd
%attr(755,root,root) %{_sbindir}/exchange-bmc-os-info
%{_sbindir}/rcipmievd
%{_sbindir}/rcexchange-bmc-os-info
%config(noreplace) %{_sysconfdir}/exchange-bmc-os-info
%config(noreplace) %{_sysconfdir}/ipmievd
%{_unitdir}/exchange-bmc-os-info.service
%{_unitdir}/ipmievd.service
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_datadir}/misc/enterprise-numbers

%files bmc-snmp-proxy
%attr(755,root,root) %{_sbindir}/bmc-snmp-proxy
%{_sbindir}/rcbmc-snmp-proxy
%config(noreplace) %{_sysconfdir}/bmc-snmp-proxy
%{_unitdir}/bmc-snmp-proxy.service

%changelog
