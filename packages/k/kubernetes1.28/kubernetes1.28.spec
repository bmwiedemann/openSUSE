#
# spec file for package kubernetes1.28
#
# Copyright (c) 2024 SUSE LLC
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
%define baseversion 1.28
%define baseversionminus1 1.27

Name:           kubernetes%{baseversion}
Version:        1.28.11
Release:        0
Summary:        Container Scheduling and Management
License:        Apache-2.0
Group:          System/Management
URL:            https://kubernetes.io/
Source:         kubernetes-%{version}.tar.xz
Source2:        genmanpages.sh
Source3:        kubelet.sh
#systemd services
Source10:       kubelet.service
#config files
Source22:       sysconfig.kubelet-kubernetes
Source23:       kubeadm.conf
Source24:       90-kubeadm.conf
Source25:       10-kubeadm.conf
Source27:       kubelet.tmp.conf
Source28:       kubernetes-rpmlintrc
Source29:       kubernetes.obsinfo
# Patch to change the default registry to registry.opensuse.org/kubic
Patch2:         kubeadm-opensuse-registry.patch
# Patch to change the version check server to kubic.opensuse.org
Patch3:         opensuse-version-checks.patch
# Patch to change the default flexvolume path in kubeadm to match that used by our kubelet, else kubeadm tries to write to /usr when kubelet is already looking at a path on /var thanks to the fix to bsc#1084766
Patch4:         kubeadm-opensuse-flexvolume.patch
# Patch to revert renaming of coredns image location to match how it's done on download.opensuse.org
Patch5:         revert-coredns-image-renaming.patch
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  go >= 1.21.11
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) = 1.21
BuildRequires:  golang(github.com/jteeuwen/go-bindata)
ExcludeArch:    %{ix86} s390 ppc64

%description
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

It groups containers that make up an application into logical units
for management and discovery.















# packages to build containerized control plane

%package apiserver
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Provides:       kubernetes-apiserver-provider = %{version}
Conflicts:      kubernetes-apiserver-provider

%description apiserver
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Provides:       kubernetes-controller-manager-provider = %{version}
Conflicts:      kubernetes-controller-manager-provider

%description controller-manager
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Provides:       kubernetes-scheduler-provider = %{version}
Conflicts:      kubernetes-scheduler-provider

%description scheduler
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy
Summary:        Kubernetes proxy for container image
Group:          System/Management
Provides:       kubernetes-proxy-provider = %{version}
Conflicts:      kubernetes-proxy-provider
Requires:       conntrack-tools
Requires:       ebtables
Requires:       ipset
Requires:       iptables

%description proxy
This subpackage contains the kube-proxy binary for Kubic images

%package kubelet
Summary:        Kubernetes kubelet daemon
Group:          System/Management
Requires:       cri-runtime
Requires:       kubernetes-kubelet-common
Recommends:     kubernetes-kubelet-common = %{version}
Provides:       kubernetes-kubelet%{baseversion} = %{version}
Obsoletes:      kubernetes-kubelet%{baseversion} < %{version}
%{?systemd_requires}

%description kubelet
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubelet daemon (current version)

%package kubelet-common
Summary:        Kubernetes kubelet daemon
Group:          System/Management
Requires:       cri-runtime
Requires:       kubernetes-kubelet%{baseversion}
Provides:       kubernetes-kubelet-common = %{version}
Conflicts:      kubernetes-kubelet-common

%description kubelet-common
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubelet daemon

%package kubeadm
Summary:        Kubernetes kubeadm bootstrapping tool
Group:          System/Management
Provides:       kubernetes-kubeadm-provider = %{version}
Conflicts:      kubernetes-kubeadm-provider
Obsoletes:      kubernetes%{baseversionminus1}-kubeadm
Requires:       cri-runtime
Requires:       cri-tools
Requires:       ebtables
Requires:       ethtool
Requires:       kubernetes-kubeadm-criconfig
Requires:       socat
Requires(pre):  shadow
Requires:       (kubernetes%{baseversion}-kubelet or kubernetes%{baseversionminus1}-kubelet)
Recommends:     kubernetes%{baseversion}-kubelet

%description kubeadm
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubeadm bootstrapping tool

