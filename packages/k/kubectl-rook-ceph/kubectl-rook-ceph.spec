#
# spec file for package kubectl-rook-ceph
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


%define executable_name kubectl-rook_ceph

Name:           kubectl-rook-ceph
Version:        0.9.3
Release:        0
Summary:        Management and troubleshooting tools for the Rook Ceph storage provider
License:        Apache-2.0
URL:            https://github.com/rook/kubectl-rook-ceph
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.23

%description
Provide common management and troubleshooting tools for the Rook Ceph storage
provider as a kubectl plugin.

%prep
%autosetup -a 1 -p 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{executable_name} cmd/main.go

# completions cannot be created currently,
# if no valid kubeconfig is existing
# https://github.com/rook/kubectl-rook-ceph/issues/353

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} --help

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
