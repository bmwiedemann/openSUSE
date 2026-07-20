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


# The internal node dependency generator would slurp package.json and emit
# bogus npm(...) Provides/Requires; the published bundle has no dependency tree.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
%define node_pty_version 1.1.0
%define node_addon_api_version 7.1.1
Name:           kimi-code
Version:        0.27.0
Release:        0
Summary:        Command-line agentic coding assistant powered by Kimi models
License:        MIT
URL:            https://github.com/MoonshotAI/kimi-code
# The published npm artifact is a self-contained, dependency-free bundle
# (dist/main.mjs). Only the optional native node-pty backend is vendored below.
Source0:        https://registry.npmjs.org/@moonshot-ai/%{name}/-/%{name}-%{version}.tgz
Source1:        https://registry.npmjs.org/node-pty/-/node-pty-%{node_pty_version}.tgz
Source2:        https://registry.npmjs.org/node-addon-api/-/node-addon-api-%{node_addon_api_version}.tgz
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
# kimi-code itself is installed straight from its npm tarball during install;
# only the vendored node-pty sources need unpacking here in order to compile.
%setup -q -c -T
# Source1: node-pty -> ./package
tar -xf %{SOURCE1}
mv package node-pty
# Source2: node-addon-api -> ./package
tar -xf %{SOURCE2}
mv package node-addon-api

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
# Install the self-contained kimi-code bundle from its npm tarball. Installing
# from the .tgz (not an unpacked dir) makes npm copy the tree into the buildroot
# instead of symlinking it; --omit=optional keeps npm from reaching out for the
# optional node-pty / clipboard packages.
npm_config_prefix=%{buildroot}%{_prefix} \
    npm install -g --omit=optional --offline %{SOURCE0}

# Locate the installed package tree (scoped package under nodejs_sitelib).
kimidir=$(dirname "$(find %{buildroot}%{nodejs_sitelib} -name main.mjs -path '*kimi-code*' | head -n1)")
kimiroot=$(dirname "$kimidir")

# Inject the freshly compiled node-pty so `import("node-pty")` resolves.
install -d "$kimiroot/node_modules/node-pty/build/Release"
cp -a node-pty/lib "$kimiroot/node_modules/node-pty/lib"
cp -a node-pty/package.json "$kimiroot/node_modules/node-pty/package.json"
# Only pty.node is needed on Linux; spawn-helper is a macOS-only path in
# node-pty's binding.gyp and pty.cc (the Linux fork path uses forkpty(3) and
# never execs the helper), so it is neither built nor referenced at runtime here.
cp -a node-pty/build/Release/pty.node "$kimiroot/node_modules/node-pty/build/Release/"

# Use a concrete node interpreter (openSUSE convention) rather than /usr/bin/env.
# kimidir is the dist/ directory that directly contains main.mjs.
sed -i '1s|^#!%{_bindir}/env node|#!%{_bindir}/node|' "$kimidir/main.mjs"

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
%{buildroot}%{_bindir}/kimi --version

%files
%{_bindir}/kimi
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/@moonshot-ai/

%changelog
