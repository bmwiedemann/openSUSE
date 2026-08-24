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


# 1.4.0 is the first release written in Rust (1.3.14 was the last in Zig).
# git_commit is the bun-v1.4.0 tag peel, used as GIT_SHA for bun --revision;
# it is not part of the RPM version.
%define git_commit 34cbb9a40b4bd1bd767d134a7065e66c2432a676
%define git_short 34cbb9a4
# The WebKit revision Source1 was made from, for reference; it is read out of
# the Bun tarball by bun_webkit, not set here.
# 0f966e81b78c84bb23213e391bc679c4ef83e56b
# The SQLite amalgamation in Bun's tree. Used for both the bundled() Provides
# and the %%check that asserts it against sqlite_version(), so the two cannot
# drift apart on a version bump.
%define bundled_sqlite 3.53.2
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
Version:        1.4.0
Release:        0
Summary:        Fast all-in-one JavaScript runtime and toolkit
# Bun itself is MIT, but it is one statically linked executable and everything
# in the Provides: bundled() list below ends up inside it, so the tag covers the
# whole binary. The notable ones are JavaScriptCore and tinycc (LGPL-2.1) and
# the Servo CSS crates (MPL-2.0); blessing comes from the SQLite amalgamation,
# Unicode-3.0 from unicode-ident, BSD-3-Clause from lol-html and lsquic.
# picohttpparser (MIT OR Artistic-1.0-Perl) is taken under its permissive half.
# See LICENSE.md, which upstream keeps current, and re-check this on every
# version bump. IJG is gone with libjpeg-turbo, the only thing that carried it,
# now that Patch5 links it from the distribution.
#
# LGPL-2.1 section 6 is satisfied by shipping the engine's source: WebKit is
# Source1 and is part of the src.rpm.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND MPL-2.0 AND Unicode-3.0 AND Zlib AND blessing
URL:            https://bun.sh/
Source0:        https://github.com/oven-sh/bun/archive/refs/tags/bun-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
# Link zstd, brotli, libdeflate, libspng, libwebp and libjpeg-turbo from the
# distribution instead of the vendored copies. These are the bundled C
# libraries whose pin is an unmodified upstream release rather than a fork and
# that Bun reaches through their installed public headers, so each can be
# tracked like any other shared library. See the patch header for the details
# that are specific to each of them.
Patch5:         bun-system-libs.patch
# Raise the LLVM version bun pins from 21 to the distribution default.
Patch6:         bun-llvm-22.patch
BuildRequires:  cargo
# LLVM 22.1.x, per Patch6. scripts/build/tools.ts enforces this for the C
# compiler and the linker only; see the PATH shim in %%build for the C++
# compiler, which it looks up without a version check.
BuildRequires:  clang22
BuildRequires:  cmake >= 3.24
BuildRequires:  gcc-c++
# Bun patches several of its vendored C dependencies with `git apply`.
BuildRequires:  git-core
BuildRequires:  lld22
BuildRequires:  llvm22
BuildRequires:  ninja
BuildRequires:  nodejs24 >= 24.3.0
# WebKit cmake. This is not a Perl package: spec-cleaner --perl explodes
# this into hundreds of perl(...) module BRs and drops git-core.
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3
# Not a floor upstream states - upstream pins a nightly - but the oldest
# release this was actually built with. An older compiler fails deep in the
# workspace instead of here.
BuildRequires:  rust >= 1.97
BuildRequires:  unzip
BuildRequires:  zstd
# Unbundled by Patch5. brotlicommon has no header of its own but is a separate
# pkg-config module, and the link line names it. libwebp's sharpyuv needs no
# entry of its own: it is a transitive dependency of libwebp.so.
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(spng)
# Bun.secrets dlopens libsecret at run time, so no ELF dependency is generated
# for it. Without it that API fails with "libsecret not available"; everything
# else works, hence Recommends rather than Requires.
Recommends:     libsecret-1-0
# Bun is a single statically linked executable and everything still listed here
# ends up inside it. Each is pinned to an exact commit, several are upstream
# forks (boringssl, tinycc, mimalloc, lol-html) and the JavaScript engine is a
# fork of WebKit, so none of them can be unbundled the way the six in Patch5
# were. Unversioned because upstream pins commits rather than releases.
# Regenerate from bun-prefetch.manifest, LICENSE.md and the crates.io
# dependencies in Cargo.toml on a version bump - the manifest and LICENSE.md
# do not list the Rust crates.
Provides:       bundled(bcrypt) = 0.19.0
Provides:       bundled(boringssl)
Provides:       bundled(c-ares)
Provides:       bundled(hdr_histogram)
Provides:       bundled(highway)
Provides:       bundled(libarchive)
Provides:       bundled(lol-html)
Provides:       bundled(ls-hpack)
Provides:       bundled(ls-qpack)
Provides:       bundled(lsquic)
Provides:       bundled(mimalloc)
Provides:       bundled(picohttpparser)
Provides:       bundled(rust-argon2)
# bun:sqlite and node:sqlite are built against the SQLite amalgamation in
# Bun's own tree. Unbundling is not possible even in principle: the alternative
# Bun offers (LAZY_LOAD_SQLITE) is a macOS-only path that dlopens a hardcoded
# "libsqlite3.dylib" (src/jsc/bindings/sqlite/lazy_sqlite3.h), so on Linux
# there is no configuration that links or loads the system library.
Provides:       bundled(sqlite3) = %{bundled_sqlite}
Provides:       bundled(tinycc)
Provides:       bundled(usockets)
Provides:       bundled(uwebsockets)
Provides:       bundled(webkit)
Provides:       bundled(zlib-ng)
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
%autosetup -p1 -n %{name}-bun-v%{version}

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

