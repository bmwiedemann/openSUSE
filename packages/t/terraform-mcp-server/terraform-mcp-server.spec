#
# spec file for package terraform-mcp-server
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

Name:           terraform-mcp-server
Version:        1.4.1
Release:        0
Summary:        Official Terraform MCP server for Infrastructure as Code
License:        MPL-2.0
URL:            https://github.com/hashicorp/terraform-mcp-server
Source0:        https://github.com/hashicorp/terraform-mcp-server/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.26.10

%description
The Terraform MCP Server is a Model Context Protocol (MCP) server that
integrates with the Terraform Registry and HCP Terraform (Terraform Cloud)
APIs, enabling automation and interaction capabilities for Infrastructure
as Code (IaC) development. It exposes Terraform Registry modules,
providers and policies as MCP tools and resources for AI assistants.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}

%build
go build \
	-o %{name} \
	-mod=vendor \
	-buildmode=pie \
	./cmd/terraform-mcp-server

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# e2e/ needs docker (upstream `make test-e2e`); the skipped tests
# reach registry.terraform.io / app.terraform.io
go test -mod=vendor \
    -skip '^(TestSendRegistryCall|TestGetTfeClientForSession|TestGetTfeClient_DelegatesPerSession|TestOrganizationListerForRequestIgnoresContextAddress)$' \
    ./pkg/... ./cmd/... ./test/... ./version/...

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}

%changelog
