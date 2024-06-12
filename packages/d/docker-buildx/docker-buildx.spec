#
# spec file for package docker-buildx
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

%define archive_name buildx
%define binary_name buildx

Name:           docker-buildx
Version:        0.15.0
Release:        0
Summary:        Docker CLI plugin for extended build capabilities with BuildKit
License:        Apache-2.0
URL:            https://github.com/docker/buildx
Source:         buildx-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  docker
BuildRequires:  go >= 1.20
Requires:       docker

%description
buildx is a Docker CLI plugin for extended build capabilities with BuildKit.

Key features:
- Familiar UI from docker build
- Full BuildKit capabilities with container driver
- Multiple builder instance support
- Multi-node builds for cross-platform images
- Compose build support
- High-level build constructs (bake)
- In-container driver support (both Docker and Kubernetes)

%prep
%setup -q -n %{archive_name}-%{version}
%setup -q -n %{archive_name}-%{version} -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/docker/buildx/version.Version=%{version} -X github.com/docker/buildx/version.Revision=v%{version}" \
   -o bin/docker-buildx ./cmd/buildx

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/usr/lib/docker/cli-plugins/%{name}"

%files
%doc README.md
%license LICENSE
/usr/lib/docker/cli-plugins/%{name}

%changelog
