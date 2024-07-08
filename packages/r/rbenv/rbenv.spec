#
# spec file for package rbenv
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


Name:           rbenv
Version:        1.3.0
Release:        0
BuildArch:      noarch
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/rbenv/rbenv
Summary:        Simple Ruby version Management
Source0:        https://github.com/rbenv/rbenv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{undefined sle_version}
BuildRequires:  bats
BuildRequires:  git
BuildRequires:  procps
%endif
Requires:       procps
Recommends:     ruby-build

%description
rbenv does…

- Let you change the global Ruby version on a per-user basis.
- Provide support for per-project Ruby versions.
- Allow you to override the Ruby version with an environment variable.

In contrast with rvm, rbenv does not…

- Need to be loaded into your shell. Instead, rbenv's shim approach works by adding a directory to your $PATH.
- Override shell commands like cd. That's dangerous and error-prone.
- Have a configuration file. There's nothing to configure except which version of Ruby you want to use.
- Install Ruby. You can build and install Ruby yourself, or use ruby-build to automate the process.
- Manage gemsets. Bundler is a better way to manage application dependencies. If you have projects that are not yet using Bundler you can install the rbenv-gemset plugin.
- Require changes to Ruby libraries for compatibility. The simplicity of rbenv means as long as it's in your $PATH, nothing else needs to know about it.
- Prompt you with warnings when you switch to a project. Instead of executing arbitrary code, rbenv reads just the version name from each project. There's nothing to "trust."

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%setup -q

%build

%install
install -Dm0755 libexec/* -t %{buildroot}%{_bindir}

install -Dm0644 completions/rbenv.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 completions/_rbenv %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm0644 share/man/man1/rbenv.1 %{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}/usr/lib/rbenv
cp -r rbenv.d/* %{buildroot}/usr/lib/rbenv

sed -i 's|#!/usr/bin/env bash|#!/bin/bash|g' %{buildroot}%{_bindir}/*

%check
%if %{undefined sle_version}
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/rbenv*
/usr/lib/rbenv
%{_mandir}/man1/%{name}*

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%changelog
