#
# spec file for package rtk
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


Name:           rtk
Version:        0.46.0
Release:        0
Summary:        CLI proxy that reduces LLM token consumption of dev commands
# Legal-Review-Notice: rtk itself is Apache-2.0, but the binary statically links
# the vendored Rust dependencies, so the tag below covers the whole linked set.
# Derived on this re-vendor with "cargo tree --offline -p rtk -e normal" over the
# vendored tree (193 crates vendored, 134 in the linked graph): MPL-2.0 comes
# from colored and option-ext, Unicode-3.0 from the 18 ICU/zerovec crates, ISC
# from rustls-webpki and untrusted (and from ring, "Apache-2.0 AND ISC"),
# CDLA-Permissive-2.0 from webpki-roots, BSD-3-Clause from subtle, and MIT from
# thirteen MIT-only crates (rusqlite, libsqlite3-sys, which, quick-xml, ...). Every
# dual/triple "OR" expression in the graph is satisfied by Apache-2.0 or MIT,
# both already named. r-efi offers an LGPL-2.1-or-later option but is
# UEFI-target-only and absent from the Linux graph. MPL-2.0 section 3.2 is
# satisfied because the complete vendor.tar.zst ships in the src.rpm.
License:        Apache-2.0 AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0
URL:            https://github.com/rtk-ai/rtk
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM rtk-unbundle-sqlite.patch mpluskal@suse.com -- link the system SQLite instead of the copy bundled in libsqlite3-sys, https://github.com/rtk-ai/rtk/pull/3446 (upstream keeps bundling as an opt-out default feature; drop this and build with --no-default-features once it lands)
Patch0:         rtk-unbundle-sqlite.patch
# PATCH-FIX-UPSTREAM rtk-no-deny-warnings.patch mpluskal@suse.com -- do not turn rustc warnings into errors, the distribution rustc moves independently of upstream's floor, https://github.com/rtk-ai/rtk/pull/3447
Patch1:         rtk-no-deny-warnings.patch
BuildRequires:  cargo >= 1.91
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)
Requires:       git-core
ExclusiveArch:  %{rust_tier1_arches}

%description
rtk (Rust Token Killer) is a command line proxy for the shell commands that
coding agents run most often. It executes the wrapped command, filters and
compresses the output, and prints only the part that carries information,
which cuts the number of tokens the result costs in an LLM context window.

It ships filters for more than a hundred commands across build systems,
linters, test runners, version control and cloud tooling, and falls back to
passing output through unchanged for anything it does not recognise.

%prep
%autosetup -p1 -a1

%build
# Upstream's release profile sets strip = true, which discards the DWARF that
# find-debuginfo.sh needs to build the -debuginfo/-debugsource packages.
export CARGO_PROFILE_RELEASE_STRIP=none
%{cargo_build}

%install
%cargo_install

%check
# The integration tests create repositories and configuration below $HOME.
export HOME=%{_builddir}/fakehome
mkdir -p "$HOME"
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/rtk

%changelog
