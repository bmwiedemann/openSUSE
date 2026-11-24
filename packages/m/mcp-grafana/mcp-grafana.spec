#
# spec file for package mcp-grafana
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


Name:           mcp-grafana
Version:        2.4.0
Release:        0
Summary:        MCP server for Grafana
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/grafana/mcp-grafana
Source0:        https://github.com/grafana/mcp-grafana/archive/refs/tags/v%{version}.tar.gz#/mcp-grafana-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE mcp-grafana-usage-stats-opt-in.patch -- no usage stats by default
Patch0:         mcp-grafana-usage-stats-opt-in.patch
# go1.27 ClientHello is reset by F5/Palo Alto TLS middleboxes (golang/go#81199)
BuildRequires:  golang(API) = 1.26

%description
A Model Context Protocol (MCP) server for Grafana. It provides access to
a Grafana instance and the surrounding observability ecosystem (dashboards,
logs, traces) to MCP-compatible clients.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X github.com/grafana/mcp-grafana/v2.version=v%{version}" \
   -o mcp-grafana ./cmd/mcp-grafana

%install
install -D -m0755 mcp-grafana %{buildroot}%{_bindir}/mcp-grafana

%check
go test -tags unit -mod=vendor -count=1 ./...
cd lokiguard && go test -count=1 ./...

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/mcp-grafana

%changelog
