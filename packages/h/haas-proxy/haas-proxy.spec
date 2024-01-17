#
# spec file for package haas-proxy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define hash bbf8629d1d64840407eefc23d2b6c8835365347b
Name:           haas-proxy
Version:        1.9
Release:        0
Summary:        Man in the middle proxy for honeypot as a service
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://haas.nic.cz
Source0:        https://gitlab.labs.nic.cz/haas/proxy/raw/%{hash}/release/%{name}-%{version}.tar.gz
Source1:        haas-proxy.service
Source2:        haas-sysconfig
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
Requires:       python3-Twisted
Requires:       python3-base
Requires:       python3-cachetools
Requires:       python3-pycrypto
Requires:       python3-service_identity
Requires:       sshpass
BuildArch:      noarch
%{?systemd_requires}

%description
HaaS proxy application forwards incoming traffic from port 22 (commonly used
for SSH) to the HaaS server, where Cowrie honeypot simulates a device and
records executed commands.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/haas-proxy
rm -rf %{buildroot}%{_sysconfdir}/init.d
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/haas-proxy.service
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rchaas-proxy
find %{buildroot} -name '*.pyc' -delete

%pre
%service_add_pre haas-proxy.service

%post
%service_add_post haas-proxy.service

%preun
%service_del_preun haas-proxy.service

%postun
%service_del_postun haas-proxy.service

%files
%config(noreplace) %{_sysconfdir}/haas-proxy
%{python3_sitelib}/*
%{_sbindir}/rchaas-proxy
%{_unitdir}/haas-proxy.service

%changelog
