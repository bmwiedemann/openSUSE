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
%global opentui_version 0.4.5
# The two native libraries loaded through bun:ffi at run time. Both ABIs are
# private to the TypeScript that ships in the vendor tree, so the packages
# are required at exactly the version that tree was generated from; %%prep
# checks the pins.
%global fff_version 0.9.4
%global bun_pty_version 0.4.8
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
# Node's names for the platform, not RPM's: the build target is derived from
# them, and @opentui/core resolves its native library by the same names.
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
Name:           opencode
Version:        1.18.30
Release:        0
Summary:        AI coding agent for the terminal
# opencode itself is MIT. The npm dependency tree is compiled into the
# executable, so its licences are part of the binary; see README.SUSE-maint
# for how the expression below is derived and rechecked on a bump.
# Legal-Review-Notice: rederived for 1.18.30 from the declared license field
# of all 508 unique packages in the vendor tarball (510 store entries). No
# copyleft of any kind. The SPDX set is unchanged from 1.18.29. Two
# conclusions are not visible from the packages themselves: poe-oauth 0.0.8
# declares no licence and ships no text, its MIT grant comes from the
# upstream repository root; caniuse-lite is CC-BY-4.0, whose attribution
# clause is why %%prep installs its LICENSE separately.
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
# The models.dev catalogue, which the build otherwise fetches at build time.
Source2:        models.dev-api-%{version}.json
Source3:        %{name}_vendor
Source4:        %{name}_vendor_trace
Source5:        %{name}-vendor-keep.txt
Source6:        README.SUSE-maint
# Header-only N-API wrapper @parcel/watcher's addon is compiled against.
Source11:       https://registry.npmjs.org/node-addon-api/-/node-addon-api-%{node_addon_api_version}.tgz
# C side of the native shell parser (Patch5).
Source12:       %{name}-tsshim.c
# Upstream's build script fails unless bun satisfies a caret range around the
# version it pins. It pins 1.3.14 and Factory has 1.4.2, so the check passes
# and this patch is inert today; it stays because both versions float, and a
# major bump on either side would otherwise stop the build over upstream's
# convenience rather than a real incompatibility. See README.SUSE-maint.
Patch0:         %{name}-relax-bun-version.patch
# The next three stop the binary fetching code over the network at runtime.
# Each patch's header says what it stops, why it cannot be configured away,
# and which environment variable puts upstream's behaviour back.
Patch1:         %{name}-no-self-update.patch
Patch2:         %{name}-no-runtime-npm-install.patch
Patch3:         %{name}-no-grammar-download.patch
# PATCH-FIX-UPSTREAM opencode-fix-filesystem-cycle.patch boo#1280159 gh#anomalyco/opencode#48397
Patch4:         %{name}-fix-filesystem-cycle.patch
# Parses shell commands with the system libtree-sitter and grammar packages
# through bun:ffi; the wasm route needs a runtime module only emscripten can
# build. Placeholders are filled in below.
Patch5:         %{name}-native-tree-sitter.patch
# No floor. Which bun upstream wants changes with every release and Patch0
# turns a mismatch into a warning; a floor here would be a guess at which
# older bun still works, and the package is a git snapshot anyway, so
# 1.4.0~git sorts below 1.4.0.
BuildRequires:  bun
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  nodejs26-devel
BuildRequires:  photon-node = %{photon_version}
# %%prep reads the @opentui/core pin out of package.json.
BuildRequires:  python3-base
# Only for %%check, which loads every system grammar module with its
# queries the way the highlighter will.
BuildRequires:  tree-sitter-agda-queries
BuildRequires:  tree-sitter-agda-wasm
BuildRequires:  tree-sitter-bash
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
BuildRequires:  tree-sitter-devel
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
BuildRequires:  tree-sitter-powershell
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
BuildRequires:  zstd
Requires:       bun-pty = %{bun_pty_version}
Requires:       fff = %{fff_version}
Requires:       git-core
# Native TUI library, loaded at runtime (not compiled into the binary).
# Equality because the FFI ABI is private and unversioned.
Requires:       opentui = %{opentui_version}
# Downloaded on first use otherwise; opencode shells out to it for grep.
Requires:       ripgrep
Requires:       tree-sitter-bash
Requires:       tree-sitter-powershell
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
Provides:       bundled(parcel-watcher) = %{parcel_watcher_version}
# Embedded from the distribution's own packages (the exact BuildRequires
# above keep these versions truthful; an update of one of those packages
# makes this one unresolvable until the pin follows).
Provides:       bundled(photon-node) = %{photon_version}
Provides:       bundled(tree-sitter-javascript) = %{ts_javascript_version}
Provides:       bundled(tree-sitter-markdown) = %{ts_markdown_version}
Provides:       bundled(tree-sitter-typescript) = %{ts_typescript_version}
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
# npm binaries are removed so nothing embeds them. Pins first.
for pin in "@ff-labs+fff-bun@%{fff_version}" "bun-pty@%{bun_pty_version}" \
           "@silvia-odwyer+photon-node@%{photon_version}" \
           "@parcel+watcher@%{parcel_watcher_version}"; do
    test -d "node_modules/.bun/$pin" || {
        echo "vendor tree has no $pin; the pinned package versions in this spec are stale" >&2
        exit 1
    }
done
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

# Patch5's placeholders, and the npm modules the shell tool no longer loads.
sed -i 's|@OPENCODE_LIBDIR@|%{_libdir}/%{name}|; s|@TREE_SITTER_GRAMMARS@|%{_libdir}/tree-sitter|' \
    packages/opencode/src/tool/shell.ts packages/opencode/src/tool/shell-native.ts
