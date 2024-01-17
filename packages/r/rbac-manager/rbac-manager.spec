#
# spec file for package rbac-manager
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
# nodebuginfo


Name:           rbac-manager
Version:        1.4.2
Release:        0
Summary:        Kubernetes operator for easier RBAC management
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/FairwindsOps/rbac-manager
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.17
ExcludeArch:    s390
ExcludeArch:    %{ix86}
%{go_nostrip}

%description
RBAC Manager is designed to simplify authorization in Kubernetes.
This is an operator that supports declarative configuration for RBAC with new custom resources.
Instead of managing role bindings or service accounts directly, you can specify a desired state and RBAC Manager will make the necessary changes to achieve that state.

%package k8s-yaml
Summary:        Kubernetes yaml file to run rbac-manager
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
rbac-manager in a kubernetes cluster.

%prep
%setup -qa1

%build
go build -mod vendor -buildmode=pie -a -o rbac-manager ./cmd/manager/main.go

%check
make test

%install
mkdir -p %{buildroot}%{_sbindir}/
install -D -m 0755 rbac-manager %{buildroot}%{_sbindir}/

# Install provided yaml file to download and run the rbac-manager
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/rbac-manager
install -m 0644 deploy/0_namespace.yaml %{buildroot}%{_datadir}/k8s-yaml/rbac-manager
install -m 0644 deploy/1_rbac.yaml %{buildroot}%{_datadir}/k8s-yaml/rbac-manager
install -m 0644 deploy/2_crd.yaml %{buildroot}%{_datadir}/k8s-yaml/rbac-manager
install -m 0644 deploy/3_deployment.yaml %{buildroot}%{_datadir}/k8s-yaml/rbac-manager
sed -i -e 's|image: "quay.io/reactiveops/rbac-manager:.*|image: "kubic/rbac-manager:%{version}"|g' %{buildroot}%{_datadir}/k8s-yaml/rbac-manager/3_deployment.yaml

%files
%license LICENSE
%doc docs/* examples
%{_sbindir}/rbac-manager

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%{_datarootdir}/k8s-yaml/rbac-manager

%changelog
