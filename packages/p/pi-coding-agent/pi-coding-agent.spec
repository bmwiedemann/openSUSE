#
# spec file for package pi-coding-agent
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global npm_name @earendil-works/pi-coding-agent
# Every runtime dependency is vendored, so the nodejs dependency generator must
# not turn package.json's "dependencies" into npm(...) symbols that nothing in
# the distribution provides.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
Name:           pi-coding-agent
Version:        1.5.2
Release:        0
Summary:        Minimal terminal coding agent
# Legal-Review-Notice: pi itself is MIT. The 122 vendored dependencies are
# MIT (59), Apache-2.0 (38), BSD-3-Clause (13), ISC (7), BlueOak-1.0.0 (3),
# Unlicense (1) and 0BSD (1); every dependency declares a license. The tag
# below is the union of all of them.
# - The QuickJS runtime is built from Source20/21 (MIT quickjs-wasi 3.6.2,
#   MIT quickjs-ng 6d46d07, Apache-2.0 ada 3.4.3).
# - mbedtls 4.0 is Apache-2.0 OR GPL-2.0-or-later; Apache-2.0 is elected.
License:        0BSD AND Apache-2.0 AND BSD-3-Clause AND BlueOak-1.0.0 AND ISC AND MIT AND Unlicense
URL:            https://github.com/earendil-works/pi
Source0:        https://registry.npmjs.org/%{npm_name}/-/pi-coding-agent-%{version}.tgz
# The npm tarball ships no license file; taken from the upstream git tag.
Source1:        LICENSE
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
# The vendored sources above carry no prebuilt binaries: the tarballs
# with them are stripped when the node_modules service output is made
# (dev/optional platform .node addons are dropped outright -- the
# --omit=dev --omit=optional install below never fetches them -- and
# pi-tui, photon-node and quickjs-wasi are repacked without their
# binary members, with the lockfile integrity hashes re-taken).
# Source0 stays byte-identical to upstream (download_files requires
# it); its one prebuilt binary is excepted below. After every
# `osc service manualrun`, re-apply the same strip before committing,
# or source-binaries.py goes red again.
Source13:       %{name}-rpmlintrc
Source20:       https://github.com/vercel-labs/quickjs-wasi/archive/refs/tags/quickjs-wasi@3.6.2.tar.gz#/quickjs-wasi-3.6.2.tar.gz
Source21:       https://github.com/quickjs-ng/quickjs/archive/6d46d07d04041b40f4f49eaa7fdebe44c314c699.tar.gz#/quickjs-ng-6d46d07.tar.gz
Patch0:         pi-disable-self-update.patch
# PATCH-FIX-OPENSUSE pi-use-modular-runtime.patch mpluskal@suse.com -- point bin and the rpc-entry export at the modular runtime we ship and patch, not at the pre-bundled copy
Patch1:         pi-use-modular-runtime.patch
BuildRequires:  binaryen
BuildRequires:  clang >= 23
BuildRequires:  fdupes
# libclang_rt23 >= 23.1.4 carries the wasm32 builtins the link needs.
BuildRequires:  libclang_rt23 >= 23.1.4
BuildRequires:  lld
BuildRequires:  llvm >= 23
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  nodejs >= 22.19.0
BuildRequires:  nodejs-packaging
BuildRequires:  wasi-libc
Requires:       nodejs >= 22.19.0
Recommends:     %{name}-examples = %{version}-%{release}
# On Linux dist/utils/clipboard.js drives these tools directly -- copying
# skips pi-tui's native X11 helper entirely and reading only falls back to it
# after they fail -- and %%build drops that helper (see there), so these are
# the local clipboard route here. pi's own error text names xclip and xsel.
Recommends:     wl-clipboard
Recommends:     xclip
Recommends:     xsel
# cln builds an unrelated Archimedes' constant demo from its own pi.cc and
# installs it as /usr/bin/pi next to libcln.so, so the two cannot be
# co-installed. Upstream cln's "make install" does not ship that binary.
Conflicts:      cln
# dist/core/export-html/vendor/highlight.min.js and marked.min.js are embedded
# verbatim into the standalone HTML that "pi export" produces, so they cannot
# be unbundled.
Provides:       bundled(highlight.js)
Provides:       bundled(marked)
# The wasm runtime below links these; their versions are in the notice above.
Provides:       bundled(ada) = 3.4.3
Provides:       bundled(mbedtls) = 4.0.0
Provides:       bundled(quickjs-ng) = 0.17.0
BuildArch:      noarch
%include        %{_sourcedir}/node_modules.spec.inc

