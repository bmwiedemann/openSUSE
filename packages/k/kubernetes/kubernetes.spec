#
# spec file for package kubernetes
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


%{!?tmpfiles_create:%global tmpfiles_create systemd-tmpfiles --create}
# baseversion - version of kubernetes for this package
%define baseversion 1.15
# maxcriversion - version of cri-tools which is notsupported by this version of kubeadm.
%define maxcriversion 1.16
Name:           kubernetes
Version:        %{baseversion}.2
Release:        0
Summary:        Container Scheduling and Management
License:        Apache-2.0
Group:          System/Management
URL:            http://kubernetes.io
Source:         %{name}-%{version}.tar.xz
Source2:        genmanpages.sh
#systemd services
Source10:       kube-apiserver.service
Source11:       kube-controller-manager.service
Source12:       kubelet.service
Source13:       kube-proxy.service
Source14:       kube-scheduler.service
#config files
Source23:       kubeadm.conf
Source24:       50-kubeadm.conf
Source25:       10-kubeadm.conf
Source26:       kubernetes.tmp.conf
Source27:       kubelet.tmp.conf
Source28:       kubernetes-rpmlintrc
Source29:       kubernetes.obsinfo
# Patch to fix cgroup error in k8s 1.15.0 - should already be in 1.15.1
Patch1:         fix-cgroup-kubeadm.patch
# Patch to change the default registry to registry.opensuse.org/kubic
Patch2:         kubeadm-opensuse-registry.patch
# Patch to change the version check server to kubic.opensuse.org
Patch3:         opensuse-version-checks.patch
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  go-go-md2man
# Kubernetes 1.15.0 requires at least go 1.12.5 (see changelog)
BuildRequires:  golang(API) = 1.12
BuildRequires:  go >= 1.12.5
BuildRequires:  golang(github.com/jteeuwen/go-bindata)
BuildRequires:  golang-packaging
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
ExcludeArch:    %{ix86} s390
%{go_nostrip}
%{go_provides}

%description
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

It groups containers that make up an application into logical units
for management and discovery.

%if !0%{?is_opensuse}
# package layout for CaaSP

%package common
Summary:        Kubernetes common files
Group:          System/Management

%description common
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

This subpackage contains the Kubernetes common files.

%endif

%package master
Summary:        Kubernetes services for master host
Group:          System/Management
%if !0%{?is_opensuse}
Requires:       kubernetes-common = %{version}-%{release}
%endif
Requires(pre):  shadow
# if the master is installed with node, version and release must be the same
Conflicts:      kubernetes-node < %{version}-%{release}
Conflicts:      kubernetes-node > %{version}-%{release}
%{?systemd_requires}
%if 0%{?suse_version}
Recommends:     kubernetes-client = %{version}-%{release}
%endif

%description master
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

This subpackage contains the Kubernetes services for master hosts.


%if 0%{?is_opensuse}
# packages to build containerized control plane

%package apiserver
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Conflicts:      kubernetes-common
Conflicts:      kubernetes-master

%description apiserver
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Conflicts:      kubernetes-common
Conflicts:      kubernetes-master

%description controller-manager
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Conflicts:      kubernetes-common
Conflicts:      kubernetes-master

%description scheduler
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy
Summary:        Kubernetes proxy for container image
Group:          System/Management
Requires:       conntrack-tools
Requires:       ebtables
Requires:       ipset
Requires:       iptables
Conflicts:      kubernetes-node

%description proxy
This subpackage contains the kube-proxy binary for Kubic images

%endif

%package kubelet
Summary:        Kubernetes kubelet daemon
Group:          System/Management
Requires:       cri-runtime
%if !0%{?is_opensuse}
Requires:       kubernetes-common = %{version}-%{release}
%endif
# if master is installed with node, version and release must be the same
Conflicts:      kubernetes-master < %{version}-%{release}
Conflicts:      kubernetes-master > %{version}-%{release}
%{?systemd_requires}

%description kubelet
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubelet daemon

