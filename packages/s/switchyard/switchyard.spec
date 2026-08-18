#
# spec file for package switchyard
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


%define python_subpackage_only 1
Name:           switchyard
Version:        0.2.0
Release:        0
Summary:        Routing and translating proxy for LLM traffic
# Legal-Review-Notice: the shipped binaries statically link their Rust
# dependencies, so License: is the union over the link closures of the TWO
# workspace targets this package builds - switchyard-server (the daemon) and
# switchyard-py (the pyo3 extension module) - not over the whole vendor tree.
# Method: vendor.tar.zst was extracted over the source and
#   cargo tree --offline -p <target> -e normal --prefix none \
#       --target {x86_64,aarch64}-unknown-linux-gnu
# unioned to 222 crates for switchyard-server and 232 for switchyard-py (a
# strict superset); each was mapped to vendor/<name>-<version>/Cargo.toml and
# its "license =" field read.
#  - No GPL/LGPL/AGPL/MPL/EPL/CDDL/CC-BY-SA/SSPL/OSL crate is in either closure.
#  - Where a crate offers a choice, Apache-2.0 is elected (MIT where Apache-2.0
#    is not on offer). That collapses "MIT OR Apache-2.0" (111 crates),
#    "Apache-2.0 OR MIT" (10), "Apache-2.0 OR ISC OR MIT" (3),
#    "Apache-2.0 OR BSL-1.0" (1), "BSD-2-Clause OR Apache-2.0 OR MIT" (1) and
#    "Unlicense OR MIT" (2) into Apache-2.0/MIT.
#  - The identifiers below are the irreducible remainder:
#    * MIT          - 53 MIT-only crates (e.g. serde_json's transitive set,
#                     plus pythonize from the pyo3 stack)
#    * Unicode-3.0  - 19 crates: the icu_* / zerovec / yoke / tinystr family
#                     and unicode-ident ("(MIT OR Apache-2.0) AND Unicode-3.0")
#    * ISC          - aws-lc-rs, aws-lc-sys, rustls-webpki, untrusted
#    * BSD-3-Clause - subtle, matchit ("MIT AND BSD-3-Clause"), aws-lc-sys
#    * MIT-0        - borrow-or-share
#    * Zlib         - foldhash
#  All seven identifiers are on openSUSE's accepted list
#  (format_spec_file.files/licenses_changes.txt); nothing had to be omitted.
#  The extension module adds exactly ten crates over the daemon's closure: the
#  pyo3 / pyo3-ffi / pyo3-macros / pyo3-macros-backend / pyo3-build-config
#  family and pyo3-async-runtimes (Apache-2.0 or "MIT OR Apache-2.0"),
#  pythonize (MIT), target-lexicon and the switchyard-components /
#  switchyard-py workspace members - so no new identifier. target-lexicon is
#  "Apache-2.0 WITH LLVM-exception" and is NOT declared: it is reachable only
#  beneath pyo3-macros, a proc-macro crate compiled into a build-time rustc
#  plugin and never linked into either shipped artifact, and in any case that
#  expression imposes a strict subset of the Apache-2.0 obligations already
#  declared. The workspace crates NOT built (switchyard-skill-distillation)
#  impose nothing - see %%build's -p scoping.
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND ISC AND MIT-0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/NVIDIA-NeMo/Switchyard
Source0:        Switchyard-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}.service
Source3:        system-user-%{name}.conf
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module anthropic >= 0.99.0}
# requires-python = ">=3.12"
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module fastapi >= 0.136.1}
BuildRequires:  %{python_module httpx >= 0.28.1}
# Upstream's declared PEP 517 backend is maturin (>=1.9,<2.0); it is what places
# the abi3 cdylib as switchyard_rust/_switchyard_rust and emits the console
# script, so it is not an optional convenience here.
BuildRequires:  %{python_module maturin >= 1.9}
BuildRequires:  %{python_module openai >= 2.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.13.3}
BuildRequires:  %{python_module uvicorn >= 0.46.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cargo
BuildRequires:  cargo-packaging >= 1.2.0
# aws-lc-sys (pulled by rustls' aws-lc-rs backend) compiles its bundled AWS-LC
# C sources through cmake.
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Cargo enforces the workspace's rust-version = "1.96.1", so declare the floor
# rather than letting OBS start a build that can only die in cargo.
BuildRequires:  rust >= 1.96.1
BuildRequires:  sysuser-tools
BuildRequires:  zstd
# The proxy speaks TLS to every upstream provider and reqwest's
# rustls-platform-verifier reads the system trust store, refusing to build a
# client when it is empty ("No CA certificates were loaded from the system").
Requires:       ca-certificates-mozilla
# The daemon itself embeds no Python, and the CLI never execs the
# switchyard-server binary - it hosts the server in-process through the pyo3
# binding - so the two halves do not require each other. But the workflow
# upstream documents is the `switchyard` command, so a default installation
# (zypper honours Recommends) must still get it; --no-recommends keeps a
# minimal proxy host free of the Python stack.
Recommends:     python3-%{name} = %{version}-%{release}
ExclusiveArch:  %{rust_tier1_arches}
%sysusers_requires
%{?systemd_ordering}
%{?python_enable_dependency_generator}
%python_subpackages

%description
Switchyard is a proxy and library for LLM traffic. It routes requests across
providers, translates between the OpenAI Chat, Anthropic Messages and OpenAI
Responses wire formats, and exports Prometheus metrics for requests, errors,
latency, tokens and routing overhead.

Routing algorithms are configured declaratively in TOML: pass-through, random
spread across several models for A/B benchmarking, LLM-as-classifier routing,
and signal-driven stage routing between a capable and an efficient target.

This package ships the standalone proxy as %{_bindir}/switchyard-server
together with a systemd service. The user-facing %{_bindir}/switchyard command
and the importable Python library are in the python-switchyard subpackage.

%package -n python-%{name}
Summary:        Switchyard command-line client and Python library
# The wheel's metadata carries upstream's four base requirements (openai,
# anthropic, httpx, pydantic) and openSUSE's Python dependency generator turns
# those into versioned Requires by itself, so they are not repeated here.
# These three are not covered by it and are declared by hand:
#  - fastapi and uvicorn live in upstream's optional "server" extra, but the
#    console script imports switchyard.server.server_util at module level and
#    both `switchyard serve` and `switchyard launch` serve over HTTP, so they
#    are mandatory for everything this subpackage exists to do.
#  - PyYAML is required and *undeclared upstream*: route bundles are YAML and
#    switchyard/cli/route_bundle.py reaches it through import_module("yaml"),
#    which no metadata scanner can see.
Requires:       python-PyYAML
Requires:       python-fastapi >= 0.136.1
Requires:       python-uvicorn >= 0.46.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Upstream publishes this distribution to PyPI as nemo-switchyard while the
# import name is switchyard; provide the distribution name so it is findable.
Provides:       python-nemo-switchyard = %{version}-%{release}
# Deliberately NOT required, contrary to upstream's own extras:
#  - sse-starlette is listed in the "server" extra but nothing in the tree
#    imports it; SSE is emitted through fastapi.responses.StreamingResponse.
#  - prompt-toolkit is listed in the "cli" extra but the tree has zero
#    prompt_toolkit references; the terminal UI is built on stdlib pty/termios.
#  - ddtrace (tracing extra) is not in Factory at all, and redis (affinity-redis
#    extra) is pinned <6 while Factory ships 7.0.1. Both are lazily imported
#    behind feature checks that no-op when the module is absent, so neither
#    blocks anything.
#  - claude/codex/openclaw are launch targets, not dependencies: a missing
#    binary exits with an install hint.

%description -n python-%{name}
Switchyard routes LLM traffic across providers and translates between the
OpenAI Chat, Anthropic Messages and OpenAI Responses wire formats.

This package provides the %{_bindir}/switchyard command - the entry point for
the documented workflow, e.g. "switchyard launch claude --model switchyard",
which starts a routing proxy in-process and runs a coding agent through it -
and the importable switchyard and switchyard_rust Python modules, including the
compiled extension the library is built on.

%prep
%autosetup -n Switchyard-%{version} -p1 -a1
# Upstream pins an exact toolchain and would make the build invoke rustup;
# drop it so the distribution cargo/rustc is used.
rm -f rust-toolchain.toml
# Upstream's .cargo/config.toml raises the ISA baseline to x86-64-v3 (AVX2,
# Haswell 2013+) and to neoverse-n1. Extracting vendor.tar.zst replaces that
# file with the [source.*]-only one obs-service-cargo generates, which is what
# the offline build needs - but the tuning must not come back by any route,
# because %%{cargo_build} neutralises config-file rustflags only as a side
# effect of exporting a non-empty RUSTFLAGS, and maturin gets no such
# protection. Distribution binaries must run on the openSUSE baseline, so strip
# any [target.*] table and then assert that no rustflags survive anywhere under
# .cargo/ (including a .cargo/config, which cargo would prefer over
# .cargo/config.toml and silently shadow it).
sed -i '/^\[target\./,/^$/d' .cargo/config.toml
if grep -rqE 'rustflags|target-cpu' .cargo/; then
    echo "ERROR: .cargo/ still carries rustflags that raise the ISA baseline" >&2
    exit 1
fi
# The CLI entry point is reached through the generated console script, never run
# directly, so it is installed 0644 as the library module it is - but it carries
# a "#!/usr/bin/env python3" line, and rpmlint judges by the shebang
# (non-executable-script). Drop it before maturin copies the file into the wheel.
sed -i '1{/^#!.*python/d}' switchyard/cli/switchyard_cli.py

%build
export CARGO_NET_OFFLINE=true
# switchyard-server is the only workspace member that produces a binary; the
# remaining members are libraries. crates/switchyard-py is built separately
# below, by maturin, because it is a pyo3 cdylib that has to land inside the
# Python package tree rather than in %%{_bindir}.
%{cargo_build} -p switchyard-server
# Record the crates actually linked into the two shipped artifacts for the
# attribution installed below (see the Legal-Review-Notice above).
{ cargo tree --offline -p switchyard-server -e normal --prefix none
  cargo tree --offline -p switchyard-py -e normal --prefix none
} | awk 'NF >= 2 { print $1 "-" substr($2, 2) }' | sort -u > linked-crates.txt
# maturin is not driven through %%__cargo, so the distribution's hardening flags
# and the DWARF that find-debuginfo.sh needs have to be handed to it explicitly;
# this is the exact expression %%__cargo uses. Keeping RUSTFLAGS non-empty is
# also the second line of defence behind %%prep's guard, since cargo consults
# config-file rustflags only when RUSTFLAGS is unset.
export RUSTFLAGS="%{?__rustflags} %{?build_rustflags}"
# The pyo3 extension is built abi3-py312, so one stable-ABI object serves every
# supported interpreter; each flavour still gets its own wheel so that pip
# writes the correct dist-info and console script per flavour.
%pyproject_wheel
%sysusers_generate_pre %{SOURCE3} %{name} system-user-%{name}.conf

%install
install -D -m 0755 target/release/switchyard-server %{buildroot}%{_bindir}/switchyard-server
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}
# The daemon has no built-in configuration; the admin drops config.toml here.
install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}

