#
# spec file for package popeye
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           popeye
Version:        0.11.1
Release:        0
Summary:        A Kubernetes cluster resource sanitizer
License:        Apache-2.0
URL:            https://github.com/derailed/popeye
Source:         popeye-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17

%description
Pluto is a utility to help users find deprecated Kubernetes apiVersions in their code repositories and their helm releases.
peye is a utility that scans live Kubernetes cluster and reports potential issues with deployed resources and configurations. It sanitizes your cluster based on what's deployed and not what's sitting on disk. By scanning your cluster, it detects misconfigurations and helps you to ensure that best practices are in place, thus preventing future headaches. It aims at reducing the cognitive overload one faces when operating a Kubernetes cluster in the wild. Furthermore, if your cluster employs a metric-server, it reports potential resources over/under allocations and attempts to warn you should your cluster run out of capacity.
Popeye is a readonly tool, it does not alter any of your Kubernetes resources in any way!

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