%description
pi is a terminal coding agent. It runs in interactive, print/JSON, and RPC
modes, and can be embedded in other applications through its SDK.

It is extended with TypeScript extensions, skills, prompt templates and
themes rather than by forking it, and those extensions are distributed as
pi packages via npm or git.

%package examples
Summary:        Example extensions for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example pi extensions, skills and prompt templates, read by the /examples
command of %{name}.

%prep
%setup -q -c -T
tar -xf %{SOURCE0}
mv package %{name}
cd %{name}
%patch -P 0 -p1
%patch -P 1 -p1
cp -p %{SOURCE1} LICENSE

# Source maps (4.9 MB) and TypeScript declarations (0.6 MB) are of no use in
# a runtime package and there is no -devel consumer for a CLI.
find dist -name '*.map' -delete
find dist -name '*.d.ts' -delete

# Documentation screenshots, useless for a terminal application.
rm -rf docs/images

# The 9.1 MB pre-bundled runtime added in 0.84.3. Patch1 points bin and the
# rpc-entry export back at the modular tree, so nothing references this any
# more, and it carries an unpatched second copy of detectInstallMethod() that
# pi-disable-self-update.patch cannot reach.
rm -rf dist/bundle

# The doom-overlay example ships doom.wasm/doom.js built from doomgeneric,
# which is derived from the GPL-2.0 id Software Doom sources -- the complete
# corresponding source is not in this package, and the extension downloads a
# non-redistributable shareware WAD on first run. Source0 stays pristine
# (see above), so this rm keeps it out of the payload instead.
# Source-Binary-Exception: */examples/extensions/doom-overlay/* -- test-data: example asset only, deleted in %%prep and never shipped, loaded or linked by anything this package builds or tests; not rebuildable here without the full Doom sources
rm -rf examples/extensions/doom-overlay

# Upstream stopped shipping a shrinkwrap in 1.0.1 (it was production-only and
# omitted the integrity field for the @earendil-works/* sibling packages,
# which the node_modules source service rejects), so Source10 is the full
# package-lock.json npm generated for this tree, with integrity for every
# entry. It must stay in place for the install below, or npm re-resolves the
# ranges in package.json and wants tarballs the vendored archive does not
# carry.
cp -p %{SOURCE10} npm-shrinkwrap.json

# dist/ is shipped prebuilt and nothing here compiles or runs the upstream
# test suite, so drop the devDependencies; the --omit=dev install below then
# has nothing to reconcile.
npm pkg delete devDependencies

# The packaged 1.5.2 pins undici 8.12.3 (boo#1290296 & co.); pin the
# vendored 8.12.4 here so the offline npm install does not re-resolve.
npm pkg set dependencies.undici=8.12.4

%build
cd %{name}
# --omit=optional: every optionalDependency in this tree is a per-architecture
# prebuilt binary, which would make the payload of this noarch package differ
# between build hosts. Since 0.99.0 the dev-side vite chain adds rolldown,
# lightningcss and fsevents platform packages to the optional set (1.2.0
# dropped the @earendil-works/chord dependency that used to pull in
# esbuild's platform packages). Those tarballs are stripped from the vendored
# archive outright (see above); Source10 keeps their entries and the install
# below simply never fetches them.
local-npm-registry %{_sourcedir} install --omit=dev --omit=optional --ignore-scripts
rm -f npm-shrinkwrap.json package-lock.json

