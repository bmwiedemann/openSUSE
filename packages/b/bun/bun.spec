#
# spec file for package bun
#
# Copyright (c) 2026 SUSE LLC
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


# Bun is being rewritten from Zig to Rust. The last release written in Zig is
# 1.3.14; the first written in Rust will be 1.4.0, which is not tagged yet.
# This packages a snapshot of the Rust rewrite, because the Zig branch is no
# longer developed - there will be no 1.3.15 and no fixes for it. The snapshot
# is a commit upstream's own CI published as a canary build, not an arbitrary
# one. Switch Source0 back to a release tarball once 1.4.0 is tagged.
%define git_commit 52bf09cb1cdbed0fbda4cf576e5d329cf92366ef
%define git_short 52bf09cb
%define git_date 20260808
# The WebKit revision Source1 was made from, for reference; it is read out of
# the Bun tarball by bun_webkit, not set here.
# ddea71318fec9b923465c7c45ded8fa713ca3251
%define bootstrap_version 1.3.14
%define dl_boot https://github.com/oven-sh/bun/releases/download/bun-v%{bootstrap_version}
# Building Bun requires an existing Bun. The build driver runs on Node, but 24
# of the code-generation steps do not: they use Bun.build and Bun.Transpiler,
# for which Node.js has no equivalent, and Bun's own bundler is what emits the
# JavaScript builtins with JavaScriptCore private-name intrinsics. Upstream
# tracks removing that dependency (scripts/build/CLAUDE.md) but it is not
# removable today.
#
# So, as for ghc, rust and sbcl, the first build has to start from an upstream
# binary. Turn this switch off once the package is in the distribution: it then
# builds with the Bun that is already there, and no foreign binary is involved.
%bcond_without bootstrap
# Bun pins a Rust nightly, but every unstable feature it uses is present in the
# Rust that Factory ships; only the nightly gate is missing. Rather than
# packaging a dated nightly snapshot, build with the distribution compiler and
# open the gate, which is what rustc's own bootstrap does.
%bcond_with rust_nightly
# WebKit (JavaScriptCore) is Bun's JavaScript engine. Upstream publishes
# prebuilt WebKit tarballs; this builds it from source instead, which is much
# slower but keeps the package free of foreign binaries.
%bcond_without webkit_source
Name:           bun
Version:        1.4.0~git%{git_date}.%{git_short}
Release:        0
Summary:        Fast all-in-one JavaScript runtime and toolkit
# Bun itself is MIT, but it is one statically linked executable and everything
# in the Provides: bundled() list below ends up inside it, so the tag covers the
# whole binary. The notable ones are JavaScriptCore and tinycc (LGPL-2.1) and
# the Servo CSS crates (MPL-2.0); IJG comes from libjpeg-turbo, blessing from
# the SQLite amalgamation, Unicode-3.0 from unicode-ident. zstd
# (BSD-3-Clause OR GPL-2.0-only) and picohttpparser (MIT OR Artistic-1.0-Perl)
# are taken under their permissive halves. See LICENSE.md, which upstream keeps
# current, and re-check this on every version bump.
#
# LGPL-2.1 section 6 is satisfied by shipping the engine's source: WebKit is
# Source1 and is part of the src.rpm.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND IJG AND LGPL-2.1-or-later AND MIT AND MPL-2.0 AND Unicode-3.0 AND Zlib AND blessing
URL:            https://bun.sh/
Source0:        https://github.com/oven-sh/bun/archive/%{git_commit}.tar.gz#/%{name}-%{version}.tar.gz
# JavaScriptCore source. Upstream's fork, at the revision Bun is developed
# against; not fetched by Bun's dependency machinery, which expects a manual
# clone. Produced by the bun_webkit generator.
Source1:        webkit-%{version}.tar.zst
# The C and C++ dependencies Bun downloads while building, in the
# content-addressed layout scripts/build/download.ts reads.
Source2:        bun-prefetch-%{version}.tar.zst
# Rust crates, from cargo vendor.
Source3:        bun-vendor-%{version}.tar.zst
# npm packages the code generators need.
Source4:        bun-node-modules-%{version}.tar.zst
# The generators for the four sources above. Not built and not installed: they
# are run by the maintainer on a version bump, not by the package. Kept here so
# that the generated sources can be reproduced from what the package ships.
Source5:        bun_prefetch
Source6:        bun-deps.mjs
Source7:        bun_webkit
# How to run them, and what each generated source contains.
Source8:        README.SUSE-maint
# A record of what Source2 and Source1 contain, so that they can be audited
# without being unpacked. Not used by the build.
Source9:        bun-prefetch.manifest
Source10:       webkit.revision
# Bootstrap binaries. Not shipped and not installed: unpacked in %%prep and
# used during %%build only. Checksums are in Source8.
Source100:      %{dl_boot}/bun-linux-x64-baseline.zip
Source101:      %{dl_boot}/bun-linux-aarch64.zip
NoSource:       100
NoSource:       101
# Legal-Review-Notice: Source100 and Source101 are prebuilt Bun binaries from
# upstream's own release, used at build time only to run Bun's code generators
# - Bun cannot be built without an existing Bun. They are not installed, not
# shipped, and not linked into the result. NoSource: keeps them out of the
# src.rpm but they remain published with the package sources. Same arrangement
# as rust, sbcl, fpc, ghc and deno. Removed once the package can build with the
# Bun already in the distribution (%%bcond bootstrap).
#
# NoSource: otherwise makes post-build-checks delete the debuginfo and
# debugsource packages (post-build-checks/checks/50-check-debuginfo).
#KEEP NOSOURCE DEBUGINFO
# Bun's build installs the pinned Rust nightly with rustup and downloads its
# dependencies. Neither is possible in a build environment, and both are
# avoidable: serve the downloads from the prefetch cache and use the Rust that
# Factory ships.
Patch0:         bun-offline-build.patch
# Two allow() attributes name a lint that is newer than the released compiler,
# and the workspace denies warnings, so the unknown lint is fatal. Allowing
# unknown_lints alongside it is correct on both compilers.
Patch1:         bun-unknown-lint.patch
# Do not compile Highway's length-agnostic SVE targets: Highway defines
# BitsFromMask only for the fixed-length ones, and three of Bun's SIMD helpers
# call it unconditionally.
Patch2:         bun-highway-scalable-sve.patch
# Emit debug information debugedit can read, so rpm can build a debuginfo
# package: DWARF 5 from rustc, as clang and the standard library already emit,
# and without the DWARF 5 accelerator table, which debugedit does not know.
Patch3:         bun-uniform-dwarf.patch
# Do not let WebKit put types in their own units. The linker keeps one copy of
# each and drops the rest, leaving .debug_str_offsets entries no unit refers to
# any more, and debugedit asserts on the first of those.
Patch4:         bun-webkit-no-type-units.patch
BuildRequires:  cargo
# LLVM 21.1.x is required and enforced by the build (scripts/build/tools.ts).
BuildRequires:  clang21
BuildRequires:  cmake >= 3.24
BuildRequires:  gcc-c++
# Bun patches several of its vendored C dependencies with `git apply`.
BuildRequires:  git-core
BuildRequires:  lld21
BuildRequires:  llvm21
BuildRequires:  ninja
BuildRequires:  nodejs24 >= 24.3.0
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3
# Not a floor upstream states - upstream pins a nightly - but the oldest
# release this was actually built with. An older compiler fails deep in the
# workspace instead of here.
BuildRequires:  rust >= 1.97
BuildRequires:  unzip
BuildRequires:  zstd
# Bun is a single statically linked executable and its build system has no
# option to link any of these from the distribution: each is pinned to an exact
# commit, several are upstream forks (boringssl, tinycc, mimalloc, lol-html)
# and the JavaScript engine is a fork of WebKit. Unversioned because upstream
# pins commits rather than releases. Regenerate from bun-prefetch.manifest and
# LICENSE.md on a version bump.
Provides:       bundled(boringssl)
Provides:       bundled(brotli) = 1.1.0
Provides:       bundled(c-ares)
Provides:       bundled(hdr_histogram)
Provides:       bundled(highway)
Provides:       bundled(libarchive)
Provides:       bundled(libdeflate)
Provides:       bundled(libjpeg-turbo)
Provides:       bundled(libspng)
Provides:       bundled(libwebp)
Provides:       bundled(lol-html)
Provides:       bundled(ls-hpack)
Provides:       bundled(ls-qpack)
Provides:       bundled(lsquic)
Provides:       bundled(mimalloc)
Provides:       bundled(picohttpparser)
# bun:sqlite and node:sqlite are built against the SQLite amalgamation in
# Bun's own tree. Unbundling is not possible even in principle: the alternative
# Bun offers (LAZY_LOAD_SQLITE) is a macOS-only path that dlopens a hardcoded
# "libsqlite3.dylib" (src/jsc/bindings/sqlite/lazy_sqlite3.h), so on Linux
# there is no configuration that links or loads the system library.
Provides:       bundled(sqlite3) = 3.53.2
Provides:       bundled(tinycc)
Provides:       bundled(usockets)
Provides:       bundled(uwebsockets)
Provides:       bundled(webkit)
Provides:       bundled(zlib-ng)
Provides:       bundled(zstd)
# Upstream supports linux-x64 and linux-arm64 only, and Bun can only be built
# where an upstream bootstrap binary is published for the same architecture.
ExclusiveArch:  x86_64 aarch64
%if %{with webkit_source}
# JavaScriptCore's own build system.
BuildRequires:  ruby
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
%endif
%if %{without bootstrap}
BuildRequires:  bun
%endif

