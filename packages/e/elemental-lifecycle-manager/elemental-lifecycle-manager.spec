#
# spec file for package elemental-lifecycle-manager
#
# Copyright (c) 2026 SUSE LLC
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


Name:           elemental-lifecycle-manager
Version:        0.1.0.20260602+9ae3c44
Release:        0
Summary:        Elemental Lifecycle Manager
License:        Apache-2.0
URL:            https://github.com/SUSE/elemental-lifecycle-manager
Source0:        elemental-lifecycle-manager-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  golang(API) = 1.26
BuildRequires:  zstd

%description
Elemental Lifecycle Manager is a Kubernetes operator that manages the
lifecycle of platforms built on Elemental.

%prep
%setup -q -a1 -n elemental-lifecycle-manager-%{version}

%build
go build -trimpath -buildmode=pie -mod=vendor -o bin/lcm ./cmd/main.go

%install
install -m 0755 -D bin/lcm %{buildroot}/%{_bindir}/lcm

%check
# tests require a Kubernetes environment (envtest / kubebuilder assets)
# go test ./...

%files
%license LICENSE
%{_bindir}/lcm

%changelog
