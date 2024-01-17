#
# spec file for package kubectl-capacity
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

Name:           kubectl-capacity
Version:        0.7.4
Release:        0
Summary:        Show resource requests, limits, and utilization in a Kubernetes cluster
License:        Apache-2.0
URL:            https://github.com/robscott/kube-capacity
Source:         kube-capacity-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
This is a simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster. It attempts to combine the best parts of the output from kubectl top and kubectl describe into an easy to use CLI focused on cluster resources.

%prep
%autosetup -p1 -a 1 -n kube-capacity-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 kube-capacity "%{buildroot}/%{_bindir}/%{name}"
ln -s %{name} "%{buildroot}/%{_bindir}/kube-capacity"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kube-capacity

%changelog
