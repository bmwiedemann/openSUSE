#!/bin/bash
#
# Regenerate the livekit-libwebrtc source tarball.
#
# There is no upstream source archive for libwebrtc: the tree is assembled by
# depot_tools' gclient from webrtc-sdk/webrtc plus ~45 DEPS'd repositories.
# This script reproduces exactly that assembly, prunes everything a Linux
# shared-library build never reads, and packs the result.
#
# Usage:  ./make-source.sh [workdir]
#         WEBRTC_COMMIT=<sha> ./make-source.sh
#
# Needs: git, python3, tar, zstd, ~30 GB of free disk and network access.
# Produces: webrtc-<milestone>-<shortsha>.tar.zst in the current directory.
#
set -euo pipefail
set -E
trap 'echo "make-source.sh: failed at line $LINENO" >&2' ERR

# webrtc-sdk/webrtc commit that livekit's WEBRTC_TAG refers to
WEBRTC_URL="${WEBRTC_URL:-https://github.com/webrtc-sdk/webrtc.git}"
WEBRTC_COMMIT="${WEBRTC_COMMIT:-0001d84a16a3502e45b86a065253df4c511026ae}"
WEBRTC_MILESTONE="${WEBRTC_MILESTONE:-m137}"

# depot_tools is not released; pin it so the DEPS resolution is reproducible
DEPOT_TOOLS_URL="${DEPOT_TOOLS_URL:-https://chromium.googlesource.com/chromium/tools/depot_tools.git}"
DEPOT_TOOLS_COMMIT="${DEPOT_TOOLS_COMMIT:-4a978d8f1f3567d5bd729aec018bfc345a14e1cd}"

JOBS="${JOBS:-8}"

outdir="$PWD"
workdir="${1:-$PWD/webrtc-src-workdir}"
mkdir -p "$workdir"
workdir="$(cd "$workdir" && pwd)"

short="${WEBRTC_COMMIT:0:7}"
name="webrtc-${WEBRTC_MILESTONE}-${short}"

echo "=== workdir:  $workdir"
echo "=== commit:   $WEBRTC_COMMIT"
echo "=== tarball:  $outdir/$name.tar.zst"

# ---------------------------------------------------------------- depot_tools
if [ ! -d "$workdir/depot_tools/.git" ]; then
	git clone --depth 1 "$DEPOT_TOOLS_URL" "$workdir/depot_tools"
fi
git -C "$workdir/depot_tools" fetch --depth 1 origin "$DEPOT_TOOLS_COMMIT"
git -C "$workdir/depot_tools" checkout -q "$DEPOT_TOOLS_COMMIT"

export PATH="$workdir/depot_tools:$PATH"
export DEPOT_TOOLS_UPDATE=0
export DEPOT_TOOLS_METRICS=0
export GIT_TERMINAL_PROMPT=0
# depot_tools ships its own python ("vpython"); use the system one instead
export VPYTHON_BYPASS="manually managed python not supported by chrome operations"

# ---------------------------------------------------------------- gclient sync
# Same solution as livekit's webrtc-sys/libwebrtc/.gclient, but pinned to a
# commit instead of a branch and restricted to Linux (no android/ios/mac/win).
src="$workdir/checkout"
mkdir -p "$src"
cat > "$src/.gclient" <<EOF
solutions = [
  {
    "name": "src",
    "url": "$WEBRTC_URL",
    "custom_deps": {},
    "deps_file": "DEPS",
    "managed": False,
  },
]
target_os = ["linux"]
target_os_only = True
EOF

# --nohooks: every DEPS hook either downloads a toolchain we replace with the
# distribution's (clang, rust, gn, ninja, siso), installs a sysroot we do not
# use (use_sysroot=false), targets win/mac/fuchsia, or fetches test payloads
# (src/resources, testing/location_tags.json).  None of them is needed to run
# `gn gen` + `ninja :default`; see README/the fact sheet.
cd "$src"
gclient sync --no-history --nohooks --shallow -R -j"$JOBS" -r "src@$WEBRTC_COMMIT"

# commit timestamp, used as the tarball mtime so the archive is reproducible
epoch="$(git -C "$src/src" log -1 --format=%ct)"
echo "=== commit epoch: $epoch ($(date -u -d "@$epoch" +%Y-%m-%dT%H:%M:%SZ))"

echo "=== size before prune: $(du -sh "$src" | cut -f1)"

# ---------------------------------------------------------------------- prune
cd "$src"

drop() { [ -e "$1" ] && rm -rf "$1" || true; }

