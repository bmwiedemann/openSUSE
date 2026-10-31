#
# spec file for package opencode
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


# bun build --compile appends its payload to the end of the executable, past
# everything the ELF headers describe. eu-strip rewrites the file and drops
# it, and the result aborts at startup, so there is no debuginfo package to
# be had here.
%global debug_package %{nil}
%global __strip /bin/true
# The TypeScript and libopentui.so talk over a private FFI ABI with no
# versioning of its own, so the runtime opentui package must be the
# release this tree pins. %%prep checks that this still matches.
%global opentui_version 0.8.0
# The two native libraries loaded through bun:ffi at run time. Both ABIs are
# private to the TypeScript that ships in the vendor tree, so the packages
# are required at exactly the version that tree was generated from; %%prep
# checks the pins.
%global fff_version 0.10.5
%global bun_pty_version 0.4.11
%global photon_version 0.3.4
# The tree-sitter grammars @opentui/core highlights with. The modules come
# from the tree-sitter-<lang>-wasm packages at these versions (its own
# parsers-config.ts pins javascript 0.25.0 and markdown 0.5.1; the
# highlight queries were checked against the packaged releases).
%global ts_javascript_version 0.23.1
%global ts_typescript_version 0.23.2
%global ts_markdown_version 0.5.3
%global ts_zig_version 1.1.2
%global parcel_watcher_version 2.5.1
%global node_addon_api_version 7.1.1
# The TUI highlighter's languages served from tree-sitter-<lang>-wasm and
# -queries packages (grammar names as in the upstream descriptor list; the
# c_sharp module lives in tree-sitter-c-sharp).
%global opencode_system_grammars python rust go cpp csharp bash c java ruby php scala html json yaml haskell css julia lua ocaml clojure swift toml nix diff elixir fsharp r make vim xml agda
# The pty helper (@opencode/pty 0.4.0, packages/process-daemon) is built
# from source in %%build instead of shipping upstream's prebuilt binaries.
%global opencode_pty_version 0.4.0
# Ghostty revision the helper's build.rs pins (packages/process-daemon
# ghostty-revision), and the zig that builds its libghostty-vt. Ghostty's
# build.zig.zon sets minimum_zig_version 0.16.0, so this is an equality
# pin like the grammar modules above: a Factory zig move makes this
# package unresolvable until the revision is re-verified against it.
%global zig_version 0.16.0
# Node's names for the platform, not RPM's: the build target is derived from
# them, and @opentui/core resolves its native library by the same names.
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
Name:           opencode
Version:        2.2.5
Release:        0
Summary:        AI coding agent for the terminal
# opencode itself is MIT. The npm dependency tree is compiled into the
# executable, so its licences are part of the binary; see README.SUSE-maint
# for how the expression below is derived and rechecked on a bump.
# Legal-Review-Notice: rederived for 2.2.5 from the declared license field
# of all 346 packages in the vendor tarball (347 store entries: one entry
# is the symlink farm, which is not a package; several names resolve at two
# versions, same as before). The retraced keep list still names 349 entries:
# the two @opencode/pty-linux-* entries it names are stripped from the
# tarball after pruning (see below), so the tarball holds two fewer. No
# copyleft, no proprietary packages. The SPDX
# set is unchanged from 2.2.0 except for those two MIT entries leaving
# (MIT 191, Apache-2.0 67,
# ISC 65, BlueOak-1.0.0 9, rest as before). The pty helper embedded in the
# payload is built from source in %%build (see "Native code" below), so its
# own closure joins the binary too: the process-daemon 0.4.0 crate (MIT)
# with 42 crates in its linux normal closure (3 proc-macro plugins plus
# their syn/quote/unicode-ident inputs are build-time only), everything
# linked into the helper MIT, Apache-2.0, ISC or BSD-2-Clause (memchr
# under its MIT option), plus Ghostty libghostty-vt (MIT) with uucode
# (MIT) and simdutf/highway (Apache-2.0) compiled in. No copyleft, no
# proprietary code; the License tag already covers all of it.
# The two @opencode/pty-linux-{arm64,x64}-gnu prebuilt ELF
# bin/opencode-pty files are stripped from the vendor tarball after
# pruning (opencode_vendor, like the native .so files it already drops):
# superseded by the from-source pty build embedded via OPENCODE_PTY_BIN,
# never opened, never executed at build time. Only the build arch's one
# would ever have been used; the other was already inert. Both were MIT,
# same shape @opencode-ai/pty shipped at 2.2.0, renamed upstream in the
# v2.2.0..v2.2.4 range. %%check proves the payload carries the from-source
# bytes (sha256) and the npm binaries are gone from the tree. See
# README.SUSE-maint "Native code".
# @anthropic-ai/claude-agent-sdk 0.3.301, new in this range for the Claude
# Agent provider, declares "SEE LICENSE IN README.md" and ships a
# proprietary Anthropic LICENSE.md ("All rights reserved", Commercial Terms;
# no OSI grant in the README either), so it must not be compiled into the
# executable. Patch4 adds it to `external` in packages/cli/script/build.ts;
# nothing imports its values statically (every other source import is
# `import type`), so the retraced keep list drops its store entry and the
# provider degrades at runtime to its designed "isn't installed" error. The
# License tag below therefore covers everything shipped. See README.SUSE-maint
# "Licensing".
# Three conclusions are not visible from the packages themselves:
# @npmcli/redact says ISC and ships MIT text, abbrev says ISC and its LICENSE
# says "ISC OR MIT", and caniuse-lite is CC-BY-4.0, whose attribution clause
# is why %%prep installs its LICENSE separately. One trap when counting: a
# store entry also holds nested subpath packages (zod's v3/v4/mini, solid-js's
# h/html/store, effect's ai-docs) whose manifests carry no license field, so
# only the manifest whose name matches the entry is a package.
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0 AND ISC AND MIT
URL:            https://opencode.ai
# Not the upstream tarball. Upstream ships the web console, the desktop app
# and the marketing site in the same repository: 48 MB of mp4 plus the Inter
# and JetBrains Mono fonts, which come with no licence text. None of it is
# reachable from the CLI build. opencode_vendor drops it and records what it
# dropped.
Source0:        %{name}-%{version}.tar.zst
# The npm dependency tree. bun build --compile needs it on disk and there is
# no way to build from a plain release tarball.
Source1:        %{name}-vendor-%{version}.tar.zst
# The 2.2.5 vendor closure carries one prebuilt file.
# tree-sitter.wasm is the runtime grammar asset the web-tree-sitter
# highlighter loads (reached through @opentui/core's parser worker, which
# peer-depends on web-tree-sitter; %%check asserts it is embedded and loads
# every system grammar through it). Kept for the same reason as the npm
# file it is: building it needs emscripten, which the distribution does
# not have. Embedded at build time, never executed at build time.
# (A full strip of the web-tree-sitter entry was verified to break the
# build: @opentui/core's runtime-assets import it, the retraced keep list
# keeps it, and the TUI highlights through it. Deleting it wants an
# emscripten build or a highlighter without it first.)
# Source-Binary-Exception: opencode-vendor-2.2.5.tar.zst:node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/tree-sitter.wasm -- bootstrap: runtime grammar asset the highlighter loads, embedded at build time, never executed at build time
# Everything else that used to be excepted is stripped at tarball time
# instead: the @opencode/pty-linux-* ELFs (opencode_vendor drops the two
# entries after pruning), the cargo vendor's Windows-only import libs and
# wasm-only artifacts (stripped with .cargo-checksum.json repair per
# crate), and Ghostty zig-pkg's test/ and examples/ dirs. No exception
# lines for any of them remain.
# The models.dev catalogue, which the build otherwise fetches at build time.
Source2:        models.dev-api-%{version}.json
Source3:        %{name}_vendor
Source4:        %{name}_vendor_trace
Source5:        %{name}-vendor-keep.txt
Source6:        README.SUSE-maint
# Header-only N-API wrapper @parcel/watcher's addon is compiled against.
Source11:       https://registry.npmjs.org/node-addon-api/-/node-addon-api-%{node_addon_api_version}.tgz
# The pty helper crate (packages/process-daemon from the 2.2.5 tree).
Source20:       %{name}-process-daemon-%{version}.tar.zst
# Its locked cargo closure, from the cargo_vendor service (_service,
# respect-lockfile) with the non-Linux weight stripped afterwards (see
# above). Unpacks into the crate dir in %%prep.
Source21:       vendor.tar.zst
# Ghostty at ab0b9da9e88fcb4b0533a1854e84628f663930af (short
# ab0b9da9, as in the file name) with .git (build.rs asserts the revision
# and a clean include/ghostty) and a pre-fetched zig-pkg/ with the 25 zig
# deps `zig build` resolves at configure time (OBS builds have no
# network), minus their top-level test/ and examples/ dirs except
# translate_c's test/cases.zig and libxev's examples/ (their build.zig
# files open them at configure; see above). Regeneration recipe in
# README.SUSE-maint "Native code".
Source22:       ghostty-ab0b9da9.tar.zst
# Upstream's build script fails unless bun satisfies a caret range around the
# version it pins. It pins 1.4.4 and Factory has 1.4.2, so without this the
# check would fail the build; the patch warns instead, because both versions
# float and the check is upstream's convenience rather than a real
# incompatibility (the build is Bun.build() plus shell calls, and %%check
# runs the resulting binary). See README.SUSE-maint.
Patch0:         %{name}-relax-bun-version.patch
# The next three stop the binary fetching code over the network at runtime.
# Each patch's header says what it stops, why it cannot be configured away,
# and which environment variable puts upstream's behaviour back.
Patch1:         %{name}-no-self-update.patch
Patch2:         %{name}-no-runtime-npm-install.patch
Patch3:         %{name}-no-grammar-download.patch
# @anthropic-ai/claude-agent-sdk is proprietary (SEE LICENSE IN README.md,
# Anthropic Commercial Terms) and must not be compiled into the executable.
# The Claude Agent provider already degrades to its designed "isn't
# installed" error when the SDK is absent (dynamic import with a .catch in
# claude/sdk.ts; every other source import is `import type`), so leaving the
# package external only turns that provider off. See README.SUSE-maint.
# PATCH-FIX-OPENSUSE %{name}-externalize-claude-agent-sdk.patch mpluskal@suse.com -- proprietary SDK must not be compiled in, upstream will not drop it
Patch4:         %{name}-externalize-claude-agent-sdk.patch
# No floor. Which bun upstream wants changes with every release and Patch0
# turns a mismatch into a warning; a floor here would be a guess at which
# older bun still works, and the package is a git snapshot anyway, so
# 1.4.0~git sorts below 1.4.0.
BuildRequires:  bun
# The pty helper toolchain: cargo with the rust it comes with (the crate
# asks rust 1.90.0 in rust-toolchain.toml, which Factory's rust satisfies;
# the file is inert without rustup), git for build.rs's Ghostty revision
# asserts, and exactly the zig Ghostty's build.zig.zon asks for.
BuildRequires:  cargo-packaging
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  nodejs26-devel
BuildRequires:  photon-node = %{photon_version}
BuildRequires:  pkgconfig
# %%prep reads the @opentui/core pin out of package.json.
BuildRequires:  python3-base
# Only for %%check, which loads every system grammar module with its
# queries the way the highlighter will.
BuildRequires:  tree-sitter-agda-queries
BuildRequires:  tree-sitter-agda-wasm
BuildRequires:  tree-sitter-bash-queries
BuildRequires:  tree-sitter-bash-wasm
BuildRequires:  tree-sitter-c-queries
BuildRequires:  tree-sitter-c-sharp-queries
BuildRequires:  tree-sitter-c-sharp-wasm
BuildRequires:  tree-sitter-c-wasm
BuildRequires:  tree-sitter-clojure-queries
BuildRequires:  tree-sitter-clojure-wasm
BuildRequires:  tree-sitter-cpp-queries
BuildRequires:  tree-sitter-cpp-wasm
BuildRequires:  tree-sitter-css-queries
BuildRequires:  tree-sitter-css-wasm
BuildRequires:  tree-sitter-diff-queries
BuildRequires:  tree-sitter-diff-wasm
BuildRequires:  tree-sitter-elixir-queries
BuildRequires:  tree-sitter-elixir-wasm
BuildRequires:  tree-sitter-fsharp-queries
BuildRequires:  tree-sitter-fsharp-wasm
BuildRequires:  tree-sitter-go-queries
BuildRequires:  tree-sitter-go-wasm
BuildRequires:  tree-sitter-haskell-queries
BuildRequires:  tree-sitter-haskell-wasm
BuildRequires:  tree-sitter-html-queries
BuildRequires:  tree-sitter-html-wasm
BuildRequires:  tree-sitter-java-queries
BuildRequires:  tree-sitter-java-wasm
BuildRequires:  tree-sitter-javascript-wasm = %{ts_javascript_version}
BuildRequires:  tree-sitter-json-queries
BuildRequires:  tree-sitter-json-wasm
BuildRequires:  tree-sitter-julia-queries
BuildRequires:  tree-sitter-julia-wasm
BuildRequires:  tree-sitter-lua-queries
BuildRequires:  tree-sitter-lua-wasm
BuildRequires:  tree-sitter-make-queries
BuildRequires:  tree-sitter-make-wasm
BuildRequires:  tree-sitter-markdown-wasm = %{ts_markdown_version}
BuildRequires:  tree-sitter-nix-queries
BuildRequires:  tree-sitter-nix-wasm
BuildRequires:  tree-sitter-ocaml-queries
BuildRequires:  tree-sitter-ocaml-wasm
BuildRequires:  tree-sitter-php-queries
BuildRequires:  tree-sitter-php-wasm
BuildRequires:  tree-sitter-python-queries
BuildRequires:  tree-sitter-python-wasm
BuildRequires:  tree-sitter-r-queries
BuildRequires:  tree-sitter-r-wasm
BuildRequires:  tree-sitter-ruby-queries
BuildRequires:  tree-sitter-ruby-wasm
BuildRequires:  tree-sitter-rust-queries
BuildRequires:  tree-sitter-rust-wasm
BuildRequires:  tree-sitter-scala-queries
BuildRequires:  tree-sitter-scala-wasm
BuildRequires:  tree-sitter-swift-queries
BuildRequires:  tree-sitter-swift-wasm
BuildRequires:  tree-sitter-toml-queries
BuildRequires:  tree-sitter-toml-wasm
BuildRequires:  tree-sitter-typescript-wasm = %{ts_typescript_version}
BuildRequires:  tree-sitter-vim-queries
BuildRequires:  tree-sitter-vim-wasm
BuildRequires:  tree-sitter-xml-queries
BuildRequires:  tree-sitter-xml-wasm
BuildRequires:  tree-sitter-yaml-queries
BuildRequires:  tree-sitter-yaml-wasm
BuildRequires:  tree-sitter-zig-wasm = %{ts_zig_version}
BuildRequires:  zig = %{zig_version}
BuildRequires:  zstd
# The two native libraries are loaded from their packages at run time;
# the floor is the tree's version, but newer binaries stay compatible:
# the vendored bun-pty 0.4.11 binds exactly the eight cdylib symbols 0.4.9
# bound (close, get_exit_code, get_pid, kill, read, resize, spawn, write;
# verified by export comparison against 0.4.11's librust_pty.so), and
# every fff_* entry point fff-bun 0.10.5 references resolves in fff
# 0.11.0's libfff_c.so.
Requires:       bun-pty >= %{bun_pty_version}
Requires:       fff >= %{fff_version}
# opencode spawns the git binary (packages/core/src/git.ts), so git-core is the
# dependency, not its perl modules; spec-cleaner --perl wants to expand it into
# ~20 perl(Git*) lines that no longer pull the binary in. Accepted deviation.
Requires:       git-core
# Native TUI library, loaded at runtime (not compiled into the binary).
# Equality because the FFI ABI is private and unversioned.
Requires:       opentui = %{opentui_version}
# Downloaded on first use otherwise; opencode shells out to it for grep.
Requires:       ripgrep
# The 31 languages the TUI highlighter can load from the distribution
# (see %%prep): a missing pair means plain text for that language.
Recommends:     tree-sitter-agda-queries
Recommends:     tree-sitter-agda-wasm
Recommends:     tree-sitter-bash-queries
Recommends:     tree-sitter-bash-wasm
Recommends:     tree-sitter-c-queries
Recommends:     tree-sitter-c-sharp-queries
Recommends:     tree-sitter-c-sharp-wasm
Recommends:     tree-sitter-c-wasm
Recommends:     tree-sitter-clojure-queries
Recommends:     tree-sitter-clojure-wasm
Recommends:     tree-sitter-cpp-queries
Recommends:     tree-sitter-cpp-wasm
Recommends:     tree-sitter-css-queries
Recommends:     tree-sitter-css-wasm
Recommends:     tree-sitter-diff-queries
Recommends:     tree-sitter-diff-wasm
Recommends:     tree-sitter-elixir-queries
Recommends:     tree-sitter-elixir-wasm
Recommends:     tree-sitter-fsharp-queries
Recommends:     tree-sitter-fsharp-wasm
Recommends:     tree-sitter-go-queries
Recommends:     tree-sitter-go-wasm
Recommends:     tree-sitter-haskell-queries
Recommends:     tree-sitter-haskell-wasm
Recommends:     tree-sitter-html-queries
Recommends:     tree-sitter-html-wasm
Recommends:     tree-sitter-java-queries
Recommends:     tree-sitter-java-wasm
Recommends:     tree-sitter-json-queries
Recommends:     tree-sitter-json-wasm
Recommends:     tree-sitter-julia-queries
Recommends:     tree-sitter-julia-wasm
Recommends:     tree-sitter-lua-queries
Recommends:     tree-sitter-lua-wasm
Recommends:     tree-sitter-make-queries
Recommends:     tree-sitter-make-wasm
Recommends:     tree-sitter-nix-queries
Recommends:     tree-sitter-nix-wasm
Recommends:     tree-sitter-ocaml-queries
Recommends:     tree-sitter-ocaml-wasm
Recommends:     tree-sitter-php-queries
Recommends:     tree-sitter-php-wasm
Recommends:     tree-sitter-python-queries
Recommends:     tree-sitter-python-wasm
Recommends:     tree-sitter-r-queries
Recommends:     tree-sitter-r-wasm
Recommends:     tree-sitter-ruby-queries
Recommends:     tree-sitter-ruby-wasm
Recommends:     tree-sitter-rust-queries
Recommends:     tree-sitter-rust-wasm
Recommends:     tree-sitter-scala-queries
Recommends:     tree-sitter-scala-wasm
Recommends:     tree-sitter-swift-queries
Recommends:     tree-sitter-swift-wasm
Recommends:     tree-sitter-toml-queries
Recommends:     tree-sitter-toml-wasm
Recommends:     tree-sitter-vim-queries
Recommends:     tree-sitter-vim-wasm
Recommends:     tree-sitter-xml-queries
Recommends:     tree-sitter-xml-wasm
Recommends:     tree-sitter-yaml-queries
Recommends:     tree-sitter-yaml-wasm
# Compiled into the executable from source during this build.
Provides:       bundled(node-addon-api) = %{node_addon_api_version}
Provides:       bundled(opencode-pty) = %{opencode_pty_version}
Provides:       bundled(parcel-watcher) = %{parcel_watcher_version}
# Embedded from the distribution's own packages (the exact BuildRequires
# above keep these versions truthful; an update of one of those packages
# makes this one unresolvable until the pin follows).
Provides:       bundled(photon-node) = %{photon_version}
Provides:       bundled(tree-sitter-javascript) = %{ts_javascript_version}
Provides:       bundled(tree-sitter-markdown) = %{ts_markdown_version}
Provides:       bundled(tree-sitter-typescript) = %{ts_typescript_version}
# 0.6.8's sixth grammar module, tsx for typescriptreact, ships in the same
# tree-sitter-typescript-wasm package as the typescript one above.
Provides:       bundled(tree-sitter-tsx) = %{ts_typescript_version}
Provides:       bundled(tree-sitter-zig) = %{ts_zig_version}
# The one module still taken from npm: web-tree-sitter's runtime needs
# emscripten, which the distribution does not have. Used by the highlighter.
Provides:       bundled(web-tree-sitter) = 0.25.10
# bun only supports these two.
ExclusiveArch:  x86_64 aarch64

