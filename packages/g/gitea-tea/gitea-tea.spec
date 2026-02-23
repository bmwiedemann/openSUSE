#
# spec file for package gitea-tea
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


Name:           gitea-tea
Version:        0.12.0
Release:        0
Summary:        A command line tool to interact with Gitea servers
License:        MIT
URL:            https://gitea.com/gitea/tea
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25
Conflicts:      tea

%description
Tea can be used to manage most entities on one or multiple Gitea
instances and provides local helpers like 'tea pr checkout'.

It tries to make use of context provided by the repository in $PWD
if available. And works best in a upstream/fork workflow, when the
local main branch tracks the upstream repo. It also assumes that
local git state is published on the remote before doing operations.
Configuration lives in $XDG_CONFIG_HOME/tea.

%package bash-completion
Summary:        Bash Completion for Gitea's tea CLI
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for Gitea's tea CLI.

%package zsh-completion
Summary:        Zsh Completion for Gitea's tea CLI
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for Gitea's tea CLI.

%prep
%autosetup -a1 -p1

%build
go build \
   -o tea \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}"

# building docs
go run \
   docs/docs.go \
   -o docs/CLI.md \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}"

%install
install -v -m 0755 -D -t %{buildroot}%{_bindir} tea

./tea completion bash > contrib/autocomplete.sh
sed -i '1d' contrib/autocomplete.sh
install -v -m 0644 -D contrib/autocomplete.sh \
    %{buildroot}%{_datadir}/bash-completion/completions/tea

./tea completion zsh > contrib/autocomplete.zsh
install -v -m 0644 -D contrib/autocomplete.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_tea

%files
%license LICENSE
%doc CHANGELOG.md docs/CLI.md CONTRIBUTING.md README.md
%{_bindir}/tea

%files bash-completion
%{_datadir}/bash-completion/completions/tea

%files zsh-completion
%{_datadir}/zsh/site-functions/_tea

%changelog
