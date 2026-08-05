#
# spec file for package slack-mcp-server
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# Flags shared by %%build and %%check:
#   -buildmode=pie  position independent executable, the openSUSE default
#   -mod=vendor     build strictly from the vendored tree unpacked from Source1,
#                   never from the network (OBS workers have none)
#   -modcacherw     leave the module cache writable so cleanup cannot fail
%define goflags "-buildmode=pie -mod=vendor -modcacherw"
# Go module path, as declared in go.mod; the version variables live under it.
%define gomodule github.com/korotovsky/slack-mcp-server
Name:           slack-mcp-server
Version:        1.3.0
Release:        0
Summary:        Model Context Protocol server for Slack
License:        MIT
URL:            https://github.com/korotovsky/slack-mcp-server
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# cgo stays enabled so -buildmode=pie links through the system linker, which is
# what emits the GNU build-id that debuginfo extraction needs.
BuildRequires:  gcc
# go.mod declares "go 1.25"; require the next stable API so the toolchain is
# always new enough without pinning one compiler package.
BuildRequires:  golang(API) >= 1.25
BuildRequires:  zstd

%description
A Model Context Protocol (MCP) server for Slack. It exposes Slack conversations,
channel and user directories, message history and search to MCP capable AI
clients and editors, over the stdio and server-sent-events transports.

It authenticates either with the browser session tokens of an existing Slack
login or with an OAuth user token, so it needs no workspace app installation and
no administrator approval. Slack Enterprise and GovSlack workspaces, direct
messages and group direct messages are supported.

%prep
%autosetup -p1 -a 1

%build
export GOFLAGS=%{goflags}
export GOPROXY=off
export GOTOOLCHAIN=local
export CGO_ENABLED=1

# Upstream's Makefile passes "-s -w", which strips the symbol table and DWARF
# and would leave the debuginfo subpackage empty; only the version stamping is
# kept here. BinaryName is what the server reports as its own name over MCP, so
# it has to match the installed binary.
go build \
    -ldflags "-X %{gomodule}/pkg/version.Version=v%{version} -X %{gomodule}/pkg/version.BinaryName=%{name}" \
    -o bin/%{name} ./cmd/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%check
export GOFLAGS=%{goflags}
export GOPROXY=off
export GOTOOLCHAIN=local
# The TestIntegration* cases in pkg/handler drive a real Slack workspace and an
# OpenAI endpoint -- they fail outright with "SLACK_MCP_XOXP_TOKEN not set" and
# "SLACK_MCP_OPENAI_API must be set" rather than skipping themselves. Everything
# else in that package, and every other package, runs.
go test -skip '^TestIntegration' ./...

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/%{name}

%changelog
