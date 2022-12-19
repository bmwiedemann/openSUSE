#
# spec file for package fzf
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


Name:           fzf
Version:        0.35.1
Release:        0
Summary:        A command-line fuzzy finder
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/junegunn/fzf
Source0:        https://github.com/junegunn/fzf/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.19

%description
fzf is an interactive Unix filter for command-line that can be used with any list; files,
command history, processes, hostnames, bookmarks, git commits, etc.

%package tmux
Summary:        Tmux integration for fzf
Group:          Productivity/File utilities
Supplements:    (fzf and tmux)
BuildArch:      noarch

%description tmux
Tmux integration for fzf. Includes a wrapper script, fzf-tmux, that opens your list in a
separate tmux pane.

%package bash-completion
Summary:        Bash completion for fzf
Group:          Productivity/File utilities
Requires:       bash-completion
Supplements:    (fzf and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for fzf

%package fish-completion
Summary:        Fish completion for fzf
Group:          Productivity/File utilities
Requires:       fish
Supplements:    (fzf and fish)
BuildArch:      noarch

%description fish-completion
fish shell completions for fzf

To enable it, ensure you have a file ~/.config/fish/functions/fish_user_key_bindings.fish
which contains:
function fish_user_key_bindings
	fzf_key_bindings
end

(or append fzf_key_bindings to the fish_user_key_bindings function if the file already exists)

%package zsh-completion
Summary:        ZSH completion for fzf
Group:          Productivity/File utilities
Supplements:    (fzf and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for fzf

%define     vimplugin_dir %{_datadir}/vim/site

%package -n vim-fzf
Summary:        Vim plugin for fzf
Group:          Productivity/File utilities
Requires:       (vim or neovim)
BuildArch:      noarch

%description -n vim-fzf
Plugin for vim allowing use of fzf.

%prep
%autosetup -p1 -a1

# fix  E: env-script-interpreter
sed -i 's,#!%{_bindir}/env ,#!/bin/,' ./bin/fzf-tmux

%build
export FZF_VERSION=%{version} FZF_REVISION=tarball
export GOCACHE=$(readlink -f vendor/)
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.revision=%{version}"

%install
install -Dm755 fzf %{buildroot}%{_bindir}/fzf
install -Dm755 bin/fzf-tmux %{buildroot}%{_bindir}/fzf-tmux
install -Dm644 man/man1/fzf.1 %{buildroot}%{_mandir}/man1/fzf.1
install -Dm644 man/man1/fzf-tmux.1 %{buildroot}%{_mandir}/man1/fzf-tmux.1

# shell completions
install -Dm0644 shell/completion.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/fzf
install -Dm0644 shell/key-bindings.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/fzf-key-bindings
install -Dm0644 shell/completion.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_fzf
install -Dm0644 shell/key-bindings.zsh \
    %{buildroot}%{_sysconfdir}/zsh_completion.d/fzf-key-bindings
install -Dm0644 shell/key-bindings.fish \
    %{buildroot}%{_datadir}/fish/vendor_functions.d/fzf_key_bindings.fish

# vim plugin
install -D -m0644 -t %{buildroot}%{vimplugin_dir}/doc doc/*
install -D -m0644 -t %{buildroot}%{vimplugin_dir}/plugin plugin/*

%check
export SHELL=/bin/sh GOOS=
export GOCACHE=$(readlink -f vendor/)
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go test -v -x -mod=vendor ${BUILDMOD} -a \
    -ldflags "-X main.revision=%{version}" \
    github.com/junegunn/fzf/src \
    github.com/junegunn/fzf/src/algo \
    github.com/junegunn/fzf/src/tui \
    github.com/junegunn/fzf/src/util

%files
%doc README.md
%{_bindir}/fzf
%{_mandir}/man1/fzf.1%{?ext_man}
%license LICENSE

%files tmux
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf-tmux.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/fzf
%{_datadir}/bash-completion/completions/fzf-key-bindings

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/fzf_key_bindings.fish

%files zsh-completion
%{_datadir}/zsh
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/fzf-key-bindings

%files -n vim-fzf
%doc README-VIM.md
%dir %{_datadir}/vim
%dir %{vimplugin_dir}
%{vimplugin_dir}/doc
%{vimplugin_dir}/plugin

%changelog