# Prebuilt .node addons. 0.86.0 moved the clipboard helpers in-tree and added
# native/linux/prebuilds/linux-{x64,arm64}/linux-platform-x11.node (libxcb),
# which native-platform.js DOES load on Linux -- a noarch package cannot ship
# an ELF addon, and its C source would need libxcb-devel and an arch-dependent
# package, so it goes and clipboard.js falls back to the xclip/wl-clipboard
# tools recommended above. The darwin and win32 addons are never loaded here.
# photon-node is loaded lazily behind a try/catch and only powers image
# conversion, so it degrades gracefully. The vendored pi-tui and photon-node
# tarballs are already repacked without these (see above); the rms stay so a
# service refresh that restores the binaries still cannot reach the payload.
rm -rf node_modules/@earendil-works/pi-tui/native
rm -f node_modules/@silvia-odwyer/photon-node/photon_rs_bg.wasm

# The sandbox runtime is built from Source20/21 with the
# distribution toolchain, then installed over the stripped tree.
mkdir -p %{_builddir}/quickjs-wasi %{_builddir}/qjs-sdk/bin
tar -xzf %{SOURCE20} -C %{_builddir}/quickjs-wasi --strip-components=1
tar -xzf %{SOURCE21} -C %{_builddir}/quickjs-wasi/quickjs-ng --strip-components=1
for t in clang clang++ llvm-ar wasm-ld; do ln -sf %{_bindir}/$t %{_builddir}/qjs-sdk/bin/$t; done
# The C interface must match the vendored JS exactly.
grep -q '"version": "3.6.2"' node_modules/quickjs-wasi/package.json
%make_build -C %{_builddir}/quickjs-wasi quickjs.wasm extensions/encoding/encoding.so extensions/headers/headers.so extensions/structured-clone/structured-clone.so extensions/crypto/crypto.so WASI_SDK=%{_builddir}/qjs-sdk SYSROOT=%{_datadir}/wasi-sysroot WASM_OPT=%{_bindir}/wasm-opt
cp -p %{_builddir}/quickjs-wasi/quickjs.wasm node_modules/quickjs-wasi/quickjs.wasm
for e in encoding headers structured-clone crypto; do install -D -m644 %{_builddir}/quickjs-wasi/extensions/$e/$e.so node_modules/quickjs-wasi/extensions/$e/$e.so; done

# Zero-length sources upstream never trimmed.
find . -type f -size 0 -delete

%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -a %{name}/. %{buildroot}%{nodejs_sitelib}/%{npm_name}/

install -d %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/dist/cli.js %{buildroot}%{_bindir}/pi

# Windows helpers and CI metadata from the dependency tree.
find %{buildroot}%{nodejs_sitelib} -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' \) -delete
find %{buildroot}%{nodejs_sitelib} -type d \
    \( -name '.github' -o -name '.bin' \) -prune -exec rm -rf {} +
# Linter/CI dotfiles, named explicitly: a blanket "-name '.*' -delete" also
# takes @earendil-works/pi-ai's dist/providers/data/.manifest.json, which is a
# runtime data file the provider catalogue imports.
# Some of these (.history) are directories in the dependency tree, so prune
# and rm -rf rather than -delete, which refuses a non-empty directory.
find %{buildroot}%{nodejs_sitelib} \
    \( -name '.editorconfig' -o -name '.eslintrc' -o -name '.eslintrc.cjs' \
    -o -name '.eslintrc.js' -o -name '.eslintignore' -o -name '.gitkeep' \
    -o -name '.history' -o -name '.keep' -o -name '.jscs.json' \
    -o -name '.jshintrc' -o -name '.npmignore' -o -name '.nvmrc' \
    -o -name '.package-lock.json' -o -name '.prettierignore' \
    -o -name '.prettierrc' -o -name '.prettierrc.json' \
    -o -name '.prettierrc.yaml' -o -name '.travis.yml' \
    -o -name '.yarnrc.yml' \) \
    -prune -exec rm -rf {} +