%pyproject_install
# Every flavour installs the same %%{_bindir}/switchyard, so the console script
# goes through update-alternatives.
%python_clone -a %{buildroot}%{_bindir}/%{name}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Apache-2.0 section 4(d) and the MIT/BSD/ISC notice clauses apply to the
# statically linked crates, so ship each one's own licence text. The tree is
# assembled once here and then copied into every package that ships a
# statically linked artifact, rather than listed as a relative %%license entry,
# because %%license copies happen after %%install and %%fdupes would then not
# see them: the ~350 files hold only ~130 distinct texts, and without the
# deduplication rpmlint scores a megabyte of files-duplicated-waste. Each copy
# is deduplicated on its own so that no symlink ever crosses a package
# boundary, which one shared %%fdupes run over %%{_defaultlicensedir} would do.
while read -r crate; do
    for f in "vendor/$crate"/LICENSE* "vendor/$crate"/LICENCE* \
             "vendor/$crate"/COPYING* "vendor/$crate"/NOTICE*; do
        [ -f "$f" ] || continue
        install -D -m 0644 "$f" "vendor-licenses/$crate/$(basename "$f")"
    done
done < linked-crates.txt
install -d %{buildroot}%{_defaultlicensedir}/%{name}
cp -a vendor-licenses %{buildroot}%{_defaultlicensedir}/%{name}/vendor
%fdupes -s %{buildroot}%{_defaultlicensedir}/%{name}
%python_expand install -d %{buildroot}%{_defaultlicensedir}/$python-%{name}
%python_expand cp -a vendor-licenses %{buildroot}%{_defaultlicensedir}/$python-%{name}/vendor
%python_expand %fdupes -s %{buildroot}%{_defaultlicensedir}/$python-%{name}