grep -q '%{_libdir}/tree-sitter/libtree-sitter-bash.so' packages/opencode/src/tool/shell.ts

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
rm -rf node_modules/.bun/tree-sitter-bash@*/node_modules/tree-sitter-bash/prebuilds
rm -f node_modules/.bun/tree-sitter-bash@*/node_modules/tree-sitter-bash/tree-sitter-bash.wasm \
      node_modules/.bun/tree-sitter-powershell@*/node_modules/tree-sitter-powershell/tree-sitter-powershell.wasm \
      node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/lib/tree-sitter.wasm \
      node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/lib/tree-sitter.wasm.map \
      node_modules/.bun/web-tree-sitter@*/node_modules/web-tree-sitter/tree-sitter.wasm.map

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
# packages (bun embeds what sits in the asset directories).
assets=$(ls -d node_modules/.bun/@opentui+core@%{opentui_version}+*/node_modules/@opentui/core/assets)
for lang in javascript typescript markdown markdown_inline zig; do
    install -pm 0644 %{_datadir}/tree-sitter/wasm/tree-sitter-$lang.wasm "$assets/$lang/tree-sitter-$lang.wasm"
done

export HOME="$PWD/.home"
export BUN_INSTALL_CACHE_DIR="$PWD/.bun-cache"
mkdir -p "$HOME" "$BUN_INSTALL_CACHE_DIR"

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
gcc %{optflags} -g0 -shared -fPIC -o libopencode-tsshim.so %{SOURCE12} -ltree-sitter
strip --strip-unneeded libopencode-tsshim.so
cd packages/opencode
# --single builds only the host platform. --skip-embed-web-ui leaves out the
# browser interface, which needs another 101 npm packages and embeds two fonts
# that ship without a licence.
bun run ./script/build.ts --single --skip-install --skip-embed-web-ui

%install
# brp-15-strip-debug runs binutils strip, not %%__strip, on every ELF that
# `file` reports as not stripped. Whether that is the case depends on how
# the bun it was compiled from was stripped (a project without debuginfo
# leaves bun's .symtab in place), and strip rewrites the file just as
# eu-strip does.
export NO_BRP_STRIP_DEBUG=true
install -Dpm 0755 packages/opencode/dist/%{name}-linux-%{node_arch}/bin/%{name} \
    %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 libopencode-tsshim.so %{buildroot}%{_libdir}/%{name}/libopencode-tsshim.so

%check
# The executable carries its own runtime and payload; if anything stripped or
# truncated it, it does not get this far.
%{buildroot}%{_bindir}/%{name} --version
test "$(%{buildroot}%{_bindir}/%{name} --version)" = "%{version}"

# What the payload carries: the distribution's modules and the addon built
# above, nothing from npm.
python3 - %{buildroot}%{_bindir}/%{name} %{_datadir}/tree-sitter/wasm %{_datadir}/photon-node/photon_rs_bg.wasm watcher.node <<'EOF'
import sys
exe = open(sys.argv[1], "rb").read()
for f in ["{}/tree-sitter-{}.wasm".format(sys.argv[2], l) for l in
          ("javascript", "typescript", "markdown", "markdown_inline", "zig")] + sys.argv[3:]:
    assert open(f, "rb").read() in exe, f + " is not embedded as built"
# bun's embedded-file table names every module the payload carries.
import re
found = sorted(set((m.group(1), m.group(2)) for m in
               re.finditer(rb"\$bunfs/root/([A-Za-z0-9_.-]+?)-[a-z0-9]{8}\.(so|node|wasm)\b", exe)))
expected = sorted([(b"photon_rs_bg", b"wasm"), (b"tree-sitter", b"wasm"), (b"watcher", b"node")] +
                  [(b"tree-sitter-" + l.encode(), b"wasm") for l in
                   ("javascript", "typescript", "markdown", "markdown_inline", "zig")])
assert found == expected, "embedded native/wasm files: {}".format(found)
EOF
# The native shell parser through the shim that ships and the grammar
# packages: a pipeline yields its two commands.
cat > check-parse.ts <<'EOF'
import { NativeParser, loadLanguage } from "./packages/opencode/src/tool/shell-native"
const bash = new NativeParser(loadLanguage("%{_libdir}/tree-sitter/libtree-sitter-bash.so", "tree_sitter_bash"))
const tree = bash.parse("cat foo | grep -i bar > out")
const cmds = tree.rootNode.descendantsOfType("command").map((n) => n.text)
if (cmds.length !== 2 || cmds[0] !== "cat foo") { console.log(cmds); process.exit(1) }
// Everything else shell.ts reads from a node or a tree.
const root = tree.rootNode
const first = root.child(0)
if (root.childCount < 1 || first === null || first.parent !== root || first.type === "" || cmds[1] !== "grep -i bar") {
  console.log({ childCount: root.childCount, first: first?.type, parent: first?.parent?.type, cmds })
  process.exit(1)
}
tree.delete()
const ps = new NativeParser(loadLanguage("%{_libdir}/tree-sitter/libtree-sitter-powershell.so", "tree_sitter_powershell"))
if (ps.parse("Get-ChildItem -Recurse | Select-Object -First 5").rootNode.descendantsOfType("command").length < 1) process.exit(1)
EOF
OPENCODE_TSSHIM=%{buildroot}%{_libdir}/%{name}/libopencode-tsshim.so bun check-parse.ts
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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libopencode-tsshim.so

%changelog
