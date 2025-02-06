#
# spec file for package hauler
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


Name:           hauler
Version:        1.1.1
%global git_commit 090f4dc905e1d68b5a3e41e04feafe6063c85639
Release:        0
Summary:        Airgap Swiss Army Knife
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/rancherfederal/hauler
Source:         %{name}-%{version}.tar.zst
Patch1:         0001-Bump-the-go_modules-group-across-1-directory-with-2-.patch
Source1:        vendor.tar.zst
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cosign
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.23

%description
Rancher Government Hauler simplifies the airgap experience without requiring
users to adopt a specific workflow. Hauler simplifies the airgapping process,
by representing assets (images, charts, files, etc...) as content and
collections to allow users to easily fetch, store, package, and distribute
these assets with declarative manifests or through the command line.

Hauler does this by storing contents and collections as OCI Artifacts and
allows users to serve contents and collections with an embedded registry and
fileserver. Additionally, Hauler has the ability to store and inspect various
non-image OCI Artifacts.

%prep
%autosetup -p1 -a1

%build
export CGO_ENABLED=1
mkdir -p cmd/hauler/binaries/
%ifarch aarch64
cp -p %{_bindir}/cosign cmd/hauler/binaries/cosign-linux-arm64
%endif
%ifarch x86_64
cp -p %{_bindir}/cosign cmd/hauler/binaries/cosign-linux-amd64
%endif
# s -w -X {{ .Env.vpkg }}.gitVersion={{ .Version }} -X {{ .Env.vpkg }}.gitCommit={{ .ShortCommit }} -X {{ .Env.vpkg }}.gitTreeState={{if .IsGitDirty}}dirty{{else}}clean{{end}} -X {{ .Env.vpkg }}.buildDate={{ .Date }}
go build -o hauler -mod=vendor -buildmode=pie -trimpath -ldflags "-s -w -X github.com/rancherfederal/hauler/internal/version.gitVersion=%{version} \
    -X github.com/rancherfederal/hauler/internal/version.gitCommit=%{git_commit} \
    -X github.com/rancherfederal/hauler/internal/version.gitTreeState=clean" cmd/hauler/main.go

%install
install -D -m 755 hauler %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
