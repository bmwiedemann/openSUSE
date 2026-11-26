#
# spec file for package a2a-serve
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

Name:           a2a-serve
Version:        0.1.0
Release:        0
Summary:        Serve a coding agent over A2A from its project directory
# Legal-Review-Notice: MPL-2.0 vendor code is not shipped
# - MPL-2.0: go-yamux/v5, golang-lru/v2 via google/agentmesh, all behind
#   the `agentmesh` build tag; default `go list -deps` shows none linked.
License:        Apache-2.0
URL:            https://github.com/a2aproject/a2a-serve
Source0:        https://github.com/a2aproject/a2a-serve/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.26.6
# upstream ships binaries for amd64 and arm64 only, and the tailscale/gvisor
# dependencies do not build everywhere
ExclusiveArch:  x86_64 aarch64

%description
Turn opencode, Claude Code, or any ACP coding agent into a sandboxed A2A
agent that people, messengers, and other agents can call. Run one agent
per project directory, with Docker sandboxing, pairing-code identities,
Tailscale and relay networking, Telegram/Discord/email messengers, voice,
schedules, backups, and recipes.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}

%build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/.gocache
go build \
    -mod=vendor \
    -buildmode=pie \
    -ldflags "-X github.com/a2aproject/a2a-serve/internal/cli.version=%{version}" \
    -o a2a-serve .

%install
install -D -m0755 a2a-serve %{buildroot}%{_bindir}/a2a-serve

%check
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/.gocache
go test -mod=vendor ./...

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/a2a-serve

%changelog
