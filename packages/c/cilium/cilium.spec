#
# spec file for package cilium
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


%global provider        github
%global provider_tld    com
%global project         cilium
%global repo            cilium
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%define cni_bin_dir     %{_libexecdir}/cni

%define sover 1
%define lname libcilium%{sover}

%define bash_completion_dir %{_datadir}/bash-completion/completions

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           cilium
Version:        1.5.7
Release:        0
Summary:        Linux Native, HTTP Aware Networking and Security for Containers
License:        Apache-2.0 AND GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/cilium/cilium
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        cilium-cni-install
Source3:        cilium-cni-uninstall
# PATCH-FIX-UPSTREAM bsc#1145258 -- Update configmap values for etcd v3.4.0
Patch0:         0001-etcd-use-ca-file-field-from-etcd-option-if-available.patch
# PATCH-FIX-UPSTREAM bsc#1145258 -- Separate kvstore initialization in daemon to
# the separate function - needed for the next patch to apply without conflicts
Patch1:         0002-daemon-separate-kvstore-initialization-into-separate.patch
# PATCH-FIX-UPSTREAM bsc#1145258 -- Update etcd library to v3.4.0
Patch2:         0003-deps-update-etcd-to-v3.4.0.patch
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  glibc-devel
# glibc-devel-32bit is needed to compile bpf objects
# https://github.com/cilium/cilium/issues/368
BuildRequires:  glibc-devel-32bit
BuildRequires:  golang-github-jteeuwen-go-bindata
BuildRequires:  golang-packaging
%if 0%{?suse_version} > 1510 && 0%{?is_opensuse}
BuildRequires:  ineffassign
%endif
BuildRequires:  libelf-devel
BuildRequires:  llvm
BuildRequires:  protobuf-devel
BuildRequires:  shadow
BuildRequires:  unzip
BuildRequires:  golang(API) >= 1.10
Requires:       awk
Requires:       binutils
# clang and glibc headers are needed as runtime dependencies for compiling BPF
# programs by cilium
Requires:       clang
# Although clang is used as a compiler for BPF programs, they need to have
# libgcc and libgcc_s linked in.
# https://github.com/cilium/cilium/issues/7273
Requires:       gcc
Requires:       glibc-devel
# glibc-devel-32bit is needed to compile bpf objects
# https://github.com/cilium/cilium/issues/368
Requires:       glibc-devel-32bit
Requires:       iproute2
# Despite the fact that cilium is using BPF programs and aims to replace
# iptables for container security policies, iptables is still needed for
# defining few rules which redirect the traffic from kube-proxy to cilium. Then
# cilium replaces some of kube-proxy functionality, using BPF programs. So, in
# fact, cilium uses few iptables rules to prevent iptables usage. :)
Requires:       gzip
Requires:       iptables
Requires:       llvm
Requires:       protobuf-c
Requires:       util-linux
Requires:       which
ExclusiveArch:  aarch64 x86_64
Requires(post): %fillup_prereq

%description
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

%package cni
Summary:        CNI plugin for Cilium
Group:          System/Management
Requires:       cilium
Requires:       cni
Requires:       cni-plugins

%description cni
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a CNI (Container Network Interface) plugin for Cilium.

%package docker
Summary:        Docker libnetwork plugin for Cilium
Group:          System/Management
Requires:       cilium
Requires:       docker

%description docker
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a Docker libnetwork plugin for Cilium.

%package init
Summary:        Script for the Cilium init container
Group:          System/Management

%description init
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a script for the Cilium init container which cleans BPF
maps states which should be executed before launching Cilium in Kubernetes
clusters.

%package operator
Summary:        Kubernetes operator for Cilium
Group:          System/Management

%description operator

Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a Kubernetes operator that does garbage collector work
for Cilium.

%package -n %{lname}
Summary:        Shared library for Cilium
Group:          System/Libraries

%description -n %{lname}
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package contains shared library for Cilium which is used by Cilium filters
in Envoy.

%package devel
Summary:        Development files for Cilium
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package contains shared development files for Cilium which are used by
Cilium filters in Envoy.

%package k8s-yaml
Summary:        Kubernetes yaml file to run Cilium containers
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package contains the yaml file requried to download and run Cilium
containers in a Kubernetes cluster.

%prep
%setup -q
%patch0
%patch1
# patch macro adds the --fuzz=0 option which does not work with the last patch
patch --no-backup-if-mismatch -p0 %{PATCH2}

%build
%goprep %{provider_prefix}
export GOPATH=%{_builddir}/go
cd $GOPATH/src/%{provider_prefix}

export EXTRA_GOBUILD_FLAGS="-v -p 4 -x -buildmode=pie"

sed -i '/groupadd /s/^/#/' daemon/Makefile
sed -i '/groupadd /s/^/#/' operator/Makefile
# create bindata.go which is no included in the source as it is ignored
# because of .gitignore
make -C daemon apply-bindata

%if 0%{?suse_version} > 1510 && 0%{?is_opensuse}
make precheck
make govet
make ineffassign
make logging-subsys-field
%endif

make build

%install
export GOPATH=%{_builddir}/go
cd $GOPATH/src/%{provider_prefix}

