#
# spec file for package kubespy
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

Name:           kubespy
Version:        0.6.1
Release:        0
Summary:        Tools for observing Kubernetes resources in real time, powered by Pulumi
License:        Apache-2.0
URL:            https://github.com/pulumi/kubespy
Source:         kubespy-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
What happens when you boot up a Pod? What happens to a Service before it is allocated a public IP address? How often is a Deployment's status changing?

kubespy is a small tool that makes it easy to observe how Kubernetes resources change in real time, derived from the work we did to make Kubernetes deployments predictable in Pulumi's CLI. Run kubespy at any point in time, and it will watch and report information about a Kubernetes resource continuously until you kill it.

%prep
%setup -q
%setup -q -T -D -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
ls -lh
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/pulumi/kubespy/version.Version=%{version}" \
   -o bin/kubespy

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/kubectl-spy"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kubectl-spy

%changelog