%description
Bun is an all-in-one JavaScript runtime and toolkit with a bundler, test
runner, and Node.js-compatible package manager.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

# JavaScriptCore. Bun's build expects a manual checkout here.
mkdir -p vendor/WebKit
tar --zstd -xf %{SOURCE1} -C vendor/WebKit --strip-components=1

# The dependency downloads, and the Rust crates and npm packages that are not
# part of that cache.
mkdir -p prefetch
tar --zstd -xf %{SOURCE2} -C prefetch
tar --zstd -xf %{SOURCE3}
tar --zstd -xf %{SOURCE4}

# The build runs node_modules/.bin/esbuild (scripts/build/configure.ts), and
# bun links that name straight at the prebuilt binary for the architecture the
# install ran on, so it is the one thing in that archive that cannot serve both
# architectures. Point it at esbuild's own launcher instead - the node script
# npm links here, which picks the platform package at run time. The archive
# carries that package for every architecture this builds for; everything else
# in it already chooses at run time.
find . -path '*/node_modules/.bin/esbuild' -exec ln -sf ../esbuild/bin/esbuild {} \;

# lol-html is both a download and a Rust path dependency of the workspace, so
# it has to be unpacked before cargo can read the manifest.
mkdir -p vendor/lolhtml
tar -xzf "prefetch/by-url/$(grep -F 'oven-sh/lol-html' prefetch/manifest.sha256 | cut -d' ' -f1)" \
    -C vendor/lolhtml --strip-components=1

