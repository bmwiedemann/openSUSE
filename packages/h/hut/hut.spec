#
# spec file for package hut
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


Name:           hut
Version:        0.5.0
Release:        0
Summary:        A CLI tool for sr.ht
License:        AGPL-3.0-or-later
Group:          Development/Tools/Navigators
URL:            https://sr.ht/~xenrox/hut
Source0:        https://git.sr.ht/~xenrox/hut/archive/v%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17
BuildRequires:  golang-packaging
BuildRequires:  scdoc
%{go_nostrip}

%description
hut is a CLI companion utility to interact with sr.ht.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for hut.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for hut.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for hut.

%prep
%autosetup -p1 -a1 -n %{name}-v%{version}

%build
make GOFLAGS='-mod=vendor -buildmode=pie -ldflags=-s'

%install
%make_install PREFIX=%{_prefix}

%check
go test -v

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%_mandir/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