# lol-html and rust-argon2 are both downloads and Rust path dependencies of
# the workspace, so they have to be unpacked before cargo can read the
# manifest. rust-argon2 was a crates.io dep in the snapshot; 1.4.0 vendors
# it to apply patches/rust-argon2/legacy-low-memory.patch (Bun.password
# still verifies argon2 hashes with memoryCost below 8).
mkdir -p vendor/lolhtml vendor/rust-argon2
tar -xzf "prefetch/by-url/$(grep -F 'oven-sh/lol-html' prefetch/manifest.sha256 | cut -d' ' -f1)" \
    -C vendor/lolhtml --strip-components=1
tar -xzf "prefetch/by-url/$(grep -F 'sru-systems/rust-argon2' prefetch/manifest.sha256 | cut -d' ' -f1)" \
    -C vendor/rust-argon2 --strip-components=1
patch -p1 -d vendor/rust-argon2 < patches/rust-argon2/legacy-low-memory.patch

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
# Bun resolves its own toolchain (scripts/build/tools.ts) and never reads CC,
# CXX, AR or RANLIB - those are for the cc crate in the Rust workspace. Its
# resolver looks up "clang" with a version check, so an unversioned clang of a
# different major is rejected and clang-22 is found instead; but it looks up
# "clang++" with checkVersion:false ("clang++ is the same binary from the same
# install", which does not hold here) and takes the first hit in PATH.
# /usr/bin/clang++ is whatever major the unversioned clang package currently
# points at, so every C++ unit - JavaScriptCore and Bun's own bindings alike -
# can end up built by a different compiler than the C units. Put the right one
# first in PATH; the resolver tries each name across all of PATH before moving
# to the next name variant, so this wins. It is needed even while 22 is the
# distribution default, because that default moves on its own.
mkdir -p _clangshim
ln -sf %{_bindir}/clang-22 _clangshim/clang
ln -sf %{_bindir}/clang++-22 _clangshim/clang++
export PATH="$PWD/_clangshim:$PATH"
# llvm-ar, llvm-ranlib, llvm-nm and llvm-strip are looked up unversioned too,
# but openSUSE ships no unversioned names for those, so they already resolve to
# the 22 variants. ld.lld is version-checked like clang.
export CC=clang-22
export CXX=clang++-22
export AR=llvm-ar-22
export RANLIB=llvm-ranlib-22
export GIT_SHA="%{git_commit}"
# process.versions.zstd and .libdeflate are generated from the vendored commit
# hashes, which say nothing once the distribution libraries are linked instead
# (Patch5). Report what is actually linked. The other four have no such macro,
# so they need no counterpart.
export BUN_SYSTEM_VERSION_ZSTD="$(pkg-config --modversion libzstd)"
export BUN_SYSTEM_VERSION_LIBDEFLATE="$(pkg-config --modversion libdeflate)"
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
# Anchored on the release form. A canary reports 1.4.0-canary.<stamp>+<sha>,
# which a bare substring match for the short sha would have accepted.
%{buildroot}%{_bindir}/bun --revision | grep -E "^%{version}\+%{git_short}"
%{buildroot}%{_bindir}/bun -e 'if (6 * 7 !== 42) process.exit(1)'
# The bundler and the package manager are the reason this package exists.
%{buildroot}%{_bindir}/bun build --help >/dev/null
%{buildroot}%{_bindir}/bun install --help >/dev/null

