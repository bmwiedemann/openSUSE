#
# spec file for package skim
#
# Copyright (c) 2021 SUSE LLC
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


Name:           skim
Version:        0.20.5
Release:        0
Summary:        A fuzzy finder for the command line
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/skim-rs/skim
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        README.suse-maint.md
BuildRequires:  cargo >= 1.31
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(bash-completion)

%description
Half of our life is spent on navigation: files, lines, commands… You need skim!
It is a general fuzzy finder that saves you time.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for skim, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for skim, generated during the build.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -Dm 0755 target/release/sk %{buildroot}%{_bindir}/sk

install -d -m 0755 %{buildroot}%{_mandir}/man1/
install -m 0644 man/man1/sk.1 %{buildroot}%{_mandir}/man1/sk.1

install -m 0755 bin/sk-tmux %{buildroot}%{_bindir}/sk-tmux
sed -i 's#/usr/bin/env bash#%{_bindir}/bash#g' %{buildroot}%{_bindir}/sk-tmux
install -m 0644 man/man1/sk-tmux.1 %{buildroot}%{_mandir}/man1/sk-tmux.1

install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 shell/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/sk

install -d -m 0755 %{buildroot}%{_datadir}/zsh/site-functions
install -m 0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_sk

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/sk
%{_bindir}/sk-tmux
%{_mandir}/man1/sk.1%{?ext_man}
%{_mandir}/man1/sk-tmux.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/sk

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_sk

%changelog
