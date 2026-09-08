#
# spec file for package ghq
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


Name:           ghq
Version:        1.10.1
Release:        0
Summary:        Remote repository management made easy
License:        MIT
URL:            https://github.com/x-motemen/ghq
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.gz
BuildRequires:  git-core
BuildRequires:  golang(API) >= 1.26
BuildRequires:  zstd
Requires:       git-core

%description
ghq provides a way to organize remote repository clones, like go get does.
When you clone a remote repository by ghq get, ghq makes a directory under a
specific root directory (by default ~/ghq) using the remote repository URL's
host and path.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a 1 -p1

%build
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
go build -o bin/%{name} -ldflags="-X main.revision=%{version}"

%install
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 misc/bash/_%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 misc/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 misc/fish/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%check
export GOFLAGS="-mod=vendor -modcacherw"
git config --global user.name test
git config --global user.email test@example.com
go test ./...

%files
%license LICENSE
%doc README.adoc CHANGELOG.md CREDITS
%{_bindir}/%{name}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
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
