#
# spec file for package hostapd
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without  apparmor
Name:           hostapd
Version:        2.10
Release:        0
Summary:        Daemon for running a WPA capable Access Point
License:        BSD-3-Clause OR GPL-2.0-only
Group:          Hardware/Wifi
URL:            https://w1.fi/
Source:         https://w1.fi/releases/hostapd-%{version}.tar.gz
Source1:        https://w1.fi/releases/hostapd-%{version}.tar.gz.asc
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2B6EF432EFC895FA#/%%{name}.keyring
Source2:        %{name}.keyring
Source3:        config
Source4:        hostapd.service
Source5:        apparmor-usr.sbin.hostapd
BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Recommends:     apparmor-abstractions
%endif

%description
hostapd is a user space daemon for access point and authentication
servers. It implements IEEE 802.11 access point management, IEEE
802.1X/WPA/WPA2/EAP Authenticators, RADIUS client, EAP server, and
RADIUS authentication server. Currently, hostapd supports HostAP,
madwifi, and prism54 drivers. It also supports wired IEEE 802.1X
authentication via any ethernet driver.

%prep
%setup -q
cp %{SOURCE3} hostapd/.config
%autopatch -p1

%build
cd hostapd
CFLAGS="%{optflags} -D_GNU_SOURCE $(getconf LFS_CFLAGS)" CC="gcc" make  %{?_smp_mflags} V=1

%install
cd hostapd
install -d %{buildroot}/%{_sbindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}/%{_mandir}/man8
install -m 755 hostapd %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rchostapd
install -m 755 hostapd_cli %{buildroot}/%{_sbindir}
install -m 600 hostapd.conf %{buildroot}%{_sysconfdir}
install -m 644 hostapd.accept %{buildroot}%{_sysconfdir}
install -m 644 hostapd.deny %{buildroot}%{_sysconfdir}
install -m 600 hostapd.eap_user %{buildroot}%{_sysconfdir}
install -m 600 hostapd.radius_clients %{buildroot}%{_sysconfdir}
install -m 644 hostapd.sim_db %{buildroot}%{_sysconfdir}
install -m 644 hostapd.vlan %{buildroot}%{_sysconfdir}
install -m 600 hostapd.wpa_psk %{buildroot}%{_sysconfdir}
install -m 644 hostapd.8 %{buildroot}/%{_mandir}/man8
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/hostapd.service
%if %{with apparmor}
# AppArmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.hostapd
%endif

%pre
%service_add_pre hostapd.service

%post
%service_add_post hostapd.service
%if %{with apparmor}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.hostapd
%endif

%preun
%service_del_preun hostapd.service

%postun
%service_del_postun hostapd.service

%files
%config(noreplace) %{_sysconfdir}/hostapd.*
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.hostapd
%endif
%{_sbindir}/*
%license COPYING
%doc hostapd/ChangeLog hostapd/README hostapd/wired.conf hostapd/hostapd.conf
%{_mandir}/man8/*
%{_unitdir}/hostapd.service

%changelog