# The native surfaces this package makes bundled() claims about. --help exiting
# 0 proves nothing about any of them, and all three are statically linked, so
# nothing else in the build would notice if they broke.
#
# bun:sqlite, against the version the Provides advertises.
%{buildroot}%{_bindir}/bun -e 'import{Database}from"bun:sqlite";const v=new Database(":memory:").query("select sqlite_version() v").get().v;if(v!=="%{bundled_sqlite}")throw new Error("bundled(sqlite3) says %{bundled_sqlite}, runtime says "+v)'
# bun:ffi, dlopening a library built here rather than a system one, so the test
# fails on a broken FFI rather than on a missing dependency.
cat > _ffi_check.c <<'EOF'
long long ffi_smoke(long long a, long long b) { return a * b + 1; }
EOF
gcc -shared -fPIC -o _ffi_check.so _ffi_check.c
%{buildroot}%{_bindir}/bun -e 'import{dlopen,FFIType}from"bun:ffi";const{symbols:{ffi_smoke:f}}=dlopen("./_ffi_check.so",{ffi_smoke:{args:[FFIType.i64,FFIType.i64],returns:FFIType.i64}});const r=f(6n,7n);if(r!==43n)throw new Error("bun:ffi returned "+r)'
# bundled(tinycc): cc() compiles at run time with the vendored tcc. No #include,
# so this does not depend on the buildroot's libc headers.
cat > _tcc_check.c <<'EOF'
int tcc_smoke(int x) { return x * 2 + 2; }
EOF
%{buildroot}%{_bindir}/bun -e 'import{cc}from"bun:ffi";const{symbols:{tcc_smoke:g}}=cc({source:"./_tcc_check.c",symbols:{tcc_smoke:{args:["int"],returns:"int"}}});const r=g(20);if(r!==42)throw new Error("bundled(tinycc) returned "+r)'

# Patch5 must have taken effect: every unbundled library has to be an ELF
# dependency now. A silently reverted patch would otherwise still build and
# still pass every test above.
ldd %{buildroot}%{_bindir}/bun
for lib in libzstd libbrotlienc libbrotlidec libbrotlicommon libdeflate \
           libspng libwebp libwebpmux libwebpdemux libturbojpeg; do
    ldd %{buildroot}%{_bindir}/bun | grep -qE "\<$lib\.so" || \
        { echo "$lib is not linked - Patch5 did not take effect"; exit 1; }
done
# ... and each one works through the binary, not just at link time.
%{buildroot}%{_bindir}/bun -e 'const c=Bun.zstdCompressSync(Buffer.from("z".repeat(4096)));if(Bun.zstdDecompressSync(c).length!==4096)throw new Error("zstd round trip failed")'
%{buildroot}%{_bindir}/bun -e 'const z=require("node:zlib");const c=z.brotliCompressSync(Buffer.from("b".repeat(4096)));if(z.brotliDecompressSync(c).length!==4096)throw new Error("brotli round trip failed")'
# Bun.gzipSync/deflateSync are libdeflate, not zlib-ng.
%{buildroot}%{_bindir}/bun -e 'const b=Buffer.from("d".repeat(4096));for(const[c,d]of[[Bun.gzipSync,Bun.gunzipSync],[Bun.deflateSync,Bun.inflateSync]])if(d(c(b)).length!==4096)throw new Error("libdeflate round trip failed")'
# The three image codecs, chained so that one seed exercises all of them:
# libspng decodes, libjpeg-turbo re-encodes and decodes, libwebp likewise, and
# libspng encodes at the end. A struct-layout or ABI-constant mismatch between
# Bun's hand-written Rust externs and the distribution headers shows up here as
# a wrong size or a decode failure rather than at link time.
cat > _img_check.mjs <<'EOF'
const seed = Buffer.from(
  "iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAAXklEQVR42hXKMQHAMAgAsEqp" +
  "FKQgBSlIQQpOtvTIl3NOfZcgKZphOecKBEnRDHtfCIEgKZph44UUCJKiGTZfKIEgKZph64UW" +
  "CJKiGbZfGIEgKZph54UVCJKiGXbr+wH6kZfBPhkbiwAAAABJRU5ErkJggg==", "base64");
let bytes = seed;
for (const fmt of ["jpeg", "webp", "png"]) {
  bytes = await new Bun.Image(bytes)[fmt]().bytes();
  const m = await new Bun.Image(bytes).metadata();
  if (m.width !== 8 || m.height !== 8) {
    throw new Error(`${fmt}: got ${m.width}x${m.height}, expected 8x8`);
  }
  if (m.format !== fmt) throw new Error(`${fmt}: sniffed as ${m.format}`);
}
EOF
%{buildroot}%{_bindir}/bun run _img_check.mjs
# process.versions reports the linked libraries, not the vendored commits.
%{buildroot}%{_bindir}/bun -e 'for(const[k,w]of[["zstd","'"$(pkg-config --modversion libzstd)"'"],["libdeflate","'"$(pkg-config --modversion libdeflate)"'"]]){const v=process.versions[k];if(v!==w)throw new Error("process.versions."+k+" is "+v+", linked is "+w)}'

%files
%license LICENSE.md
%doc README.md
%{_bindir}/bun
%{_bindir}/bunx

%changelog
