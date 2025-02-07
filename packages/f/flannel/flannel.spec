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
Version:        0.26.4
Release:        0
Summary:        An etcd backed network fabric for containers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/flannel-io/flannel
Source0:        flannel-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:       iproute2
Requires:       iptables
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.23
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
%setup -q -a1 -n flannel-%{version}

%build
%define project github.com/flannel-io/flannel
CGO_ENABLED=1 go build -mod=vendor -v -buildmode=pie -o dist/flanneld \
	  -ldflags '-s -w -X github.com/flannel-io/flannel/pkg/version.Version=v%{version}'

%install
rm -rf %{buildroot}/%{_libdir}/go/contrib

# move the binary
install -D -m 0755 dist/flanneld %{buildroot}%{_sbindir}/flanneld

# Install provided yaml file to download and run the flannel container
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/flannel
install -m 0644 Documentation/kube-flannel.yml %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml
sed -i -e 's|image: docker.io/flannel/flannel:.*|image: %{flannel_container_path}:%{version}|g' %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml
sed -i -e 's|/opt/bin/flanneld|/usr/sbin/flanneld|g' %{buildroot}%{_datadir}/k8s-yaml/flannel/kube-flannel.yaml

%files
%defattr(-,root,root)
%doc README.md DCO
%license LICENSE
%{_sbindir}/flanneld

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/flannel
%{_datarootdir}/k8s-yaml/flannel/kube-flannel.yaml

%changelog
