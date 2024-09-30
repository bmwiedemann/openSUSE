#
# spec file for package gum
#
# Copyright (c) 2024 SUSE LLC
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


%global _lto_cflags %nil
Name:           gum
Version:        0.14.5
Release:        0
Summary:        Tool for glamorous shell scripts
License:        MIT
URL:            https://github.com/charmbracelet/gum
Source0:        https://github.com/charmbracelet/gum/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  zstd
BuildRequires:  golang(API)

%description
Gum leverages the power of Bubbles and Lip Gloss in your scripts and aliases.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_CPPFLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.Version=%{version}"

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

# Completions
for sh in bash zsh fish; do
  ./%{name} completion $sh > %{name}.${sh}
done
install -Dm644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
