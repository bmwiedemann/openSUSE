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
%define ws_version 8.21.3
%define qrcode_version 1.5.4
%define pngjs_version 5.0.0
%define dijkstrajs_version 1.0.3
%define chokidar_version 4.0.3
%define readdirp_version 4.1.2
# Commit of the @moonshot-ai/kimi-code@2.4.1 release tag the NAPI helper
# sources below are vendored from (tag object 1fc1d165c83b175873a46897e1e9db73dc70c984).
%define pi_tui_git 2c73f3f50af4fa7f2540ca0d2e33b07a1408e3a7
Name:           kimi-code
Version:        2.4.1
Release:        0
Summary:        Command-line agentic coding assistant powered by Kimi models
License:        MIT
URL:            https://github.com/MoonshotAI/kimi-code
# The published npm artifact is a prebuilt bundle (dist/main.mjs). Since 0.39.0
# it no longer inlines ws and qrcode, so those - plus qrcode's own runtime
# dependencies - are vendored below. Since 2.3.0 the bundle also imports
# chokidar externally (file watching), so it and its own dependency readdirp
# are vendored too. The node-pty backend went away upstream in 2.4.0
# (session terminal service removed). The NAPI clipboard helper upstream only
# ships as prebuilt .node files is compiled from source in %build instead.
# Repacked npm tarball: package/native (6 prebuilt .node files for
# darwin/linux/win32 on x64+arm64) is deleted; the darwin/win32 legs never
# load on Linux and only the Linux leg is rebuilt.
# Recipe: gunzip the registry tarball, tar --delete -f it package/native,
# gzip -9 it again.
# https://registry.npmjs.org/@moonshot-ai/kimi-code/-/kimi-code-2.4.1.tgz
Source0:        kimi-code-%{version}.tgz
Source1:        https://registry.npmjs.org/ws/-/ws-%{ws_version}.tgz
Source2:        https://registry.npmjs.org/qrcode/-/qrcode-%{qrcode_version}.tgz
Source3:        https://registry.npmjs.org/pngjs/-/pngjs-%{pngjs_version}.tgz
Source4:        https://registry.npmjs.org/dijkstrajs/-/dijkstrajs-%{dijkstrajs_version}.tgz
Source5:        https://registry.npmjs.org/chokidar/-/chokidar-%{chokidar_version}.tgz
Source6:        https://registry.npmjs.org/readdirp/-/readdirp-%{readdirp_version}.tgz
# Linux NAPI helper sources from the private @moonshot-ai/pi-tui workspace
# package (never published to the registry), pinned to the release tag above.
Source10:       https://raw.githubusercontent.com/MoonshotAI/kimi-code/%{pi_tui_git}/packages/pi-tui/native/napi.h
Source11:       https://raw.githubusercontent.com/MoonshotAI/kimi-code/%{pi_tui_git}/packages/pi-tui/native/clipboard.h
Source12:       https://raw.githubusercontent.com/MoonshotAI/kimi-code/%{pi_tui_git}/packages/pi-tui/native/linux/src/linux-platform-x11.c
Source13:       https://raw.githubusercontent.com/MoonshotAI/kimi-code/%{pi_tui_git}/packages/pi-tui/native/linux/src/clipboard-worker.h
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  nodejs >= 22.19
BuildRequires:  nodejs-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
Requires:       fd
Requires:       nodejs >= 22.19
Requires:       ripgrep
# Only the dependencies that are shipped as separate trees are listed here;
# dist/main.mjs is a prebuilt bundle whose inlined build-time dependencies
# cannot be enumerated from the published artifact.
Provides:       bundled(chokidar) = %{chokidar_version}
Provides:       bundled(dijkstrajs) = %{dijkstrajs_version}
Provides:       bundled(pngjs) = %{pngjs_version}
Provides:       bundled(qrcode) = %{qrcode_version}
Provides:       bundled(readdirp) = %{readdirp_version}
Provides:       bundled(ws) = %{ws_version}
# Only the Linux arches are built: the NAPI helper is compiled from source in
# %build, and the darwin/win32 prebuilds never load on Linux.
ExclusiveArch:  x86_64 aarch64

