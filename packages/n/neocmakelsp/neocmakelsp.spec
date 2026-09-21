#
# spec file for package neocmakelsp
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


Name:           neocmakelsp
Version:        0.11.1
Release:        0
Summary:        CMake LSP implementation based on Tower and Tree-sitter
# Legal-Review-Notice: neocmakelsp itself is MIT. The shipped binary
# statically links Apache-2.0 (sync_wrapper via tower) and Unicode-3.0
# (icu_* via idna/url/tower-lsp-f). No copyleft crate is in the
# cargo-tree -e normal graph; r-efi (MIT OR Apache-2.0 OR
# LGPL-2.1-or-later) is vendored but not linked on Linux. tiny-keccak
# (CC0-1.0) is compile-time-only via const-random-macro.
License:        Apache-2.0 AND MIT AND Unicode-3.0
URL:            https://github.com/neocmakelsp/neocmakelsp
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  bash
BuildRequires:  cargo >= 1.89
BuildRequires:  cargo-packaging
BuildRequires:  fish
BuildRequires:  zsh
ExclusiveArch:  %{rust_tier1_arches}

%package        fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%description
NeoCmakeLSP is another Cmake LSP. It differs from other LSP implementations as it uses
TreeSitter and Tower, crates that are written in Rust.

It provides the following features such as:
* Intelligent Code Completion: Provides precise code completions by analyzing CMake files, enhancing development efficiency.
* Real-time Error Detection: Integrates linting functionality to check for potential issues in your code, help maintaining code quality.
* Support for Neovim, Emacs, VSCode, Helix: Compatible with these popular editors, catering to diverse developer needs.
* Simple Configuration: Easy to set up and use, minimizing configuration time so you can focus on development.
* CLI Integration: Not only an LSP, but also includes command-line tools for code formatting, making it convenient for different environments.

%prep
%autosetup -a1

%build
export CARGO_TARGET_DIR="%{_builddir}/%{buildsubdir}/target"
%{cargo_build}

%check
export CARGO_TARGET_DIR="%{_builddir}/%{buildsubdir}/target"
%{cargo_test}

%install
export CARGO_TARGET_DIR="%{_builddir}/%{buildsubdir}/target"
%cargo_install
install -Dpm 0644 -t %{buildroot}%{_datadir}/bash-completion/completions/%{name}    completions/bash/%{name}
install -Dpm 0644 -t %{buildroot}%{_datadir}/zsh/site-functions/_%{name}            completions/zsh/_%{name}
install -Dpm 0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish completions/fish/%{name}.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
