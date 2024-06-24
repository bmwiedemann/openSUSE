#
# spec file for package docker-compose
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

Name:           docker-compose
Version:        2.28.0
Release:        0
Summary:        Define and run multi-container applications with Docker
License:        Apache-2.0
URL:            https://github.com/docker/compose
Source:         compose-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.21
Requires:       docker
Requires:       docker-compose-switch

%description
Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. A Compose file is used to define how the one or more containers that make up your application are configured. Once you have a Compose file, you can create and start your application with a single command: docker compose up.
About update and backward compatibility

Docker Compose V2 is a major version bump release of Docker Compose. It has been completely rewritten from scratch in Golang (V1 was in Python). The installation instructions for Compose V2 differ from V1. V2 is not a standalone binary anymore, and installation scripts will have to be adjusted. Some commands are different.

For a smooth transition from legacy docker-compose 1.xx, please consider installing compose-switch to translate docker-compose ... commands into Compose V2's docker compose .... . Also check V2's --compatibility flag.

%prep
%setup -q -a 1 -n compose-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags="-s -w -X github.com/docker/compose/v2/internal.Version=%{version}" \
   -o bin/docker-compose ./cmd/

%install
install -d -m 0755 "%{buildroot}/usr/lib/docker/cli-plugins/"
install -D -m 0755 bin/%{name} "%{buildroot}/usr/lib/docker/cli-plugins/%{name}"

%files
%doc README.md
%license LICENSE
%dir /usr/lib/docker/
%dir /usr/lib/docker/cli-plugins/
/usr/lib/docker/cli-plugins/%{name}

%changelog
