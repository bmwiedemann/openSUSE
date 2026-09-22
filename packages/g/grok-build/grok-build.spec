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
Version:        1.0.38+git20260919.4247f66
Release:        0
Summary:        Terminal AI coding agent by xAI
# Legal-Review-Notice (boo#1273104): licences of the statically linked Rust
# dependencies, verified against the vendored tree with
# "cargo tree -p xai-grok-pager-bin -e normal" (1009 crates in this graph,
# 1246 vendored):
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
#  - colored_json (EPL-2.0) is NOT in this binary's dependency graph. Its only
#    reference is xai-ratatui-inline, which IS built and linked here (via
#    xai-grok-pager, -render and -minimal), but names colored_json in its
#    [dev-dependencies], so it is never part of a non-test build.
#  - onig_sys bundles the Oniguruma C library (BSD-2-Clause), so the src.rpm
#    now ships 177 files under vendor/onig_sys-69.9.3/oniguruma/ that were
#    absent at 1.0.32. They are NOT compiled: %%build sets
#    RUSTONIG_SYSTEM_LIBONIG=1 to link the system libonig instead, and the
#    debugsource package contains only vendor/onig-6.5.2/src/*.rs and not one
#    oniguruma C file. BSD-2-Clause therefore stays out of License.
#  - GPL-2.0 WITH Linking-exception and LGPL-2.1-or-later cover the libgit2 C
#    sources that libgit2-sys bundles and links statically: libgit2 itself is
#    GPL-2.0 with the linking exception, and its deps/xdiff (LibXDiff) is
#    LGPL-2.1-or-later. The LGPL-covered deps/winhttp is Windows-only and is
#    not compiled here.
#  - aws-lc-sys, rust-stemmers and zstd-sys ship a GPL licence text but none
#    applies: aws-lc expressly elects ISC over GPL-2.0, rust-stemmers' GPL-3.0
#    covers only its test_data, and zstd is dual BSD-3-Clause/GPL-2.0.
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
BuildRequires:  pkgconfig(oniguruma) >= 6.9.3
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
# Memory: the xai-grok-shell rustc alone grows with the parallel LLVM
# threads it gets from the cargo jobserver (28 GB RSS with 32 jobs, OOM-killed
# at 14 GB with 8); the shipped debuginfo is limited to line tables (the last
# -C debuginfo wins), which halves every crate's peak, and the job count is
# capped at one per 8 GB so that it binds on the 32 GB workers _constraints
# asks for (memory + swap in MB / 8000).
%global build_rustflags %{build_rustflags} -C debuginfo=1
%limit_build -m 8000
export PROTOC=%{_bindir}/protoc
# syntect's regex engine is onig_sys, which otherwise compiles the oniguruma C
# sources it bundles; link the system library instead (pre-generated bindings,
# so no bindgen is pulled in).
export RUSTONIG_SYSTEM_LIBONIG=1
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