%description
Kimi Code is Moonshot AI's command-line coding agent: an interactive terminal
assistant for software-engineering tasks, driven by the Kimi family of models.

It bundles a prebuilt web dashboard and shells out to ripgrep and fd for fast
code search.

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
unpack_npm %{SOURCE1} ws
unpack_npm %{SOURCE2} qrcode
unpack_npm %{SOURCE3} pngjs
unpack_npm %{SOURCE4} dijkstrajs
unpack_npm %{SOURCE5} chokidar
unpack_npm %{SOURCE6} readdirp
chmod -R a+rX,u+w,go-w .

%build
# The Linux NAPI clipboard helper, compiled from source. Upstream ships it
# only as prebuilt .node files (packages/pi-tui/native in the unpublished
# pi-tui workspace package); the Linux helper is a single C11 file using
# only libxcb, with the small N-API surface node provides declared in the
# vendored napi.h. Flags mirror upstream's native/linux/build.sh.
mkdir -p pi-tui-native/native/linux/src
cp %{SOURCE10} pi-tui-native/native/napi.h
cp %{SOURCE11} pi-tui-native/native/clipboard.h
cp %{SOURCE12} pi-tui-native/native/linux/src/linux-platform-x11.c
cp %{SOURCE13} pi-tui-native/native/linux/src/clipboard-worker.h
cc %{optflags} -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Werror \
    -fPIC -pthread -fvisibility=hidden -fno-stack-protector -shared -nostdlib \
    -Wl,--unresolved-symbols=ignore-all -Wl,--no-as-needed -Wl,--gc-sections \
    -Wl,-z,nodelete pi-tui-native/native/linux/src/linux-platform-x11.c \
    -lxcb -o linux-platform-x11.node

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
cp -a ws qrcode pngjs dijkstrajs chokidar readdirp "$kimiroot/node_modules/"
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

# Use a concrete node interpreter (openSUSE convention) rather than /usr/bin/env.
sed -i '1s|^#!%{_bindir}/env node|#!%{_bindir}/node|' "$kimiroot/dist/main.mjs"
chmod 0755 "$kimiroot/dist/main.mjs"
install -d %{buildroot}%{_bindir}
ln -sr "$kimiroot/dist/main.mjs" %{buildroot}%{_bindir}/kimi

# Drop npm lifecycle postinstall scripts: they only migrate a legacy python
# shim at npm-install time and are unused by the packaged CLI.
rm -rf "$kimiroot/scripts"

# Install the from-source NAPI helper where the inlined pi-tui loader looks
# for it: <kimiroot>/native/<platform>/prebuilds/<platform>-<arch>/. Only the
# Linux leg is built (ExclusiveArch); darwin/win32 never load on Linux and
# the repacked tarball ships no prebuilds at all.
case "%{_target_cpu}" in
    x86_64) nativearch="x64" ;;
    aarch64) nativearch="arm64" ;;
esac
install -D -m 0755 linux-platform-x11.node "$kimiroot/native/linux/prebuilds/linux-$nativearch/linux-platform-x11.node"
find %{buildroot}%{nodejs_sitelib} -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' -o -name '*.pdb' \) -delete

%fdupes %{buildroot}%{nodejs_sitelib}

%check
# Starting the CLI evaluates dist/main.mjs, whose top-level imports of ws and
# qrcode fail loudly if the vendored trees are missing or incomplete.
%{buildroot}%{_bindir}/kimi --version
# The from-source NAPI helper must load and export the clipboard surface the
# smoke path (KIMI_CODE_NATIVE_ASSET_SMOKE=1) requires of the Linux prebuild.
node -e "const h = require('%{buildroot}%{nodejs_sitelib}/@moonshot-ai/kimi-code/native/linux/prebuilds/linux-' + (process.arch === 'arm64' ? 'arm64' : 'x64') + '/linux-platform-x11.node'); if (typeof h.getText !== 'function' || typeof h.getImage !== 'function') throw new Error('unexpected native helper exports')"

%files
%{_bindir}/kimi
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/@moonshot-ai/

%changelog