%description
opencode is an AI coding agent that runs in the terminal. It works with a
range of model providers, reads and edits files in a project, runs commands,
and keeps a session history.

This build is the command line client only. The optional web interface is not
included.

It also does not update itself, install npm packages into your home
directory, or download syntax highlighting grammars from GitHub, all of which
upstream does by default. README.SUSE-maint lists the environment variables
that turn each of them back on.

%prep
%autosetup -p1 -a1
# rpm honours one -a per %%autosetup, so the second tarball by hand.
tar -xzf %{SOURCE11}
cp -a %{SOURCE6} .

# Dependencies compiled into the executable whose licence asks for the text to
# travel with it. The rest are covered by the tree's own LICENSE.
mkdir -p licenses
install -pm 0644 node_modules/.bun/caniuse-lite@*/node_modules/caniuse-lite/LICENSE \
    licenses/LICENSE.caniuse-lite

# The vendored dependency tree is pruned to what the build reads, so a bump
# that changes the closure has to be noticed here rather than halfway through
# a link. Bun reports a missing module as a hard resolution error, but only
# for the architecture being built, so check the pin as well.
pinned=$(python3 -c "import json; print(json.load(open('package.json'))['workspaces']['catalog']['@opentui/core'])")
if [ "$pinned" != "%{opentui_version}" ]; then
    echo "opencode pins @opentui/core $pinned but this package builds against %{opentui_version}." >&2
    echo "Bump the opentui package first; the FFI ABI between them is private." >&2
    exit 1
