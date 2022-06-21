#
# spec file for package weggli
#
# Copyright (c) 2022 SUSE LLC
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           weggli
Version:        0.2.3
Release:        0
Summary:        weggli is a fast and robust semantic search tool for C and C++ codebases
License:        Apache-2.0
URL:            https://github.com/googleprojectzero/weggli
Source:         https://github.com/googleprojectzero/weggli/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  rust >= 1.55

%description
weggli is a fast and robust semantic search tool for C and C++ codebases. It is
designed to help security researchers identify interesting functionality in
large codebases.

weggli performs pattern matching on Abstract Syntax Trees based on user
provided queries. Its query language resembles C and C++ code, making it easy
to turn interesting code patterns into queries.

weggli is inspired by great tools like Semgrep, Coccinelle, joern and CodeQL,
but makes some different design decisions:

C++ support: weggli has first class support for modern C++ constructs, such as
lambda expressions, range-based for loops and constexprs.

Minimal setup: weggli should work out-of-the box against most software you will
encounter. weggli does not require the ability to build the software and can
work with incomplete sources or missing dependencies.

Interactive: weggli is designed for interactive usage and fast query
performance. Most of the time, a weggli query will be faster than a grep
search. The goal is to enable an interactive workflow where quick switching
between code review and query creation/improvement is possible.

Greedy: weggli's pattern matching is designed to find as many (useful) matches
as possible for a specific query. While this increases the risk of false
positives it simplifies query creation. For example, the query $x = 10; will
match both assignment expressions (foo = 10;) and declarations (int bar = 10;).

%prep
%autosetup -p1 -a1

install -d -m 0755 .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
cargo build --release %{?_smp_mflags}

%install
export RUSTFLAGS=%{rustflags}
cargo install --path . --root=%{buildroot}%{_prefix}

# remove residue crate file
rm -f %{buildroot}%{_prefix}/.crates*

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/weggli

%changelog
