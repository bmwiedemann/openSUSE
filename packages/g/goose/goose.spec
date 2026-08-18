#
# spec file for package goose
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


%global goose_features aws-providers,nostr,otel,rustls-tls,system-keyring,tui,disable-update
Name:           goose
Version:        1.46.0
Release:        0
Summary:        Extensible open source AI agent that automates engineering tasks
# Legal-Review-Notice: goose itself is Apache-2.0, but the shipped binary
# statically links its vendored Rust dependencies, so the tag below covers the
# whole linked set. Derived on this vendoring with
# "cargo tree --offline -p goose-cli -e normal --no-default-features
#  --features %%{goose_features}" over the vendored tree
# (1235 crates vendored, 608 in the linked graph -- the code-mode and
# local-inference branches, and with them v8/candle/llama-cpp, are not built),
# then reading "license =" from every vendor-crates/<name>-<version>/Cargo.toml.
# Where a crate offers a choice the Apache-2.0 branch is elected, and MIT where
# Apache-2.0 is not on offer; both are already named, so no "OR" expression in
# the graph adds an identifier. The remaining entries are crates with no choice
# to make: LGPL-3.0-or-later from ansi_colours (pulled in by bat),
# MPL-2.0 from option-ext (via dirs-sys), Unicode-3.0 from the 20 ICU crates,
# CC0-1.0 from the five bitcoin_hashes/secp256k1 crates (nostr),
# CDLA-Permissive-2.0 from webpki-roots, ISC from rustls-webpki and untrusted
# (and from ring, "Apache-2.0 AND ISC"), BSD-3-Clause from subtle/brotli/
# alloc-no-stdlib, BSD-2-Clause from arrayref, Zlib from foldhash and friends,
# MIT-0 from borrow-or-share, bzip2-1.0.6 from libbz2-rs-sys, and MIT from the
# 165 MIT-only crates. MPL-2.0 section 3.2 and the LGPL-3.0 source requirement
# are satisfied because the complete vendor-crates.tar.zst ships in the src.rpm;
# the two texts are additionally installed as %%license files.
# Beside the crates, goose-mcp include_str!()s six minified JavaScript/CSS
# libraries into the binary -- chart.js (MIT), d3 (ISC), d3-sankey
# (BSD-3-Clause), leaflet (BSD-2-Clause), leaflet.markercluster (MIT) and
# mermaid (MIT). Every one of those identifiers is already carried above by a
# Rust crate, so they add nothing to the tag; their texts, which upstream keeps
# in crates/goose-mcp/licenses/, are installed as %%license files.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND LGPL-3.0-or-later AND MIT AND MIT-0 AND MPL-2.0 AND Unicode-3.0 AND Zlib AND bzip2-1.0.6
URL:            https://github.com/aaif-goose/goose
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-crates.tar.zst
# PATCH-FIX-OPENSUSE goose-system-libdbus.patch mpluskal@suse.com -- link the system libdbus instead of the copy bundled in libdbus-sys; not sent upstream because upstream needs the vendored build for its portable/musl binaries
Patch0:         goose-system-libdbus.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
# upstream declares rust-version = "1.94.1" in the workspace manifest and cargo
# refuses to build below it
BuildRequires:  rust >= 1.94.1
# libdbus-sys (via keyring -> dbus-secret-service) probes for it
BuildRequires:  pkgconfig(dbus-1) >= 1.6
# libsqlite3-sys is pulled in by sqlx-sqlite with default-features off, so it
# links the system SQLite rather than the bundled copy
BuildRequires:  pkgconfig(sqlite3)
# The computer-controller extension shells out to these; goose warns at start-up
# when none of them is present, but works without them.
Recommends:     wtype
Recommends:     xdotool
ExclusiveArch:  %{rust_tier1_arches}

%description
goose is an extensible open source AI agent that goes beyond code suggestions:
it installs, executes, edits and tests with any large language model, and
drives external tools over the Model Context Protocol.

This package ships the command line agent. The "code mode" and local inference
features are not enabled: both need a build-time download of a prebuilt V8 or
llama.cpp, which an offline distribution build cannot do. Telemetry reporting
is not compiled in either.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p1 -a1
# upstream pins an exact toolchain here and the build would call out to rustup
rm -f rust-toolchain.toml
# hermit launchers that download cmake/node/rust on first use
rm -rf bin

%build
%limit_build -m 2000
%{cargo_build} -p goose-cli --bins --no-default-features --features %{goose_features}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# shell completions, straight from the clap definitions
install -d %{buildroot}%{_datadir}/bash-completion/completions \
           %{buildroot}%{_datadir}/fish/vendor_completions.d \
           %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/%{name} completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%{buildroot}%{_bindir}/%{name} completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{buildroot}%{_bindir}/%{name} completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

# man pages: upstream ships a generator binary that walks the same clap tree
CARGO_MANIFEST_DIR=$PWD/crates/goose-cli target/release/generate_manpages
install -d %{buildroot}%{_mandir}/man1
install -m 0644 target/man/*.1 %{buildroot}%{_mandir}/man1/

# licences of the two copyleft crates linked into the binary
install -m 0644 vendor-crates/ansi_colours-*/LICENSE LICENSE.ansi_colours
install -m 0644 vendor-crates/option-ext-*/LICENSE.txt LICENSE.option-ext

%fdupes -s %{buildroot}%{_prefix}

%check
# The workspace test suite is not run: goose-cli's scenario_tests drive live
# provider back ends (crates/goose-cli/src/scenario_tests/provider_configs.rs
# reads OPENAI_API_KEY, ANTHROPIC_API_KEY and friends and opens sockets to the
# vendors), so it neither builds a useful signal offline nor passes without
# credentials. Exercise the produced binary instead -- this already covers the
# clap tree, the config loader and the provider catalogue.
%{buildroot}%{_bindir}/%{name} --version
%{buildroot}%{_bindir}/%{name} info
# the self-updater is compiled out, so the subcommand must be gone
if %{buildroot}%{_bindir}/%{name} update --help >/dev/null 2>&1; then
    echo "ERROR: the update subcommand is still present" >&2
    exit 1
fi

%files
%license LICENSE LICENSE.ansi_colours LICENSE.option-ext
%license crates/goose-mcp/licenses/*.license
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