fi

# The npm @opentui/core-linux-* packages ship a prebuilt libopentui.so, which
# opencode_vendor removed. Do not copy the distro .so into the tree: bun
# --compile would embed it. Point the native module at the opentui package
# path so bun:ffi dlopens it at runtime.
otui="node_modules/.bun/@opentui+core-linux-%{node_arch}@%{opentui_version}/node_modules/@opentui/core-linux-%{node_arch}"
mkdir -p "$otui"
cat > "$otui/index.bun.js" <<EOF
export default "%{_libdir}/opentui/@opentui/core-linux-%{node_arch}/libopentui.so"
EOF
cat > "$otui/index.js" <<EOF
export default "%{_libdir}/opentui/@opentui/core-linux-%{node_arch}/libopentui.so"
EOF

# The two native libraries are loaded from their packages at run time, like
# libopentui.so above: the vendor tree's loaders get literal paths and the
# npm binaries are removed so nothing embeds them. Pins first. The
# @opencode/pty-linux-* entries are stripped from the tarball (see above),
# so their absence is asserted rather than their presence: with
# OPENCODE_PTY_BIN set the build never opens them.
for pin in "@ff-labs+fff-bun@%{fff_version}" "bun-pty@%{bun_pty_version}" \
           "@silvia-odwyer+photon-node@%{photon_version}" \
           "@parcel+watcher@%{parcel_watcher_version}"; do
    test -d "node_modules/.bun/$pin" || {
        echo "vendor tree has no $pin; the pinned package versions in this spec are stale" >&2
        exit 1
    }