%package kubeadm
Summary:        Kubernetes kubeadm bootstrapping tool
Group:          System/Management
Requires:       cri-runtime
# Kubeadm 1.15.0 requires cri-tools 1.14.0 or higher (see changelog)
Requires:       cri-tools >= 1.14.0
Requires:       ebtables
Requires:       ethtool
Requires:       kubernetes-kubeadm-criconfig
# Kubeadm 1.15.2 requires kubernetes-kubelet from 1.14.0 to 1.15.2
# kubeadm accepts the previous version. This is important for performing upgrades
# because we can update kubeadm first, and then kubelet.
Requires:       kubernetes-kubelet >= 1.14.0
Requires:       socat
Requires(pre):  shadow
Conflicts:      kubernetes-kubelet > %{version}-%{release}
Conflicts:      cri-tools >= %{maxcriversion}
# if master is installed with node, version and release must be the same
Conflicts:      kubernetes-master < %{version}-%{release}
Conflicts:      kubernetes-master > %{version}-%{release}

%description kubeadm
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubeadm bootstrapping tool

%package node
Summary:        Kubernetes services for node host
Group:          System/Management
Requires:       conntrack-tools
Requires:       cri-runtime
Requires:       ethtool
Requires:       iptables
%if !0%{?is_opensuse}
Requires:       kubernetes-common = %{version}-%{release}
%endif
Requires:       kubernetes-kubelet = %{version}-%{release}
Requires:       socat
Requires(pre):  shadow
# if master is installed with node, version and release must be the same
Conflicts:      kubernetes-master < %{version}-%{release}
Conflicts:      kubernetes-master > %{version}-%{release}
%{?systemd_requires}

%description node
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

This subpackage contains the Kubernetes services for node hosts.

%package client
Summary:        Kubernetes client tools
Group:          System/Management
%if 0%{?is_opensuse}
Recommends: bash-completion
%else
Requires:       bash-completion
Requires:       kubernetes-common = %{version}-%{release}
%endif

%description client
Kubernetes client tools like kubectl.

%package extra
Summary:        Kubernetes extra resources
Group:          System/Management
Requires:       go

%description extra
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

This subpackage contains Kubernetes extra resources: cluster
providers, demos, testsuite...

%prep
%setup -q
%patch1 -p1
%if 0%{?is_opensuse}
%patch2 -p0
%patch3 -p1
%endif
%{goprep} github.com/kubernetes/kubernetes

%build
# This is fixing bug bsc#1065972
export KUBE_GIT_COMMIT=$(grep "commit:" %{SOURCE29} | cut -d ":" -f2 | tr -d " ")
# KUBE_GIT_TREE_STATE="clean" indicates no changes since the git commit id
# KUBE_GIT_TREE_STATE="dirty" indicates source code changes after the git commit id
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_VERSION=v%{version}

# https://bugzilla.redhat.com/show_bug.cgi?id=1392922#c1
%ifarch ppc64le
export GOLDFLAGS='-linkmode=external'
%endif
%if 0%{?is_opensuse}
make %{?_smp_mflags} WHAT="cmd/kube-apiserver cmd/kube-controller-manager cmd/kube-scheduler cmd/kube-proxy cmd/kubelet cmd/kubectl cmd/kubeadm test/e2e/e2e.test"
%else
make %{?_smp_mflags} WHAT="cmd/hyperkube cmd/kubeadm test/e2e/e2e.test"
%endif
make %{?_smp_mflags} ginkgo

# The majority of the documentation has already been moved into
# http://kubernetes.io/docs/admin, and most of the files stored in the `docs`
# directory simply point there. That being said, some of the files are actual
# man pages, but they have to be generated with `hack/generate-docs.sh`. So,
# let's do that and run `genmanpages.sh`.
./hack/generate-docs.sh || true
pushd docs
pushd admin
cp kube-apiserver.md kube-controller-manager.md kube-proxy.md kube-scheduler.md kubelet.md ..
popd
cp %{SOURCE2} genmanpages.sh
bash genmanpages.sh
popd

%install

%ifarch ppc64le aarch64
output_path="_output/local/go/bin"
%else
output_path="_output/local/bin/linux/%{go_arch}"
%endif

install -m 755 -d %{buildroot}%{_bindir}

echo "+++ INSTALLING kubeadm"
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubeadm

