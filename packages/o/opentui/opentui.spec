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
%global zig_version 0.15.2
# The npm names for the platform the native library is built for. OpenTUI
# resolves it as @opentui/core-<platform>-<arch>/libopentui.so, using Node's
# names for both, not the RPM ones.
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
Name:           opentui
Version:        0.4.5
Release:        0
Summary:        Library for building terminal user interfaces
# OpenTUI itself is MIT. miniaudio is vendored as a single header in
# packages/core/src/zig/vendor and is dual licensed; yoga and uucode are
# pulled in as Zig dependencies and are both MIT.
License:        MIT AND (Unlicense OR MIT-0)
URL:            https://opentui.com
Source0:        https://github.com/anomalyco/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# The two Zig dependencies, prepared for an offline build by opentui_zigdeps.
Source1:        %{name}-zig-deps-%{version}.tar.zst
Source2:        opentui_zigdeps
Source3:        README.SUSE-maint
# Ask the linker for a build ID, without which rpm cannot split a debuginfo
# package off the library.
Patch0:         opentui-build-id.patch
# Without this the library is generated for whatever CPU the build worker has
# and SIGILLs on older machines of the same architecture.
Patch1:         opentui-baseline-cpu.patch
BuildRequires:  binutils
BuildRequires:  python3-base
BuildRequires:  zig = %{zig_version}
BuildRequires:  zstd
Provides:       bundled(miniaudio) = 0.11.24
Provides:       bundled(uucode) = 0.1.0
Provides:       bundled(yoga) = 3.2.1
# Upstream supports no other architecture: SUPPORTED_TARGETS in
# packages/core/src/zig/build.zig lists only x86_64 and aarch64.
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

%description    devel
The TypeScript half of OpenTUI: the core bindings, the keymap library and
the SolidJS renderer.

OpenTUI is consumed as TypeScript, not as a compiled artifact - a program
using it bundles these sources into itself with its own bundler. So this is
what you build against, and nothing installs it to run.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}

%build
# Zig resolves the entries in build.zig.zon over the network unless --system
# points it at a directory of already-unpacked packages, which is what
# Source1 is. Both caches have to be inside the build directory as well, or
# Zig writes to $HOME.
export ZIG_GLOBAL_CACHE_DIR="$PWD/.zig-global-cache"
export ZIG_LOCAL_CACHE_DIR="$PWD/.zig-local-cache"
zig_deps="$PWD/deps"

cd packages/core/src/zig
# -Dtarget=native keeps the host's libc and libstdc++, which is what a
# distribution build wants. What it must not keep is the host's CPU model -
# see Patch1.
zig build \
    --system "$zig_deps" \
    -Dtarget=native \
    -Doptimize=ReleaseFast \
    --verbose

%install
install -d %{buildroot}%{_libdir}/%{name}/%{native_pkg}
install -m 0755 packages/core/src/zig/lib/native/libopentui.so \
    %{buildroot}%{_libdir}/%{name}/%{native_pkg}/libopentui.so

# The whole point of the explicit -Dtarget above. If a rebase ever puts a
# host-detected CPU model back, catch it here rather than in a bug report from
# somebody with an older machine.
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

# The TypeScript, laid out so that a consumer can point at
# %%{_libdir}/%%{name} and have @opentui/* resolve, or set
# OTUI_ASSET_ROOT to it and have the native library resolve. None of these
# packages declares a files field, so npm would ship the whole directory;
# copy it wholesale and then drop what only serves upstream's own build. Note
# that src/testing.ts and src/testing are exported API and stay, while
# src/tests is the suite and goes.
for pkg in core keymap solid; do
    cp -a packages/$pkg %{buildroot}%{_libdir}/%{name}/@opentui/
    ( cd %{buildroot}%{_libdir}/%{name}/@opentui/$pkg
      rm -rf src/zig src/tests src/benchmark tests examples \
             dev docs bench-before bench-after node_modules \
             tsconfig.json tsconfig.build.json tsconfig.node-test.json
      # scripts/ is mostly upstream's own build and release plumbing, but in
      # solid it also holds four modules the exports map points at, so drop
      # the plumbing by name rather than the directory.
      rm -f scripts/build.ts scripts/publish.ts scripts/dist-test.ts \
            scripts/standalone-test.ts scripts/test.ts scripts/test-node.ts \
            scripts/test-node-hook.mjs scripts/test-packed-consumer.ts
      rmdir scripts 2>/dev/null || :
      find . -name '*.test.ts' -delete
      find . -name '.gitignore' -delete
      # A couple of modules are exported API that also run themselves as a
      # CLI under import.meta.main, so they carry a bun shebang. Nothing here
      # is meant to be executed in place, and leaving the shebang on would
      # have rpm demand an interpreter the distribution does not have yet.
      grep -rlZ '^#!/usr/bin/env ' --include='*.ts' . \
          | xargs -0 -r sed -i '1{/^#!/d}'
      # workspace:* only means anything inside upstream's monorepo. These
      # packages are installed side by side, so pin the sibling to the
      # version that is actually here, which is what npm publish would do.
      sed -i 's/"workspace:\*"/"%{version}"/g' package.json )
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
zig_deps="$PWD/deps"
cd packages/core/src/zig
zig build test \
    --system "$zig_deps" \
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
