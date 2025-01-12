#
# spec file for package git-absorb
#
# Copyright (c) 2025 SUSE LLC
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


Name:           git-absorb
Version:        0.6.17
Release:        0
Summary:        git commit --fixup, but automatic
License:        BSD-3-Clause
URL:            https://github.com/tummychow/git-absorb
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Requires:       git-core
BuildRequires:  cargo >= 1.79
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A convenient git subcommand to automatically create
fixup! commits

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for git-absorb, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for git-absorb, generated during the build.

%package nushell-completion
Summary:        Nushell Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and nushell)
BuildArch:      noarch

%description nushell-completion
The official nushell completion script for git-absorb, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for git-absorb, generated during the build.

%prep
%autosetup -p1 -a1

%build

%install
%{cargo_install}

install -D Documentation/git-absorb.1 %{buildroot}%{_mandir}/man1/git-absorb.1
chmod -x %{buildroot}%{_mandir}/man1/git-absorb.1
TARGETBIN=target/release/git-absorb
$TARGETBIN --gen-completions bash > git-absorb.bash
$TARGETBIN --gen-completions fish > git-absorb.fish
$TARGETBIN --gen-completions nushell > git-absorb.nushell
$TARGETBIN --gen-completions zsh > git-absorb.zsh
install -Dm 644 git-absorb.bash %{buildroot}%{_datadir}/bash-completion/completions/git-absorb
install -Dm 644 git-absorb.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/git-absorb.fish
install -Dm 644 git-absorb.nushell %{buildroot}%{_datadir}/nushell/completions/git-absorb.nu
install -Dm 644 git-absorb.zsh %{buildroot}%{_datadir}/zsh/site-functions/_git-absorb

%check
%{cargo_test}

%files
%license LICENSE.md
%doc README.md
%{_mandir}/man1/git-absorb.1%{?ext_man}
%{_bindir}/%{name}

%files bash-completion
%license LICENSE.md
%{_datadir}/bash-completion

%files fish-completion
%license LICENSE.md
%{_datadir}/fish

%files nushell-completion
%license LICENSE.md
%{_datadir}/nushell

%files zsh-completion
%license LICENSE.md
%{_datadir}/zsh

%changelog
