#
# spec file for package git-bug
#
# Copyright (c) 2024 SUSE LLC
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


# The npm native build tools have only been validated on x86_64. Keep the
# CLI available elsewhere; enable other architectures after testing them.
%ifarch x86_64
%bcond_without webui
%else
%bcond_with webui
%endif

Name:           git-bug
Version:        0.11.0
Release:        0
Summary:        Distributed, offline-first bug tracker embedded in git, with bridges
%if %{with webui}
# Conservative union of the frontend production dependency licenses. The
# notices collector includes dependencies even when Vite tree-shakes them.
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC-BY-4.0 AND ISC AND MIT AND OFL-1.1 AND Python-2.0 AND Unlicense
%else
License:        MIT
%endif
URL:            https://github.com/MichaelMure/git-bug
Source0:        https://github.com/MichaelMure/%{name}/archive/refs/tags/v%{version}.tar.gz#/git-bug-%{version}.tar.gz
# Source0:        git-bug-%%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        package-lock.json
Source3:        webui-package.json
Source4:        node_modules.spec.inc
Source5:        test-webui.py
Source6:        node-sources.json
Source7:        pnpm-to-obs.py
Source8:        prepare-webui-lock.py
Source9:        test_pnpm_to_obs.py
Source10:       test_prepare_webui_lock.py
Source11:       webui-lock-report.json
Source12:       WEBUI-PACKAGING.md
Source13:       collect-webui-licenses.py
Source14:       test_collect_webui_licenses.py
BuildRequires:  git
BuildRequires:  golang(API) >= 1.26
BuildRequires:  golang-packaging
%if %{with webui}
# OBS/osc unpacks node_modules.obscpio into the source directory. This include
# declares its npm tarballs as individual sources for the source RPM.
%include %{_sourcedir}/node_modules.spec.inc
# The npm esbuild wrapper requires an executable with the identical version.
BuildRequires:  esbuild = 0.28.2
BuildRequires:  local-npm-registry >= 1.1.0
BuildRequires:  nodejs24
BuildRequires:  npm24
BuildRequires:  python3-base
%endif

%description
git-bug is a bug tracker that:

* is fully embedded in git: you only need your git repository to have
  a bug tracker
* is distributed: use your normal git remote to collaborate, push and
  pull your bugs!
* works offline: in a plane or under the sea? Keep reading and
  writing bugs!
* prevents vendor lock-in: your usual service is down or went bad?
  You already have a full backup.
* is fast: listing bugs or opening them is a matter of
  milliseconds
* doesn't pollute your project: no files are added in your
  project
* integrates with your tooling: use the UI you like (CLI,
  terminal, web) or integrate with your existing tools through
  the CLI or the GraphQL API
* bridges to other bug trackers: use bridges to import and export
  to other trackers.

%package bash-completion
Summary:        Bash completion for git-bug
Requires:       bash-completion
Requires:       %{name} = %{version}
Supplements:    (git-bug and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for git-bug

%package fish-completion
Summary:        Fish completion for git-bug
Requires:       fish
Requires:       %{name} = %{version}
Supplements:    (git-bug and fish)
BuildArch:      noarch

%description fish-completion
Fish shell completions for git-bug

%package zsh-completion
Summary:        ZSH completion for git-bug
Group:          Productivity/File utilities
Requires:       zsh
Requires:       %{name} = %{version}
Supplements:    (git-bug and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for git-bug

%prep
%autosetup -p1 -a1
%if %{with webui}
# Use the npm-generated installation tree, not the service download inventory.
cp %{SOURCE2} webui/package-lock.json
cp %{SOURCE3} webui/package.json
%endif

%build
export GOTOOLCHAIN=local
export GOPROXY=off
export GOSUMDB=off
export GOFLAGS="-mod=vendor -buildmode=pie"
%if %{with webui}
# Keep npm configuration and caches inside the build tree. All dependencies
# come from source tarballs served over loopback; disable install scripts.
export npm_config_cache="$PWD/.npm-cache"
export npm_config_userconfig="$PWD/.npmrc"
export npm_config_globalconfig="$PWD/.npmrc-global"
export npm_config_update_notifier=false
export NODE_OPTIONS="--max-old-space-size=1536"
export ESBUILD_BINARY_PATH="$(command -v esbuild)"
test -x "$ESBUILD_BINARY_PATH"
pushd webui
local-npm-registry %{_sourcedir} ci \
    --include=dev --ignore-scripts --legacy-peer-deps \
    --no-audit --no-fund --maxsockets=2
npm run build
test -s dist/index.html.gz
popd
python3 %{SOURCE13} webui webui-licenses
go build -tags webui
%else
go build
%endif

%install
install -Dm755 git-bug %{buildroot}%{_bindir}/git-bug
install -Dm644 -t %{buildroot}%{_mandir}/man1/ doc/man/*

# shell completions
install -Dm0644 misc/completion/bash/git-bug  \
    %{buildroot}%{_datadir}/bash-completion/completions/git-bug
install -Dm0644 misc/completion/fish/git-bug  \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/git-bug.fish
install -Dm0644 misc/completion/zsh/git-bug  \
    %{buildroot}%{_sysconfdir}/zsh_completion.d/git-bug

%check
export GOTOOLCHAIN=local
export GOPROXY=off
export GOSUMDB=off
export GOFLAGS="-mod=vendor -buildmode=pie"
# The full suite includes network-dependent bridge tests (gh#git-bug/git-bug#1313).
# Run the offline Web UI handler tests without suppressing failures.
%if %{with webui}
go test -v -tags webui ./webui
python3 %{SOURCE5} ./git-bug
%else
go test -v ./webui
%endif

%files
%license LICENSE
%if %{with webui}
%license webui-licenses
%endif
%doc README.md
%{_bindir}/git-bug
%{_mandir}/man1/git*.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/git-bug

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/git-bug.fish

%files zsh-completion
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/git-bug

%changelog
