#
# spec file for package dhcpcd
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dhcpcd
Version:        10.2.0
Release:        0
Summary:        Minimal DHCPv4 and DHCPv6 client
License:        BSD-2-Clause
URL:            https://github.com/NetworkConfiguration/dhcpcd
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        dhcpcd.conf
Source4:        dhcpcd.service
Source5:        dhcpcd@.service
BuildRequires:  sysuser-tools
%sysusers_requires

%description
dhcpcd is a DHCP and a DHCPv6 client. It's also an IPv4LL (aka ZeroConf)
client. In layperson's terms, dhcpcd runs on your machine and silently
configures your computer to work on the attached networks without trouble and
mostly without configuration.

%prep
%autosetup -p1

%build
%configure \
    --dbdir=%{_sharedstatedir}/dhcpcd \
    --runstatedir=%{_rundir} \
    --privsepuser=dhcpcd
%make_build
%sysusers_generate_pre %{SOURCE3} dhcpcd dhcpcd.conf

%check
%make_build test

%install
%make_install
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/dhcpcd.service
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/dhcpcd@.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/dhcpcd.conf
install -d %{buildroot}%{_sharedstatedir}/dhcpcd

%pre -f dhcpcd.pre
%service_add_pre dhcpcd.service

%post
%service_add_post dhcpcd.service

%preun
%service_del_preun dhcpcd.service

%postun
%service_del_postun dhcpcd.service

%files
%license LICENSE
%doc README.md
%doc %{_mandir}/man5/*5*
%doc %{_mandir}/man8/*8*
%{_sbindir}/dhcpcd
%config(noreplace) %{_sysconfdir}/dhcpcd.conf
%dir %{_libexecdir}/dhcpcd-hooks
%{_libexecdir}/dhcpcd-hooks/01-test
%{_libexecdir}/dhcpcd-hooks/20-resolv.conf
%{_libexecdir}/dhcpcd-hooks/30-hostname
%{_libexecdir}/dhcpcd-run-hooks
%dir %{_datadir}/dhcpcd
%dir %{_datadir}/dhcpcd/hooks
%{_datadir}/dhcpcd/hooks/10-wpa_supplicant
%{_datadir}/dhcpcd/hooks/15-timezone
%{_datadir}/dhcpcd/hooks/29-lookup-hostname
%{_datadir}/dhcpcd/hooks/50-yp.conf
%{_unitdir}/dhcpcd.service
%{_unitdir}/dhcpcd@.service
%{_sysusersdir}/dhcpcd.conf
%attr(0750,root,root) %dir %{_sharedstatedir}/dhcpcd

%changelog