%if %{with bootstrap}
mkdir -p bootstrap
%ifarch x86_64
unzip -q %{SOURCE100} -d bootstrap
%endif
%ifarch aarch64
unzip -q %{SOURCE101} -d bootstrap
%endif
mv bootstrap/bun-linux-*/bun bootstrap/bun
chmod +x bootstrap/bun
%endif

# Point cargo at the vendored crates. This has to go in CARGO_HOME rather than
# .cargo/config.toml, which Bun's build regenerates on every configure.
mkdir -p .cargo-home
cat >.cargo-home/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/cargo-vendor"
EOF

%if %{without rust_nightly}
# Bun pins a Rust nightly. Use the distribution compiler instead and open the
# unstable-feature gate, as rustc's own bootstrap does.
rm -f rust-toolchain.toml
%endif

%build
export CC=clang-21
export CXX=clang++-21
export AR=llvm-ar-21
export RANLIB=llvm-ranlib-21
export GIT_SHA="%{git_commit}"
export CARGO_HOME="$PWD/.cargo-home"
export CARGO_NET_OFFLINE=true
%if %{without rust_nightly}
export RUSTC_BOOTSTRAP=1
%endif
# Serve every dependency download from the prepared cache.
export BUN_BUILD_PREFETCH_DIR="$PWD/prefetch"
export BUN_WEBKIT_PATH="$PWD/vendor/WebKit"
%if %{with bootstrap}
export PATH="$PWD/bootstrap:$PATH"
%endif

# The build driver itself runs on Node - upstream's own CI invokes it this way
# (.buildkite/ci.mjs) - so the bootstrap Bun above is reached only by the code
# generators that genuinely need it.
#
# --canary=off  otherwise the version is reported as a canary build.
# --lto=off     cross-language LTO needs rustc's own LLVM tools, which the
#               distribution compiler does not ship; it is off by default
#               outside upstream CI anyway.
# --baseline    on x86_64 this targets Nehalem, matching the openSUSE
#               x86-64-v2 baseline; the default needs AVX2. Not passed on
#               aarch64, which has a single target.
build_args=(--profile=release
            --build-dir=build/release
            --cache-dir="$PWD/build/cache"
            --canary=off
            --lto=off)
%if %{with webkit_source}
build_args+=(--webkit=local)
%endif
%ifarch x86_64
build_args+=(--baseline=on)
%endif

node --experimental-strip-types --no-warnings scripts/build.ts "${build_args[@]}"

%install
# bun-profile, not bun: a release build links bun-profile and then strips it
# into bun with --strip-all --strip-debug. Installing the stripped one leaves
# rpm nothing to extract, so no debuginfo package is built and the result is
# still flagged unstripped. bun-profile is the same binary before that step.
install -D -m 0755 build/release/bun-profile %{buildroot}%{_bindir}/bun
# Bun dispatches on argv[0]: invoked as bunx it runs `bun x`, the package
# runner (src/runtime/cli/mod.rs). Upstream's installer makes the same link.
ln -s bun %{buildroot}%{_bindir}/bunx

%check
%{buildroot}%{_bindir}/bun --version
%{buildroot}%{_bindir}/bun --revision | grep -F "%{git_short}"
%{buildroot}%{_bindir}/bun -e 'if (6 * 7 !== 42) process.exit(1)'
# The bundler and the package manager are the reason this package exists.
%{buildroot}%{_bindir}/bun build --help >/dev/null
%{buildroot}%{_bindir}/bun install --help >/dev/null

%files
%license LICENSE.md
%doc README.md
%{_bindir}/bun
%{_bindir}/bunx

%changelog
