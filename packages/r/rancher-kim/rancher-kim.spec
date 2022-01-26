#
# spec file for package rancher-kim
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

Name:           rancher-kim
Version:        0.1.0~beta.7
Release:        0
Summary:        Rancher kim - The Kubernetes Image Manager
License:        Apache-2.0
URL:            https://github.com/rancher/kim
Source:         kim-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
kim is a Kubernetes-aware CLI that will install a small builder backend consisting of a BuildKit daemon bound to the Kubelet's underlying containerd socket (for building images) along with a small server-side agent that the CLI leverages for image management (think push, pull, etc) rather than talking to the backing containerd/CRI directly. kim enables building images locally, natively on your k3s cluster.

%prep
%setup -q -n kim-%{version}
%setup -q -T -D -a 1 -n kim-%{version}

%build -n kim-%{version}
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 kim "%{buildroot}/%{_bindir}/%{name}"

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
