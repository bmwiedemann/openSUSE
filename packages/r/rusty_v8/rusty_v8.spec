#
# spec file for package rusty_v8
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


%global __requires_exclude_from ^%{_libdir}/crates/rusty_v8/.*$

Name:           rusty_v8
Version:        130.0.1
Release:        0
Summary:        Build tooling for Deno (do not install or use!)
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/denoland/rusty_v8
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source100:      rusty_v8-rpmlintrc
Patch0:         deno-v8-arm.patch
# Based on https://gitlab.archlinux.org/archlinux/packaging/packages/chromium/-/raw/main/compiler-rt-adjust-paths.patch
Patch1:         compiler-rt-adjust-paths.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang19
BuildRequires:  fdupes
BuildRequires:  gn
BuildRequires:  lld19
BuildRequires:  llvm19
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  zstd
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-i18n)
# Rusty V8 does not guarantee builds for 32 bit and ppc
ExclusiveArch:  %{rust_tier1_arches}
%ifarch ppc64 # wants g++ for some reason
BuildRequires:  gcc-c++
%endif

%description
V8 build tooling for Deno. This represents all of the common
cruft that is dragged along into the deno build from V8,
Chromium, etc.

%prep
%autosetup -a1 -p1
# Keeping this ifarch in case someone tries to build 32 bit
# which is not our problem
%ifarch x86_64 || x86_64_v3 || aarch64
# lib to lib64
sed -i 's|lib/clang|lib64/clang|g' build/config/clang/BUILD.gn
%endif

%build
# Ensure that the clang version matches. This command came from Archlinux. Thanks.
export CLANG_VERSION=$(clang --version | grep -m1 version | sed 's/.* \([0-9]\+\).*/\1/')
export V8_FROM_SOURCE=1
export CLANG_BASE_PATH=%{_prefix}
export CC=clang
export CXX=clang++
# https://www.chromium.org/developers/gn-build-configuration
export GN_ARGS="clang_version=${CLANG_VERSION} use_lld=true enable_nacl = false blink_symbol_level = 0 v8_symbol_level = 0"
export CFLAGS="%{optflags} -Wno-unknown-warning-option"
export CXXFLAGS="%{optflags} -Wno-unknown-warning-option"
export RUST_BACKTRACE=full
%{cargo_build}

%install
mkdir -p %{buildroot}%{_libdir}/crates/
# We are doing this so we can manipulate deno's Cargo.toml file later.
# The previous deno build does not use this and it does not make sense.
# Let's just use this to experiment rusty_v8 builds and patches before
# updating deno ;) it's chonky though
cp -rv $PWD \
	%{buildroot}%{_libdir}/crates/rusty_v8

cp target/release/*.rlib %{buildroot}%{_libdir}

# we don't need those
pushd %{buildroot}%{_libdir}/crates/rusty_v8
rm -rf .github
rm .prettierrc.json
rm .rustfmt.toml
rm -rf vendor
rm -rf target
%fdupes $PWD
popd

%files
%license LICENSE
%doc README.md
%{_libdir}/libv8.rlib
%dir %{_libdir}/crates/
%dir %{_libdir}/crates/rusty_v8
%dir %{_libdir}/crates/rusty_v8/.cargo
%{_libdir}/crates/rusty_v8/*
%{_libdir}/crates/rusty_v8/.cargo/config.toml
%{_libdir}/crates/rusty_v8/.clang-format
%{_libdir}/crates/rusty_v8/.gn

%changelog
