#
# spec file for package zeroclaw
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

# Upstream default feature set (root Cargo.toml [features] default):
# agent-runtime + default-channels (channel-acp-server, channel-webhook,
# channel-email, channel-telegram, channel-discord, channel-filesystem) +
# acp-bridge, gateway, observability-prometheus, schema-export. Pinned
# explicitly so an upstream default change becomes a conscious spec
# decision instead of a silent closure change.
%define features agent-runtime,default-channels,acp-bridge,gateway,observability-prometheus,schema-export
Name:           zeroclaw
Version:        0.8.5
Release:        0
Summary:        Fast, small, and fully autonomous AI personal assistant infrastructure
# Legal-Review-Notice: Rust closure 406 crates (385 vendored + 21 workspace path) via cargo tree --offline -e normal -p zeroclaw --no-default-features --features agent-runtime,default-channels,acp-bridge,gateway,observability-prometheus,schema-export plus -p zerocode against vendor.tar.zst (update=false, matches Cargo.lock; 1255 vendor dirs = 1288 lock - 33 path); declared license + LICENSE files audited, only copyleft linked is option-ext 0.2.0 MPL-2.0 via dirs-sys/directories (AND; vendor.tar.zst in src.rpm satisfies MPL-2.0 Sec.3.2) and self_cell 1.2.2 Apache-2.0 OR GPL-2.0-only via async-imap/fluent elects Apache-2.0 (self_cell 0.10.3 is Apache-2.0-only), zero GPL/LGPL/AGPL/EPL/CDDL/OSL in linked set, workspace licence MIT OR Apache-2.0; web/dist is data files (embedded-web OFF, not linked) from 291 npm modules: bundle path 150 non-dev per package-lock is MIT/ISC/BSD-3-Clause only with zero copyleft, 12x MPL-2.0 lightningcss 1.32.0 + 11 platform binaries are dev-only build-time CSS tools not shipped; vite 8.0.16 MIT, tailwindcss 4.3.1 MIT, @tailwindcss/vite 4.3.1 MIT, typescript 5.7.3 Apache-2.0 verified.
License:        (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://github.com/zeroclaw-labs/zeroclaw
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        package-lock.json
Source100:      node_modules.spec.inc
# PATCH-FIX-OPENSUSE zeroclaw-use-npm-ci-for-web-build.patch mpluskal@suse.com -- offline hermetic builds must install the web tree with lockfile-only npm ci instead of resolving npm install
Patch0:         zeroclaw-use-npm-ci-for-web-build.patch
BuildRequires:  cargo >= 1.96.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  local-npm-registry
BuildRequires:  memory-constraints
BuildRequires:  nodejs >= 24
BuildRequires:  nodejs-packaging
# git_operations tool and skills sync shell out to git; pinggy tunnel spawns ssh
Recommends:     git
Recommends:     openssh
# Upstream wires linkers for x86_64/aarch64 only and the workspace needs
# 64-bit; keep 32-bit and exotic arches from scheduling builds that can
# only FTBFS.
ExclusiveArch:  %{rust_tier1_arches}
%include        %{_sourcedir}/node_modules.spec.inc

%description
ZeroClaw is an agent runtime — a single Rust binary you configure and run. It
talks to LLM providers (Anthropic, OpenAI, Ollama, and ~20 others), reaches
the world through 30+ channels (Discord, Telegram, Matrix, email, voice,
webhooks, your own CLI), and acts through tools (shell, browser, HTTP, hardware,
custom MCP servers). Everything runs on your machine, with your keys, in your
workspace.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}
# Upstream sets strip = true in [profile.release], which kills DWARF at
# link time and leaves empty debuginfo packages; release defaults to
# debug = false anyway, so request symbols explicitly for the distro
# find-debuginfo machinery. Fail fast if upstream reshapes the profile.
sed -i 's/^strip = true/debug = true/' Cargo.toml
grep -q '^debug = true' Cargo.toml
pushd web
local-npm-registry %{_sourcedir} install --include=dev
popd

%build
# 406-crate fat-LTO workspace shipping 50 MB binaries: cap parallel jobs
# by RAM so a small worker cannot OOM on concurrent full-DWARF links.
# 32 G workers (per _constraints) build -j8; a 16 G box degrades to -j4.
# %%limit_build only computes the cap as RPM macros, which bare cargo
# never reads, so hand it to cargo explicitly (both sections compile).
%limit_build -m 4000
export CARGO_BUILD_JOBS="%{_smp_build_ncpus}"
# Upstream's .cargo/config.toml pins linker aarch64-linux-gnu-gcc for the
# aarch64 target (Debian cross-toolchain naming); it does not exist on
# openSUSE, so use the default cc toolchain. Env overrides the config file
# and is inert on other arches.
export CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=cc
cargo run --release -p xtask --bin web -- build
cargo build --release --no-default-features --features "%{features}"

%install
export CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=cc
export CARGO_BUILD_JOBS="%{_smp_build_ncpus}"
cargo install --root=%{buildroot}%{_prefix} --path . --no-default-features --features "%{features}"
cargo install --root=%{buildroot}%{_prefix} --path apps/zerocode

# install web_dist in a non-standard location since it's checked by default according
# to https://docs.zeroclawlabs.ai/v0.8.0-beta-2/en/gateway/web-dashboard.html
install -d -m 755 %{buildroot}%{_datarootdir}/zeroclawlabs/web/dist
cp -a web/dist/. %{buildroot}%{_datarootdir}/zeroclawlabs/web/dist/

mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} completions bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/%{name} completions zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/%{name} completions fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# remove residue crate files
rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%check
# Upstream's test suites need network, LLM provider keys and GPU-backed
# fixtures; the smoke run below proves the shipped binaries start. The
# completions generation in %%install exercises the same path three times.
%{buildroot}%{_bindir}/%{name} --version
%{buildroot}%{_bindir}/%{name} --help > /dev/null

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-acp-bridge
%{_bindir}/zerocode
%dir %{_datarootdir}/zeroclawlabs
%dir %{_datarootdir}/zeroclawlabs/web
%{_datarootdir}/zeroclawlabs/web/dist

%files bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
