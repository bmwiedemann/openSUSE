#
# spec file for package cilium
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.8.5
Release:        0
Summary:        Linux Native, HTTP Aware Networking and Security for Containers
License:        Apache-2.0 AND GPL-2.0-or-later
URL:            https://github.com/cilium/cilium
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        cilium-cni-install
Source3:        cilium-cni-uninstall
# PATCH-FIX-UPSTREAM 0001-operator-make-Add-install-target.patch
Patch0:         0001-operator-make-Add-install-target.patch
# Cilium needs to be aware of the version string of cilium-proxy
BuildRequires:  cilium-proxy
BuildRequires:  clang
BuildRequires:  git-core
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
BuildRequires:  golang(API) = 1.13
Requires:       awk
Requires:       binutils
Requires:       bpftool
%requires_eq    cilium-proxy
# clang is needed as runtime dependency for compiling BPF programs by cilium
Requires:       clang
# Although clang is used as a compiler for BPF programs, they need to have
# libgcc and libgcc_s linked in.
# https://github.com/cilium/cilium/issues/7273
Requires:       gcc
Requires:       gzip
Requires:       iproute2
# Despite the fact that cilium is using BPF programs and aims to replace
# iptables for container security policies, iptables is still needed for
# defining few rules which redirect the traffic from kube-proxy to cilium. Then
# cilium replaces some of kube-proxy functionality, using BPF programs. So, in
# fact, cilium uses few iptables rules to prevent iptables usage. :)
#
# TODO(mrostecki): (27-02-2020) That comment above is actually quite old. After
# upgrade to 1.7.x we can get rid of kube-proxy and thus get rid of iptables.
# But I need to test that properly.
Requires:       iptables
Requires:       llvm
Requires:       protobuf-c
Requires:       util-linux
Requires:       which
ExclusiveArch:  aarch64 x86_64 s390x ppc64le
Requires(post): %fillup_prereq

%description
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

%package cni
Summary:        CNI plugin for Cilium
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
Requires:       cilium
Requires:       docker

%description docker
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a Docker libnetwork plugin for Cilium.

%package operator
Summary:        Kubernetes operator for Cilium

%description operator

Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package provides a Kubernetes operator that does garbage collector work
for Cilium.

%package -n %{lname}
Summary:        Shared library for Cilium

%description -n %{lname}
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package contains shared library for Cilium which is used by Cilium filters
in Envoy.

%package devel
Summary:        Development files for Cilium
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
BuildArch:      noarch

%description k8s-yaml
Cilium is a software for providing, and transparently securing, network
connectivity, and for load-balancing between application containers and
services deployed using Linux container management platforms like Docker and
Kubernetes.

This package contains the yaml file requried to download and run Cilium
containers in a Kubernetes cluster.

%prep
%autosetup -p1

# generate the BPF_SRCFILES which is normally part of the release tarballs but
# not when we generate it from git (but don't run the dist scripts)
find bpf/ -type f | grep -v .gitignore | tr "\n" ' ' > BPF_SRCFILES

%build
%goprep %{provider_prefix}
export GOPATH=%{_builddir}/go
cd $GOPATH/src/%{provider_prefix}

export EXTRA_GOBUILD_FLAGS="-v -p 4 -x -buildmode=pie"
export CILIUM_ENVOY_SHA="$(cilium-envoy --version | cut -d : -f 2 | xargs echo -n)"

sed -i '/groupadd /s/^/#/' daemon/Makefile
sed -i '/groupadd /s/^/#/' operator/Makefile
# create bindata.go which is no included in the source as it is ignored
# because of .gitignore
make -C daemon CILIUM_ENVOY_SHA="${CILIUM_ENVOY_SHA}"

%if 0%{?suse_version} > 1510 && 0%{?is_opensuse}
make precheck
make govet
make ineffassign
make logging-subsys-field
%endif

make build CILIUM_ENVOY_SHA="${CILIUM_ENVOY_SHA}"

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

sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE2}
install -D -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/cilium-cni-install
install -D -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}/cilium-cni-uninstall
install -D -m 0755 contrib/packaging/docker/init-container.sh %{buildroot}/%{_bindir}/cilium-init
install -D -m 0644 contrib/systemd/cilium %{buildroot}%{_fillupdir}/sysconfig.cilium
install -D -m 0644 proxylib/libcilium.h %{buildroot}%{_includedir}/libcilium.h
pushd install/kubernetes/cilium
for yaml_file in $(find . -type f -name "*.yaml"); do
    install -D -m 0644 ${yaml_file} %{buildroot}%{_datadir}/k8s-helm/cilium/${yaml_file}
done
popd

# Adjust Helm charts values to our images.
sed -i \
    -e 's|integration: none|integration: crio|' \
    -e 's|registry: docker.io/cilium|registry: registry.opensuse.org/kubic|' \
    -e 's|tag: v%{version}|tag: %{version}|' \
    %{buildroot}%{_datadir}/k8s-helm/cilium/values.yaml
sed -i \
    -e 's|/cni-install.sh|cilium-cni-install|' \
    -e 's|/cni-uninstall.sh|cilium-cni-uninstall|' \
    -e 's|/init-container.sh|cilium-init|' \
    %{buildroot}%{_datadir}/k8s-helm/cilium/charts/agent/templates/daemonset.yaml
sed -i \
    -e 's|image: operator|image: cilium-operator|' \
    %{buildroot}%{_datadir}/k8s-helm/cilium/charts/operator/values.yaml

mkdir -p %{buildroot}%{bash_completion_dir}
%{buildroot}%{_bindir}/cilium completion > %{buildroot}%{bash_completion_dir}/cilium
rm %{buildroot}%{_sysconfdir}/bash_completion.d/cilium
mv %{buildroot}%{_sysconfdir}/bash_completion.d/hubble-relay %{buildroot}%{bash_completion_dir}/hubble-relay

mv %{buildroot}%{_sysconfdir}/cni/net.d/05-cilium-cni.conf %{buildroot}%{_sysconfdir}/cni/net.d/10-cilium-cni.conf

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
%{bash_completion_dir}/hubble-relay
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
%{_bindir}/cilium-health-responder
%{_bindir}/cilium-init
%{_bindir}/cilium-map-migrate
%{_bindir}/cilium-node-monitor
%{_bindir}/cilium-probe-kernel-hz
%{_bindir}/hubble-relay
%{_bindir}/maptool
%{_localstatedir}/lib/cilium
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

%files operator
%{_bindir}/cilium-operator
%{_bindir}/cilium-operator-aws
%{_bindir}/cilium-operator-azure
%{_bindir}/cilium-operator-generic

%files -n %{lname}
%{_libdir}/libcilium.so.%{sover}

%files devel
%{_includedir}/libcilium.h
%{_libdir}/libcilium.so

%files k8s-yaml
%dir %{_datadir}/k8s-helm
%{_datadir}/k8s-helm/cilium

%changelog
