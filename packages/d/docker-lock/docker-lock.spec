#
# spec file for package docker-lock
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

Name:           docker-lock
Version:        0.8.10
Release:        0
Summary:        Automatically manage image digests in Dockerfiles, docker-compose files, and Kubernetes manifests
License:        Apache-2.0
URL:            https://github.com/safe-waters/docker-lock
Source:         docker-lock-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.13

%description
docker-lock is a cli tool that automates managing image digests by tracking them in a separate Lockfile (think package-lock.json or Pipfile.lock). With docker-lock, you can refer to images in Dockerfiles, docker-compose V3 files, and Kubernetes manifests by mutable tags (as in python:3.6) yet receive the same benefits as if you had specified immutable digests (as in python:3.6@sha256:25a189a536ae4d7c77dd5d0929da73057b85555d6b6f8a66bfbcc1a7a7de094b).

%prep
%setup -q
%setup -q -T -D -a 1

%build
mkdir out
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}" \
   -o . ./...

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
