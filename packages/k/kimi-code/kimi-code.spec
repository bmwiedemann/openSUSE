#
# spec file for package kimi-code
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


# The internal node dependency generator would slurp the bundled package.json
# files and emit bogus npm(...) Provides/Requires; everything the CLI needs at
# runtime is vendored below.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
%define node_pty_version 1.1.0
%define node_addon_api_version 7.1.1
%define ws_version 8.21.3
%define qrcode_version 1.5.4
%define pngjs_version 5.0.0
%define dijkstrajs_version 1.0.3
Name:           kimi-code
Version:        0.42.0
Release:        0
Summary:        Command-line agentic coding assistant powered by Kimi models
License:        MIT
URL:            https://github.com/MoonshotAI/kimi-code
# The published npm artifact is a prebuilt bundle (dist/main.mjs). Since 0.39.0
# it no longer inlines ws and qrcode, so those - plus qrcode's own runtime
# dependencies - are vendored alongside the optional native node-pty backend.
Source0:        https://registry.npmjs.org/@moonshot-ai/%{name}/-/%{name}-%{version}.tgz
Source1:        https://registry.npmjs.org/node-pty/-/node-pty-%{node_pty_version}.tgz
Source2:        https://registry.npmjs.org/node-addon-api/-/node-addon-api-%{node_addon_api_version}.tgz
Source3:        https://registry.npmjs.org/ws/-/ws-%{ws_version}.tgz
Source4:        https://registry.npmjs.org/qrcode/-/qrcode-%{qrcode_version}.tgz
Source5:        https://registry.npmjs.org/pngjs/-/pngjs-%{pngjs_version}.tgz
Source6:        https://registry.npmjs.org/dijkstrajs/-/dijkstrajs-%{dijkstrajs_version}.tgz
Source99:       kimi-code-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs-devel >= 22.19
BuildRequires:  nodejs-packaging
BuildRequires:  npm
BuildRequires:  python3
Requires:       fd
Requires:       nodejs >= 22.19
Requires:       ripgrep
# Only the dependencies that are shipped as separate trees are listed here;
# dist/main.mjs is a prebuilt bundle whose inlined build-time dependencies
# cannot be enumerated from the published artifact.
Provides:       bundled(dijkstrajs) = %{dijkstrajs_version}
Provides:       bundled(node-addon-api) = %{node_addon_api_version}
Provides:       bundled(node-pty) = %{node_pty_version}
Provides:       bundled(pngjs) = %{pngjs_version}
Provides:       bundled(qrcode) = %{qrcode_version}
Provides:       bundled(ws) = %{ws_version}
# node-pty compiles a native addon; the pure-JS bundle is otherwise portable, but
# only these arches are verified/relevant for the coding-agent workload.
ExclusiveArch:  x86_64 aarch64

%description
Kimi Code is Moonshot AI's command-line coding agent: an interactive terminal
assistant for software-engineering tasks, driven by the Kimi family of models.

It bundles a prebuilt web dashboard and shells out to ripgrep and fd for fast
code search. The interactive shell backend is provided by a compiled node-pty
addon.

%prep
%setup -q -c -T
# Every Source is an npm tarball with a single top-level package/ directory.
# pngjs ships mode-0666 directory entries, so restore directory permissions
# only after extraction and normalise the modes afterwards.
unpack_npm() {
    rm -rf package
    tar -xf "$1" --delay-directory-restore
    mv package "$2"
}
unpack_npm %{SOURCE0} kimi-code
unpack_npm %{SOURCE1} node-pty
unpack_npm %{SOURCE2} node-addon-api
unpack_npm %{SOURCE3} ws
unpack_npm %{SOURCE4} qrcode
unpack_npm %{SOURCE5} pngjs
unpack_npm %{SOURCE6} dijkstrajs
chmod -R a+rX,u+w,go-w .

%build
# Compile the node-pty native addon fully offline.
# node-pty's binding.gyp resolves node-addon-api via require(), so place it
# where node-pty's own module resolution will find it.
mkdir -p node-pty/node_modules
cp -a node-addon-api node-pty/node_modules/node-addon-api
# node-gyp ships bundled inside npm; locate it rather than assuming it is on PATH.
node_gyp=$(find %{_prefix}/lib %{_libdir} -type f \
    -path '*node-gyp/bin/node-gyp.js' 2>/dev/null | head -n1)
