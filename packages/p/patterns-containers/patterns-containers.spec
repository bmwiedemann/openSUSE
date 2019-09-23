#
# spec file for package patterns-containers
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


Name:           patterns-containers
Version:        5.0
Release:        0
Summary:        Patterns for container technologies
License:        MIT
Group:          Metapackages
Url:            http://en.opensuse.org/Patterns
Source0:        %name-rpmlintrc
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package kubeadm
Summary:        kubeadm Stack
Group:          Metapackages
Provides:       pattern() = kubeadm
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9030
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-kubeadm
Obsoletes:      patterns-caasp-kubeadm <= 4.0
Requires:       autofs
Requires:       ceph-common
Requires:       cilium-k8s-yaml
Requires:       cri-runtime
Requires:       cri-tools
Requires:       flannel-k8s-yaml
Requires:       health-checker-plugins-kubic
Requires:       hello-kubic-k8s-yaml
Requires:       kubernetes-client
Requires:       kubernetes-kubeadm
Requires:       kubernetes-kubeadm-criconfig
Requires:       kubernetes-kubelet
Requires:       kured-k8s-yaml
Requires:       lvm2
Requires:       metallb-k8s-yaml
Requires:       nfs-client
Requires:       rook-k8s-yaml
Requires:       rpcbind
Requires:       weave-k8s-yaml
Requires:       pattern() = basesystem

%description kubeadm
This provides a vanilla kubeadm stack. It contains everything needed to
setup kubernetes using kubeadm.

%package container_runtime
Summary:        Container Runtime for non-clustered systems
Group:          Metapackages
Provides:       pattern() = container_runtime
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9040
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-container-runtime
Obsoletes:      patterns-caasp-container-runtime <= 4.0
Requires:       podman
Requires:       podman-cni-config
Requires:       pattern() = basesystem

%description container_runtime
This pattern installs the default container runtime packages for non-clustered systems.

%package container_runtime_kubernetes
Summary:        Container Runtime for kubernetes clustered systems
Group:          Metapackages
Provides:       pattern() = container_runtime_kubernetes
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9041
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-container-runtime-kubernetes
Obsoletes:      patterns-caasp-container-runtime-kubernetes <= 4.0
Requires:       cri-o
Requires:       cri-o-kubeadm-criconfig
Requires:       pattern() = basesystem

%description container_runtime_kubernetes
This pattern installs the default container runtime packages for kubernetes clustered systems.

%package kubic_admin
Summary:        Kubic Admin Node
Group:          Metapackages
Provides:       pattern() = kubic_admin
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9018
Provides:       pattern-visible()
Requires:       kubicd
Requires:       salt-master
Requires:       yomi-formula
Requires:       pattern() = basesystem
Requires:       pattern() = container_runtime_kubernetes
Requires:       pattern() = kubeadm

%description kubic_admin
This pattern installs the the software required for an openSUSE Kubic Admin Node.

%package kubic_worker
Summary:        Kubic Worker Node
Group:          Metapackages
Provides:       pattern() = kubic_worker
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9019
Provides:       pattern-visible()
Requires:       kubicctl
Requires:       salt-minion
Requires:       pattern() = basesystem
Requires:       pattern() = container_runtime_kubernetes
Requires:       pattern() = kubeadm

%description kubic_worker
This pattern installs the the software required for an openSUSE Kubic Worker Node.

%package kubic_loadbalancer
Summary:        Kubic Loadbalancer Node
Group:          Metapackages
Provides:       pattern() = kubic_loadbalancer
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9020
Provides:       pattern-visible()
Requires:       haproxy
Requires:       salt-minion
Requires:       pattern() = basesystem

%description kubic_loadbalancer
This pattern installs the the software required for an openSUSE Kubic Loadbalancer Node.


%package kubernetes_utilities
Summary:        Utilities to manage kubernetes
Group:          Metapackages
Provides:       pattern() = kubernetes_utilities
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9050
Provides:       pattern-visible()
Requires:       helm
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
mkdir -p %buildroot/usr/share/doc/packages/patterns-containers/
echo 'This file marks the pattern kubeadm to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/kubeadm.txt
echo 'This file marks the pattern container_runtime to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/container_runtime.txt
echo 'This file marks the pattern container_runtime_kubernetes to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/container_runtime_kubernetes.txt
echo 'This file marks the pattern kubic_admin to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/kubic_admin.txt
echo 'This file marks the pattern kubic_worker to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/kubic_worker.txt
echo 'This file marks the pattern kubic_loadbalancer to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/kubic_loadbalancer.txt
echo 'This file marks the pattern kubernetes_utilities to be installed.' >%buildroot/usr/share/doc/packages/patterns-containers/kubernetes_utilities.txt

%files kubeadm
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/kubeadm.txt

%files container_runtime
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/container_runtime.txt

%files container_runtime_kubernetes
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/container_runtime_kubernetes.txt

%files kubic_admin
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/kubic_admin.txt

%files kubic_worker
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/kubic_worker.txt

%files kubic_loadbalancer
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/kubic_loadbalancer.txt

%files kubernetes_utilities
%defattr(-,root,root)
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/kubernetes_utilities.txt

%changelog
