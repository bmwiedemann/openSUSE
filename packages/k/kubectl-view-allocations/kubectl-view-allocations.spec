#
# spec file for package kubectl-view-allocations
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           kubectl-view-allocations
Version:        0.20.3
Release:        0
Summary:        kubectl plugin to list allocations
License:        CC0-1.0
URL:            https://github.com/davidB/kubectl-view-allocations
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Recommends:     fzf
BuildRequires:  cargo
# kube-client v0.90.0 requires rust 1.75 or higher
BuildRequires:  rust >= 1.75.0

%description
kubectl plugin lists allocations for resources (cpu, memory, gpu,...) as
defined into the manifest of nodes and running pods. It doesn't list usage like
kubectl top. It can provide result grouped by namespaces, nodes, pods and
filtered by resources'name.

Columns displayed :

* Requested : Quantity of resources requested by the container in the pod's manifest. It's the sum group by pod, namespace, node where container is running. With percentage of resources requested over what is allocatable in the group.
* Limit : Quantity of resources max (limit) requestable by the container in the pod's manifest. It's the sum group by pod, namespace, node where container is running. With percentage of resources max / limit over what is allocatable in the group.
* Allocatable : Allocatable resources defined (or detected) on nodes.
* Free : Allocatable - max (Limit, Requested)
* Utilization : Quantity of resources (cpu & memory only) used as reported by Metrics API. It's disable by default, metrics-server is optional and should be setup into the cluster.

%prep
%autosetup -a1

%build
RUSTFLAGS=%{rustflags} cargo build --release --all-features

%install
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .
rm -f %{buildroot}/usr/.crates.toml
rm -f %{buildroot}/usr/.crates2.json

# make this available as a kubectl plugin
cd %{buildroot}/%{_bindir}/
ln -s ./%{name} ./kubectl-view_allocations

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/kubectl-view_allocations

%changelog
