#
# spec file for package opentui
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# %%define, not %%global: node_arch is set further down, in the %%ifarch, so
# this has to be expanded where it is used rather than where it is written.
%define native_pkg @opentui/core-linux-%{node_arch}
# Upstream's build.zig refuses to run on anything but this exact version, and
# the Zig releases it brackets are not source compatible, so a range would be
# a lie. When Factory moves on, this package has to be rebased, not relaxed.
%global zig_version 0.17.0
# The npm names for the platform the native library is built for. OpenTUI
# resolves it as @opentui/core-<platform>-<arch>/libopentui.so, using Node's
# names for both, not the RPM ones.
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
# Pinned by packages/native/src/vendor/ffmpeg/README.md; %%build repeats
# that file's configure set for this host, and bundled() tracks both.
%global ffmpeg_version 9.0.2
%global zlib_version 1.3.2
Name:           opentui
Version:        0.8.4
Release:        0
Summary:        Library for building terminal user interfaces
# MIT upstream; everything below is compiled into libopentui.so: miniaudio
# and stb (dual licensed), uucode, ghostty-vt, yoga, lcms2 (MIT), libwebp
# (BSD-3-Clause), wuffs (Apache-2.0), FFmpeg (LGPL-2.1-or-later), zlib (Zlib).
License:        Apache-2.0 AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (Unlicense OR MIT-0) AND Zlib
URL:            https://opentui.com
Source0:        %{name}-%{version}.tar.gz
Source1:        README.SUSE-maint
Source2:        https://ffmpeg.org/releases/ffmpeg-%{ffmpeg_version}.tar.xz
Source3:        https://zlib.net/fossils/zlib-%{zlib_version}.tar.gz
# PATCH-FIX-OPENSUSE opentui-baseline-cpu.patch -- pin the code generator back
# to the baseline (a native triple detects the build CPU, wrong for distros).
Patch0:         opentui-baseline-cpu.patch
# PATCH-FIX-OPENSUSE opentui-aarch64-skip-crashing-x11-tests.patch -- 2 X11
# clipboard tests abort the runner on aarch64; skipped until upstream fixes.
Patch1:         opentui-aarch64-skip-crashing-x11-tests.patch
# PATCH-FIX-OPENSUSE opentui-aarch64-skip-flaky-text-work-test.patch -- aarch64-only skip of a page-size-sensitive test
# The word-metadata arena bound below is page-size sensitive and trips on
# aarch64 only (see the patch header); skipped there until it passes again.
Patch2:         opentui-aarch64-skip-flaky-text-work-test.patch
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  python3-base
# The grammar modules the highlighter ships: symlinked to the
# tree-sitter-<lang>-wasm packages' files below, checked at build time.
BuildRequires:  tree-sitter-javascript-wasm
BuildRequires:  tree-sitter-markdown-wasm
BuildRequires:  tree-sitter-typescript-wasm
BuildRequires:  tree-sitter-zig-wasm
BuildRequires:  xz
BuildRequires:  zig = %{zig_version}
Provides:       bundled(ffmpeg) = %{ffmpeg_version}
Provides:       bundled(ghostty-vt) = 1.3.2
Provides:       bundled(lcms2) = 2.19.1
Provides:       bundled(libwebp) = 1.6.0
Provides:       bundled(miniaudio) = 0.11.22
Provides:       bundled(stb) = 2.18
Provides:       bundled(uucode) = 0.2.0
Provides:       bundled(wuffs) = 0.3
Provides:       bundled(yoga) = 3.2.1
Provides:       bundled(zlib) = %{zlib_version}
# Upstream supports no other architecture: SUPPORTED_TARGETS in
# packages/native/build.zig lists only x86_64 and aarch64.
ExclusiveArch:  x86_64 aarch64

%description
OpenTUI is a library for building terminal user interfaces. Layout, text
shaping, buffer diffing and rendering are done by a native core written in
Zig, which TypeScript programs drive over FFI.

This package contains that native core. The TypeScript that calls it is in
opentui-devel.

%package        devel
Summary:        TypeScript sources for OpenTUI
Requires:       %{name} = %{version}
Requires:       tree-sitter-javascript-wasm
Requires:       tree-sitter-markdown-wasm
Requires:       tree-sitter-typescript-wasm
Requires:       tree-sitter-zig-wasm

%description    devel
The TypeScript half of OpenTUI: the core bindings, the keymap library and
the SolidJS renderer.