# npm publishes whole dependency trees mode 0755. Drop the execute bit
# everywhere, then restore it only for files that really are executable, and
# point their interpreter at the packaged node. The interpreter has to be
# matched properly rather than just testing for "#!": Rust sources in the
# dependency tree open with #![deny(clippy::all)], which a naive test marks
# executable and rpmlint then reports as a wrong-script-interpreter.
find %{buildroot}%{nodejs_sitelib} -type f -exec chmod a-x {} +
find %{buildroot}%{nodejs_sitelib} -type f -exec sh -c '
    for f; do
        if head -n1 "$f" | grep -qE "^#! ?/(usr/)?(bin|local/bin)/(env +)?(node|sh|bash)\\b"; then
            sed -i "1s|^#! *%{_bindir}/env  *node$|#!%{_bindir}/node|" "$f"
            chmod 0755 "$f"
        fi
    done' _ {} +

%fdupes %{buildroot}%{nodejs_sitelib}

%check
# pi writes its settings on startup, so it needs a writable HOME. --version
# exits before the migration and extension-loading paths, and performs no
# network access; --help would load extensions and is deliberately not used.
export HOME=%{_builddir}/fakehome
export PI_SKIP_VERSION_CHECK=1
export PI_TELEMETRY=0
mkdir -p "$HOME"
# The %%{_bindir} symlink is absolute and does not resolve inside the buildroot.
test "$(node %{buildroot}%{nodejs_sitelib}/%{npm_name}/dist/cli.js --version)" = "%{version}"

# The wasm runtime is built above: a script must evaluate to a real result,
# and every shipped extension must load and answer a basic call.
cd %{buildroot}%{nodejs_sitelib}/%{npm_name}
node --input-type=module -e '
import { QuickJS } from "./node_modules/quickjs-wasi/dist/index.js";
import { readFileSync } from "node:fs";
const dir = "./node_modules/quickjs-wasi";
const wasm = readFileSync(dir + "/quickjs.wasm");
const vm = await QuickJS.create({ wasm });
if (vm.dump(vm.evalCode("40 + 2")) !== 42) throw new Error("codemode wasm smoke failed");
vm.dispose();
const probes = {
  "encoding": "new TextDecoder().decode(new TextEncoder().encode(\"hi\"))",
  "headers": "new Headers({\"x-a\": \"1\"}).get(\"x-a\")",
  "structured-clone": "structuredClone({a: [1, 2]}).a[1]",
  "crypto": "crypto.getRandomValues(new Uint8Array(8)).length"
};
const wants = { "encoding": "hi", "headers": "1", "structured-clone": 2, "crypto": 8 };
for (const name of Object.keys(probes)) {
  const v = await QuickJS.create({ wasm, extensions: [{ name, wasm: readFileSync(dir + "/extensions/" + name + "/" + name + ".so") }] });
  if (v.dump(v.evalCode(probes[name])) !== wants[name]) throw new Error(name + " smoke failed");
  v.dispose();
}'

%files
# Marked in place rather than copied to %%{_docdir}: pi resolves README.md and
# CHANGELOG.md at runtime relative to its own package directory.
%license %{nodejs_sitelib}/%{npm_name}/LICENSE
%doc %{nodejs_sitelib}/%{npm_name}/README.md
%doc %{nodejs_sitelib}/%{npm_name}/CHANGELOG.md
%{_bindir}/pi
%dir %{nodejs_sitelib}
%dir %{nodejs_sitelib}/@earendil-works
%dir %{nodejs_sitelib}/%{npm_name}
%{nodejs_sitelib}/%{npm_name}/package.json
%{nodejs_sitelib}/%{npm_name}/dist
%{nodejs_sitelib}/%{npm_name}/docs
%{nodejs_sitelib}/%{npm_name}/node_modules
%{nodejs_sitelib}/%{npm_name}/schemas

%files examples
%dir %{nodejs_sitelib}
%dir %{nodejs_sitelib}/@earendil-works
%dir %{nodejs_sitelib}/%{npm_name}
%{nodejs_sitelib}/%{npm_name}/examples

%changelog
