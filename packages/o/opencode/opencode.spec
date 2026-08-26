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
# Node's names for the platform, not RPM's: the build target is derived from
# them, and @opentui/core resolves its native library by the same names.
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
Name:           opencode
Version:        1.18.23
Release:        0
Summary:        AI coding agent for the terminal
# opencode itself is MIT. The npm dependency tree is compiled into the
# executable, so its licences are part of the binary; see README.SUSE-maint
# for how the expression below is derived and rechecked on a bump.
# Legal-Review-Notice: rederived for 1.18.23 from the declared license field
# of all 509 unique packages in the vendor tarball (512 store entries). No
# copyleft of any kind. The SPDX set is unchanged from 1.18.19. Two
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
# Upstream's build script fails unless bun satisfies a caret range around the
# version it pins. It pins 1.3.14 and Factory has 1.4.0, so the check passes
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
# No floor. Which bun upstream wants changes with every release and Patch0
# turns a mismatch into a warning; a floor here would be a guess at which
# older bun still works, and the package is a git snapshot anyway, so
# 1.4.0~git sorts below 1.4.0.
BuildRequires:  bun
# %%prep reads the @opentui/core pin out of package.json.
BuildRequires:  python3-base
BuildRequires:  zstd
Requires:       git-core
# Native TUI library, loaded at runtime (not compiled into the binary).
# Equality because the FFI ABI is private and unversioned.
Requires:       opentui = %{opentui_version}
# Downloaded on first use otherwise; opencode shells out to it for grep.
Requires:       ripgrep
# bun only supports these two, and so do the prebuilt native modules left in
# the dependency tree.
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

%build
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

cd packages/opencode
# --single builds only the host platform. --skip-embed-web-ui leaves out the
# browser interface, which needs another 101 npm packages and embeds two fonts
# that ship without a licence.
bun run ./script/build.ts --single --skip-install --skip-embed-web-ui

%install
install -Dpm 0755 packages/opencode/dist/%{name}-linux-%{node_arch}/bin/%{name} \
    %{buildroot}%{_bindir}/%{name}

%check
# The executable carries its own runtime and payload; if anything stripped or
# truncated it, it does not get this far.
%{buildroot}%{_bindir}/%{name} --version
test "$(%{buildroot}%{_bindir}/%{name} --version)" = "%{version}"

%files
%license LICENSE licenses/LICENSE.caniuse-lite
%doc README.md README.SUSE-maint
%{_bindir}/%{name}

%changelog
