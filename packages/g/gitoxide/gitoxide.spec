#
# spec file for package gitoxide
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


Name:           gitoxide
Version:        0.58.0
Release:        0
Summary:        An idiomatic & safe pure-Rust implementation of Git
# Legal-Review-Notice: gitoxide itself is "Apache-2.0 OR MIT", but the
# binaries statically link the vendored Rust dependencies. Derived on this
# re-vendor with "cargo tree --offline -p gitoxide -e normal" over the
# vendored tree (538 crates, 304 in the linked graph): the only copyleft
# licence in the graph is MPL-2.0, from two crates - uluru, an LRU cache
# pulled in via gix-pack (itself reached through gitoxide-core, gix and
# gix-odb), and option-ext, reached through directories and dirs-sys,
# which gix-tix newly depends on in 0.58.0. Everything else is
# permissive (MIT, Apache-2.0 including the LLVM-exception variant,
# BSD-3-Clause, ISC, CC0-1.0, Unicode-3.0, Zlib, Unlicense, BSL-1.0).
# dua-core, the directory walker, is MIT. r-efi offers an
# LGPL-2.1-or-later option but is UEFI-target-only and is absent from the
# Linux graph. MPL-2.0 section 3.2 is satisfied because the complete
# vendor.tar.zst ships in the src.rpm.
License:        (Apache-2.0 OR MIT) AND MPL-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
Source0:        https://github.com/GitoxideLabs/gitoxide/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  pkgconfig
# Upstream Cargo.toml: rust-version = "1.85" (edition 2024)
BuildRequires:  rust >= 1.85
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_arches}

%description
gitoxide is an implementation of git written in Rust for providing a pleasant
and unsurprising developer experience.

%prep
%autosetup -a 1 -p 1

%build
%{cargo_build}

%install
%cargo_install

%check
%{cargo_test}

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/gix
%{_bindir}/ein

%changelog
