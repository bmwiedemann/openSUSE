#
# spec file for package mcp-dap-server
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


Name:           mcp-dap-server
Version:        0.0.0+git20250716.7ffcc1d
Release:        0
Summary:        MCP server to communicate with DAP servers
License:        MIT
Group:          Development/Languages/Go
URL:            https://github.com/delve/mcp-dap-server
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description

A Model Context Protocol (MCP) server that provides debugging capabilities through the
Debug Adapter Protocol (DAP). This server enables AI assistants and other MCP clients
to interact with debuggers for various programming languages.

The MCP DAP Server acts as a bridge between MCP clients and DAP-compatible debuggers,
allowing programmatic control of debugging sessions. It provides a comprehensive set
of debugging tools that can be used to:

- Start and stop debugging sessions
- Set breakpoints (line-based and function-based)
- Control program execution (continue, step in/out/over, pause)
- Inspect program state (threads, stack traces, variables, scopes)
- Evaluate expressions
- Attach to running processes
- Handle exceptions

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
