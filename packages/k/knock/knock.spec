#
# spec file for package knock
#
# Copyright (c) 1980 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           knock
Version:        0.8
Release:        0
Summary:        A Port-Knocking Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://www.zeroflux.org/knock/
Source0:        http://www.zeroflux.org/proj/knock/files/%{name}-%{version}.tar.gz
Source1:        %{name}d.sysconfig
Source2:        %{name}d.init
Source3:        %{name}d.conf
Source4:        %{name}d.service
BuildRequires:  libpcap-devel
BuildRequires:  systemd-rpm-macros

%description
The server part (package knockd) listens to all traffic on an ethernet
(or PPP) interface, looking for special "knock" sequences of port hits.
This client makes these port hits by sending a TCP (or UDP) packet to a
port on the server. This port does not need to be open. Since knockd
listens at the link-layer level, it sees all traffic even if it is
destined for a closed port. When the server detects a specific sequence
of port hits, it runs a command defined in its configuration file. This
can be used to open up holes in a firewall for quick access.

%package -n knockd
Summary:        A port-knocking server
Group:          Productivity/Networking/Security
%{?systemd_requires}

%description -n knockd
It listens to all traffic on an ethernet (or PPP) interface, looking
for special "knock" sequences of port-hits. A client (package knock)
makes these port-hits by sending a TCP (or UDP) packet to a port on the
server. This port need not be open -- since knockd listens at the
link-layer level, it sees all traffic even if it's destined for a
closed port. When the server detects a specific sequence of port-hits,
it runs a command defined in its configuration file. This can be used
to open up holes in a firewall for quick access.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
sed -i -e "s:iptables:%{_sbindir}/iptables:" %{SOURCE3}
install -m 600 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}d.conf
install -D -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/%{name}d.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}d
rm -rf %{buildroot}%{_datadir}/doc

%pre -n knockd
%service_add_pre %{name}d.service

%post -n knockd
%service_add_post %{name}d.service

%preun -n knockd
%service_del_preun %{name}d.service

%postun -n knockd
%service_del_postun %{name}d.service

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.*
%{_sbindir}/knock_helper_ipt.sh

%files -n knockd
%defattr(-,root,root)
%doc README.md ChangeLog TODO
%license COPYING
%{_sbindir}/%{name}d
%{_unitdir}/%{name}d.service
%{_sbindir}/rc%{name}d
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/%{name}d.conf
%{_mandir}/man?/%{name}d.*

%changelog
