#
# spec file for package csi-node-driver-registrar
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


%{go_nostrip}

%define project github.com/kubernetes-csi/node-driver-registrar
%define package csi-node-driver-registrar
%define source node-driver-registrar

Name:           %{package}
Version:        2.0.1
Release:        0
Summary:        Registers the CSI driver with Kubelet
License:        Apache-2.0
Group:          System/Management
URL:            https://%{project}
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12

%description
Kubernetes node-driver-registrar is a sidecar container that registers the CSI driver with Kubelet using the kubelet plugin registration mechanism.

%prep
%setup -q
%setup -q -T -D -a 1

%build
%goprep %{project}

export CGO_ENABLED=0

%gobuild -a -mod=vendor -ldflags "-X main.version=%{version}" cmd/%{package}

%install
%goinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{package}

%changelog
