#
# spec file for package kubectl-tree
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kubectl-tree
Version:        0.4.6
Release:        0
Summary:        Kubectl plugin to browse Kubernetes object hierarchies as a tree
License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectl-tree
Source:         kubectl-tree-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18

%description
A kubectl plugin to explore ownership relationships between Kubernetes objects through ownersReferences on the objects.

The kubectl lineage plugin is very similar to kubectl tree, but it understands logical relationships between some API objects without needing ownerReferences.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   --buildmode=pie \
   -o %{name} ./cmd/kubectl-tree

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
