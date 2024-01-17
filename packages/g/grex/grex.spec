#
# spec file for package grex
#
# Copyright (c) 2023 SUSE LLC
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


Name:           grex
Version:        1.4.4
Release:        0
Summary:        CLI regex generator
License:        Apache-2.0 AND MPL-2.0 AND MIT AND (Apache-2.0 OR MIT) AND BSL-1.0 AND Apache-2.0 WITH LLVM-exception
URL:            https://github.com/pemistahl/grex
Source0:        https://github.com/pemistahl/grex/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo

%description
grex is a library as well as a command-line utility that is meant to simplify the
often complicated and tedious task of creating regular expressions. It does so by
automatically generating a single regular expression from user-provided test cases.
The resulting expression is guaranteed to match the test cases which it was generated from.

It started as a Rust port of the JavaScript tool regexgen written by Devon Govett.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build} --features "default cli"

%install
%{cargo_install} --features "default cli"

%files
%doc *.md
%license LICENSE
%{_bindir}/%{name}

%changelog
