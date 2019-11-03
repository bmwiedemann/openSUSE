#
# spec file for package flannel
#
# Copyright (c) 2017, 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Use Tumbleweed Kubic containers
%define flannel_container_path registry.opensuse.org/kubic/flannel

Name:           flannel
Version:        0.11.0
Release:        0
Summary:        An etcd backed network fabric for containers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/coreos/flannel
Source:         %{name}-%{version}.tar.gz
Source1:        kube-flannel.yaml
Requires:       iproute2
# arp is used:
Requires:       net-tools-deprecated
Requires:       iptables
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.11
# go1.11.3 contains sec. fixes bsc#1118897(CVE-2018-16873) bsc#1118897(CVE-2018-16873) bsc#1118899(CVE-2018-16875)
BuildRequires:  go1.11 >= 1.11.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390
%{go_nostrip}
%{go_provides}

%description
flannel is a virtual network that gives a subnet to each host for use with
container runtimes.

Platforms like Google's Kubernetes assume that each container (pod) has a
unique, routable IP address inside the cluster. The advantage of this model is that it
reduces the complexity of doing port mapping.

This package contains the binary to be included into a container image

%package k8s-yaml
Summary:        Kubernetes yaml file to run flannel container
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
flannel container in a kubernetes cluster.

flannel is a virtual network that gives a subnet to each host for use with
container runtimes.

Platforms like Google's Kubernetes assume that each container (pod) has a
unique, routable IP address inside the cluster. The advantage of this model is that it
reduces the complexity of doing port mapping.

%prep
%setup -q

%build
gofmt -w -r "x -> \"%{version}\"" version/version.go
%{goprep} github.com/coreos/flannel
%{gobuild}

%install
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib

# Install provided yaml file to download and run the flannel container
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/flannel
#install -m 0644 Documentation/kube-flannel.yml %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml
sed -i -e 's|image: quay.io/coreos/flannel:.*|image: %{flannel_container_path}:%{version}|g' %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml
sed -i -e 's|/opt/bin/flanneld|/usr/sbin/flanneld|g' %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml

# Move
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/flannel %{buildroot}%{_sbindir}/flanneld

%files
%defattr(-,root,root)
%doc README.md DCO NOTICE
%license LICENSE
%{_sbindir}/flanneld

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/flannel
%{_datarootdir}/k8s-yaml/flannel/kube-flannel.yaml

%changelog
