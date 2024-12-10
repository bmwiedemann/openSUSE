#
# spec file for package rke2
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define directory_name rke2
%define binary_name rke2
%define kubernetes_version v1.31.3
%define kubernetes_version_major_minor 1.31
%define kubernetes_version_next 1.32
# check the upstream dependency file and adapt according to the 'golang: upstream version'
# https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_VERSION}/build/dependencies.yaml
# curl -sL https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_VERSION}/build/dependencies.yaml | yq e '.dependencies[] | select(.name == "golang: upstream version").version'
# example:
# result of the command 1.22.2 => golang_version go1.22 (including go prefix, without patch version)
# result of the command 1.22.2 => min_required_golang_minor_version 1.22.2
%define golang_version go1.22
%define min_required_golang_minor_version 1.22.8

#
%define hardened_etcd_version build20241106

Name:           rke2
Version:        1.31.3+rke2r1
Release:        0
Summary:        Rancher Kubernetes Engine
License:        Apache-2.0
URL:            https://github.com/rancher/rke2
Source0:        rke2-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        rke2-agent.env
Source3:        rke2-agent.service
Source4:        rke2-server.env
Source5:        rke2-server.service
BuildRequires:  %{golang_version} >= %{min_required_golang_minor_version}
BuildRequires:  fdupes
BuildRequires:  git
Provides:       rke2 = %{version}-%{release}
Conflicts:      rke2 < %{kubernetes_version_major_minor}
Conflicts:      rke2 >= %{kubernetes_version_next}

# /var/lib/kubelet is also packaged in kubernetes1.XX-kubelet-common
# this in turn Requires kubernetes-kubelet-common
# by conflicting with kubernetes-kubelet-common we conflict with all
# kubernetes-version packages
Conflicts:      kubernetes-kubelet-common
Conflicts:      k3s

# if iptables is missing, the nginx-controller pod does not start
Requires:       iptables

%description
RKE2, also known as RKE Government, is Rancher's next-generation Kubernetes
distribution.
It is a fully conformant Kubernetes distribution that focuses on security and
compliance within the U.S. Federal Government sector.

To meet these goals, RKE2 does the following:
* Provides defaults and configuration options that allow clusters to pass the
  CIS Kubernetes Benchmark with minimal operator intervention
* Enables FIPS 140-2 compliance
* Supports SELinux policy and Multi-Category Security (MCS) label enforcement
* Regularly scans components for CVEs using trivy in our build pipeline

%prep
%autosetup -p 1 -a 1 -n %{directory_name}-%{version}

cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .

%build

# instead of hardcoding the various pieces of information,
# run the upstream script
# VERSION_GOLANG tries to download the dependencies.yaml from upstream Kubernetes
# that is being packaged, so we remove that line from the script
sed -i '/^VERSION_GOLANG/d' ./scripts/version.sh
source ./scripts/version.sh

# instead of getting the golang version from the kubernetes dependencies.yaml,
# we hardcode the goland version that we are using
# As long as the go major version is not different, this should be fine
VERSION_GOLANG="go$(rpm -q %{golang_version}|cut -d '-' -f 2)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -tags="selinux netgo osusergo no_stage static_build sqlite_omit_load_extension no_embedded_executor no_cri_dockerd" \
   -ldflags=" \
    -X github.com/k3s-io/k3s/pkg/version.GitCommit=v%{version} \
    -X github.com/k3s-io/k3s/pkg/version.Program=${PROG} \
    -X github.com/k3s-io/k3s/pkg/version.Version=%{version} \
    -X github.com/k3s-io/k3s/pkg/version.UpstreamGolang=${VERSION_GOLANG} \
    -X github.com/rancher/rke2/pkg/images.DefaultRegistry=docker.io \
    -X github.com/rancher/rke2/pkg/images.DefaultEtcdImage=rancher/hardened-etcd:${ETCD_VERSION}-%{hardened_etcd_version} \
    -X github.com/rancher/rke2/pkg/images.DefaultKubernetesImage=rancher/hardened-kubernetes:${KUBERNETES_IMAGE_TAG} \
    -X github.com/rancher/rke2/pkg/images.DefaultPauseImage=rancher/mirrored-pause:${PAUSE_VERSION} \
    -X github.com/rancher/rke2/pkg/images.DefaultRuntimeImage=${REPO}/${PROG}-runtime:${DOCKERIZED_VERSION} \
    -X github.com/rancher/rke2/pkg/images.DefaultCloudControllerManagerImage=rancher/rke2-cloud-provider:${CCM_VERSION}"

%install
# Install the binary.
install -D -m 0755 %{binary_name} %{buildroot}/%{_bindir}/%{binary_name}

# systemd unit and env files
install -D -m 0644 rke2-agent.service %{buildroot}/%{_unitdir}/rke2-agent.service
install -D -m 0644 rke2-agent.env %{buildroot}/%{_unitdir}/rke2-agent.env
install -D -m 0644 rke2-server.service %{buildroot}/%{_unitdir}/rke2-server.service
install -D -m 0644 rke2-server.env %{buildroot}/%{_unitdir}/rke2-server.env

# configuration directory
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cni/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cni/net.d/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/rancher/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/rancher/node/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/rancher/%{binary_name}/
install -d -m 0750 %{buildroot}/%{_sharedstatedir}/kubelet/
install -d -m 0755 %{buildroot}/%{_sharedstatedir}/rancher/
install -d -m 0755 %{buildroot}/%{_sharedstatedir}/rancher/%{binary_name}/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/containers/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/pods/

%fdupes %{buildroot}/%{_unitdir}/

%check

%pre
%service_add_pre rke2-agent.service
%service_add_pre rke2-server.service

%post
%service_add_post rke2-agent.service
%service_add_post rke2-server.service

%preun
%service_del_preun rke2-agent.service
%service_del_preun rke2-server.service

%postun
%service_del_postun rke2-agent.service
%service_del_postun rke2-server.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{binary_name}
%{_unitdir}/%{binary_name}-agent.env
%{_unitdir}/%{binary_name}-agent.service
%{_unitdir}/%{binary_name}-server.env
%{_unitdir}/%{binary_name}-server.service
%dir %config %{_sysconfdir}/cni/
%dir %config %{_sysconfdir}/cni/net.d/
%dir %config %{_sysconfdir}/rancher/
%dir %config %{_sysconfdir}/rancher/node/
%dir %config %{_sysconfdir}/rancher/rke2/
%dir %attr(750,root,root) %{_sharedstatedir}/kubelet/
%dir %{_sharedstatedir}/rancher/
%dir %{_sharedstatedir}/rancher/rke2/
%dir %{_localstatedir}/log/containers/
%dir %{_localstatedir}/log/pods/

%changelog
