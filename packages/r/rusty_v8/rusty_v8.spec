#
# spec file for package rusty_v8
#
# Copyright (c) 2025 SUSE LLC
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


%global _min_clang_version 19
%global __requires_exclude_from ^%{_libdir}/crates/rusty_v8/.*$

%if 0%{?suse_version} > 1600
%bcond_without mold
%else
%bcond_with    mold
%endif

%if %{with mold}
%global build_rustflags "-C" "linker=clang++" "-C" "link-arg='-fuse-ld=/usr/bin/mold -Wl,-z,relro,-z,now,-zstack-size=8388608'" "-C" "debuginfo=2" "-C" "incremental=false" "-C" "strip=none" "-A" "warnings"
%else
%global build_rustflags "-C" "linker=clang++" "-C" "link-arg='-fuse-ld=/usr/bin/ld.lld -Wl,-z,relro,-z,now,-zstack-size=8388608'" "-C" "debuginfo=2" "-C" "incremental=false" "-C" "strip=none" "-A" "warnings"
%endif


Name:           rusty_v8
Version:        145.0.0
Release:        0
Summary:        Build tooling for Deno (do not install or use!)
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/denoland/rusty_v8
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        https://storage.googleapis.com/chromium-browser-clang/Linux_x64/rust-toolchain-a4cfac7093a1c1c7fbdb6bc75d6b6dc4d385fc69-2-llvmorg-22-init-17020-gbd1bd178.tar.xz#/chromium-rust-toolchain.tar.xz
Source100:      rusty_v8-rpmlintrc
Patch0:         deno-v8-arm.patch
# Based on https://gitlab.archlinux.org/archlinux/packaging/packages/chromium/-/raw/main/compiler-rt-adjust-paths.patch
Patch1:         compiler-rt-adjust-paths.patch
Patch2:         disable-rust-toolchain-download.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang >= %{_min_clang_version}
BuildRequires:  clang-devel >= %{_min_clang_version}
BuildRequires:  llvm >= %{_min_clang_version}
BuildRequires:  llvm-devel >= %{_min_clang_version}
BuildRequires:  lld >= %{_min_clang_version}
%if 0%{?suse_version} > 1600
BuildRequires:  mold
%endif
BuildRequires:  binutils
BuildRequires:  fdupes
BuildRequires:  gn
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  rust-bindgen
BuildRequires:  zstd
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-i18n)
# Rusty V8 does not guarantee builds for 32 bit and ppc
ExclusiveArch:  x86_64 x86_64_v3
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
mkdir -p third_party/rust-toolchain
tar xf %{SOURCE2} -C third_party/rust-toolchain

%build
%ifarch aarch64
export RUSTC_BOOTSTRAP=1
%endif
# Ensure that the clang version matches. This command came from Archlinux. Thanks.
export CLANG_VERSION=$(clang --version | grep -m1 version | sed 's/.* \([0-9]\+\).*/\1/')
export LIBCLANG_PATH=%{_libdir}
export V8_FROM_SOURCE=1
export CLANG_BASE_PATH=%{_prefix}
export CC=clang
export CXX=clang++
export AR=ar NM=nm
export CFLAGS="%{optflags} -Wno-unknown-warning-option"
export CXXFLAGS="%{optflags} -Wno-unknown-warning-option"
# https://www.chromium.org/developers/gn-build-configuration
export RUSTC_SYSROOT=$(rustc --print sysroot)
export RUSTC_VERSION=$(rustc -V | cut -d' ' -f2)
export GN="/usr/bin/gn"
export NINJA="/usr/bin/ninja"
export RUSTC="/usr/bin/rustc"
export GN_ARGS="
	clang_version=${CLANG_VERSION} 
	v8_symbol_level=0 
	custom_toolchain=\"//build/toolchain/linux/unbundle:default\" 
	host_toolchain=\"//build/toolchain/linux/unbundle:default\"
	fatal_linker_warnings=false
	is_debug=false
	use_system_libffi=true
	use_custom_libcxx=false
	use_sysroot=false
	"
export EXTRA_GN_ARGS="use_custom_libcxx=false"

# Included limited debug info.
export CARGO_PROFILE_RELEASE_DEBUG=1
# Use "thin" instead of "fat" to speed up builds (it costs +4% binary size).
export CARGO_PROFILE_RELEASE_LTO="thin"
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
rm -rf false
rm -rf vendor
rm -rf target
rm -rf third_party/rust-toolchain
%fdupes $PWD
popd

# Remove Windows-specific vendored libs that break readelf/rpmlint
find %{buildroot}%{_libdir}/crates/rusty_v8/third_party -name "windows_*" -type d -exec rm -rf {} +

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