%check
# The whole Rust suite runs offline and nothing is excluded. The config tests do
# construct a reqwest client, and reqwest's rustls-platform-verifier reads the
# system trust store, so the build root needs one (BuildRequires:
# ca-certificates-mozilla) or they fail with "No CA certificates were loaded
# from the system". No test contacts the network: the integration tests bind
# 127.0.0.1:0 and the configured endpoints are example.test URLs.
%{cargo_test} -p switchyard-server
# Upstream's pytest suite needs unpackaged plugins (pytest-markdown-docs, respx)
# and a git-only harbor dependency, so the Python side is covered by a smoke
# test instead. It has to assert more than "import switchyard": the library
# fails closed on a missing extension module, so import the cdylib explicitly
# and require the native translation path to report itself available; check the
# three data files that are read at import time or on the zero-config launch
# path; and finally run the console script this subpackage exists to ship.
# Two mechanics matter here. Each %%python_expand argument must be ONE physical
# line: the macro re-emits its argument per flavour, and a backslash-continued
# argument gets truncated at the first newline for every flavour but the last -
# which fails as a shell syntax error, not as a test failure. And $python needs
# -P, or sys.path[0] would be the current directory - the unbuilt source tree -
# which shadows the installed package the test is supposed to exercise.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -P -B -c "import os, switchyard, switchyard_rust, switchyard_rust._switchyard_rust as native; d = os.path.dirname(switchyard.__file__); assert d.startswith('%{buildroot}'), d; assert switchyard_rust.is_native_translation_available(), 'native translation unavailable'; assert switchyard.__version__ == '%{version}', switchyard.__version__; assert os.path.isfile(d + '/cli/defaults/openrouter.toml'); assert os.path.isfile(d + '/lib/processors/prompts/escalation_judge.md'); assert os.path.isfile(d + '/lib/processors/stage_router/prompts/tier_classifier.md'); print('smoke ok:', switchyard.__version__, native.__file__)"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} %{buildroot}%{_bindir}/%{name}-%{$python_bin_suffix} --version
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} %{buildroot}%{_bindir}/%{name}-%{$python_bin_suffix} --help

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post -n python-%{name}
%python_install_alternative %{name}

%postun -n python-%{name}
%python_uninstall_alternative %{name}

%files
%license LICENSE NOTICE
%license %{_defaultlicensedir}/%{name}/vendor
# INSTALLATION.md is deliberately not shipped here: it documents installing the
# Python distribution, so it belongs with python-switchyard.
%doc README.md CHANGELOG.md SECURITY.md docs
%doc dev-server/config.toml
%dir %attr(0750,root,switchyard) %{_sysconfdir}/%{name}
%{_bindir}/switchyard-server
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/system-user-%{name}.conf

%files %{python_files %{name}}
%license LICENSE NOTICE
%license %{_defaultlicensedir}/%{python_flavor}-%{name}/vendor
%doc README.md INSTALLATION.md
%python_alternative %{_bindir}/%{name}
%{python_sitearch}/switchyard
%{python_sitearch}/switchyard_rust
%{python_sitearch}/nemo_switchyard-%{version}.dist-info

%changelog