# VCS metadata and gclient scratch state
find . -maxdepth 6 -type d -name .git -prune -exec rm -rf {} + 2>/dev/null || true
drop .cipd
drop .gclient_previous_sync_commits

# Prebuilt binaries: the distribution supplies its own compiler and build tools
drop src/third_party/llvm-build		# Chromium's hermetic clang
drop src/third_party/rust-toolchain	# Chromium's hermetic rust (stubbed below)
drop src/third_party/siso		# Siso build tool, we build with ninja
drop src/third_party/ninja		# prebuilt ninja
drop src/third_party/depot_tools	# second copy of depot_tools
drop src/buildtools/linux64		# prebuilt gn, host-arch specific
drop src/buildtools/linux64-format	# prebuilt clang-format
drop src/buildtools/reclient		# remote execution client
drop src/third_party/jdk		# Java toolchain, Android only
drop src/third_party/pipewire		# prebuilt pipewire, for running tests
drop src/tools/luci-go			# LUCI test infrastructure binaries
drop src/tools/resultdb			# LUCI test infrastructure binaries
drop src/third_party/instrumented_libs/binaries	# MSan prebuilt libs, 2.2 GB

# Trees no target in the `:default` build graph references
drop src/third_party/blink		# Chromium renderer
drop src/third_party/tflite_support	# Chromium ML support
drop src/third_party/test_fonts		# test fonts
drop src/third_party/sqlite/fuzz	# fuzzer corpus
drop src/tools/perf			# telemetry benchmarks
drop src/resources			# test media (rtc_include_tests=false)
drop src/examples			# rtc_build_examples=false
drop src/data				# test data

# Platform trees a Linux build never compiles
drop src/third_party/android_deps
drop src/third_party/android_toolchain
drop src/third_party/android_sdk
drop src/third_party/android_ndk
drop src/third_party/android_build_tools
drop src/third_party/fuchsia-sdk
drop src/third_party/fuchsia-gn-sdk

# gn parses build files from these but `:default` compiles nothing out of them
# (verified with `ninja -t inputs :default`), so keep only what gn reads plus
# the licences.  gn never stats the `sources` it is handed, so an empty tree
# with its BUILD.gn intact still generates.  Everything in the second group is
# a library build/linux/unbundle/replace_gn_files.py can replace by the system
# one, so dropping the bundled copy is what a distribution wants anyway.
strip_to_build_files() {
	local d
	for d in "$@"; do
		[ -d "$d" ] || continue
		find "$d" -type f \
			! -name '*.gn' ! -name '*.gni' ! -name '*.isolate' \
			! -iname 'LICENSE*' ! -iname 'COPYING*' ! -iname 'NOTICE*' \
			-delete 2>/dev/null || true
	done
}
# catapult: telemetry/trace viewer.  grpc: not in the :default graph.
# rust: vendored crates, nothing compiles Rust here.  The first group compiles
# into nothing; the second is replaced by the distribution's copies, and their
# build files have to stay for replace_gn_files.py to overwrite.
strip_to_build_files \
	src/third_party/catapult \
	src/third_party/grpc \
	src/third_party/rust \
	src/third_party/brotli src/third_party/fontconfig \
	src/third_party/freetype src/third_party/harfbuzz-ng \
	src/third_party/icu src/third_party/jsoncpp \
	src/third_party/libpng src/third_party/libwebp \
	src/third_party/libxml src/third_party/libxslt \
	src/third_party/re2 \
	src/third_party/dav1d src/third_party/libaom \
	src/third_party/libjpeg_turbo src/third_party/libvpx \
	src/third_party/opus src/third_party/zlib

# Test/fuzz payloads inside third_party, never their build files or licences
for sub in test tests testdata test_data fuzz fuzzing benchmarks demos; do
	find src/third_party -mindepth 2 -maxdepth 4 -type d -name "$sub" -print0 2>/dev/null |
	while IFS= read -r -d '' t; do
		find "$t" -type f ! -name '*.gn' ! -name '*.gni' \
			! -iname 'LICENSE*' ! -iname 'COPYING*' -delete 2>/dev/null || true
	done || true
done
find src/third_party -type d -empty -delete 2>/dev/null || true


# Payload directories nothing in the graph reads
drop src/base/test/data
drop src/third_party/liblouis/wasm
drop src/test/fuzzers/corpora

# Trees whose licence would have to be reviewed although nothing reads their
# build files: widevine is not open source, unrar is non-free, mutter is
# GPL-2.0.  The rest are crash handlers and test corpora.
drop src/third_party/widevine
drop src/third_party/unrar
drop src/third_party/mutter
drop src/third_party/libzip
drop src/third_party/afl
drop src/third_party/breakpad
drop src/third_party/crashpad
drop src/third_party/apache-win32
drop src/third_party/hyphenation-patterns