pushd node-pty
export npm_config_nodedir=%{_prefix}
export npm_config_build_from_source=true
# scripts/prebuild.js only checks local files (no network); with
# build_from_source set it deletes the shipped darwin/win32 prebuilds and exits
# non-zero, so build the Linux addon (pty.node + spawn-helper) from source here.
node "$node_gyp" rebuild --nodedir=%{_prefix}
popd

%install
# The bundle is installed by hand rather than with `npm install`: since 0.39.0
# kimi-code declares runtime dependencies, so npm resolves them against the
# registry (and drags in qrcode's CLI-only yargs tree) instead of using the
# vendored copies below.
kimiroot=%{buildroot}%{nodejs_sitelib}/@moonshot-ai/%{name}
install -d %{buildroot}%{nodejs_sitelib}/@moonshot-ai
cp -a kimi-code "$kimiroot"

# Vendor the declared runtime dependencies into the package's own node_modules.
install -d "$kimiroot/node_modules"
cp -a ws qrcode pngjs dijkstrajs "$kimiroot/node_modules/"
# qrcode's bin/qrcode is the sole consumer of yargs and is not a supported entry
# point here; dropping it keeps that dependency out of the package.
rm -rf "$kimiroot/node_modules/qrcode/bin"
rm -rf "$kimiroot/node_modules/pngjs/coverage"
rm -rf "$kimiroot/node_modules/dijkstrajs/test"
# The vendored trees also carry linter/CI dotfiles, CRLF line endings and stray
# executable bits on plain library sources; rpmlint rejects all three.
find "$kimiroot/node_modules" -name '.*' -prune -exec rm -rf {} +
find "$kimiroot/node_modules" -type f -name '*.js' -exec chmod 0644 {} +
find "$kimiroot/node_modules" -type f -name '*.js' -exec sed -i 's/\r$//' {} +

# Inject the freshly compiled node-pty so `import("node-pty")` resolves.
install -d "$kimiroot/node_modules/node-pty/build/Release"
cp -a node-pty/lib "$kimiroot/node_modules/node-pty/lib"
cp -a node-pty/package.json "$kimiroot/node_modules/node-pty/package.json"
# Only pty.node is needed on Linux; spawn-helper is a macOS-only path in
# node-pty's binding.gyp and pty.cc (the Linux fork path uses forkpty(3) and
# never execs the helper), so it is neither built nor referenced at runtime here.
cp -a node-pty/build/Release/pty.node "$kimiroot/node_modules/node-pty/build/Release/"

# Use a concrete node interpreter (openSUSE convention) rather than /usr/bin/env.
sed -i '1s|^#!%{_bindir}/env node|#!%{_bindir}/node|' "$kimiroot/dist/main.mjs"
chmod 0755 "$kimiroot/dist/main.mjs"
install -d %{buildroot}%{_bindir}
ln -sr "$kimiroot/dist/main.mjs" %{buildroot}%{_bindir}/kimi

# Drop npm lifecycle postinstall scripts: they only migrate a legacy python
# shim at npm-install time and are unused by the packaged CLI.
rm -rf "$kimiroot/scripts"

# Strip non-Linux prebuilt addons shipped in the bundle (darwin/win32 only).
find %{buildroot}%{nodejs_sitelib} -type d -name 'darwin-*' -prune -exec rm -rf {} +
find %{buildroot}%{nodejs_sitelib} -type d -name 'win32-*' -prune -exec rm -rf {} +
find %{buildroot}%{nodejs_sitelib} -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' -o -name '*.pdb' \) -delete

%fdupes %{buildroot}%{nodejs_sitelib}

%check
# Starting the CLI evaluates dist/main.mjs, whose top-level imports of ws and
# qrcode fail loudly if the vendored trees are missing or incomplete.
%{buildroot}%{_bindir}/kimi --version
# node-pty is only reached through a dynamic import at runtime, so load the
# compiled addon explicitly to prove it works on this architecture.
node -e 'require("%{buildroot}%{nodejs_sitelib}/@moonshot-ai/%{name}/node_modules/node-pty")'

%files
%{_bindir}/kimi
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/@moonshot-ai/

%changelog