done
test ! -e "node_modules/.bun/@opencode+pty-linux-%{node_arch}-gnu@%{opencode_pty_version}" || {
    echo "vendor tree still ships the superseded prebuilt pty helper; opencode_vendor must strip it" >&2
    exit 1
}
fffbun="node_modules/.bun/@ff-labs+fff-bun@%{fff_version}/node_modules/@ff-labs/fff-bun/src"
cat > "$fffbun/embedded.ts" <<EOF
export const embeddedLibPath: string | null = "%{_libdir}/fff/libfff_c.so"
EOF
sed -i 's|const isEmbedded = embeddedLibPath?.includes("$bunfs") ?? false;|const isEmbedded = embeddedLibPath !== null;|' "$fffbun/ffi.ts"
grep -q 'const isEmbedded = embeddedLibPath !== null;' "$fffbun/ffi.ts"
rm -rf node_modules/.bun/@ff-labs+fff-bin-*
pty="node_modules/.bun/bun-pty@%{bun_pty_version}/node_modules/bun-pty/src/terminal.ts"
python3 - "$pty" <<'EOF'
import sys
p = sys.argv[1]; s = open(p).read()
a = s.index("\t// For bun compile:")
b = s.index("\t// Fallback: dynamic resolution")
s = s[:a] + '\treturn "@BUN_PTY_LIB@";\n\n' + s[b:]
open(p, "w").write(s)
EOF
sed -i 's|@BUN_PTY_LIB@|%{_libdir}/bun-pty/librust_pty.so|' "$pty"
grep -q 'return "%{_libdir}/bun-pty/librust_pty.so";' "$pty"
rm -rf node_modules/.bun/bun-pty@%{bun_pty_version}/node_modules/bun-pty/rust-pty

