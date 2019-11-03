#
# spec file for package metallb
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


Name:           metallb
Version:        0.8.2
Release:        0
Summary:        Load Balancer for bare metal Kubernetes clusters
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/google/metallb
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.12
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.

%package controller
Summary:        MetalLB controller binary
Group:          System/Management

%description controller
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.
This package contains the controller binary.

%package speaker
Summary:        MetalLB speaker binary
Group:          System/Management

%description speaker
MetalLB is a load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.
This package contains the speaker binary.

%package k8s-yaml
Summary:        Kubernetes yaml file to run MetalLB container
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
MetalLB container in a kubernetes cluster.

%prep
%setup -qa1

%build
go install -v -mod vendor -buildmode=pie ./controller ./speaker

%install
# Install the binary.
mkdir -p %{buildroot}%{_sbindir}/
install -D -m 0755 $HOME/go/bin/controller %{buildroot}%{_sbindir}/
install -D -m 0755 $HOME/go/bin/speaker %{buildroot}%{_sbindir}/

# Install provided yaml file to download and run the kured container
cd manifests
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/metallb
install -m 0644 *.yaml %{buildroot}%{_datadir}/k8s-yaml/metallb
sed -i -e 's|image: metallb/controller.*|image: registry.opensuse.org/kubic/metallb-controller:%{version}|g' %{buildroot}%{_datadir}/k8s-yaml/metallb/metallb.yaml
sed -i -e 's|image: metallb/speaker.*|image: registry.opensuse.org/kubic/metallb-speaker:%{version}|g' %{buildroot}%{_datadir}/k8s-yaml/metallb/metallb.yaml

%files controller
%license LICENSE
%{_sbindir}/controller

%files speaker
%license LICENSE
%{_sbindir}/speaker

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%{_datarootdir}/k8s-yaml/metallb

%changelog
