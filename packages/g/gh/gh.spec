#
# spec file for package gh
#
# Copyright (c) 2022 SUSE LLC
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


%define goflags "-buildmode=pie -trimpath -mod=vendor -modcacherw"
%define sname cli
Name:           gh
Version:        2.20.2
Release:        0
Summary:        The official CLI for GitHub
License:        MIT
Group:          Development/Tools/Other
URL:            https://cli.github.com/
Source0:        https://github.com/cli/cli/archive/v%{version}.tar.gz#/%{sname}-%{version}.tar.gz
Source1:        vendor.tar.gz
# Completions
BuildRequires:  fish
BuildRequires:  zsh
# Build/Test requirements
BuildRequires:  git-core
BuildRequires:  golang(API) >= 1.18
Requires:       git-core

%description
Official CLI client for GitHub written in Go

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
%if 0%{?suse_version} == 1315
Supplements:    packageand(gh:bash-completion)
%else
Supplements:    (gh and bash-completion)
%endif
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} == 1315
Supplements:    packageand(gh:zsh)
%else
Supplements:    (gh and zsh)
%endif
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} == 1315
Supplements:    packageand(gh:fish)
%else
Supplements:    (gh and fish)
%endif
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -n %{sname}-%{version} -a 1
# Upstream decided to tweak Makefile for easier cross-compiling. But the tweak
# overrides variables so we need to remove them to pass GOFLAGS.
sed -i 's/GOOS= GOARCH= GOARM= GOFLAGS= CGO_ENABLED=//g' Makefile

%build
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw -ldflags=-linkmode=external"
%if 0%{?suse_version} == 1315
make %{?_smp_mflags} GH_VERSION="v%{version}" bin/gh manpages
%else
%make_build GH_VERSION="v%{version}" bin/gh manpages
%endif

%install
bin/gh completion -s bash | install -Dm644 /dev/stdin \
       %{buildroot}%{_datadir}/bash-completion/completions/gh
bin/gh completion -s zsh  | install -Dm644 /dev/stdin \
       %{buildroot}%{_datadir}/zsh/site-functions/_gh
bin/gh completion -s fish | install -Dm644 /dev/stdin \
       %{buildroot}%{_datadir}/fish/vendor_completions.d/gh.fish

install -Dm755 bin/gh %{buildroot}%{_bindir}/gh
install -d %{buildroot}%{_mandir}/man1/
cp share/man/man1/* %{buildroot}%{_mandir}/man1

%check
GOFLAGS=%{goflags} make test

%files
%doc README.md
%license LICENSE
%{_bindir}/gh
%{_mandir}/man1/*

%files bash-completion
%{_datadir}/bash-completion/completions/gh

%files zsh-completion
%{_datadir}/zsh/site-functions/_gh

%files fish-completion
%{_datadir}/fish/vendor_completions.d/gh.fish

%changelog