export DISABLE_ENVOY_INSTALLATION=1
export PKG_BUILD=1
export BINDIR=%{_bindir}
export CNIBINDIR=%{cni_bin_dir}
export DESTDIR=%{buildroot}
export LIBDIR=%{_libdir}
%make_install

mkdir -p %{buildroot}%{_sbindir}
for service in cilium cilium-docker cilium-etcd cilium-consul; do
    install -D -m 644 contrib/systemd/${service}.service \
    %{buildroot}%{_unitdir}/${service}.service
    ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done

install -D -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/cilium-cni-install
install -D -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}/cilium-cni-uninstall
install -D -m 0755 contrib/packaging/docker/init-container.sh %{buildroot}/%{_bindir}/cilium-init
install -D -m 0644 contrib/systemd/cilium %{buildroot}%{_fillupdir}/sysconfig.cilium
install -D -m 0644 proxylib/libcilium.h %{buildroot}%{_includedir}/libcilium.h
install -D -m 0644 examples/kubernetes/1.14/cilium-crio.yaml %{buildroot}%{_datadir}/k8s-yaml/cilium/cilium.yaml
sed -i \
    -e 's|image: docker.io/cilium/cilium:.*|image: registry.opensuse.org/kubic/cilium:%{version}|g' \
    -e 's|image: docker.io/cilium/cilium-init:.*|image: registry.opensuse.org/kubic/cilium-init:%{version}|g' \
    -e 's|image: docker.io/cilium/operator:.*|image: registry.opensuse.org/kubic/cilium-operator:%{version}|g' \
    -e 's|image: docker.io/cilium/cilium-etcd-operator:.*|image: registry.opensuse.org/kubic/cilium-etcd-operator:2.0|g' \
    -e 's|/init-container.sh|cilium-init|g' \
    -e 's|/cni-install.sh|cilium-cni-install|g' \
    -e 's|/cni-uninstall.sh|cilium-cni-uninstall|g' \
    -e 's|--container-runtime=crio|--container-runtime=crio\n        - --disable-envoy-version-check|g' \
    %{buildroot}%{_datadir}/k8s-yaml/cilium/cilium.yaml

mkdir -p %{buildroot}%{bash_completion_dir}
%{buildroot}%{_bindir}/cilium completion > %{buildroot}%{bash_completion_dir}/cilium

mv %{buildroot}%{_sysconfdir}/cni/net.d/05-cilium-cni.conf %{buildroot}%{_sysconfdir}/cni/net.d/10-cilium-cni.conf

#TODO removed after https://github.com/cilium/cilium/pull/8184
sed -i '2 i\
    "cniVersion": "0.3.1",'  %{buildroot}%{_sysconfdir}/cni/net.d/10-cilium-cni.conf

%pre
getent group cilium >/dev/null || groupadd -r cilium
%service_add_pre cilium-consul.service cilium-etcd.service cilium.service

%pre docker
%service_add_pre cilium-docker.service

%post
%service_add_post cilium-consul.service cilium-docker.service cilium-etcd.service cilium.service
%{fillup_only -n cilium}

%post docker
%service_add_post cilium-docker.service

%post -n %{lname} -p /sbin/ldconfig

%preun
%service_del_preun cilium-consul.service cilium-etcd.service cilium.service

%preun docker
%service_del_preun cilium-docker.service

%postun
%service_del_postun cilium-consul.service cilium-etcd.service cilium.service

%postun docker
%service_del_postun cilium-docker.service

%postun -n %{lname} -p /sbin/ldconfig

%files
%{bash_completion_dir}/cilium
%{_fillupdir}/sysconfig.cilium
%{_unitdir}/cilium-consul.service
%{_unitdir}/cilium-etcd.service
%{_unitdir}/cilium.service
%{_sbindir}/rccilium-consul
%{_sbindir}/rccilium-etcd
%{_sbindir}/rccilium
%{_bindir}/cilium
%{_bindir}/cilium-align-checker
%{_bindir}/cilium-agent
%{_bindir}/cilium-bugtool
%{_bindir}/cilium-health
%{_bindir}/cilium-map-migrate
%{_bindir}/cilium-node-monitor
%{_bindir}/cilium-ring-dump
%license LICENSE

%files cni
%dir %{_sysconfdir}/cni
%dir %{_sysconfdir}/cni/net.d
%dir %{cni_bin_dir}
%config(noreplace) %{_sysconfdir}/cni/net.d/10-cilium-cni.conf
%{cni_bin_dir}/cilium-cni
%{_sbindir}/cilium-cni-install
%{_sbindir}/cilium-cni-uninstall

%files docker
%{_unitdir}/cilium-docker.service
%{_sbindir}/rccilium-docker
%{_bindir}/cilium-docker

%files init
%{_bindir}/cilium-init

%files operator
%{_bindir}/cilium-operator

%files -n %{lname}
%{_libdir}/libcilium.so.%{sover}

%files devel
%{_includedir}/libcilium.h
%{_libdir}/libcilium.so

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/cilium
%{_datadir}/k8s-yaml/cilium/cilium.yaml

%changelog
