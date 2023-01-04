#
# spec file for package git-cliff
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


Name:           git-cliff
Version:        1.0.0
Release:        0
Summary:        Changelog generator for git repositories
URL:            https://github.com/orhun/git-cliff
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND GPL-3.0-only
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo
ExclusiveArch:  %{rust_arches}

%description
git-cliff is a utility to generate changelogs that follows the
Conventional Commit Specifications.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build} --no-default-features
mkdir -p target/completions/
mkdir -p target/man/
OUT_DIR=target/completions/ ./target/release/%{name}-completions
OUT_DIR=target/man/ ./target/release/%{name}-mangen

%install
install -Dm755 -T ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 -T ./target/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 -T ./target/completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 -T ./target/completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 -T ./target/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/git-cliff.1%{?ext_man}
%license LICENSE
%doc README.md RELEASE.md CHANGELOG.md

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
