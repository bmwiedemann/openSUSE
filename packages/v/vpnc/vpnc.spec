#
# spec file for package vpnc
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


%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           vpnc
Version:        0.5.3r550
Release:        0
Summary:        A Client for Cisco VPN concentrator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://svn.unix-ag.uni-kl.de/vpnc/branches/vpnc-nortel
Source:         %{name}-%{version}.tar.bz2
# only for checkin warnings...
Source1:        checkout_svn.sh
Source2:        %{name}.conf
Source3:        %{name}.service
# most ugly hack ever
Patch1:         vpnc-restart-after-timeout.diff
BuildRequires:  gnutls
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
BuildRequires:  pkg-config
Requires:       %{_bindir}/sed
Requires:       /sbin/ip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%endif

%description
A VPN client compatible with Cisco's EasyVPN equipment.

Cisco 3000, IOS routers, PIX/ASA Zecurity Appliances, and
Juniper/Netscreen as well as Nortel Contivity (experimental).

Supported Authentications: Pre-Shared-Key + XAUTH, Pre-Shared-Key
Supported IKE DH-Groups: dh1 dh2 dh5 Supported Hash Algo (IKE/IPSEC):
md5 sha1 Supported Encryptions (IKE/IPSEC): (null) (1des) 3des aes128
aes192 aes256 Perfect Forward Secrecy: nopfs dh1 dh2 dh5

It runs entirely in userspace and uses the TUN/TAP driver for access.

%prep
%setup -q -n %{name}
%patch1 -p1

%build
export CFLAGS="%{optflags}"
make PREFIX=/usr %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_rundir}/vpnc
make install \
	DESTDIR=%{buildroot} \
	PREFIX=/usr
rm -rfv %{buildroot}%{_datadir}/doc/vpnc
%if 0%{?suse_version} >= 1210
install -D -m 0644 $RPM_SOURCE_DIR/%{name}.service %{buildroot}/%{_unitdir}/%{name}@.service
install -D -m 0644 $RPM_SOURCE_DIR/%{name}.conf %{buildroot}/%{_tmpfilesdir}/%{name}.conf
%endif
sed -i -e '1c#!/usr/bin/perl' %{buildroot}%{_bindir}/pcf2vpnc

%pre
%if 0%{?suse_version} >= 1210
%service_add_pre %{name}@.service
%endif

%post
%if 0%{?suse_version} >= 1210
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}@.service
%endif

%preun
%if 0%{?suse_version} >= 1210
%service_del_preun %{name}@.service
%endif

%postun
%if 0%{?suse_version} >= 1210
%service_del_postun %{name}@.service
%endif

%files
%defattr(-,root,root)
%attr(0600,root,root) %config(noreplace) %ghost %{_sysconfdir}/%{name}/default.conf

%ghost %{_rundir}/vpnc
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/vpnc-script
%{_sbindir}/vpnc
%{_sbindir}/vpnc-disconnect
%{_bindir}/cisco-decrypt
%{_bindir}/pcf2vpnc
%{_mandir}/man1/cisco-decrypt.1.*
%{_mandir}/man1/pcf2vpnc.1.*
%{_mandir}/man8/vpnc.8.*
%if 0%{?suse_version} >= 1210
%{_unitdir}/%{name}@.service
%{_tmpfilesdir}/%{name}.conf
%endif
%doc ChangeLog README TODO VERSION
%license COPYING

%changelog
