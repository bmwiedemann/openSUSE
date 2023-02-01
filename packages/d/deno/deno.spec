#
# spec file for package deno
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2023 Avindra Goolcharan <avindra@opensuse.org>
# Copyright (c) 2018-2023 the Deno authors
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
Version:        1.30.0
Release:        0
Summary:        A secure JavaScript and TypeScript runtime
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/denoland/deno
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source99:       revendor_source.sh
# PATCH-FIX-OPENSUSE - Disable LTO
Patch1:         deno-disbale-lto.patch
# gcc-c++ needed to build SPIRV-Cross
BuildRequires:  clang
BuildRequires:  cargo-packaging
BuildRequires:  gcc-c++
BuildRequires:  gn
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rust >= 1.62.1
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
# deno does not build on 32-bit archs
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le s390x

%description
A JavaSript and TypeScript platform built on V8

Deno has standard library and has features such as
a linter, a language server protocol, a code formatter and
a unit test runner.

Remote code is fetched and cached on first execution, and only
updated with the --reload flag.

%prep
%autosetup -a1 -p1
cp %{SOURCE2} .cargo/config
# Drop lock file due to revendor_source.sh breaking check
rm Cargo.lock

%build
# workaround to use python3
# where "python" is invoked
mkdir "$(pwd)/bin"
ln -sf %{_bindir}/python3 "$(pwd)/bin/python"
export PATH="$PATH:$(pwd)/bin"

export V8_FROM_SOURCE=1
export CLANG_BASE_PATH=%{_prefix}
# https://www.chromium.org/developers/gn-build-configuration
export GN_ARGS="enable_nacl = false blink_symbol_level = 0 v8_symbol_level = 0"
# enable binary stripping
export RUSTFLAGS="%{__global_rustflags} -Clink-arg=-s"
%{cargo_build}

%install
# place deno cli manually (cannot cargo install)
mkdir -p %{buildroot}%{_bindir}
cp target/release/deno %{buildroot}%{_bindir}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
