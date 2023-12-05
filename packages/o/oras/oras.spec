#
# spec file for package trivy
#
# Copyright (c) 2023 SUSE LLC
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


%global git_commit 7079c468a06fb5815c99395eb4aaf46dd459d3fa
Name:           oras
Version:        1.1.0
Release:        0
Summary:        OCI registry client - managing content like artifacts, images, packages
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/oras-project/oras
Source:         https://github.com/oras-project/oras/archive/refs/tags/v%{version}.tar.gz#/oras-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang(API) = 1.21
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
OCI registry client to manage registries which store container images and other artifacts
for easy access.
Distributing OCI artifacts means pushing them to these registries so others can
pull them for use. ORAS helps with those tasks

%prep
%autosetup -p1 -a1

%build
CGO_ENABLED=0 go build -o oras -mod=vendor -buildmode=pie -trimpath \
    -ldflags "-w -X oras.land/oras/internal/version.BuildMetadata=%{version} \
             -X oras.land/internal/version.GitTreeState=clean \
             -X oras.land/internal.version.GitCommit=%{git_commit}" cmd/oras/main.go

%install
install -D -m 755 oras %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