%package client
Summary:        Kubernetes client tools
Group:          System/Management
Provides:       kubernetes-client-provider = %{version}
Requires:       kubernetes%{baseversion}-client-common
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description client
Kubernetes client tools like kubectl.

%package client-common
Summary:        Kubernetes client tools common files
Group:          System/Management
Requires:       kubernetes%{baseversion}-client
Provides:       kubernetes-client-common = %{version}
Conflicts:      kubernetes-client-common
Recommends:     bash-completion

%description client-common
Kubernetes client tools common files

%package client-bash-completion
Summary:        Bash Completion for %{name}-client
Group:          System/Shells
BuildRequires:  bash-completion
Requires:       bash-completion
Requires:       kubernetes%{baseversion}-client = %{version}
Supplements:    (kubernetes%{baseversion}-client and bash-completion)
BuildArch:      noarch
Obsoletes:      kubernetes%{baseversionminus1}-client-bash-completion
Provides:       kubernetes-client-bash-completion = %{version}
Conflicts:      kubernetes-client-bash-completion

%description client-bash-completion
Bash command line completion support for %{name}-client

%package client-fish-completion
Summary:        Fish Completion for %{name}-client
Group:          System/Shells
BuildRequires:  fish
Requires:       kubernetes%{baseversion}-client = %{version}
Supplements:    (kubernetes%{baseversion}-client and fish)
BuildArch:      noarch
Obsoletes:      kubernetes%{baseversionminus1}-client-fish-completion
Provides:       kubernetes-client-fish-completion = %{version}
Conflicts:      kubernetes-client-fish-completion

%description client-fish-completion
Fish command line completion support for %{name}-client.

%prep
%setup -q -n kubernetes-%{version}
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p0
%patch -P 5 -p1

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

#TEST
export FORCE_HOST_GO=y
make WHAT="cmd/kube-apiserver cmd/kube-controller-manager cmd/kube-scheduler cmd/kube-proxy cmd/kubelet cmd/kubectl cmd/kubeadm" GOFLAGS="-buildmode=pie"

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

binaries=(kube-apiserver kube-controller-manager kube-scheduler kube-proxy)
for bin in "${binaries[@]}"; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/${bin}
done

for bin in kubelet kubectl; do
  echo "+++ INSTALLING ${bin} with %{baseversion} suffix"
  install -p -m 755 ${output_path}/${bin} %{buildroot}%{_bindir}/${bin}%{baseversion}
done

echo "+++ INSTALLING kubelet multi-version loader"
install -p -m 755 %{SOURCE3} %{buildroot}%{_bindir}/kubelet

# create sysconfig.kubelet-kubernetes in fullupdir
sed -i -e 's|BASE_VERSION|%{baseversion}|g' %{SOURCE22}
install -D -m 0644 %{SOURCE22} %{buildroot}%{_fillupdir}/sysconfig.kubelet-kubernetes%{baseversion}

# install the bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/kubectl%{baseversion} completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl

# install the fish completion
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/kubectl%{baseversion} completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/kubectl.fish

# move CHANGELOG-%{baseversion}.md to old location
mv CHANGELOG/CHANGELOG-%{baseversion}.md .

# cleanup before copying dirs...
rm -f hack/.linted_packages
find .    -name '.gitignore' -type f -delete
find hack -name '*.sh.orig' -type f -delete
find hack -name '.golint_*' -type f -delete

# systemd service
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir}/ %{SOURCE10}

