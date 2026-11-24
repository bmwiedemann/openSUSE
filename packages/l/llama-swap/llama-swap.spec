#
# spec file for package llama-swap
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# document that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           llama-swap
Version:        275
Release:        0
Summary:        OpenAI-compatible proxy that hot swaps llama.cpp models on demand
License:        MIT
URL:            https://github.com/mostlygeek/llama-swap
# Source tarball of the release tag, see https://github.com/mostlygeek/llama-swap/releases
Source:         %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Go module dependencies, created by the go_modules source service (see _service)
Source1:        vendor.tar.gz
# Copy of ui/package-lock.json, input for the node_modules source service
Source2:        ui-package-lock.json
# npm dependencies for the UI, packed by ./update-npm-deps.sh from the output
# of the node_modules source service; osc cannot commit a directory, and the
# service downloads a .obscpio container or nothing at all
Source3:        node_modules.tar.gz
# Maintainer helper, not used by the build itself
Source4:        update-npm-deps.sh
# upstream ships binaries for amd64 and arm64 only, and the tailscale/gvisor
# dependencies do not build everywhere
ExclusiveArch:  x86_64 aarch64
BuildRequires:  gcc
BuildRequires:  golang(API) >= 1.27
BuildRequires:  local-npm-registry
BuildRequires:  nodejs >= 22
BuildRequires:  npm

%description
llama-swap sits in front of llama.cpp (or any compatible server binary) as an
OpenAI compatible API endpoint. Instead of starting one server per model, it
starts the server for whichever model a request asks for, unloads it when a
different model is requested, and keeps the endpoint, the API key and the port
unchanged while doing so.

A web UI on the same port manages the model list and shows activity. The
configuration is a YAML file, or a directory of them, so swapping models costs
a few seconds instead of a restart of the whole stack.

Run it with a config file, the example is in
/usr/share/doc/packages/llama-swap/config.example.yaml:

    llama-swap -config config.yaml

%prep
%autosetup -n %{name}-%{version} -p1 -a1
tar -xzf %{SOURCE3} -C %{_builddir}

# The lockfile in the tarball pins registry.npmjs.org URLs, which a build root
# cannot reach. local-npm-registry serves the tarballs of Source3 instead. They
# are the ones of ui-package-lock.json for linux on x86_64 and aarch64; the
# dependencies for other platforms are optional, npm installs without them.
cd ui
rm -rf node_modules package-lock.json
local-npm-registry %{_builddir}/node_modules install --include=dev --ignore-scripts
echo '{}' > package-lock.json

# The Makefile runs `npm ci` whenever the stamp file it keeps inside
# node_modules is older than package.json or the lockfile. Create it here so it
# uses what local-npm-registry just installed.
touch node_modules/.stamp

%build
# The upstream Makefile does the whole job: `ui` builds the web UI into
# internal/server/ui_dist (see ui/vite.config.ts) for the embed_ui build tag,
# `src` copies the sources without tests into internal/mcptools/sourcecode/_src
# for the embed_src tag, and `native` builds the binary with both. It has been
# usable from a release tarball since v275: without a .git directory it takes
# the commit hash from the .git-commit file that `git archive` filled in, and
# `src` falls back to find. GIT_VERSION still has to be passed because
# `git describe` cannot work here, and BUILD_DATE because upstream does not
# honour SOURCE_DATE_EPOCH.
#
# GOEXPERIMENT=nodwarf5 and no -trimpath are for the -debugsource package:
# debugedit rewrites only the source paths kept in .debug_line_str, while Go
# writes them as DW_FORM_string (sourceware.org bug 33204, golang/go#76630), and
# -trimpath records paths relative to the module, which are not on disk
# (sourceware.org bug 33823). With both out of the way, debugedit maps the build
# directory to /usr/src/debug and the sources are packaged. Fedora, Gentoo and
# Arch patch Go itself, openSUSE does not.
export CGO_ENABLED=1
export GOEXPERIMENT=nodwarf5
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/.gocache
make native \
    GIT_VERSION=v%{version} \
    BUILD_DATE="$(date -u -d "@${SOURCE_DATE_EPOCH:-0}" +'%Y-%m-%dT%H:%M:%SZ')"

# The Makefile names its output after Go's OS and architecture, keep the binary
# under a stable name.
install -D -m 0755 build/%{name}-$(go env GOOS)-$(go env GOARCH) bin/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 docs/config.example.yaml \
    %{buildroot}%{_defaultdocdir}/%{name}/config.example.yaml

%check
# the same environment as above, so that the packages built there are reused
export CGO_ENABLED=1
export GOEXPERIMENT=nodwarf5
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/.gocache

# upstream's own short test suite. It only talks to test servers on 127.0.0.1,
# so it runs in the build root, and it covers config.example.yaml against the
# shipped JSON schema
make test

# both the UI and the sources must have been embedded, and the version stamped
# in: without a git checkout the Makefile would fall back to "devel"
test -d internal/server/ui_dist
test -d internal/mcptools/sourcecode/_src
%{buildroot}%{_bindir}/%{name} -version | grep -F 'v%{version}'

# docs/config.example.yaml only documents the options and its models point at
# servers that are not there, so validate a minimal configuration instead
printf 'models:\n  test:\n    cmd: llama-server --port ${PORT} --model /dev/null\n' \
    > minimal-config.yaml
%{buildroot}%{_bindir}/%{name} -config minimal-config.yaml -validate

%files
%license LICENSE.md
%doc README.md
%doc %{_defaultdocdir}/%{name}/config.example.yaml
%{_bindir}/%{name}

%changelog