# photon: the module and glue come from the photon-node package. Upstream
# patches the npm glue (patches/@silvia-odwyer%%2Fphoton-node@*.patch) so
# that it bundles under bun and finds the module at the path opencode
# embeds it under; the same two edits are applied to the package's glue,
# which a different wasm-bindgen release wrote, so hunks would not apply.
photon="node_modules/.bun/@silvia-odwyer+photon-node@%{photon_version}/node_modules/@silvia-odwyer/photon-node"
rm -f "$photon"/photon_rs_bg.wasm "$photon"/photon_rs.js "$photon"/photon_rs_bg.js "$photon"/*.d.ts
cp -p %{_datadir}/photon-node/* "$photon"/
python3 - "$photon/photon_rs.js" <<'EOF'
import re, sys
p = sys.argv[1]; s = open(p).read()
s, n = re.subn(r"^imports\['__wbindgen_placeholder__'\] = module\.exports;$",
               "const __wbindgen_placeholder__ = {};\nimports['__wbindgen_placeholder__'] = __wbindgen_placeholder__;", s, flags=re.M)
assert n == 1, "placeholder line not found"
s, n = re.subn(r"^module\.exports\.(__wb\w+) = function", r"__wbindgen_placeholder__.\1 = function", s, flags=re.M)
assert n > 10, "import shims not found"
old = "const path = require('path').join(__dirname, 'photon_rs_bg.wasm');"
assert old in s, "wasm path line not found"
s = s.replace(old, "const path = globalThis.__OPENCODE_PHOTON_WASM_PATH || require('path').join(__dirname, 'photon_rs_bg.wasm');")
open(p, "w").write(s)
EOF

# The TUI highlighter's other languages: upstream downloads the grammar
# module and a highlights.scm per language on first use (blocked by
# Patch3). Point the descriptors at the tree-sitter-<lang>-wasm and
# -queries packages instead; the loader takes a local path as it takes a
# URL. hcl and kotlin stay blocked: their packaged grammars ship no queries
# (Factory's kotlin is another grammar than the one upstream pins), and a
# module without queries highlights nothing. vue stays blocked too: its
# highlights.scm inherits html_tags and carries a #set! form the
# web-tree-sitter runtime opencode ships rejects, so it never compiles.
# Anything else upstream adds stays blocked until it is packaged and
# listed here. Each descriptor must carry exactly one highlights source
# and no injections, or the rewrite (and the download block) would not
# cover it. cpp's packaged query is upstream's delta on top of the C one,
# so its descriptor gets both files, C first. The locals entries (dead:
# nothing in @opentui/core reads them) are dropped so no web URL is left
# in a descriptor the download block no longer filters.
python3 - packages/tui/src/parsers-config.ts <<'EOF'
import re, sys
langs = "%{opencode_system_grammars}".split()
grammar = {"csharp": "c_sharp"}
before = {"cpp": ["c"]}
p = sys.argv[1]; s = open(p).read()
blocks = re.split(r'(?=\n    \{\n      filetype: ")', s)
out = []; done = []
for b in blocks:
    m = re.match(r'\n    \{\n      filetype: "([a-z_]+)"', b)
    if m and m.group(1) in langs:
        ft = m.group(1); g = grammar.get(ft, ft)
        b = re.sub(r'\n\s*locals: \[.*?\],', '', b, count=1, flags=re.S)
        live = re.sub(r'^\s*//.*$', '', b, flags=re.M)
        assert "injections" not in live and "locals" not in live, ft + ": injections/locals not handled"
        hl = re.search(r'highlights: \[(.*?)\],', live, flags=re.S)
        assert hl and len(re.findall(r'"https://[^"]+"', hl.group(1))) == 1, ft + ": not exactly one highlights source"
        b, n1 = re.subn(r'wasm: "https://[^"]+"', 'wasm: "%{_datadir}/tree-sitter/wasm/tree-sitter-' + g + '.wasm"', b, count=1)
        srcs = ", ".join('"%{_datadir}/tree-sitter/queries/' + q + '/highlights.scm"' for q in before.get(ft, []) + [g])
        b, n2 = re.subn(r'highlights: \[.*?\],', 'highlights: [' + srcs + '],', b, count=1, flags=re.S)
        assert n1 == 1 and n2 == 1, ft
        done.append(ft)
    out.append(b)