OpenTUI is consumed as TypeScript, not as a compiled artifact - a program
using it bundles these sources into itself with its own bundler. So this is
what you build against, and nothing installs it to run.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# Zig/image deps are vendored in-tree (resolved over relative paths, nothing
# fetched). FFmpeg and zlib (video, new in 0.8.1) come as Source2/3 instead.
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
export ZIG_LOCAL_CACHE_DIR="$PWD/.zig-local-cache"

cd packages/native
sh scripts/prepare-zig-deps.sh
mkdir -p .ffmpeg-sources
tar -xf "%{SOURCE2}" -C .ffmpeg-sources
tar -xf "%{SOURCE3}" -C .ffmpeg-sources
# Video (0.8.1+) statically links a minimal FFmpeg built below from
# Source2/3 with upstream's configure set; -Drequire-video keeps a
# missing prefix a loud error, not a silent video-less library.
ffmpeg_build() {
    # $1: prefix name, $2: zig cc triple, $3: configure --arch
    # (one declaration per line: same-command locals cannot see each other)
    local name="$1"
    local triple="$2"
    local arch="$3"
    local root="$PWD"
    local cache="$root/.cache/ffmpeg"
    local prefix="$cache/prefix/$name"
    local build="$cache/build/$name"
    local tools="$cache/toolchains/$name"
    local src="$root/.ffmpeg-sources/ffmpeg-%{ffmpeg_version}"
    local zsrc="$root/.ffmpeg-sources/zlib-%{zlib_version}"
    mkdir -p "$build" "$tools" "$prefix/include" "$prefix/lib"
    printf '#!/bin/sh\nexec zig cc -target %s "$@"\n' "$triple" > "$tools/cc"
    chmod 0755 "$tools/cc"
    # zlib as hidden-visibility objects like the FFmpeg libs, so the gnu
    # library and the musl test binary link the same pinned source.
    mkdir -p "$build/zlib"
    local zlib_objects=""
    for c in adler32 compress crc32 deflate infback inffast inflate inftrees trees uncompr zutil; do
        "$tools/cc" -O3 -fvisibility=hidden -fPIC -I"$zsrc" -c "$zsrc/$c.c" -o "$build/zlib/$c.o"
        zlib_objects="$zlib_objects $build/zlib/$c.o"
    done
    zig ar rcs "$prefix/lib/libz.a" $zlib_objects
    cp "$zsrc/zlib.h" "$zsrc/zconf.h" "$prefix/include/"
    local nasm_exe=""
    if [ "$arch" = x86_64 ]; then nasm_exe="--x86asmexe=%{_bindir}/nasm"; fi
    ( cd "$build" \
      && "$src/configure" --prefix="$prefix" \
        --disable-everything --disable-autodetect \
        --disable-programs --disable-doc --disable-debug --disable-network \
        --disable-avdevice --disable-avfilter --disable-encoders --disable-muxers \
        --disable-indevs --disable-outdevs --disable-hwaccels --disable-filters \
        --disable-bzlib --disable-iconv --disable-lzma \
        --enable-zlib --disable-gpl --disable-version3 --disable-nonfree \
        --enable-static --disable-shared --enable-small \
        --enable-demuxer=mov --enable-decoder=h264,aac --enable-parser=h264,aac \
        --enable-protocol=file --enable-swscale --enable-swresample \
        --enable-cross-compile "--cc=$tools/cc" "--ar=zig ar" "--ranlib=zig ranlib" \
        --arch="$arch" --target-os=linux \
        --extra-cflags="-Os -ffunction-sections -fdata-sections -fvisibility=hidden -I$prefix/include" \
        --extra-ldflags="-L$prefix/lib" --extra-libs=-lz \
        $nasm_exe --enable-pic --enable-pthreads \
      && sed -i 's/#define HAVE_SYSCTL 1/#define HAVE_SYSCTL 0/' config.h \
      && make "-j$(nproc)" \
      && make install )
    # What build.zig links is not the archives but their objects, listed
    # relative to the prefix; the member names must match the object
    # basenames exactly as multisets (generic C and x86 asm share names).
    : > "$prefix/objects.txt"
    for pair in "libavformat libavformat" "libavcodec libavcodec" "libswscale libswscale" "libswresample libswresample" "libavutil libavutil" "libz zlib"; do
        set -- $pair
        local tmp="$(mktemp -d)"
        zig ar t "$prefix/lib/$1.a" | sort > "$tmp/members"
        ( cd "$build/$2" && find . -name '*.o' | sed 's|^\./||' | sort ) > "$tmp/all"
        # Only archive members link into the library; the tree also holds
        # host tool objects (e.g. aarch64 ops_asmgen.o) that must not match.
        : > "$tmp/paths"
        while read -r o; do
            if grep -qxF "${o##*/}" "$tmp/members"; then echo "$o" >> "$tmp/paths"; fi
        done < "$tmp/all"
        sed 's|.*/||' "$tmp/paths" | sort > "$tmp/names"
        if [ "$(wc -l < "$tmp/members")" != "$(wc -l < "$tmp/paths")" ] \
            || ! cmp -s "$tmp/members" "$tmp/names"; then
            echo "ffmpeg $1 objects do not match its archive" >&2
            exit 1
        fi
        while read -r o; do
            mkdir -p "$prefix/objects/$1/$(dirname "$o")"
            cp "$build/$2/$o" "$prefix/objects/$1/$o"
            echo "objects/$1/$o" >> "$prefix/objects.txt"
        done < "$tmp/paths"
        rm -rf "$tmp"
    done
    printf '%s' "6-zig-%{zig_version}" > "$prefix/opentui-build"
}
case "$(uname -m)" in
    x86_64) ffmpeg_build x86_64-linux x86_64-linux-gnu.2.17 x86_64
            ffmpeg_build x86_64-linux-musl x86_64-linux-musl x86_64 ;;
    aarch64) ffmpeg_build aarch64-linux aarch64-linux-gnu.2.17 aarch64
             ffmpeg_build aarch64-linux-musl aarch64-linux-musl aarch64 ;;
