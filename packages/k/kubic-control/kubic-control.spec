#
# spec file for package kubic-control
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kubic-control
Version:        0.9.0
Release:        0
Summary:        Simple setup tool for kubernetes
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/thkukuk/kubic-control
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
ExcludeArch:    s390 %{ix86}

%description
This package contains a simple client/server tool to setup and manage kubernetes on openSUSE Kubic

%package -n kubicd
Summary:        Daemon to setup a kubernetes cluster
Group:          System/Management
Requires:       cilium-k8s-yaml
Requires:       etcdctl
Requires:       flannel-k8s-yaml
Requires:       kubicctl
Requires:       kured-k8s-yaml
Requires:       salt-master
Requires:       weave-k8s-yaml

%description -n kubicd
kubicd is a gRPC based daemon using mutualTLS and RBAC to setup and manage a kubernetes cluster on openSUSE Kubic. Authantication is done via certificates.

%package -n kubicctl
Summary:        Cli for kubicd to setup and manage kubernetes
Group:          System/Management
Requires:       certstrap

%description -n kubicctl
kubicctl is a cli to using gRPC with mutualTLS to communicate with kubicd to setup and manage a kubernetes cluster on openSUSE Kubic. Authentication is done via certificates.

%package -n kubic-haproxycfg
Summary:        Tool to maipulate haproxy.cfg
Group:          System/Management
Requires:       haproxy

%description -n kubic-haproxycfg
haproxycfg is used by kubicd to create a haproxy.cfg for use as loadbalancer
for a kubernetes cluster with multi-master.

%prep
%setup -q

%build
make build

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/kubicctl %{buildroot}%{_bindir}
install -p -m 0755 bin/haproxycfg %{buildroot}%{_bindir}
install -d -p %{buildroot}%{_sbindir}
install -p -m 0755 bin/kubicd %{buildroot}%{_sbindir}
ln -s /sbin/service %{buildroot}%{_sbindir}/rckubicd
mkdir -p %{buildroot}%{_datadir}/defaults/kubicd/
cp -av etc/kubicd/* %{buildroot}%{_datadir}/defaults/kubicd
mkdir -p %{buildroot}%{_sysconfdir}/kubicd/pki
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system
cp -av systemd/* %{buildroot}%{_prefix}/lib/systemd/system

%pre -n kubicd
%service_add_pre kubicd.service

%post -n kubicd
%service_add_post kubicd.service

%preun -n kubicd
%service_del_preun kubicd.service

%postun -n kubicd
%service_del_postun kubicd.service

%files -n kubicd
%license LICENSE
%dir %{_sysconfdir}/kubicd
%dir %{_sysconfdir}/kubicd/pki
%dir %{_datadir}/defaults
%dir %{_datadir}/defaults/kubicd
%{_datadir}/defaults/kubicd/kubicd.conf
%{_datadir}/defaults/kubicd/rbac.conf
%{_sbindir}/kubicd
%{_sbindir}/rckubicd
%{_prefix}/lib/systemd/system/*

%files -n kubicctl
%license LICENSE
%{_bindir}/kubicctl

%files -n kubic-haproxycfg
%license LICENSE
%{_bindir}/haproxycfg

%changelog
