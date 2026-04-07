#
# spec file for package xl2tpd
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           xl2tpd
Version:        1.3.20
Release:        0
Summary:        Layer 2 Tunnelling Protocol Daemon (RFC 2661)
License:        GPL-2.0-only
URL:            https://github.com/xelerance/xl2tpd
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
BuildRequires:  linux-kernel-headers >= 2.6.19
BuildRequires:  ppp
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpcap)
Requires:       ppp
Obsoletes:      l2tpd <= 0.68
Provides:       l2tpd = 0.69
%{?systemd_ordering}

%description
xl2tpd is an implementation of the Layer 2 Tunnelling Protocol (RFC 2661).
L2TP allows you to tunnel PPP over UDP. Some ISPs use L2TP to tunnel user
sessions from dial-in servers (modem banks, ADSL DSLAMs) to back-end PPP
servers. Another important application is Virtual Private Networks where
the IPsec protocol is used to secure the L2TP connection (L2TP/IPsec,
RFC 3193). The L2TP/IPsec protocol is mainly used by Windows and
Mac OS X clients. On Linux, xl2tpd can be used in combination with IPsec
implementations such as Openswan.
Example configuration files for such a setup are included in this RPM.

xl2tpd works by opening a pseudo-tty for communicating with pppd.
It runs completely in userspace but supports kernel mode L2TP.

xl2tpd supports IPsec SA Reference tracking to enable overlapping internak
NAT'ed IP's by different clients (eg all clients connecting from their
linksys internal IP 192.168.1.101) as well as multiple clients behind
the same NAT router.

xl2tpd supports the pppol2tp kernel mode operations on 2.6.23 or higher,
or via a patch in contrib for 2.4.x kernels.

Xl2tpd is based on the 0.69 L2TP by Jeff McAdams <jeffm@iglou.com>
It was de-facto maintained by Jacco de Leeuw <jacco2@dds.nl> in 2002 and 2003.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
install -p -D -m644 examples/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -D -m600 doc/l2tp-secrets.sample %{buildroot}%{_sysconfdir}/%{name}/l2tp-secrets
install -p -d -m755 %{buildroot}%{_rundir}/%{name}
install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i 's|%{_localstatedir}/run/|%{_rundir}/|' %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -p -d -m755 %{buildroot}%{_prefix}/lib/modules-load.d
echo "l2tp_ppp" > %{buildroot}%{_prefix}/lib/modules-load.d/%{name}.conf

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc BUGS CHANGES COMPATIBILITY_ISSUES CONTRIBUTION.md CREDITS README.md TODO
%doc doc/COMMON_SOLUTIONS doc/README.patents examples/chapsecrets.sample
%config(noreplace) %{_sysconfdir}/%{name}
%dir %ghost %{_rundir}/%{name}
%dir %{_prefix}/lib/modules-load.d
%ghost %{_rundir}/%{name}/l2tp-control
%{_bindir}/pfc
%{_mandir}/man?/%{name}-control.?%{?ext_man}
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/%{name}.conf.?%{?ext_man}
%{_mandir}/man?/l2tp-secrets.?%{?ext_man}
%{_mandir}/man?/pfc.?%{?ext_man}
%{_prefix}/lib/modules-load.d/%{name}.conf
%{_sbindir}/%{name}
%{_sbindir}/%{name}-control
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service

%changelog