missing = sorted(set(langs) - set(done))
assert not missing, "not in upstream parsers-config: " + " ".join(missing)
open(p, "w").write("".join(out))
EOF
rm -f node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/lib/tree-sitter.wasm \
      node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/lib/tree-sitter.wasm.map \
      node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/tree-sitter.wasm.map

# The pty helper sources: the process-daemon crate (Source20), its locked
# cargo vendor (Source21, cargo_vendor service output) overlaid into the
# crate dir, and Ghostty with .git plus pre-fetched zig deps (Source22).
# They unpack at the build root, next to this tree, not into it.
tar --use-compress-program=unzstd -xf %{SOURCE20} -C %{_builddir}
tar --use-compress-program=unzstd -xf %{SOURCE21} --strip-components=1 \
    -C %{_builddir}/%{name}-process-daemon-%{version}/process-daemon
tar --use-compress-program=unzstd -xf %{SOURCE22} -C %{_builddir}

%build
# @parcel/watcher's addon, compiled from the source in its own npm package:
# the sources and defines are binding.gyp's Linux branch, the headers are
# Node's and node-addon-api's (Source11 unpacks as package/).
w="node_modules/.bun/@parcel+watcher@%{parcel_watcher_version}/node_modules/@parcel/watcher"
plat="node_modules/.bun/@parcel+watcher-linux-%{node_arch}-glibc@%{parcel_watcher_version}/node_modules/@parcel/watcher-linux-%{node_arch}-glibc"
test -d "$plat"
g++ %{optflags} -shared -fPIC -std=c++17 -DNAPI_DISABLE_CPP_EXCEPTIONS -DWATCHMAN -DINOTIFY -DBRUTE_FORCE \
    -I%{_includedir}/node26 -Ipackage -I"$w/src" \
    "$w"/src/binding.cc "$w"/src/Watcher.cc "$w"/src/Backend.cc "$w"/src/DirTree.cc \
    "$w"/src/Glob.cc "$w"/src/Debounce.cc "$w"/src/watchman/BSER.cc \
    "$w"/src/watchman/WatchmanBackend.cc "$w"/src/shared/BruteForceBackend.cc \
    "$w"/src/linux/InotifyBackend.cc "$w"/src/unix/legacy.cc -o watcher.node
