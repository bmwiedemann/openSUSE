#
# spec file for package tilth
#
# Copyright (c) 2026 SUSE LLC
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


Name:           tilth
Version:        0.10.1
Release:        0
Summary:        Tree-sitter indexed code lookups for humans and AI agents
# Legal-Review-Notice: upstream is MIT; the remaining tags come from crates
# statically linked into the binary (cargo tree -e normal,build, linux target):
#   Apache-2.0   tree-sitter-elixir (sole term, no MIT alternative)
#   BSD-3-Clause encoding_rs ((Apache-2.0 OR MIT) AND BSD-3-Clause)
#   Zlib         foldhash (sole term)
# Everything else elects MIT.  Unicode-3.0 from unicode-ident is deliberately
# NOT declared: it is reachable only through proc-macro2 <- the proc-macro
# crates (clap_derive, serde_derive, thiserror-impl, syn), which run on the
# build host and are not linked into the target binary.
# Windows/WASI/Redox-only crates are not built and impose nothing.
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND Zlib
URL:            https://github.com/jahala/tilth
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
# "tilth diff"/"overview" shell out to git at runtime; %%check builds throwaway repos
BuildRequires:  git-core
Requires:       git-core
ExclusiveArch:  %{rust_tier1_arches}

%description
tilth indexes a source tree with tree-sitter and answers structural
queries about it - definitions, references, call sites and file
overviews - instead of dumping whole files. It is usable directly from
the command line and as an MCP server, which cuts the token cost of
letting an AI agent read a code base.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion for %{name}, generated during the build.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion for %{name}, generated during the build.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion for %{name}, generated during the build.

%prep
%autosetup -a1

%build
# upstream's release profile sets strip = true, which would leave -debuginfo empty
export CARGO_PROFILE_RELEASE_STRIP=false
%{cargo_build}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

BIN=target/release/%{name}
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d %{buildroot}%{_datadir}/zsh/site-functions
$BIN --completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
$BIN --completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
$BIN --completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
%{cargo_test}

%files
%license LICENSE
%doc ARCHITECTURE.md README.md SECURITY.md
%{_bindir}/%{name}

%files bash-completion
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
