#
# spec file for package kube-no-trouble
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           kube-no-trouble
Version:        0.7.0
Release:        0
Summary:        Easily check your cluster for use of deprecated APIs
License:        MIT
URL:            https://github.com/doitintl/kube-no-trouble
Source:         kube-no-trouble-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
Easily check your cluster for use of deprecated APIs

Kubernetes 1.16 is slowly starting to roll out, not only across various managed Kubernetes offerings, and with that come a lot of API deprecations1.

Kube No Trouble (kubent) is a simple tool to check whether you're using any of these API versions in your cluster and therefore should upgrade your workloads first, before upgrading your Kubernetes cluster.

This tool will be able to detect deprecated APIs depending on how you deploy your resources, as we need the original manifest to be stored somewhere. In particular following tools are supported:
* file - local manifests in YAML or JSON
* kubectl - uses the kubectl.kubernetes.io/last-applied-configuration annotation
* Helm v2 - uses Tiller manifests stored in K8s Secrets or ConfigMaps
* Helm v3 - uses Helm manifests stored as Secrets or ConfigMaps directly in individual namespaces

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}" \
   -o bin/kubent ./cmd/kubent/main.go

%install
# Install the binary.
install -D -m 0755 bin/kubent "%{buildroot}/%{_bindir}/kubent"

%files
%doc README.md
%license LICENSE
%{_bindir}/kubent

%changelog
