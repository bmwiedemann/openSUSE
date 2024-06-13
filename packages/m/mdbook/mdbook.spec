#
# spec file for package mdbook
#
# Copyright (c) 2024 SUSE LLC
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


Name:           mdbook
Version:        0.4.40
Release:        0
Summary:        Create books from markdown
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/rust-lang/mdBook
Source0:        https://github.com/rust-lang/mdBook/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
mdbook is a utility to create books from Markdown files

%prep
%autosetup -a1 -n mdBook-%{version}

%build
%{cargo_build} --all-features --locked

%install
%{cargo_install} --all-features --locked

%check
%{cargo_test} --all-features --locked

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/mdbook

%changelog
