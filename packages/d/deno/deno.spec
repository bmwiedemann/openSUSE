#
# spec file for package deno
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020-2024 Avindra Goolcharan <avindra@opensuse.org>
# Copyright (c) 2018-2024 the Deno authors
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


%global _lto_cflags %nil
%global _v8_version 137.2.1
Name:           deno
Version:        2.4.2
Release:        0
Summary:        A secure JavaScript and TypeScript runtime
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/denoland/deno
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo-packaging

%if 0%{?suse_version} > 1600
BuildRequires:  clang19
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif

# needed by `libz-ng-sys` after 1.36.1
# see: https://build.opensuse.org/package/show/devel:languages:javascript/deno#comment-1808174
BuildRequires:  cmake
BuildRequires:  cargo >= 1.80
BuildRequires:  gn
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rusty_v8 = %{_v8_version}
BuildRequires:  zstd
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(protobuf)
ExclusiveArch:  %{rust_tier1_arches}
# PATCH-FIX-OPENSUSE - Disable LTO (to reduce req memory)
Patch10:        deno-disable-lto.patch

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name}
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name}
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name}
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%description
A JavaScript and TypeScript platform built on V8

Deno has standard library and has features such as
a linter, a language server protocol, a code formatter and
a unit test runner.

Remote code is fetched and cached on first execution, and only
updated with the --reload flag.

%prep
%autosetup -a1 -p1

unlink rusty_v8 || true
ln -sf %{_libdir}/crates/rusty_v8/ $PWD/rusty_v8
echo -e "\n[patch.crates-io]\nv8 = { path = './rusty_v8' }" >> Cargo.toml

%build
export CARGO_HOME="$PWD/.cargo"
# Ensure that the clang version matches. This command came from Archlinux. Thanks.
export CLANG_VERSION=$(clang --version | grep -m1 version | sed 's/.* \([0-9]\+\).*/\1/')
export V8_FROM_SOURCE=1
export CLANG_BASE_PATH=%{_prefix}
%if 0%{?suse_version} > 1600
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -Wno-unknown-warning-option"
export CXXFLAGS="%{optflags} -Wno-unknown-warning-option"
%else
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%endif

# https://www.chromium.org/developers/gn-build-configuration
export GN_ARGS="clang_version=${CLANG_VERSION} use_lld=true enable_nacl = false blink_symbol_level = 0 v8_symbol_level = 0"
%{__cargo} update --offline
%{cargo_build}

%install
# place deno cli manually (cannot cargo install)
mkdir -p %{buildroot}%{_bindir}
export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions

cp target/release/deno %{buildroot}%{_bindir}

deno completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
deno completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
deno completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
export PATH="${PATH}:%{buildroot}%{_bindir}"
deno run tests/testdata/run/002_hello.ts

%files
%license LICENSE.md
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
