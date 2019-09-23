#
# spec file for package ovnkube
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global provider        github
%global provider_tld    com
%global project         ovn-org
%global repo            ovn-kubernetes
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define cni_bin_dir     %{_libexecdir}/cni

Name:           ovnkube
Version:        v0.3.11+20190912
Release:        0
Summary:        Kubernetes integration for Open Virtual Network (OVN)
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/ovn-org/ovn-kubernetes
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.8
Requires:       openvswitch
Requires:       openvswitch-ovn-common
Requires:       openvswitch-ovn-central
Requires:       openvswitch-ovn-host
Requires:       openvswitch-ovn-vtep

%description
ovnkube is the project which integrates Open Virtual Network (OVN) with
Kubernetes.

%package cni
Summary:        CNI plugin for Open Virtual Network (OVN)
Group:          System/Management
Requires:       cni
Requires:       cni-plugins
Requires:       ovnkube

%description cni
ovnkube is the project which integrates Open Virtual Network (OVN) with
Kubernetes.

This package provides a CNI (Container Network Interface) plugin for Cilium.

%prep
%setup -q

%build
cd go-controller
make

%install
pushd go-controller
install -D -m 755 _output/go/bin/ovnkube %{buildroot}%{_bindir}/ovnkube
install -D -m 755 _output/go/bin/ovn-kube-util %{buildroot}%{_bindir}/ovn-kube-util
install -D -m 755 _output/go/bin/ovn-k8s-cni-overlay %{buildroot}%{cni_bin_dir}/ovn-k8s-cni-overlay
popd
install -D -m 644 ./dist/ansible/hosts -t %{buildroot}%{_datadir}/k8s-yaml/%{name}/ansible
install -D -m 755 ./dist/images/daemonset.sh -t %{buildroot}%{_datadir}/k8s-yaml/%{name}/images
install -D -m 644 ./dist/templates/* -t %{buildroot}%{_datadir}/k8s-yaml/%{name}/templates
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/%{name}/yaml

%files
%license LICENSE
%doc README.md
%{_bindir}/ovn-kube-util
%{_bindir}/ovnkube
%dir %{_datadir}/k8s-yaml
%dir %{_datadir}/k8s-yaml/%{name}
%dir %{_datadir}/k8s-yaml/%{name}/ansible
%{_datadir}/k8s-yaml/%{name}/ansible/hosts
%dir %{_datadir}/k8s-yaml/%{name}/images
%{_datadir}/k8s-yaml/%{name}/images/daemonset.sh
%dir %{_datadir}/k8s-yaml/%{name}/templates
%{_datadir}/k8s-yaml/%{name}/templates/cleanup-ovn-cni.conf.j2
%{_datadir}/k8s-yaml/%{name}/templates/ovn-setup.yaml.j2
%{_datadir}/k8s-yaml/%{name}/templates/ovnkube-db-vip.yaml.j2
%{_datadir}/k8s-yaml/%{name}/templates/ovnkube-db.yaml.j2
%{_datadir}/k8s-yaml/%{name}/templates/ovnkube-master.yaml.j2
%{_datadir}/k8s-yaml/%{name}/templates/ovnkube-node.yaml.j2
%dir %{_datadir}/k8s-yaml/%{name}/yaml

%files cni
%{cni_bin_dir}
%{cni_bin_dir}/ovn-k8s-cni-overlay

%changelog

