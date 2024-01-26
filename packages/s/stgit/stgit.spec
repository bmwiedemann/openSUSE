#
# spec file for package stgit
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


Name:           stgit
Version:        2.4.2
Release:        0
Summary:        Stacked GIT - Source Code Management Tool
License:        GPL-2.0-or-later
URL:            https://stacked-git.github.io
Source0:        https://github.com/ctmarinas/stgit/releases/download/v%{version}/stgit-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  asciidoc
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(openssl)
Requires:       git-core
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
Stacked Git, StGit for short, is an application for managing Git commits
as a stack of patches.
With a patch stack workflow, multiple patches can be developed
concurrently and efficiently, with each patch focused on a single
concern, resulting in both a clean Git commit history and improved
productivity.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (stgit and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (stgit and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (stgit and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%package emacs
Summary:        emacs plugin for for %{name}
Requires:       %{name} = %{version}
Requires:       emacs
Supplements:    (stgit and emacs)
BuildArch:      noarch

%description emacs
emacs command line completion support for %{name}.

%package vim-plugin
Summary:        VIM plugin for for %{name}
Requires:       %{name} = %{version}
Requires:       vim
Supplements:    (stgit and vim)
BuildArch:      noarch

%description vim-plugin
VIM command line completion support for %{name}.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%make_install prefix=%{_prefix} install-completion install-contrib install-man

%files
%doc AUTHORS.md README.md CHANGELOG.md
%license COPYING
%{_bindir}/stg
%{_mandir}/man1/stg*

%files bash-completion
%{_datadir}/bash-completion/completions/stg

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/stg.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_stg

%files emacs
%{_datadir}/emacs/site-lisp/stgit.el

%files vim-plugin
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/ftdetect/stg.vim
%{_datadir}/vim/vimfiles/syntax/stg*.vim

%changelog