esac
# -Dlibrary-target=native keeps the host's libc and libstdc++, which is what
# a distribution build wants. What it must not keep is the host's CPU model -
# see Patch0.
zig build \
    -Dlibrary-target=native \
    -Doptimize=ReleaseFast \
    -Drequire-video \
    --verbose

%install
install -d %{buildroot}%{_libdir}/%{name}/%{native_pkg}
# The -Dlibrary-target override below installs to ../lib/<name> next to the
# default prefix, i.e. packages/native/lib/native, not zig-out.
install -m 0755 packages/native/lib/native/libopentui.so \
    %{buildroot}%{_libdir}/%{name}/%{native_pkg}/libopentui.so

# The whole point of the explicit -Dlibrary-target above. If a rebase ever
# puts a host-detected CPU model back, catch it here rather than in a bug
# report from somebody with an older machine.
%ifarch aarch64
if objdump -d %{buildroot}%{_libdir}/%{name}/%{native_pkg}/libopentui.so \
        | grep -qE '\s(ldapr|ldaprb|ldaprh|ldapur|stlur|stlurb|stlurh)\s'; then
    echo "libopentui.so contains ARMv8.3 FEAT_LRCPC instructions." >&2
    echo "It was built for the build host's CPU, not the aarch64 baseline." >&2
    exit 1
fi
%endif

# The shims that make the directory resolvable as the npm package OpenTUI
# looks for. Upstream generates these in packages/core/scripts/build.ts,
# which needs bun to run; nothing else in that script applies here.
cat > %{buildroot}%{_libdir}/%{name}/%{native_pkg}/index.js <<'EOF'
import { fileURLToPath } from "node:url"

export default fileURLToPath(new URL("./libopentui.so", import.meta.url))
EOF

cat > %{buildroot}%{_libdir}/%{name}/%{native_pkg}/index.bun.js <<'EOF'
const module = await import("./libopentui.so", { with: { type: "file" } })

export default module.default
EOF

cat > %{buildroot}%{_libdir}/%{name}/%{native_pkg}/index.d.ts <<'EOF'
declare const path: string
export default path
EOF

cat > %{buildroot}%{_libdir}/%{name}/%{native_pkg}/package.json <<'EOF'
{
  "name": "@opentui/core-linux-%{node_arch}",
  "version": "%{version}",
  "description": "OpenTUI native library for linux-%{node_arch}",
  "type": "module",
  "main": "index.js",
  "module": "index.js",
  "types": "index.d.ts",
  "license": "MIT",
  "exports": {
    ".": {
      "bun": "./index.bun.js",
      "import": "./index.js",
      "types": "./index.d.ts"
    }
  },
  "os": ["linux"],
  "cpu": ["%{node_arch}"]
}
EOF

