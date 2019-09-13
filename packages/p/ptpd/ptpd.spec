#
# spec file for package ptpd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ptpd
Version:        2.3.1
Release:        0
Summary:        Implementation of the Precision Time protocol (IEEE 1588)
License:        BSD-3-Clause
Group:          System/Daemons
Url:            https://github.com/ptpd/ptpd
Source0:        https://github.com/ptpd/ptpd/archive/ptpd-%{version}.tar.gz
Source1:        ptpd2.service
Source3:        conf.sysconfig.ptpd
# PATCH-FIX-UPSTREAM ptpd2-net-snmp_U64.patch gh#ptpd/ptpd#25
Patch0:         ptpd2-net-snmp_U64.patch
# PATCH-FIX-UPSTREAM resolve EVP_MD_CTX name conflict
Patch1:         ptpd-evp-md-ctx.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
%{?systemd_requires}

%description
The PTP daemon (PTPd) implements the Precision Time protocol (PTP) as
defined by the IEEE 1588 standard. PTP was developed to provide very
precise time coordination of LAN connected computers.

PTPd is a complete implementation of the IEEE 1588 specification for a
standard (non-boundary) clock. PTPd has been tested with and is known
to work properly with other IEEE 1588 implementations.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%patch1 -p1

%build
autoreconf -fiv
%configure \
  --enable-statistics \
  --enable-experimental-options
make %{?_smp_mflags}

%install
%make_install
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}/%{_unitdir}/%{name}2.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}2
# Generate default config
install -d %{buildroot}%{_sysconfdir}
./src/ptpd2 --default-config > %{buildroot}%{_sysconfdir}/%{name}2.conf
install -Dpm 0644 %{SOURCE3} \
  %{buildroot}%{_fillupdir}/sysconfig.ptpd2
# have to create the below, else ptpd will not log drift
install -d %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/ptpd2_kernelclock.drift

%pre
%service_add_pre %{name}2.service

%preun
%service_del_preun %{name}2.service

%post
%service_add_post %{name}2.service
%{fillup_only -n ptpd2}

%postun
%service_del_postun %{name}2.service

%files
%license COPYRIGHT
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/%{name}2.conf
%{_sbindir}/ptpd2
%{_sbindir}/rcptpd2
%{_mandir}/man5/ptpd2.conf.5%{?ext_man}
%{_mandir}/man8/ptpd2.8%{?ext_man}
%{_datadir}/ptpd
%{_libexecdir}/systemd/system/ptpd2.service
%{_fillupdir}/*
%config %ghost %{_localstatedir}/log/ptpd2_kernelclock.drift

%changelog
