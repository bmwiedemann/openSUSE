#
# spec file for package picsart-gen-ai
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


# Every runtime dependency is vendored in Source1, so the nodejs dependency
# generator must not turn package.json's "dependencies" into npm(...) Requires
# that nothing in the distribution provides.
%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
# The RPM is named after the service it talks to, but upstream's npm package,
# its tarball, the directory below %%{nodejs_sitelib} and the command itself
# are all called gen-ai. Everything that has to match upstream goes through
# %%{npm_name}, never %%{name}.
%define npm_name gen-ai
%define npm_scope @picsart
Name:           picsart-gen-ai
Version:        2.68.1
Release:        0
Summary:        Picsart AI CLI for generating images, video and audio
# Legal-Review-Notice: the CLI itself is MIT. The published cli.js is a bundle
# that additionally inlines @picsart/ai-sdk (MIT) and the unpublished
# @pulse/core and @pulse/server, which upstream distributes only inside this
# MIT-licensed artifact. Source1 vendors the 71 runtime dependencies the bundle
# imports; their licence fields were enumerated on this re-vendor and are MIT
# (63), ISC (5), Apache-2.0 (1), BlueOak-1.0.0 (1, the glob/minimatch family)
# and one "MIT OR CC0-1.0" satisfied by MIT. No copyleft is present.
License:        MIT AND ISC AND Apache-2.0 AND BlueOak-1.0.0
URL:            https://github.com/PicsArt/gen-ai-cli
Source0:        https://registry.npmjs.org/%{npm_scope}/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The npm artifact ships no licence file; this is upstream's LICENSE, taken
# from the git tag the release was built from.
Source2:        https://raw.githubusercontent.com/PicsArt/gen-ai-cli/v%{version}/LICENSE
# The upstream git tree cannot be built downstream: its tsup config inlines
# @pulse/core and @pulse/server, which live in a private registry and are not
# publishable to npm, so only the published bundle is buildable. Its runtime
# dependencies come via the node_modules OBS service: Source10 is regenerated
# per version in the unpacked Source0 directory with
#   npm install --package-lock-only --legacy-peer-deps --ignore-scripts
# and `osc service manualrun` then refreshes Source11 + node_modules.obscpio.
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       node_modules.sums
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
# The bundle refuses to start on anything older, see bin/gen-ai.mjs.
BuildRequires:  nodejs >= 22
BuildRequires:  nodejs-packaging
Requires:       nodejs >= 22
# The package was briefly called gen-ai in devel:tools before being renamed to
# name the service it is a client for; it never reached openSUSE:Factory. This
# replaces that copy for anyone who installed it from the devel project.
# Three deliberate details. The bound is frozen at the literal 2.60.1 rather
# than %%{version}: gen-ai only ever shipped that one version, so the set to
# obsolete is closed, and a bound that widened with every future release could
# silently remove an unrelated package that legitimately took the name later.
# It carries no release part, because gen-ai and this package build at the same
# release in the devel project and a release-qualified "<" would compare equal
# and never fire. And there is no matching Provides, because re-claiming the
# generic name in the solver would undo the rename, and nothing in OBS requires
# it; the rpmlint obsolete-not-provided warning is therefore intended.
Obsoletes:      gen-ai <= 2.60.1
BuildArch:      noarch
%include        %{_sourcedir}/node_modules.spec.inc

%description
gen-ai is Picsart's command line client for their generative AI service. It
generates and edits images, video and audio from the terminal, with an
interactive picker for models and parameters, batch re-runs of failed jobs and
a browsable history of previous generations.

Using it requires a Picsart account: the CLI is a client for a hosted API and
performs no generation locally.

%prep
%setup -q -c -T
tar -xf %{SOURCE0}
mv package %{npm_name}
cp -a %{SOURCE2} %{npm_name}/LICENSE
cp -a %{SOURCE10} %{npm_name}/package-lock.json

%build
# Nothing to compile: upstream publishes cli.js prebundled. Install the
# runtime dependency tree offline from the tarballs the node_modules
# service placed in the source directory.
cd %{npm_name}
local-npm-registry %{_sourcedir} install --omit=dev --ignore-scripts

%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_scope}/%{npm_name}
cp -a %{npm_name}/. %{buildroot}%{nodejs_sitelib}/%{npm_scope}/%{npm_name}/
install -d %{buildroot}%{_bindir}
# The command stays gen-ai even though the RPM does not: that is the name
# upstream's own documentation, npx invocations and shell completions use.
# Only the package name is service-qualified.
ln -s %{nodejs_sitelib}/%{npm_scope}/%{npm_name}/bin/%{npm_name}.mjs \
    %{buildroot}%{_bindir}/%{npm_name}
# Windows/CI leftovers that are never used on Linux.
find %{buildroot}%{nodejs_sitelib} -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' \) -delete
# Upstream CI metadata that npm ships inside the dependency tarballs, and
# npm's own bookkeeping (.bin helper symlinks, hidden lockfile copies).
find %{buildroot}%{nodejs_sitelib} -type d \( -name '.github' -o -name '.bin' \) -prune -exec rm -rf {} +
find %{buildroot}%{nodejs_sitelib} -type f -name '.*' -delete
# npm publishes whole dependency trees mode 0755, which makes rpmlint treat
# every README and JSON file as a script without a shebang. Drop the execute
# bit everywhere, then restore it only for files that really are executable,
# rewriting their interpreter to the concrete one openSUSE expects.
find %{buildroot}%{nodejs_sitelib} -type f -exec chmod a-x {} +
find %{buildroot}%{nodejs_sitelib} -type f -exec sh -c '
    for f; do
        if [ "$(head -c 2 "$f")" = "#!" ]; then
            sed -i "1s|^#!%{_bindir}/env node$|#!%{_bindir}/node|" "$f"
            chmod 0755 "$f"
        fi
    done' _ {} +
# Shipped through %%license/%%doc from the build directory instead, so they do
# not end up listed twice via the module directory below.
rm -f %{buildroot}%{nodejs_sitelib}/%{npm_scope}/%{npm_name}/LICENSE \
      %{buildroot}%{nodejs_sitelib}/%{npm_scope}/%{npm_name}/README.md
%fdupes %{buildroot}%{nodejs_sitelib}

%check
# The CLI stores its configuration below $HOME and would otherwise write into
# the build user's home directory.
export HOME=%{_builddir}/fakehome
mkdir -p "$HOME"
# Run the installed entry point directly: %%{_bindir}/%%{npm_name} is an
# absolute symlink and does not resolve inside the buildroot.
gen_ai=%{buildroot}%{nodejs_sitelib}/%{npm_scope}/%{npm_name}/bin/%{npm_name}.mjs
node "$gen_ai" --version
node "$gen_ai" --help > /dev/null

%files
%license %{npm_name}/LICENSE
%doc %{npm_name}/README.md
%{_bindir}/%{npm_name}
%dir %{nodejs_sitelib}
%dir %{nodejs_sitelib}/%{npm_scope}
%{nodejs_sitelib}/%{npm_scope}/%{npm_name}

%changelog