# It goes into the payload, where no brp script reaches it.
strip --strip-debug watcher.node
install -pm 0644 watcher.node "$plat/watcher.node"

# The highlighter's grammar modules, from the tree-sitter-<lang>-wasm
# packages (bun embeds what sits in the asset directories). Every copy in
# the tree gets them: a re-resolved tree can hold two @opentui+core entries
# (0.7.0 ships d25f280c761c3e91 live and eff4d38d6a4a2cd9 for the
# plugin/theme farms). 0.7.0 adds a sixth module, tsx for
# typescriptreact, which no upstream descriptor uses yet but bun build
# still resolves; it comes from tree-sitter-typescript-wasm like the
# typescript one, so no new pin.
for assets in node_modules/.bun/@opentui+core@%{opentui_version}+*/node_modules/@opentui/core/assets; do
    test -d "$assets" || continue
    for lang in javascript typescript markdown markdown_inline zig; do
        install -pm 0644 %{_datadir}/tree-sitter/wasm/tree-sitter-$lang.wasm "$assets/$lang/tree-sitter-$lang.wasm"
    done
    install -pm 0644 %{_datadir}/tree-sitter/wasm/tree-sitter-tsx.wasm "$assets/typescriptreact/tree-sitter-tsx.wasm"
done

export HOME="$PWD/.home"
export BUN_INSTALL_CACHE_DIR="$PWD/.bun-cache"
mkdir -p "$HOME" "$BUN_INSTALL_CACHE_DIR"

# The pty helper, built from source: process-daemon %{opencode_pty_version}
# (MIT) with its locked cargo closure, statically linking Ghostty's
# libghostty-vt (Ghostty ab0b9da9, MIT; uucode MIT and
# simdutf/highway Apache-2.0 compiled in). GHOSTTY_SOURCE_DIR satisfies
# build.rs without its git-fetch fallback; OPENCODE_ZIG_CPU=baseline
# matches upstream's release builds (packages/process-daemon
# script/release-bin/zig); the zig package cache starts empty because
# Ghostty's pre-fetched zig-pkg/ carries the configure closure (see
# README.SUSE-maint "Native code"). Everything is --offline --locked.
export GHOSTTY_SOURCE_DIR="%{_builddir}/ghostty-ab0b9da9"
export OPENCODE_ZIG_CPU=baseline
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
mkdir -p "$ZIG_GLOBAL_CACHE_DIR"
pushd %{_builddir}/%{name}-process-daemon-%{version}/process-daemon
cargo build --release --offline --locked
popd
# The CLI build below embeds this file (version "local", sha256 recorded)
# instead of @opencode/pty's prebuilt binaries. Only the build arch's
# helper is ever embedded, which matches these per-arch builds.
export OPENCODE_PTY_BIN="%{_builddir}/%{name}-process-daemon-%{version}/process-daemon/target/release/opencode-pty"

# Everything the build would otherwise reach the network for:
#   MODELS_DEV_API_JSON  the catalogue, instead of fetching models.dev/api.json
#   OPENCODE_VERSION     instead of asking the npm registry what is latest
#   OPENCODE_CHANNEL     instead of `git branch --show-current`
#   --skip-install       instead of `bun install` for the native packages
export MODELS_DEV_API_JSON="%{SOURCE2}"
export OPENCODE_VERSION="%{version}"
export OPENCODE_CHANNEL=latest

# No DWARF and stripped by hand: this package has no debuginfo subpackage
# (see the top of the file) and brp stripping is off for the payload's sake.
cd packages/cli
# --single builds only the host platform. --skip-web-ui leaves out the
# browser interface, which needs another 101 npm packages and embeds two fonts
# that ship without a licence.
bun run ./script/build.ts --single --skip-install --skip-web-ui

%install
# brp-15-strip-debug runs binutils strip, not %%__strip, on every ELF that
# `file` reports as not stripped. Whether that is the case depends on how
# the bun it was compiled from was stripped (a project without debuginfo
# leaves bun's .symtab in place), and strip rewrites the file just as
# eu-strip does.
export NO_BRP_STRIP_DEBUG=true
install -Dpm 0755 packages/cli/dist/cli-linux-%{node_arch}/bin/%{name} \
    %{buildroot}%{_bindir}/%{name}

