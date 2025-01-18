#
# spec file for package kubectl-operator
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           kubectl-operator
Version:        0.6.0
Release:        0
Summary:        Manage Kubernetes Operators from the command line
License:        Apache-2.0
URL:            https://github.com/operator-framework/kubectl-operator
Source:         kubectl-operator-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
kubectl operator is a kubectl plugin that functions as a package manager for
Operators in your cluster. It simplifies adding and removing Operator catalogs,
and it has familiar commands for installing, uninstalling, and listing
available and installed Operators.

NOTE: This plugin requires Operator Lifecycle Manager to be installed in your cluster. See the OLM installation instructions here:
https://olm.operatorframework.io/docs/getting-started/

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-s -w \
   -X github.com/operator-framework/kubectl-operator/internal/version.GitVersion=%{version} \
   -X github.com/operator-framework/kubectl-operator/internal/version.GitCommit=v%{version} \
   -X github.com/operator-framework/kubectl-operator/internal/version.GitTreeState=clean" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
