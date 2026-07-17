#
# spec file for package forge
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


Name:           forge
Version:        0.6.0
Release:        0
Summary:        A command line tool to interact with git forges
License:        MIT
URL:            https://github.com/git-pkgs/forge
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.26

%description
Go library and CLI for working with git forges. Supports GitHub, GitLab,
Gitea/Forgejo, and Bitbucket Cloud through a single interface.

%package bash-completion
Summary:        Bash Completion for forge
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for forge.

%package zsh-completion
Summary:        Zsh Completion for forge
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for forge.

%prep
%autosetup -a1 -p1
sed -i -e 's/var Version =.*/var Version = "%version"/' internal/cli/version.go

%build
go build \
   -o forge \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}" \
   cmd/forge/main.go

%check
go test -v \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-X main.Version=%{version}"

# check version output
%{buildroot}%{_bindir}/forge version | grep %{version}

%install
install -v -m 0755 -D -t %{buildroot}%{_bindir} forge

./forge completion bash > autocomplete.sh
sed -i '1d' autocomplete.sh
install -v -m 0644 -D autocomplete.sh \
    %{buildroot}%{_datadir}/bash-completion/completions/forge

./forge completion zsh > autocomplete.zsh
install -v -m 0644 -D autocomplete.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_forge

%files
%license LICENSE
%doc README.md
%{_bindir}/forge

%files bash-completion
%{_datadir}/bash-completion/completions/forge

%files zsh-completion
%{_datadir}/zsh/site-functions/_forge

%changelog
