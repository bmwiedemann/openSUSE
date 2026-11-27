#
# spec file for package mcp-server-susedoc
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for modifications and additions to the file is the
# same license as for the pristine package itself (unless the license
# for the pristine package is not an Open Source License, in which case
# the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           mcp-server-susedoc
Version:        0.1.5
Release:        0
Summary:        MCP server for openSUSE and SUSE documentation
License:        MIT
URL:            https://github.com/openSUSE/mcp-server-susedoc
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.27
BuildRequires:  golang-packaging

%description
An MCP (Model Context Protocol) server which reads openSUSE and SUSE
documentation written in DocBook, AsciiDoc, Markdown or plain text and
presents it to an LLM. It offers tools to list and read documents, to find
where a shell command is mentioned and to look up the definition of a term.
A small web interface wrapping the same functions is included.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags "-X mcp-server-susedoc/internal/mcpserver.Version=%{version}" \
   -o bin/%{name} ./cmd/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
# directory where documentation packages drop their exported documents
install -d -m 0755 %{buildroot}%{_docdir}/%{name}.d

%check
go test -mod=vendor ./...

%files
%doc README.md
%{_bindir}/%{name}
%dir %{_docdir}/%{name}.d

%changelog
