#
# spec file for package git-cliff
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Version:        2.9.0
Release:        0
Summary:        Changelog generator for git repositories
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND GPL-3.0-only AND SUSE-GPL-2.0-with-linking-exception+
URL:            https://github.com/orhun/git-cliff
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_arches}

%description
git-cliff is a utility to generate changelogs that follows the
Conventional Commit Specifications.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup -a1

%build
# We don't need to check an update. github feature is nice to have though
%{cargo_build} --ignore-rust-version --no-default-features -F github
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
%license LICENSE-MIT LICENSE-APACHE
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
