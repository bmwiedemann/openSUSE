#
# spec file for package kak-lsp
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


Name:           kak-lsp
Version:        21.0.2
Release:        0
Summary:        Language Server Protocol client for Kakoune
# Legal-Review-Notice: kak-lsp itself is "Unlicense OR MIT", but the binary
# statically links the vendored Rust dependencies. Re-derived on this
# re-vendor with "cargo tree --offline -e normal" over the vendored registry
# (337 crates vendored, 167 in the linked graph). Only the licences that
# cannot be satisfied by electing a permissive alternative are listed:
#  - MPL-2.0 from option-ext, reached through dirs -> dirs-sys,
#  - Unicode-3.0 (18 crates), MIT (20 crates), Zlib, ISC and CC0-1.0, each
#    of which is the sole licence offered by the crate carrying it.
# The slog family is "MPL-2.0 OR MIT OR Apache-2.0" and r-efi offers an
# LGPL-2.1-or-later option; we elect the permissive alternative for the
# former, and the latter is UEFI-target-only and absent from the Linux
# graph. The previous tag enumerated the vendored OR-groups but omitted
# Unicode-3.0, ISC, CC0-1.0 and the bare MPL-2.0 of option-ext.
# MPL-2.0 section 3.2 is satisfied because the complete registry.tar.zst
# ships in the src.rpm.
License:        CC0-1.0 AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/kakoune-lsp/kakoune-lsp
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(openssl)
Provides:       kakoune-lsp = %{version}
ExclusiveArch:  %{rust_tier1_arches}

%description
kak-lsp is a Language Server Protocol client for Kakoune written in Rust.

%prep
%autosetup -a1

%build
export CARGO_HOME="$PWD/.cargo"
%{cargo_build} --all-features

%install
export CARGO_HOME="$PWD/.cargo"
# Keep the braced form: the bare %%cargo_install parses --all-features as a
# macro option and fails with "Unknown option - in cargo_install(p:)".
%{cargo_install} --all-features
mkdir -p %{buildroot}%{_datadir}/%{name}/rc
install -Dm644 rc/lsp.kak %{buildroot}%{_datadir}/%{name}/rc/

%check
export CARGO_HOME="$PWD/.cargo"
%{cargo_test} --all-features

%files
%license UNLICENSE COPYING MIT
%doc README.asciidoc CHANGELOG.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/rc
%{_datadir}/%{name}/*

%{_bindir}/kak-lsp

%changelog
