#
# spec file for package github-mcp-server
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
Name:           github-mcp-server
Version:        1.9.0
Release:        0
Summary:        Model Context Protocol server for GitHub
License:        MIT
URL:            https://github.com/github/github-mcp-server
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM github-mcp-server-root-command-name.patch gh#github/github-mcp-server#2998 mpluskal@suse.com -- name the cobra root command after the installed binary so generated shell completions actually fire
Patch0:         %{name}-root-command-name.patch
# cgo stays enabled so -buildmode=pie links through the system linker, which is
# what emits the GNU build-id that debuginfo extraction needs. go1.26 pulls gcc
# in transitively, but this package depends on it directly, so say so.
BuildRequires:  gcc
# go.mod declares "go 1.25.12"; require the next stable API so the toolchain is
# always new enough without pinning one compiler package (Go refuses to build a
# module that asks for a newer patch level than the toolchain provides, and
# toolchain auto-download is unavailable offline).
BuildRequires:  golang(API) >= 1.26
BuildRequires:  zstd
# Only used for the optional OAuth browser flow (internal/oauth/env.go shells
# out to xdg-open); the token-based path needs nothing external.
Recommends:     xdg-utils

%description
GitHub's official Model Context Protocol (MCP) server. It exposes the GitHub
API - repositories, issues, pull requests, Actions, code scanning, discussions
and more - as MCP tools, so MCP capable AI clients and editors can query and
act on GitHub on the user's behalf.

The server speaks both the stdio transport and streamable HTTP, groups its
tools into toolsets that can be enabled individually, and supports a read-only
mode.

Authenticate with a GitHub personal access token. Note that this build carries
no built-in OAuth client credentials - those belong to upstream's own published
binaries and are not part of the source - so the zero configuration OAuth login
described in some of the upstream documentation is unavailable here. Use a
personal access token, GitHub App credentials, or pass your own OAuth client id
via --oauth-client-id.

%package mcpcurl
Summary:        Command line client for exploring MCP server tools

%description mcpcurl
mcpcurl connects to any Model Context Protocol server over stdio, retrieves the
tool schema the server advertises and dynamically builds a command line
interface from it: every tool becomes a subcommand whose flags are validated
against the schema.

It is a developer and debugging aid for MCP servers in general and for the
GitHub MCP server in particular. The tool is self-contained and does not
require the server package to be installed.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p1 -a 1

%build
# The MCP App UI (the ui/ directory, a Vite/TypeScript tree that script/build-ui
# compiles into pkg/github/ui_dist/) is deliberately NOT built: it would pull in
# several hundred npm packages that are not available in the distribution.
# Upstream ships a committed ui_dist/.placeholder.html so the "//go:embed
# ui_dist/*.html" directive still resolves, and every UI call site is guarded by
# github.UIAssetsAvailable() (pkg/github/server.go), which returns false when the
# real assets are absent. The server therefore starts and runs normally, only
# without the optional HTML app resources; all tools and both transports work.

# Reproducible timestamp for the version banner. SOURCE_DATE_EPOCH is exported
# by OBS but not by a plain rpmbuild, so fall back rather than fail the build.
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null \
    || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null \
    || date -u "${DATE_FMT}")

export GOFLAGS=%{goflags}
export GOPROXY=off
export GOTOOLCHAIN=local
export CGO_ENABLED=1

# ldflags notes:
#  * Upstream's Dockerfile passes "-s -w". We deliberately do not: those drop
#    the symbol table and DWARF data, which would leave the -debuginfo
#    subpackage empty and make crash reports unusable.
#  * Upstream release builds additionally inject
#    internal/buildinfo.OAuthClientID and .OAuthClientSecret. Those are
#    GitHub's own credentials for their published binaries; they are not part
#    of the source and cannot be reproduced here, so they stay unset. See the
#    note in %%description.
#  * main.commit stays empty on purpose: the sources are the upstream release
#    tarball and carry no git metadata. The release is reported via main.version.
go build \
    -ldflags "-X main.version=%{version} -X main.commit= -X main.date=${BUILD_DATE}" \
    -o bin/%{name} ./cmd/%{name}

# mcpcurl declares no build-time variables of its own, so it takes no -ldflags.
go build -o bin/mcpcurl ./cmd/mcpcurl

%install
install -D -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0755 bin/mcpcurl %{buildroot}%{_bindir}/mcpcurl

# Shell completions, generated by the binary we just built. These are only
# correct because Patch0 names the root command after the binary; without it
# cobra emits a dispatcher keyed on "server" that never fires. mcpcurl already
# names its root command correctly but is a debugging aid, so it does not get
# completion subpackages of its own.
bin/%{name} completion bash | install -D -m 0644 /dev/stdin \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
bin/%{name} completion zsh | install -D -m 0644 /dev/stdin \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
bin/%{name} completion fish | install -D -m 0644 /dev/stdin \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%check
# The unit tests run completely offline and need no GitHub token. The suites
# that do require a token and network live in e2e/ behind a "//go:build e2e"
# constraint and are not selected by ./... .
export GOFLAGS=%{goflags}
export GOPROXY=off
export GOTOOLCHAIN=local
go test ./...

%files
# third-party/ holds the license texts of the statically linked dependencies and
# third-party-licenses.linux.md is the inventory mapping them to modules; only
# the linux variant is relevant to what we ship.
%license LICENSE third-party-licenses.linux.md third-party/
%doc README.md docs/
%{_bindir}/%{name}

%files mcpcurl
%license LICENSE
%doc cmd/mcpcurl/README.md
%{_bindir}/mcpcurl

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