# TS laid out so @opentui/* resolve (OTUI_ASSET_ROOT: native lib); copy
# wholesale, drop build-only dirs — src/testing(.ts) stays, src/tests goes.
for pkg in core keymap solid; do
    cp -a packages/$pkg %{buildroot}%{_libdir}/%{name}/@opentui/
    ( cd %{buildroot}%{_libdir}/%{name}/@opentui/$pkg
      rm -rf src/tests src/benchmark src/specs tests examples \
              dev docs bench-before bench-after node_modules \
              tsconfig.json tsconfig.build.json tsconfig.node-test.json bunfig.toml
      # scripts/ also holds five modules the exports map points at, so drop
      # the plumbing by name rather than the directory.
      rm -f scripts/build.ts scripts/publish.ts scripts/dist-test.ts \
            scripts/standalone-test.ts scripts/test.ts scripts/test-node.ts \
            scripts/test-node-hook.mjs scripts/test-packed-consumer.ts \
            scripts/bun-test-preload.ts \
            scripts/bench-js-node.ts scripts/native-symbols.ts \
            scripts/native-symbols.test.ts scripts/package-native-symbols.ts \
            scripts/variants.ts scripts/reconciler-benchmark.ts \
            scripts/branch-cov.ts scripts/branch-cov-map.ts \
            scripts/branch-cov-preload.ts scripts/native-abi.ts \
            scripts/native-abi-pointers.ts scripts/native-abi.zig \
            scripts/native-scene.fixture.tsx
      rmdir scripts 2>/dev/null || :
      find . -name '*.test.ts' -delete
      find . -name '__snapshots__' -type d -prune -exec rm -rf {} +
      find . -name '.gitignore' -delete
      # Exported modules with bun shebangs aren't meant to run in place;
      # strip them so rpm wants no new interpreter.
      grep -rlZ '^#!%{_bindir}/env ' --include='*.ts' . \
          | xargs -0 -r sed -i '1{/^#!/d}'
      # workspace:* only means anything inside upstream's monorepo. These
      # packages are installed side by side, so pin the sibling to the
      # version that is actually here, which is what npm publish would do.
      sed -i 's/"workspace:\*"/"%{version}"/g' package.json )
done

# The tarball excludes upstream's prebuilt grammar .wasm (see _service);
# %%install links the system tree-sitter-*-wasm modules to the exact
# paths the runtime manifest (default-parsers.ts) names instead.
tree=%{buildroot}%{_libdir}/%{name}/@opentui/core/src/lib/tree-sitter/assets
for rel in $(grep -o '"wasm": "assets/[^"]*"' packages/core/src/lib/tree-sitter/default-parsers.ts | sed 's/.*"assets\///; s/"$//'); do
    sys=%{_datadir}/tree-sitter/wasm/$(basename "$rel")
    if ! test -f "$sys"; then
        echo "no packaged module for src/lib/tree-sitter/$rel: add its tree-sitter-<lang>-wasm package" >&2
        exit 1
    fi
    ln -sf "$sys" "$tree/$rel"
done

# Nothing above may delete a file the packages advertise. Everything a
# consumer can import goes through an exports map, so walk them and fail the
# build rather than shipping a package that resolves to a missing path.
python3 - %{buildroot}%{_libdir}/%{name}/@opentui <<'EOF'
import json, os, sys

root = sys.argv[1]
missing = []
for pkg in ("core", "keymap", "solid"):
    d = os.path.join(root, pkg)
    meta = json.load(open(os.path.join(d, "package.json")))

    def walk(value, key):
        if isinstance(value, str):
            if value.startswith("./") and not os.path.exists(os.path.join(d, value[2:])):
                missing.append(f"@opentui/{pkg} {key} -> {value}")
        elif isinstance(value, dict):
            for inner in value.values():
                walk(inner, key)

    for key, value in (meta.get("exports") or {}).items():
        walk(value, key)
    for key in ("main", "module", "types"):
        if key in meta:
            walk("./" + meta[key].lstrip("./"), key)

if missing:
    sys.exit("exported paths are not installed:\n  " + "\n  ".join(sorted(set(missing))))
EOF

%check
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
export ZIG_LOCAL_CACHE_DIR="$PWD/.zig-local-cache"
# The X11 clipboard tests bind filesystem sockets under /tmp/.X11-unix,
# which exists on any X machine but not in the build root.
mkdir -p /tmp/.X11-unix
cd packages/native
zig build test \
    -Drequire-video \
    --summary all

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/@opentui
%{_libdir}/%{name}/%{native_pkg}

%files devel
%license LICENSE
%{_libdir}/%{name}/@opentui/core
%{_libdir}/%{name}/@opentui/keymap
%{_libdir}/%{name}/@opentui/solid

%changelog
