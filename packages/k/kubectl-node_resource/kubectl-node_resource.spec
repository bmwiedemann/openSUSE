#
# spec file for package kubectl-node_resource
#
# Copyright (c) 2025 SUSE LLC
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


Name:           kubectl-node_resource
Version:        0.3.0
Release:        0
Summary:        Query node allocations/utilizations in kubectl
License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectl-node_resource/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  golang(API) >= 1.24
BuildRequires:  zsh
BuildRequires:  fdupes

%description
kubectl node-resource is a kubectl plugin that provides insights into
Kubernetes node resource allocation (based on pod requests) and actual
utilization (based on metrics-server data).

It helps administrators and developers understand how resources are being
consumed across their cluster's nodes and node pools.

%prep
%autosetup -p 1 -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build \
   -ldflags="-X main.version=v%{version}" \
   -o %{name}

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%check
# at least check that the executable is ... executable
%{buildroot}/%{_bindir}/%{name} --help

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
