#
# spec file for package kubectl-validate
#
# Copyright (c) 2021 SUSE LLC
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

Name:           kubectl-validate
Version:        0.0.4
Release:        0
Summary:        Kubectl plugin for local validation of resources
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/kubectl-validate
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22

%description
kubectl-validate is a SIG-CLI subproject to support the local validation of
resources for native Kubernetes types and CRDs.

This project has two goals:

1. Shift-left validation of resources with as close to parity to server-side
   Kubernetes as possible.
2) Improve declarative validation support in upstream Kubernetes over time,
   making those improvements available for kubectl-validate users early.

%prep
%autosetup -a 1 -p 1

%build
CGO_ENABLED=0 go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