binaries=(kube-apiserver kube-controller-manager kube-scheduler kube-proxy kubelet kubectl)
%if 0%{?is_opensuse}
for bin in "${binaries[@]}"; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/${bin}
done

%else
echo "+++ INSTALLING hyperkube"
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/hyperkube

for bin in "${binaries[@]}"; do
  echo "+++ HARDLINKING ${bin} to hyperkube"
  ln %{buildroot}%{_bindir}/hyperkube %{buildroot}%{_bindir}/${bin}
done
%endif

# install the bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl

# cleanup before copying dirs...
rm -f hack/.linted_packages
find .    -name '.gitignore' -type f -delete
find hack -name '*.sh.orig' -type f -delete
find hack -name '.golint_*' -type f -delete

# install extra things (needed for e2e tests)
kubernetes_src=%{buildroot}%{_usrsrc}/kubernetes
install -m 755 -d ${kubernetes_src}
cp -R cluster hack test ${kubernetes_src}/

# install things needed for running the e2e tests
install -d -m 0755 ${kubernetes_src}/platforms/linux/%{go_arch}
for exe in ginkgo e2e.test ; do
  install -p -m 755 -D -t ${kubernetes_src}/platforms/linux/%{go_arch}/ ${output_path}/${exe}
done

# systemd service
install -d -m 0755 %{buildroot}%{_unitdir}
for src in %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} ; do
  install -m 0644 -t %{buildroot}%{_unitdir}/ "$src"
done

# make symlinks to rc files
install -d -m 0755 %{buildroot}%{_sbindir}
for rc in kube-proxy kubelet kube-apiserver kube-controller-manager kube-scheduler ; do
  ln -sf service "%{buildroot}%{_sbindir}/rc$rc"
