#
# spec file for package git-bug
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


Name:           git-bug
Version:        0.8.0+git.1733745604.d499b6e
Release:        0
Summary:        Distributed, offline-first bug tracker embedded in git, with bridges
License:        MIT
URL:            https://github.com/MichaelMure/git-bug
# Source0:        https://github.com/MichaelMure/%%{name}/archive/refs/tags/v%%{version}.tar.gz#/git-bug-%%{version}.tar.gz
Source0:        git-bug-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-UPSTREAM remote-config.patch gh#MichaelMure/git-bug!1076 mcepl@suse.com
# try reading git-bug.remote config value before defaulting to 'origin' when no explicit REMOTE argument
Patch0:         remote-config.patch
# PATCH-FIX-UPSTREAM CVE-2024-45337-bump-go-crypto.patch bsc#1234565 mcepl@suse.com
# bump golang.org/x/crypto from v0.26.0 to v0.31.0
Patch1:         CVE-2024-45337-bump-go-crypto.patch
BuildRequires:  golang(API) = 1.22
# # PATCH-FEATURE-UPSTREAM 501-export.patch gh#MichaelMure/git-bug!501 mcepl@suse.com
# # add a command to export bugs as raw operations
# Patch0:         501-export.patch
BuildRequires:  golang-packaging
BuildRequires:  git

%description
git-bug is a bug tracker that:

* is fully embedded in git: you only need your git repository to have
  a bug tracker
* is distributed: use your normal git remote to collaborate, push and
  pull your bugs!
* works offline: in a plane or under the sea? Keep reading and
  writing bugs!
* prevents vendor lock-in: your usual service is down or went bad?
  You already have a full backup.
* is fast: listing bugs or opening them is a matter of
  milliseconds
* doesn't pollute your project: no files are added in your
  project
* integrates with your tooling: use the UI you like (CLI,
  terminal, web) or integrate with your existing tools through
  the CLI or the GraphQL API
* bridges to other bug trackers: use bridges to import and export
  to other trackers.

%package bash-completion
Summary:        Bash completion for git-bug
Requires:       bash-completion
Supplements:    (git-bug and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for git-bug

%package fish-completion
Summary:        Fish completion for git-bug
Requires:       fish
Supplements:    (git-bug and fish)
BuildArch:      noarch

%description fish-completion
Fish shell completions for git-bug

%package zsh-completion
Summary:        ZSH completion for git-bug
Group:          Productivity/File utilities
Supplements:    (git-bug and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for git-bug

%prep
%autosetup -p1 -a1

%build
%make_build build

%install
install -Dm755 git-bug %{buildroot}%{_bindir}/git-bug
install -Dm644 -t %{buildroot}%{_mandir}/man1/ doc/man/*

# shell completions
install -Dm0644 misc/completion/bash/git-bug  \
    %{buildroot}%{_datadir}/bash-completion/completions/git-bug
install -Dm0644 misc/completion/fish/git-bug  \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/git-bug.fish
install -Dm0644 misc/completion/zsh/git-bug  \
    %{buildroot}%{_sysconfdir}/zsh_completion.d/git-bug

%check
# before we mark network requiring tests (gh#git-bug/git-bug#1313)
%make_build test || true

%files
%license LICENSE
%doc README.md
%{_bindir}/git-bug
%{_mandir}/man1/git*.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/git-bug

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/git-bug.fish

%files zsh-completion
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/git-bug

%changelog
