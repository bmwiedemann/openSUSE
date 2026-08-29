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
Version:        0.84.4
Release:        0
Summary:        Minimal terminal coding agent
# Legal-Review-Notice: pi itself is MIT. The 135 vendored dependencies are
# MIT (68), Apache-2.0 (44), BSD-3-Clause (13), ISC (7), BlueOak-1.0.0 (2)
# and 0BSD (1); every dependency declares a license. The tag below is the
# union of all of them.
License:        0BSD AND Apache-2.0 AND BSD-3-Clause AND BlueOak-1.0.0 AND ISC AND MIT
URL:            https://github.com/earendil-works/pi
Source0:        https://registry.npmjs.org/%{npm_name}/-/pi-coding-agent-%{version}.tgz
# The npm tarball ships no license file; taken from the upstream git tag.
Source1:        LICENSE
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
Source13:       %{name}-rpmlintrc
Patch0:         pi-disable-self-update.patch
# PATCH-FIX-OPENSUSE pi-use-modular-runtime.patch mpluskal@suse.com -- point bin and the rpc-entry export at the modular runtime we ship and patch, not at the pre-bundled copy
Patch1:         pi-use-modular-runtime.patch
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
BuildRequires:  nodejs >= 22.19.0
BuildRequires:  nodejs-packaging
Requires:       nodejs >= 22.19.0
Recommends:     %{name}-examples = %{version}-%{release}
# The bundled native clipboard addon is dropped (see %%build), so clipboard
# support comes from pi's own fallback to these command line tools.
Recommends:     wl-clipboard
Recommends:     xclip
# cln builds an unrelated Archimedes' constant demo from its own pi.cc and
# installs it as /usr/bin/pi next to libcln.so, so the two cannot be
# co-installed. Upstream cln's "make install" does not ship that binary.
Conflicts:      cln
# dist/core/export-html/vendor/highlight.min.js and marked.min.js are embedded
# verbatim into the standalone HTML that "pi export" produces, so they cannot
# be unbundled.
Provides:       bundled(highlight.js)
Provides:       bundled(marked)
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

# Source maps (5.9 MB) and TypeScript declarations (1 MB) are of no use in a
# runtime package and there is no -devel consumer for a CLI.
find dist -name '*.map' -delete
find dist -name '*.d.ts' -delete

# Documentation screenshots, useless for a terminal application.
rm -rf docs/images

# The 7.1 MB pre-bundled runtime added in 0.84.3. Patch1 points bin and the
# rpc-entry export back at the modular tree, so nothing references this any
# more, and it carries an unpatched second copy of detectInstallMethod() that
# pi-disable-self-update.patch cannot reach.
rm -rf dist/bundle

# The doom-overlay example ships doom.wasm/doom.js built from doomgeneric,
# which is derived from the GPL-2.0 id Software Doom sources -- the complete
# corresponding source is not in this package, and the extension downloads a
# non-redistributable shareware WAD on first run.
rm -rf examples/extensions/doom-overlay

# Upstream's own shrinkwrap omits the integrity field for the six
# @earendil-works/* sibling packages, which the node_modules source service
# rejects; Source10 is the same file with those hashes filled in. It must stay
# in place for the install below, or npm re-resolves from package.json and
# reaches for devDependencies that are deliberately not vendored.
cp -p %{SOURCE10} npm-shrinkwrap.json

# That shrinkwrap is production-only, so it does not list the devDependencies
# that package.json still declares. npm treats the pair as out of sync and
# re-resolves the whole tree from package.json -- reaching for @types/* that
# are deliberately not vendored -- even under --omit=dev. dist/ is shipped
# prebuilt and nothing here compiles or runs the upstream test suite, so drop
# the devDependencies and let the two agree.
npm pkg delete devDependencies

%build
cd %{name}
local-npm-registry %{_sourcedir} install --omit=dev --ignore-scripts
rm -f npm-shrinkwrap.json package-lock.json

# Prebuilt binaries with no corresponding source. pi-tui/native holds only
# darwin and win32 .node addons, which are never loaded on Linux. photon-node
# is loaded lazily behind a try/catch and only powers image conversion, so it
# degrades gracefully.
rm -rf node_modules/@earendil-works/pi-tui/native
rm -f node_modules/@silvia-odwyer/photon-node/photon_rs_bg.wasm

# @mariozechner/clipboard resolves to a per-architecture prebuilt .node addon,
# which would make the payload of this noarch package differ between build
# hosts. It is an optionalDependency, loadClipboardNative() already wraps the
# require in try/catch, and dist/utils/clipboard.js falls back to xclip and
# wl-copy/wl-paste, so dropping it costs nothing on a Linux desktop.
rm -rf node_modules/@mariozechner/clipboard*

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

%files examples
%dir %{nodejs_sitelib}
%dir %{nodejs_sitelib}/@earendil-works
%dir %{nodejs_sitelib}/%{npm_name}
%{nodejs_sitelib}/%{npm_name}/examples

%changelog
