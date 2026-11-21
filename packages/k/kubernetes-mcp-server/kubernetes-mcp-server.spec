#
# spec file for package kubernetes-mcp-server
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

Name:           kubernetes-mcp-server
Version:        0.1.3
Release:        0
Summary:        Generic Kubernetes MCP server
# Legal-Review-Notice: binary links MPL-2.0 vendor code:
# - helm via hashicorp errwrap/go-multierror, cyphar filepath-securejoin
# - otelcol via philippgille chromem-go
License:        Apache-2.0 AND MPL-2.0
URL:            https://github.com/containers/kubernetes-mcp-server
Source0:        https://github.com/containers/kubernetes-mcp-server/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.26.10

%description
Model Context Protocol (MCP) server for Kubernetes and OpenShift.
Native Go implementation talking directly to the Kubernetes API server,
not a wrapper around kubectl or helm. Exposes generic resource CRUD,
pods, namespaces, events, Helm releases, Tekton, and observability
tools over MCP.

%prep
%autosetup -a1

%build
go build \
	-o %{name} \
	-mod=vendor \
	-buildmode=pie \
	-ldflags "-X github.com/containers/kubernetes-mcp-server/pkg/version.Version=v%{version}" \
	./cmd/kubernetes-mcp-server

%check
# Offline root: kiali discovery needs real DNS (timeouts read as
# available); pkg/mcp needs network for kubebuilder envtest binaries.
go test -mod=vendor -skip 'TestHasKiali_DiscoverFromCR' $(go list ./... | grep -v 'kubernetes-mcp-server/pkg/mcp$')

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
