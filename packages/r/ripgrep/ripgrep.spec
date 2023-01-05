#
# spec file for package ripgrep
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           ripgrep
Version:        13.0.0
Release:        0
Summary:        A search tool that combines ag with grep
License:        MIT AND Unlicense
Group:          Productivity/Text/Utilities
URL:            https://github.com/BurntSushi/ripgrep
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source999:      README.suse-maint.md
BuildRequires:  cargo
BuildRequires:  pkgconf
BuildRequires:  rust >= 1.31
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  rubygem(asciidoctor)

%description
ripgrep is a line oriented search tool that combines the usability of
The Silver Searcher (similar to ack) with the raw speed of GNU grep.
ripgrep works by recursively searching your current directory
for a regex pattern.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for ripgrep, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for ripgrep, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for ripgrep, generated during the build.

%prep
%autosetup -p1 -a1

install -d -m 0755 .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
cargo build --release --features 'pcre2' %{?_smp_mflags}

%install
export RUSTFLAGS=%{rustflags}
cargo install --path . --root=%{buildroot}%{_prefix}

# remove residue crate file
rm -f %{buildroot}%{_prefix}/.crates*

TARGETDIR=$(ls -d target/release/build/ripgrep-*/out|head -n1)
install -Dm 644 ${TARGETDIR}/rg.1 %{buildroot}%{_mandir}/man1/rg.1
install -Dm 644 ${TARGETDIR}/rg.bash %{buildroot}%{_datadir}/bash-completion/completions/rg
install -Dm 644 ${TARGETDIR}/rg.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish
install -Dm 644 complete/_rg %{buildroot}%{_datadir}/zsh/site-functions/_rg

%files
%license LICENSE-MIT UNLICENSE
%doc CHANGELOG.md README.md
%{_mandir}/man1/rg.1%{?ext_man}
%{_bindir}/rg

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