# Java/JS toolchains and Windows IDL output: their build files are imported
# from trees outside the :default graph, so only the payload can go.
strip_to_build_files \
	src/third_party/closure_compiler \
	src/third_party/google-java-format \
	src/third_party/material_web_components \
	src/third_party/r8 \
	src/third_party/win_build_output

# Nothing compiled here is prebuilt: sweep anything that is already a binary.
# `file` is authoritative; extensions are not.  It runs serially on purpose -
# several writers on one pipe interleave and truncate lines, and the sed then
# silently misses entries.
echo "=== prebuilt sweep"
find src -type f -size +64c -exec file -N --mime-type {} + 2>/dev/null |
	sed -n 's@^\(.*\):[[:space:]]*\(application/x-\(executable\|sharedlib\|object\|archive\|pie-executable\|dosexec\|mach-binary\)\|application/wasm\|application/java-archive\|application/vnd\.microsoft\.portable-executable\)$@\1@p' > "$workdir/prebuilt.txt" || true
find src -type f \( -name '*.jar' -o -name '*.apk' -o -name '*.aar' \) >> "$workdir/prebuilt.txt" || true
sort -u -o "$workdir/prebuilt.txt" "$workdir/prebuilt.txt"
if [ -s "$workdir/prebuilt.txt" ]; then
	echo "=== removing $(wc -l < "$workdir/prebuilt.txt") prebuilt binaries"
	sed 's/^/    /' "$workdir/prebuilt.txt"
	tr '\n' '\0' < "$workdir/prebuilt.txt" | xargs -0 -r rm -f
fi
find src/third_party -type d -empty -delete 2>/dev/null || true

# ffmpeg and openh264 come from the distribution: replace_gn_files.py swaps in
# build/linux/unbundle/{ffmpeg,openh264}.gn, and it backs the old file up
# before overwriting, so a placeholder has to be there.  Dropping the bundled
# ffmpeg also keeps its GPL-licensed parts out of the source package.
for d in ffmpeg openh264; do
	rm -rf "src/third_party/$d"
	mkdir -p "src/third_party/$d"
	echo "# replaced by build/linux/unbundle/$d.gn" > "src/third_party/$d/BUILD.gn"
done

# ---------------------------------------------------------------------- stubs
# build/config/rust.gni execs tools/rust/update_rust.py, which refuses to run
# unless third_party/rust-toolchain/VERSION names the revision src/tools expects
# - and the revision DEPS pins does not match it even in an unpruned checkout.
# No Rust is compiled (enable_rust only pulls in the cxx bindgen targets), so
# feed it the string it wants.  Same trick as nixpkgs' livekit-libwebrtc.
# update_rust.py exits 1 when the revisions disagree, which is exactly the case
# we are in, so its status has to be ignored - the message is what we want.
mkdir -p src/third_party/rust-toolchain
{ python3 src/tools/rust/update_rust.py --print-package-version 2>&1 || true; } |
	head -n1 |
	sed 's/.* expected Rust version is \([^ ]*\) .*/rustc 1.0 1234 (\1 chromium)/' \
	> src/third_party/rust-toolchain/VERSION
grep -q chromium src/third_party/rust-toolchain/VERSION ||
	{ echo "failed to synthesise rust-toolchain/VERSION" >&2; exit 1; }

# build/util/version.gni reads this when use_dummy_lastchange=true is not passed
echo 0 > src/build/util/LASTCHANGE.committime

echo "=== size after prune:  $(du -sh "$src" | cut -f1)"

# ----------------------------------------------------------------------- pack
stage="$workdir/stage"
rm -rf "$stage"
mkdir -p "$stage/$name"
mv "$src/src" "$stage/$name/src"
# keeps the exact revision of every DEPS'd repository, for provenance
cp "$src/.gclient_entries" "$stage/$name/gclient_entries.txt"

cd "$stage"
rm -f "$outdir/$name.tar.zst"
tar --sort=name \
	--mtime="@$epoch" \
	--owner=0 --group=0 --numeric-owner \
	--mode='u+rwX,go+rX,go-w' \
	--format=gnu \
	-cf - "$name" |
	zstd -19 -T0 -o "$outdir/$name.tar.zst"

# put the tree back so a re-run does not have to sync again
mv "$stage/$name/src" "$src/src"
rm -rf "$stage"

echo "=== done: $outdir/$name.tar.zst ($(du -h "$outdir/$name.tar.zst" | cut -f1))"
zstd --version
sha256sum "$outdir/$name.tar.zst"
