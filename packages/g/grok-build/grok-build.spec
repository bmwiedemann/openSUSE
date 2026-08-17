#
# spec file for package grok-build
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


Name:           grok-build
Version:        0+git20260815.d6a22a1
Release:        0
Summary:        Terminal AI coding agent by xAI
# Legal-Review-Notice (boo#1273104): licences of the statically linked Rust
# dependencies, verified against the vendored tree with
# "cargo tree -p xai-grok-pager-bin -e normal" (1003 vendored crates):
#  - pdf_oxide IS shipped (pulled with its "rendering" feature), but it is
#    "MIT OR Apache-2.0" and carries no GPL code. Its src/decoders/jbig2.rs is
#    a pass-through stub ("no actual decoding performed"); its sole GPL-3.0
#    string is a doc comment naming the jbig2dec crate as an implementation
#    option upstream deliberately did NOT take.
#  - The JBIG2 decoder that "rendering" really pulls in is hayro-jbig2, which
#    is "Apache-2.0 OR MIT".
#  - MPL-2.0 below covers the 8 statically linked MPL-2.0 crates: cssparser,
#    cssparser-macros, dtoa-short, nucleo, nucleo-matcher, option-ext,
#    selectors and smartstring (MPL-2.0+).
#  - colored_json (EPL-2.0) is NOT in this binary's dependency graph; it is
#    reachable only from xai-ratatui-inline, which this package does not build.
License:        Apache-2.0 AND MPL-2.0 AND GPL-2.0 WITH Linking-exception AND LGPL-2.1-or-later
URL:            https://github.com/xai-org/grok-build
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         0001-disable-self-updater.patch
Patch1:         0002-disable-telemetry-by-default.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging >= 1.2.0
# %%limit_build: cap parallel rustc jobs by available memory (see %%build)
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  ripgrep
BuildRequires:  zstd
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
# grok shells out to ripgrep at runtime for its in-tree code search; the build
# is also pointed at the system rg (see GROK_*_BUNDLE_RG_PATH in %%build).
Requires:       ripgrep
ExclusiveArch:  %{rust_tier1_arches}

%description
Grok is xAI's terminal-based AI coding agent: an interactive TUI that pairs
with the Grok models to read, edit and reason about code in your working
directory, run shell commands and drive common developer workflows from the
command line.

This package ships the agent as the %{_bindir}/grok command.

%prep
%autosetup -p1 -a1
# Upstream pins an exact toolchain via rustup; drop it so the distribution
# rust/cargo is used instead of trying to invoke rustup at build time.
rm -f rust-toolchain.toml
# The bundled bin/protoc is a dotslash launcher that downloads protoc from the
# network at build time, which is not available in the offline build. Use the
# system protoc instead (see PROTOC export in %%build, protobuf-devel).
rm -f bin/protoc

%build
# A single rustc (xai-grok-shell) peaks around 7 GB; %%cargo_build otherwise
# fans out one job per CPU, which OOM-kills the build on many-core, low-RAM
# workers. Cap the job count by available memory (paired with _constraints).
%limit_build -m 2000
export PROTOC=%{_bindir}/protoc
# The xai-grok-tools and xai-grok-shell build scripts embed a ripgrep binary
# and otherwise download it from GitHub at build time. Point both at the
# system ripgrep so the build stays offline (see BuildRequires: ripgrep).
export GROK_TOOLS_BUNDLE_RG_PATH=%{_bindir}/rg
export GROK_SHELL_BUNDLE_RG_PATH=%{_bindir}/rg
%{cargo_build} -p xai-grok-pager-bin

%install
install -D -m 0755 target/release/xai-grok-pager %{buildroot}%{_bindir}/grok

%files
%license LICENSE
%doc README.md THIRD-PARTY-NOTICES
%{_bindir}/grok

%changelog