done

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/* %{buildroot}%{_mandir}/man1

# create config folder
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}

# manifests file for the kubelet
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/manifests

# place kubernetes.tmp.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -D -m 0644 %{SOURCE26} %{buildroot}/%{_tmpfilesdir}/kubernetes.conf
install -D -m 0644 %{SOURCE27} %{buildroot}/%{_tmpfilesdir}/kubelet.conf

# install the place the kubelet defaults to put volumes
install -d %{buildroot}%{_localstatedir}/lib/kubelet

# install VolumePluginDir (bsc#1084766)
%define volume_plugin_dir %{_localstatedir}/lib/kubelet/volume-plugin
install -d %{buildroot}/%{volume_plugin_dir}

# Remove dangling symlink (breaks post-build scripts)
rm -f %{buildroot}%{_usrsrc}/kubernetes/hack/autogenerated_placeholder.txt

# Add kubeadm modprobe.d and sysctl.d drop-in configs
mkdir -p %{buildroot}%{_libexecdir}/modules-load.d
mkdir -p %{buildroot}%{_sysctldir}
install -m 0644 -t %{buildroot}%{_libexecdir}/modules-load.d/ %{SOURCE23}
install -m 0644 -t %{buildroot}%{_sysctldir} %{SOURCE24}

# Create kubeadm systemd unit drop-in
install -d -m 0755 %{buildroot}%{_unitdir}/kubelet.service.d
sed -i -e 's|PATH_TO_FLEXVOLUME|%{volume_plugin_dir}|g' %{SOURCE25}
install -m 0644 -t %{buildroot}%{_unitdir}/kubelet.service.d/ %{SOURCE25}

%fdupes -s %{buildroot}

%pre master
getent group kube >/dev/null || groupadd -r kube
getent passwd kube >/dev/null || useradd -r -g kube -d / -s /sbin/nologin \
        -c "Kubernetes user" kube
%service_add_pre kube-apiserver.service kube-controller-manager.service kube-scheduler.service

mkdir -p -m 755 %{_localstatedir}/lib/kubernetes
chown -R kube %{_localstatedir}/lib/kubernetes
chgrp -R kube %{_localstatedir}/lib/kubernetes

%post master
%service_add_post kube-apiserver.service kube-controller-manager.service kube-scheduler.service
%tmpfiles_create %{_tmpfilesdir}/kubernetes.conf

%preun master
%service_del_preun kube-apiserver.service kube-controller-manager.service kube-scheduler.service

%postun master
%service_del_postun kube-apiserver.service kube-controller-manager.service kube-scheduler.service

%pre kubelet
%service_add_pre kubelet.service

%post kubelet
%service_add_post kubelet.service
%if 0%{?suse_version} < 1500
# create some subvolumes needed by CNI
if [ ! -e %{_localstatedir}/lib/cni ]; then
  if [ "`findmnt -o FSTYPE -l  /|grep -v FSTYPE`" = "btrfs" ]; then
    %{_sbindir}/mksubvolume %{_localstatedir}/lib/cni
  fi
fi
%endif
%tmpfiles_create %{_tmpfilesdir}/kubelet.conf

%preun kubelet
%service_del_preun kubelet.service

%postun kubelet
%service_del_postun kubelet.service

%pre node
%service_add_pre kube-proxy.service

%post node
%service_add_post kube-proxy.service

%preun node
%service_del_preun kube-proxy.service

%postun node
%service_del_postun kube-proxy.service

%if !0%{?is_opensuse}
%files common
%{_bindir}/hyperkube
%endif

%files master
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kube-apiserver.1%{?ext_man}
%{_mandir}/man1/kube-controller-manager.1%{?ext_man}
%{_mandir}/man1/kube-scheduler.1%{?ext_man}
%{_mandir}/man1/cloud-controller-manager.1%{?ext_man}
%{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-scheduler.service
%{_sbindir}/rckube-apiserver
%{_sbindir}/rckube-controller-manager
%{_sbindir}/rckube-scheduler
%attr(0750,root,root) %dir %ghost %{_rundir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_tmpfilesdir}/kubernetes.conf


%if 0%{?is_opensuse}
# openSUSE is using kubeadm with containerizied control plane, we
# only need the binaries

%files apiserver
%license LICENSE
%{_bindir}/kube-apiserver

%files controller-manager
%license LICENSE
%{_bindir}/kube-controller-manager

%files scheduler
%license LICENSE
%{_bindir}/kube-scheduler

%files proxy
%license LICENSE
%{_bindir}/kube-proxy

%endif

%files kubelet
%doc README.md CONTRIBUTING.md CHANGELOG-%{baseversion}.md
%license LICENSE
%{_mandir}/man1/kubelet.1%{?ext_man}
%{_bindir}/kubelet
%{_unitdir}/kubelet.service
%dir %{_unitdir}/kubelet.service.d
%{_sbindir}/rckubelet
%dir %{_localstatedir}/lib/kubelet
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/manifests
%{_tmpfilesdir}/kubelet.conf
%attr(0750,root,root) %dir %ghost %{_rundir}/%{name}
%dir %{volume_plugin_dir}

%files kubeadm
%doc README.md CONTRIBUTING.md CHANGELOG-%{baseversion}.md
%{_unitdir}/kubelet.service.d/10-kubeadm.conf
%dir %{_libexecdir}/modules-load.d
%{_libexecdir}/modules-load.d/kubeadm.conf
%{_sysctldir}/50-kubeadm.conf
%license LICENSE
%{_bindir}/kubeadm
%{_mandir}/man1/kubeadm*

%files node
%doc README.md CONTRIBUTING.md CHANGELOG-%{baseversion}.md
%license LICENSE
%{_mandir}/man1/kube-proxy.1%{?ext_man}
%{_bindir}/kube-proxy
%{_unitdir}/kube-proxy.service
%{_sbindir}/rckube-proxy
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/manifests

%files client
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kubectl.1%{?ext_man}
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl

%files extra
%dir %{_usrsrc}/kubernetes
%dir %{_usrsrc}/kubernetes/cluster
%dir %{_usrsrc}/kubernetes/hack
%dir %{_usrsrc}/kubernetes/test
%dir %{_usrsrc}/kubernetes/platforms
%{_usrsrc}/kubernetes/cluster/*
%{_usrsrc}/kubernetes/test/*
%{_usrsrc}/kubernetes/hack/*
%{_usrsrc}/kubernetes/hack/.*
%{_usrsrc}/kubernetes/platforms/*

%changelog
