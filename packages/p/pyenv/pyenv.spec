#
# spec file for package pyenv
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


%define pyenv_dir      %{_libexecdir}/pyenv
#
Name:           pyenv
Version:        2.4.5
Release:        0
Summary:        Python Version Management
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pyenv/pyenv
Source:         https://github.com/pyenv/pyenv/archive/refs/tags/v%{version}.tar.gz#/pyenv-%{version}.tar.gz
#
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zsh
#
Requires:       pkgconfig
#
# Additional soft build requirements.
# Use list from https://github.com/pyenv/pyenv/wiki#suggested-build-environment
#
# Once pyenv is installed and user requests a new Python version,
# we need to make sure it will build:
Recommends:     automake
Recommends:     bzip2
Recommends:     findutils
Recommends:     gcc
#
Recommends:     gdbm-devel
Recommends:     gmp-devel
Recommends:     openssl-devel
Recommends:     patch
Recommends:     readline-devel
#
Recommends:     pkgconfig(bzip2)
Recommends:     pkgconfig(clzma)
Recommends:     pkgconfig(expat)
Recommends:     pkgconfig(libffi)
Recommends:     pkgconfig(liblzma)
Recommends:     pkgconfig(ncurses)
Recommends:     pkgconfig(sqlite3)
Recommends:     pkgconfig(tcl)
Recommends:     pkgconfig(tk)
Recommends:     pkgconfig(uuid)
Recommends:     pkgconfig(zlib)

%description
pyenv lets the user switch between multiple versions of Python.

This project was forked from rbenv and ruby-build, and modified for Python.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (pyenv and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (pyenv and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (pyenv and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

sed -i -e '1s,^#!%{_bindir}/env bash,#!/bin/bash,' libexec/* pyenv.d/exec/pip-rehash/* plugins/python-build/bin/*

%build
##
pushd src
%configure
%make_build
popd

%install
mkdir -p %{buildroot}%{pyenv_dir} \
         %{buildroot}%{pyenv_dir}/plugins \
         %{buildroot}%{pyenv_dir}/shims/ \
         %{buildroot}%{pyenv_dir}/share/python-build/ \
         %{buildroot}%{_sysconfdir}/pyenv.d/ \
         %{buildroot}%{_bindir}

cp -R libexec %{buildroot}%{pyenv_dir}
cp -R bin %{buildroot}%{pyenv_dir}
cp -a pyenv.d %{buildroot}%{_sysconfdir}/

## Install shell completions:
install -D -m0644 completions/pyenv.bash %{buildroot}%{_datadir}/bash-completion/completions/pyenv
install -D -m0644 completions/pyenv.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/pyenv
install -D -m0644 completions/pyenv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/pyenv.fish

## Install manpage
install -D -m0644 man/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
pushd %{buildroot}%{_mandir}/man1/
 ln -s %{name}.1 python-build.1
popd

ln -s %{pyenv_dir}/bin/pyenv %{buildroot}%{_bindir}/pyenv

## python-build
pushd plugins/python-build
 install -m755 bin/* %{buildroot}%{pyenv_dir}/libexec
 cp -a share/python-build %{buildroot}%{pyenv_dir}/share/
popd

%fdupes %{buildroot}%{pyenv_dir}

%files
%doc CHANGELOG.md COMMANDS.md README.md
%license LICENSE
%exclude %{_sysconfdir}/pyenv.d/rehash/*/.gitignore

%config %{_sysconfdir}/pyenv.d/rehash/*.d/default.list
%config %{_sysconfdir}/pyenv.d/exec/pip-rehash.bash
%config %{_sysconfdir}/pyenv.d/rehash/*.bash
%config %{_sysconfdir}/pyenv.d/install/*.bash

%{pyenv_dir}
%dir %{_sysconfdir}/pyenv.d
%dir %{_sysconfdir}/pyenv.d/exec/
%dir %{_sysconfdir}/pyenv.d/rehash/
%dir %{_sysconfdir}/pyenv.d/rehash/*.d/
%dir %{_sysconfdir}/pyenv.d/install/

%{_sysconfdir}/pyenv.d/exec/pip-rehash
%{_bindir}/pyenv
#
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/python-build.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/pyenv

%files fish-completion
%{_datadir}/fish/vendor_completions.d/pyenv.fish

%files zsh-completion
%config %{_sysconfdir}/zsh_completion.d/pyenv

%changelog
