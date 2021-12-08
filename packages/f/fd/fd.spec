#
# spec file for package fd
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


Name:           fd
Version:        8.3.0
Release:        0
Summary:        An alternative to the "find" utility
License:        Apache-2.0 AND MIT
Group:          Productivity/File utilities
URL:            https://github.com/sharkdp/fd
Source:         https://github.com/sharkdp/fd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
fd is an alternative to GNU find. It features:

* Colorized terminal output (similar to ls).
* The search is case-insensitive by default. It switches to
  case-sensitive if the pattern contains an uppercase character.
* By default, ignores patterns from .gitignore, and ignores hidden
  directories and files.
* Supports regular expressions and Unicode awareness.
* A parallel execution similar to GNU Parallel is available.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for fd, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for fd, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for fd, generated during the build.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

# install shell completions and man page
install -Dm644 target/release/build/fd-find-*/out/fd.bash %{buildroot}%{_datadir}/bash-completion/completions/fd
install -Dm644 target/release/build/fd-find-*/out/fd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/fd.fish
install -Dm644 contrib/completion/_fd %{buildroot}%{_datadir}/zsh/site-functions/_fd
install -Dm644 doc/fd.1 %{buildroot}%{_mandir}/man1/fd.1

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/fd
%{_mandir}/man1/fd.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
