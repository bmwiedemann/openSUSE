#
# spec file for package beads
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


Name:           beads
Version:        1.3.2
Release:        0
Summary:        Distributed graph issue tracker for AI coding agents
# Legal-Review-Notice: licences of the Go modules linked into bd, from
# "go list -deps -tags gms_pure_go ./cmd/bd" (216 modules) against the
# LICENSE files of the vendored tree:
#  - MIT (beads itself and most modules), Apache-2.0 (Dolt, OpenTelemetry,
#    AWS SDK, ...), BSD-2-Clause and BSD-3-Clause (golang.org/x, ...).
#  - MPL-2.0: go-sql-driver/mysql, hashicorp/golang-lru (both major versions).
#    Their sources ship in the vendor tarball of the src.rpm.
#  - LGPL-3.0-only WITH LGPL-3.0-linking-exception: dolthub/fslock. Its LICENSE
#    grants the exception for static and dynamic linking in so many words.
#  - CC0-1.0: esote/minmaxheap. Unlicense: vbauerster/mpb (upstream
#    UNLICENSE, no licence file in the vendored subset).
#  - WTFPL: kch42/buzhash.
#  - oracle/oci-go-sdk is UPL-1.0 or Apache-2.0 and is taken as Apache-2.0.
#    dolthub/gozstd (MIT) compiles the bundled zstd (BSD-3-Clause, elected
#    over GPL-2.0-only). go-sqlite3 is built against the system sqlite
#    (libsqlite3 tag); its bundled public-domain amalgamation is not compiled.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-only WITH LGPL-3.0-linking-exception AND MIT AND MPL-2.0 AND Unlicense AND WTFPL
URL:            https://github.com/gastownhall/beads
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FEATURE-OPENSUSE 0001-make-usage-metrics-opt-in.patch -- no usage metrics unless the user runs "bd metrics on"
Patch0:         0001-make-usage-metrics-opt-in.patch
BuildRequires:  gcc
BuildRequires:  go >= 1.26.5
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(sqlite3)
Recommends:     git-core
# Dolt does not build on 32-bit (int overflows), and s390x/riscv64 are untested
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
Beads (bd) gives coding agents a persistent, structured memory: a
dependency-aware graph of issues stored in an embedded Dolt database
instead of loose markdown plans. It offers JSON output, hash based issue
identifiers that do not collide across branches or agents, ready-work
detection and cross-machine sync through Dolt remotes.

The command line tool is installed as bd.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional package supplying bash command completion for beads.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional package supplying zsh command completion for beads.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Optional package supplying fish command completion for beads.

%prep
%autosetup -p1 -a1

%build
export CGO_ENABLED=1
# gms_pure_go: go-mysql-server uses the Go regexp engine, not ICU
# libsqlite3: go-sqlite3 links the system sqlite instead of its bundled copy
go build -mod=vendor -buildmode=pie -tags "gms_pure_go libsqlite3" -o bd ./cmd/bd

%install
install -Dm0755 bd %{buildroot}%{_bindir}/bd
# bd writes its user configuration at startup
export HOME=%{_builddir}/home
mkdir -p "$HOME"
install -d %{buildroot}%{_datadir}/bash-completion/completions \
           %{buildroot}%{_datadir}/zsh/site-functions \
           %{buildroot}%{_datadir}/fish/vendor_completions.d
./bd completion bash > %{buildroot}%{_datadir}/bash-completion/completions/bd
./bd completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_bd
./bd completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/bd.fish

%check
export HOME=%{_builddir}/home
mkdir -p "$HOME"
./bd version
# usage metrics must stay off until the user opts in
./bd metrics | grep -q 'Anonymous usage metrics: OFF'

%files
%license LICENSE
%doc README.md
%{_bindir}/bd

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/bd

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bd

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/bd.fish

%changelog
