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
Version:        0.31.4
Release:        0
Summary:        Terminal workspace with batteries included
License:        MIT
URL:            https://github.com/zellij-org/zellij
Source0:        https://github.com/zellij-org/zellij/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
Source3:        README.suse-maint.md
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo >= 1.62
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

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
# Remove prebuilt binaries
rm assets/plugins/*

%build
# First rebuilt plugins we just deleted
# Note: RUSTFLAGS break linking with WASM-files, so we don't use the cargo_build-macro here
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
mv target/wasm32-wasi/release/*.wasm assets/plugins/

# Build zellij proper
%{cargo_build} --all-features

%install
%{cargo_install} --all-features

%if %{with test}
%check
%{cargo_test} --all-features
%endif

%files
%{_bindir}/zellij
%license LICENSE.md

%doc README.md

%changelog
