#
# spec file for package gitea-cli
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           gitea-cli
Version:        1.2.0
Release:        0
Summary:        Command-line client for Gitea
License:        MIT
URL:            https://gitea.com/gitea/cli
Source0:        https://gitea.com/gitea/cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch1:         unix-set-R12-before-the-ppc64x-syscall-branch.patch
BuildRequires:  git-core
BuildRequires:  golang(API) >= 1.27
BuildRequires:  golang-packaging
BuildRequires:  zstd
Requires:       ca-certificates
Requires:       git-core

%description
The official Gitea command-line client, gt, manages repositories, issues,
pull requests, releases, and other Gitea resources from the terminal or CI.
It requires a Gitea server running version 28 or newer.

%prep
%autosetup -n cli -a1 -p1

%build
export GOTOOLCHAIN=local
export GOPROXY=off
export GOFLAGS="-mod=vendor"
go build -buildmode=pie \
    -ldflags="-X gitea.dev/cli/internal/version.Version=%{version}" \
    -o gt ./cmd/gt
TZ=UTC go run ./tools/cli-docs --out docs/generated

%install
install -Dm0755 gt %{buildroot}%{_bindir}/gt
install -d %{buildroot}%{_mandir}/man1
install -m0644 docs/generated/man/*.1 %{buildroot}%{_mandir}/man1/
install -Dm0644 docs/generated/completion/gt.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/gt
install -Dm0644 docs/generated/completion/_gt \
    %{buildroot}%{_datadir}/zsh/site-functions/_gt
install -Dm0644 docs/generated/completion/gt.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/gt.fish
mkdir -p %{buildroot}%{_datadir}/skills/
cp -a skills/gt %{buildroot}%{_datadir}/skills/

%check
export GOTOOLCHAIN=local
export GOPROXY=off
export GOFLAGS="-mod=vendor"
go test ./...
./gt --version

%files
%license LICENSE
%doc README.md
%{_bindir}/gt
%{_mandir}/man1/gt*.1%{?ext_man}
%dir %{_datadir}/skills
%{_datadir}/skills/gt
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gt
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_gt
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/gt.fish

%changelog
