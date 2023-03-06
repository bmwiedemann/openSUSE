#
# spec file for package clatd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           clatd
Version:        1.6
Release:        0
Summary:        CLAT / SIIT-DC Edge Relay implementation for Linux
License:        MIT
Group:          Productivity/Networking/System
URL:            https://github.com/toreanderson/clatd
#Git-Clone:     https://github.com/toreanderson/clatd.git
Source:         https://github.com/toreanderson/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        clatd.conf
BuildRequires:  NetworkManager
BuildRequires:  perl
BuildRequires:  systemd-rpm-macros
Requires:       iproute2
Requires:       iptables
Requires:       perl
Requires:       tayga
Requires:       perl(File::Temp)
Requires:       perl(IO::Socket::IP)
Requires:       perl(Net::DNS)
Requires:       perl(Net::IP)
BuildArch:      noarch

%description
clatd implements the CLAT component of the 464XLAT network architecture
specified in RFC 6877. It allows an IPv6-only host to have IPv4
connectivity that is translated to IPv6 before being routed to an upstream
PLAT (which is typically a Stateful NAT64 operated by the ISP) and there
translated back to IPv4 before being routed to the IPv4 internet.

%prep
%setup -q

%build
pod2man --name clatd --center "clatd - a CLAT implementation for Linux" --section 8 README.pod clatd.8
sed -i "s,%{_sbindir}/clatd,%{_sbindir}/clatd -c %{_sysconfdir}/clatd.conf," scripts/*

%install
install -D -m 0755 clatd %{buildroot}%{_sbindir}/clatd
install -D -m 0644 clatd.8 %{buildroot}%{_mandir}/man8/clatd.8
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/clatd.conf
install -D -m 0755 scripts/clatd.networkmanager %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/50-clatd
install -D -m 0644 scripts/clatd.systemd %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcclatd

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENCE
%doc README.pod
%{_sbindir}/clatd
%{_sbindir}/rcclatd
%config(noreplace) %{_sysconfdir}/clatd.conf
%{_sysconfdir}/NetworkManager/dispatcher.d/
%{_mandir}/man8/clatd.8%{?ext_man}
%{_unitdir}/%{name}.service

%changelog