%check
# The executable carries its own runtime and payload; if anything stripped or
# truncated it, it does not get this far.
%{buildroot}%{_bindir}/%{name} --version
test "$(%{buildroot}%{_bindir}/%{name} --version)" = "%{name} v%{version}"

# The vendor tree must hold exactly one copy of the TUI toolkit. A filtered
# install without the workspace root resolves two copies, whose theme colour
# objects then fail the identity check, so the TUI crashes at startup with
# "e.replace is not a function" (boo#1288219). Fail here rather than ship a
# binary that crashes on first start.
test "$(ls -d node_modules/.bun/@opentui+core@* 2>/dev/null | wc -l)" = "1" || {
    echo "vendor tree has more than one @opentui/core instance; see boo#1288219" >&2
    exit 1
}

# What the payload carries: the distribution's modules, the addon
# built above, and the pty helper built from source above (embedded via
# OPENCODE_PTY_BIN; the npm binaries are stripped from the tree). It carries no
# extension, so the embedded-file assertion below cannot see it; the
# sha256 assertion after it covers it instead. See
# README.SUSE-maint "Native code".
python3 - %{buildroot}%{_bindir}/%{name} %{_datadir}/tree-sitter/wasm %{_datadir}/photon-node/photon_rs_bg.wasm watcher.node <<'EOF'
import sys
exe = open(sys.argv[1], "rb").read()
for f in ["{}/tree-sitter-{}.wasm".format(sys.argv[2], l) for l in
          ("javascript", "typescript", "markdown", "markdown_inline", "zig", "tsx")] + sys.argv[3:]:
    assert open(f, "rb").read() in exe, f + " is not embedded as built"
# bun's embedded-file table names the payload's native and wasm members.
import re
found = sorted(set((m.group(1), m.group(2)) for m in
               re.finditer(rb"\$bunfs/root/([A-Za-z0-9_.-]+?)-[a-z0-9]{8}\.(so|node|wasm)\b", exe)))
expected = sorted([(b"photon_rs_bg", b"wasm"), (b"tree-sitter", b"wasm"), (b"watcher", b"node")] +
                  [(b"tree-sitter-" + l.encode(), b"wasm") for l in
                   ("javascript", "typescript", "markdown", "markdown_inline", "zig", "tsx")])
assert found == expected, "embedded native/wasm files: {}".format(found)
EOF
# The embedded pty helper is the from-source build: the CLI build records
# its sha256 into the payload. The npm binaries are stripped from the
# vendor tree (see above), so their absence is asserted rather than their
# non-embedding: there is nothing left to embed.
python3 - %{buildroot}%{_bindir}/%{name} \
    %{_builddir}/%{name}-process-daemon-%{version}/process-daemon/target/release/opencode-pty <<'EOF'
import hashlib, sys
exe = open(sys.argv[1], "rb").read()
ours = open(sys.argv[2], "rb").read()
assert hashlib.sha256(ours).hexdigest().encode() in exe, "from-source pty sha256 not recorded in payload"
EOF
test ! -e node_modules/.bun/@opencode+pty-linux-x64-gnu@%{opencode_pty_version}/node_modules/@opencode/pty-linux-x64-gnu/bin/opencode-pty
test ! -e node_modules/.bun/@opencode+pty-linux-arm64-gnu@%{opencode_pty_version}/node_modules/@opencode/pty-linux-arm64-gnu/bin/opencode-pty
# Every language the descriptors now point at the distribution for: the
# module loads in the web-tree-sitter runtime opencode ships, its
# highlights.scm compiles against it, and a parse works. A query naming a
# node the packaged grammar lacks fails here instead of leaving that
# language unhighlighted at run time.
W=$(ls -d node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter | head -1)
test -d "$W"
cat > check-grammars.ts <<EOF
const { Parser, Language, Query } = await import("$PWD/$W/tree-sitter.js")
await Parser.init({ locateFile: () => "$PWD/$W/tree-sitter.wasm" })
const grammar: Record<string, string> = { csharp: "c_sharp" }
const before: Record<string, string[]> = { cpp: ["c"] }
let bad = 0
for (const ft of "%{opencode_system_grammars}".split(" ")) {
  const g = grammar[ft] ?? ft
  try {
    const L = await Language.load("%{_datadir}/tree-sitter/wasm/tree-sitter-" + g + ".wasm")
    const parts = []
    for (const q of [...(before[ft] ?? []), g]) parts.push(await Bun.file("%{_datadir}/tree-sitter/queries/" + q + "/highlights.scm").text())
    new Query(L, parts.join("\n"))
    const p = new Parser(); p.setLanguage(L); if (!p.parse("x")) throw new Error("parse returned null")
  } catch (e) { bad++; console.log(ft + ": " + String(e).slice(0, 200)) }
}
if (bad) process.exit(1)
EOF
bun check-grammars.ts
# What stays blocked (hcl, kotlin, vue, and anything upstream adds).
echo "descriptors still pointing at the web:"
grep -B1 -E 'wasm: "https://' packages/tui/src/parsers-config.ts | grep -oE 'filetype: "[a-z_]+"' || :

%files
%license LICENSE licenses/LICENSE.caniuse-lite
%doc README.md README.SUSE-maint
%{_bindir}/%{name}

%changelog
