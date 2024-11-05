#
# spec file for package skupper
#
# Copyright (c) 2024 SUSE LLC
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

Name:           skupper
Version:        1.8.2
Release:        0
Summary:        Virtual Application Network, enabling rich hybrid cloud communication
License:        Apache-2.0
URL:            https://github.com/skupperproject/skupper
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        generated.tar.gz
Source3:        PACKAGING_README.md
BuildRequires:  go >= 1.22

%description
Skupper enables cloud communication by enabling you to create a Virtual
Application Network.

This application layer network decouples addressing from the underlying network
infrastructure. This enables secure communication without a VPN.

You can use Skupper to create a network from namespaces in one or more
Kubernetes clusters as described in the Getting Started. This guide describes a
simple network, however there are no restrictions on the topology created which
can include redundant paths.

Connecting one Skupper site to another site enables communication both ways.
Communication can occur using any path available on the network, that is,
direct connections are not required to enable communication.

Skupper supports anycast and multicast communication using the application
layer network (VAN), allowing you to configure your topology to match business
requirements.

Skupper does not require any special privileges, that is, you do not require
the cluster-admin role to create networks.

%prep
%autosetup -p 1 -a 1
tar xvf %{SOURCE2}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/skupperproject/skupper/pkg/version.Version=%{version}" \
   -o bin/%{name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
go test -v -count=1 ./client

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