# make symlinks to rc files
install -d -m 0755 %{buildroot}%{_sbindir}
ln -sf service "%{buildroot}%{_sbindir}/rckubelet"

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/* %{buildroot}%{_mandir}/man1

# create config folder
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}

# manifests file for the kubelet
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/manifests

# place kubernetes.tmp.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -D -m 0644 %{SOURCE27} %{buildroot}/%{_tmpfilesdir}/kubelet.conf

# install the place the kubelet defaults to put volumes
install -d %{buildroot}%{_localstatedir}/lib/kubelet

%define volume_plugin_dir %{_localstatedir}/lib/kubelet/volume-plugin
install -d %{buildroot}/%{volume_plugin_dir}

# Add kubeadm modprobe.d and sysctl.d drop-in configs
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d
mkdir -p %{buildroot}%{_sysctldir}
install -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE23}
install -m 0644 -t %{buildroot}%{_sysctldir} %{SOURCE24}

# Create kubeadm systemd unit drop-in
install -d -m 0755 %{buildroot}%{_unitdir}/kubelet.service.d
sed -i -e 's|PATH_TO_FLEXVOLUME|%{volume_plugin_dir}|g' %{SOURCE25}
install -m 0644 -t %{buildroot}%{_unitdir}/kubelet.service.d/ %{SOURCE25}

# alternatives
ln -s -f %{_sysconfdir}/alternatives/kubectl %{buildroot}%{_bindir}/kubectl

%fdupes -s %{buildroot}

%post client-common
%{_sbindir}/update-alternatives \
  --install %{_bindir}/kubectl kubectl %{_bindir}/kubectl%{baseversion} %(echo %{baseversion} | tr -d .)

%postun client-common
if [ ! -f %{_bindir}/kubectl%{baseversion} ] ; then
  update-alternatives --remove kubectl %{_bindir}/kubectl%{baseversion}
fi

%pre kubelet-common
%service_add_pre kubelet.service

%post kubelet-common
%fillup_only -an kubelet
# Check if /etc/sysconfig/kubelet exists
if [ -e "/etc/sysconfig/kubelet" ]; then
  # Extract the value from the fillup file
  UPDATED_KUBELET_VER=$(grep '^KUBELET_VER=' %{_fillupdir}/sysconfig.kubelet-kubernetes%{baseversion} | cut -d '=' -f2)
  # Update the value in the sysconfig file
  sed -i "s/^KUBELET_VER=.*/KUBELET_VER=$UPDATED_KUBELET_VER/" /etc/sysconfig/kubelet
fi
%service_add_post kubelet.service
if [ $1 -eq 1 ]; then
    # Check if modprobe command is available
    [ ! -x /sbin/modprobe ] || { /sbin/modprobe br_netfilter && /sbin/modprobe overlay; } || true
fi
%if 0%{?suse_version} < 1500
# create some subvolumes needed by CNI
if [ ! -e %{_localstatedir}/lib/cni ]; then
  if [ "`findmnt -o FSTYPE -l  /|grep -v FSTYPE`" = "btrfs" ]; then
    %{_sbindir}/mksubvolume %{_localstatedir}/lib/cni
  fi
fi
%endif
%tmpfiles_create %{_tmpfilesdir}/kubelet.conf

%preun kubelet-common
%service_del_preun kubelet.service

%postun kubelet-common
%service_del_postun kubelet.service

%post kubeadm
# Check if sysctl command is available
if [ -x /usr/sbin/sysctl ]; then
    # Run sysctl --system after the package installation
    /usr/sbin/sysctl -p %{_sysctldir}/90-kubeadm.conf || true
fi

%files kubelet-common
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
%{_fillupdir}/sysconfig.kubelet-kubernetes%{baseversion}

# openSUSE is using kubeadm with containerizied control plane, we
# only need the binaries

%files apiserver
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kube-apiserver.1%{?ext_man}
%{_bindir}/kube-apiserver

%files controller-manager
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kube-controller-manager.1%{?ext_man}
%{_bindir}/kube-controller-manager

%files scheduler
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kube-scheduler.1%{?ext_man}
%{_bindir}/kube-scheduler

%files proxy
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kube-proxy.1%{?ext_man}
%{_bindir}/kube-proxy

%files kubelet
%license LICENSE
%{_bindir}/kubelet%{baseversion}

%files kubeadm
%doc README.md CONTRIBUTING.md CHANGELOG-%{baseversion}.md
%{_unitdir}/kubelet.service.d/10-kubeadm.conf
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/kubeadm.conf
%{_sysctldir}/90-kubeadm.conf
%license LICENSE
%{_bindir}/kubeadm
%{_mandir}/man1/kubeadm*

%files client
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/kubectl
%{_bindir}/kubectl%{baseversion}
%ghost %_sysconfdir/alternatives/kubectl

%files client-common
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kubectl.1%{?ext_man}
%{_mandir}/man1/kubectl-*

%files client-bash-completion
%{_datadir}/bash-completion/completions/kubectl

%files client-fish-completion
%{_datadir}/fish/vendor_completions.d/kubectl.fish

%changelog
