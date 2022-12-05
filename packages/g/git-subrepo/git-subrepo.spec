#
# spec file for package git-subrepo
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


Name:           git-subrepo
Version:        0.4.5
Release:        0
Summary:        Git Submodule Alternative
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/ingydotnet/git-subrepo
Source:         https://github.com/ingydotnet/git-subrepo/archive/%{version}.tar.gz
Patch0:         fix-shebangs.patch
BuildRequires:  bash >= 4
BuildRequires:  git-core >= 2.7
BuildRequires:  make
Requires:       bash >= 4
Requires:       git-core >= 2.7
BuildArch:      noarch

%description
This git command "clones" an external git repo into a subdirectory of your
repo. Later on, upstream changes can be pulled in, and local changes can be
pushed back. Simple.

%package bash-completion
Summary:        Bash completion for git-subrepo
Group:          Productivity/File utilities
Requires:       bash-completion
Supplements:    (git-subrepo and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for git-subrepo

%package zsh-completion
Summary:        ZSH completion for git-subrepo
Group:          Productivity/File utilities
Supplements:    (git-subrepo and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for git-subrepo

%prep
%setup -q
%patch0 -p1

%build

%check
# testing needs the source directory to be a git repo
#make test

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

# completions
install -Dm0644 share/completion.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/git-subrepo
install -Dm0644 share/zsh-completion/_git-subrepo \
    %{buildroot}%{_datadir}/zsh/site-functions/_git-subrepo

%files
%license License
%doc Changes ReadMe.pod
%{_libexecdir}/git/%{name}
%{_libexecdir}/git/%{name}.d
%{_mandir}/man1/*

%files bash-completion
%{_datadir}/bash-completion/completions/git-subrepo

%files zsh-completion
%{_datadir}/zsh

%changelog
