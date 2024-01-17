#
# spec file for package patterns-kubernetes
#
# Copyright (c) 2023 SUSE LLC
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


Name:           patterns-kubernetes
Version:        5.1
Release:        0
Summary:        Patterns for kubernetes technologies
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name-rpmlintrc
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package kubeadm
Summary:        Kubernetes kubeadm Stack
Group:          Metapackages
Provides:       pattern() = kubeadm
Provides:       pattern-category() = Kubernetes
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9040
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-kubeadm
Obsoletes:      patterns-caasp-kubeadm <= 4.0
#Obsolete patterns-containers Patterns
Provides:       patterns-containers-kubeadm
Obsoletes:      patterns-containers-kubeadm <= 5.0
Requires:       autofs
Requires:       busybox-k8s-yaml
Requires:       ceph-common
Requires:       cri-runtime
Requires:       cri-tools
Requires:       flannel-k8s-yaml
Requires:       health-checker-plugins-kubic
Requires:       hello-kubic-k8s-yaml
Requires:       helm
Requires:       kuberlr
Requires:       kubernetes-client
Requires:       kubernetes-kubeadm
Requires:       kubernetes-kubeadm-criconfig
Requires:       kubernetes-kubelet
Requires:       kured-k8s-yaml
Requires:       lvm2
Requires:       metallb-k8s-yaml
Requires:       nfs-client
Requires:       nfs-client-provisioner-k8s-yaml
# ExclusiveArch in the rook package
%ifarch x86_64 aarch64
Requires:       rook-k8s-yaml
%endif
Requires:       rpcbind
Requires:       weave-k8s-yaml
Requires:       pattern() = basesystem

%description kubeadm
This provides a vanilla kubeadm stack. It contains everything needed to
setup kubernetes using kubeadm.

%package container_runtime_kubernetes
Summary:        Container Runtime for kubernetes clustered systems
Group:          Metapackages
Provides:       pattern() = container_runtime_kubernetes
Provides:       pattern-category() = Kubernetes
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9041
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-container-runtime-kubernetes
Obsoletes:      patterns-caasp-container-runtime-kubernetes <= 4.0
#Obsolete patterns-containers Patterns
Provides:       patterns-containers-container-runtime-kubernetes
Obsoletes:      patterns-containers-container-runtime-kubernetes <= 5.0
Requires:       cri-o
Requires:       cri-o-kubeadm-criconfig
Requires:       pattern() = basesystem

%description container_runtime_kubernetes
This pattern installs the default container runtime packages for kubernetes clustered systems.

%package kubernetes_utilities
Summary:        Utilities to manage kubernetes
Group:          Metapackages
#Obsolete patterns-containers Patterns
Provides:       patterns-containers-kubernetes-utilities
Obsoletes:      patterns-containers-kubernetes-utilities <= 5.0
Provides:       pattern() = kubernetes_utilities
Provides:       pattern-category() = Kubernetes
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9050
Provides:       pattern-visible()
Requires:       helm
Requires:       k9s
Requires:       kail
Requires:       kubectl-who-can
Requires:       rakkess
Requires:       rbac-lookup
Requires:       reg
Requires:       pattern() = basesystem

%description kubernetes_utilities
This pattern installs utilities helpful to manage kubernetes.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %buildroot/usr/share/doc/packages/patterns-kubernetes/
echo 'This file marks the pattern kubeadm to be installed.' >%buildroot/usr/share/doc/packages/patterns-kubernetes/kubeadm.txt
echo 'This file marks the pattern container_runtime_kubernetes to be installed.' >%buildroot/usr/share/doc/packages/patterns-kubernetes/container_runtime_kubernetes.txt
# Kubic specific packages shouldn't build for SLE/Leap
echo 'This file marks the pattern kubernetes_utilities to be installed.' >%buildroot/usr/share/doc/packages/patterns-kubernetes/kubernetes_utilities.txt

%files kubeadm
%defattr(-,root,root)
%dir %{_docdir}/patterns-kubernetes
%{_docdir}/patterns-kubernetes/kubeadm.txt

%files container_runtime_kubernetes
%defattr(-,root,root)
%dir %{_docdir}/patterns-kubernetes
%{_docdir}/patterns-kubernetes/container_runtime_kubernetes.txt

%files kubernetes_utilities
%defattr(-,root,root)
%dir %{_docdir}/patterns-kubernetes
%{_docdir}/patterns-kubernetes/kubernetes_utilities.txt

%changelog
