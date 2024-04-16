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
%define kubernetes_version v1.29.3
%define kubernetes_version_major_minor 1.29
%define kubernetes_version_next 1.30
# check the upstream dependency file and adapt according to the 'golang: upstream version'
# https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_VERSION}/build/dependencies.yaml
# curl -sL https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBERNETES_VERSION}/build/dependencies.yaml | yq e '.dependencies[] | select(.name == "golang: upstream version").version
# example:
# result of the command 1.21.8 => golang_version go1.21 (including go prefix, without patch version)
# result of the command 1.21.8 => min_required_golang_minor_version 1.21.8
%define golang_version go1.21
%define min_required_golang_minor_version 1.21.8

Name:           rke2
Version:        1.29.3+rke2r1
Release:        0
Summary:        Rancher Kubernetes Engine
License:        Apache-2.0
URL:            https://github.com/rancher/rke2
Source0:        rke2-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  %{golang_version} >= %{min_required_golang_minor_version}
BuildRequires:  git
Provides:       rke2 = %{version}-%{release}
Conflicts:      rke2 < %{kubernetes_version_major_minor}
Conflicts:      rke2 >= %{kubernetes_version_next}

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
    -X github.com/rancher/rke2/pkg/images.DefaultEtcdImage=rancher/hardened-etcd:${ETCD_VERSION}-build20230802 \
    -X github.com/rancher/rke2/pkg/images.DefaultKubernetesImage=rancher/hardened-kubernetes:${KUBERNETES_IMAGE_TAG} \
    -X github.com/rancher/rke2/pkg/images.DefaultPauseImage=rancher/mirrored-pause:${PAUSE_VERSION} \
    -X github.com/rancher/rke2/pkg/images.DefaultRuntimeImage=${REPO}/${PROG}-runtime:${DOCKERIZED_VERSION} \
    -X github.com/rancher/rke2/pkg/images.DefaultCloudControllerManagerImage=rancher/rke2-cloud-provider:${CCM_VERSION}"

%install
# Install the binary.
install -D -m 0755 %{binary_name} "%{buildroot}/%{_bindir}/%{binary_name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{binary_name}

%changelog
