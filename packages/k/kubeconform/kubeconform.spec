#
# spec file for package kubeconform
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


Name:           kubeconform
Version:        0.6.7
Release:        0
Summary:        A fast Kubernetes manifests validator, with support for custom resources
License:        Apache-2.0
URL:            https://github.com/yannh/kubeconform/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22

%description
Kubeconform is a Kubernetes manifests validation tool. It is inspired by, contains
code from and is designed to stay close to Kubeval, but with the following
improvements:

- high performance: will validate & download manifests over multiple routines, caching
  downloaded files in memory
- configurable list of remote, or local schemas locations, enabling validating Kubernetes
  custom resources (CRDs) and offline validation capabilities
- uses by default a self-updating fork of the schemas registry maintained by the
  kubernetes-json-schema project - which guarantees up-to-date schemas for all recent versions
  of Kubernetes.

%prep
%autosetup -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/ .../.

%install
install -D -m 0755 ./bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%{_bindir}/%{name}
%license LICENSE
%doc Readme.md

%changelog
