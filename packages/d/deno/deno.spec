#
# spec file for package deno
#
# Copyright (c) 2024 SUSE LLC
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


Name:           deno
Version:        2.0.0~rc10
Release:        0
Summary:        A secure JavaScript and TypeScript runtime
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/denoland/deno
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
# needed by `libz-ng-sys` after 1.36.1
# see: https://build.opensuse.org/package/show/devel:languages:javascript/deno#comment-1808174
BuildRequires:  cmake
BuildRequires:  cargo >= 1.68.0
BuildRequires:  gn
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rusty_v8
BuildRequires:  sccache
BuildRequires:  zstd
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(protobuf)
# deno does not build on 32-bit archs
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le s390x
# PATCH-FIX-OPENSUSE - Disable LTO (to reduce req memory)
%ifarch %{arm} aarch64
Patch10:        deno-disable-lto.patch
%endif

%description
A JavaScript and TypeScript platform built on V8

Deno has standard library and has features such as
a linter, a language server protocol, a code formatter and
a unit test runner.

Remote code is fetched and cached on first execution, and only
updated with the --reload flag.

%prep
%autosetup -a1 -p1

# From archlinux. We are using a patched v8 from our build
unlink $PWD/rusty_v8 || true
ln -sf %{_libdir}/crates/rusty_v8 $PWD/rusty_v8
echo -e "\n[patch.crates-io]\nv8 = { path = './rusty_v8' }" >> Cargo.toml
%{__cargo} update --offline

%build
# Ensure that the clang version matches. This command came from Archlinux. Thanks.
export CLANG_VERSION=$(clang --version | grep -m1 version | sed 's/.* \([0-9]\+\).*/\1/')
export V8_FROM_SOURCE=1
export CLANG_BASE_PATH=%{_prefix}
export CC=clang
export CXX=clang++
# https://www.chromium.org/developers/gn-build-configuration
export GN_ARGS="clang_version=${CLANG_VERSION} use_lld=true enable_nacl = false blink_symbol_level = 0 v8_symbol_level = 0"
%{cargo_build}

%install
# place deno cli manually (cannot cargo install)
mkdir -p %{buildroot}%{_bindir}
cp target/release/deno %{buildroot}%{_bindir}

%check
export PATH="${PATH}:%{buildroot}%{_bindir}"
deno run tests/testdata/run/002_hello.ts

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
