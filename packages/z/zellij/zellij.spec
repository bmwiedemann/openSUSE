#
# spec file for package zellij
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


%bcond_with     test
Name:           zellij
Version:        0.34.4
Release:        0
Summary:        Terminal workspace with batteries included
License:        MIT
URL:            https://github.com/zellij-org/zellij
Source0:        https://github.com/zellij-org/zellij/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
Source3:        README.suse-maint.md
BuildRequires:  cargo-packaging

%if 0%{?suse_version} > 1500
BuildRequires:  mandown
%endif

BuildRequires:  rust+cargo >= 1.59
ExclusiveArch:  %{rust_tier1_arches}
%if %{with test}
BuildRequires:  pkgconfig(openssl)
%endif

%description
Zellij is a workspace aimed at developers, ops-oriented people and anyone who loves the terminal.
At its core, it is a terminal multiplexer (similar to tmux and screen), but this is merely its
infrastructure layer.

Zellij includes a layout system, and a plugin system allowing one to create plugins in any
language that compiles to WebAssembly.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
# Remove prebuilt binaries
rm -v zellij-utils/assets/plugins/*

%build
# First rebuilt plugins we just deleted
# Note: RUSTFLAGS break linking with WASM-files, so we don't use the cargo_build-macro here
pushd default-plugins/compact-bar
cargo --offline build --release --target=wasm32-wasi
popd
pushd default-plugins/status-bar
cargo --offline build --release --target=wasm32-wasi
popd
pushd default-plugins/tab-bar
cargo --offline build --release --target=wasm32-wasi
popd
pushd default-plugins/strider
cargo --offline build --release --target=wasm32-wasi
popd

# Move the results to the place they are expected
mv -v target/wasm32-wasi/release/*.wasm zellij-utils/assets/plugins/

# Build zellij proper
%{cargo_build} --features unstable

for shell in "zsh" "bash" "fish"
do
  ./target/release/%{name} setup --generate-completion "$shell" > target/%{name}."$shell"
done
mandown docs/MANPAGE.md > target/zellij.1

%install
install -Dm644 -T ./target/zellij.bash %{buildroot}%{_datadir}/bash-completion/completions/zellij
install -Dm644 -T ./target/zellij.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/zellij.fish
install -Dm644 -T ./target/zellij.zsh %{buildroot}%{_datadir}/zsh/site-functions/_zellij
install -Dm644 -T %{_builddir}/%{name}-%{version}/assets/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 -T %{_builddir}/%{name}-%{version}/assets/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version} > 1500
install -Dm644 -T ./target/zellij.1 %{buildroot}%{_mandir}/man1/zellij.1
%endif

%{cargo_install} --features unstable
%if %{with test}
%check
%{cargo_test}
%endif

%files
%{_bindir}/zellij
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%if 0%{?suse_version} > 1500
%{_mandir}/man1/zellij.1%{?ext_man}
%endif

%license LICENSE.md
%doc README.md docs/ARCHITECTURE.md docs/MANPAGE.md docs/TERMINOLOGY.md docs/THIRD_PARTY_INSTALL.md

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
