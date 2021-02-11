#
# spec file for package nfs-client-provisioner
#
# Copyright (c) 2021 SUSE LLC
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


Name:           nfs-client-provisioner
Version:        4.0.0+git20210204.23ecb30
Release:        0
Summary:        Automatic provisioner using an existing and already configured NFS server
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner
Source0:        nfs-client-provisioner-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.15

%description
nfs-client is an automatic provisioner that uses an existing and already configured NFS server to support dynamic provisioning of Kubernetes Persistent Volumes via Persistent Volume Claims. Persistent volumes are provisioned as ${namespace}-${pvcName}-${pvName}.


%package k8s-yaml
Summary:        Yaml file to deploy nfs-client-provisioner

%description k8s-yaml
Yaml files to deploy the nfs-client-provisioner. nfs-client is an automatic provisioner that uses an existing and already configured NFS server to support dynamic provisioning of Kubernetes Persistent Volumes via Persistent Volume Claims. Persistent volumes are provisioned as ${namespace}-${pvcName}-${pvName}.

%prep
%setup -q -a1

%build
go build -mod vendor -buildmode=pie -o nfs-client-provisioner ./cmd/nfs-subdir-external-provisioner

%install
mkdir -p %{buildroot}%{_sbindir}
cp -av nfs-client-provisioner %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/test
cp -av deploy/*.yaml %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner
mv %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/test-*.yaml %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/test/
rm %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/deployment-arm.yaml
sed -i -e 's|quay.io/external_storage/nfs-client-provisioner:latest|registry.opensuse.org/kubic/nfs-client-provisioner:latest|g' %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/deployment.yaml
sed -i -e 's|gcr.io/google_containers/busybox:.*|registry.opensuse.org/opensuse/busybox:latest|g' %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/test/test-pod.yaml
echo -e "resources:\n- class.yaml\n- deployment.yaml\n- rbac.yaml" > %{buildroot}%{_datadir}/k8s-yaml/nfs-client-provisioner/kustomization.yaml

%files
%{_sbindir}/nfs-client-provisioner

%files k8s-yaml
%dir %{_datadir}/k8s-yaml
%dir %{_datadir}/k8s-yaml/nfs-client-provisioner
%dir %{_datadir}/k8s-yaml/nfs-client-provisioner/test
%{_datadir}/k8s-yaml/nfs-client-provisioner/*.yaml
%{_datadir}/k8s-yaml/nfs-client-provisioner/test/*.yaml

%changelog
