#
# spec file for package kak-lsp
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


Name:           kak-lsp
Version:        14.1.0
Release:        0
Summary:        Language Server Protocol client for Kakoune
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR MPL-2.0) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND MIT AND Zlib AND Unlicense
URL:            https://github.com/kak-lsp/kak-lsp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
kak-lsp is a Language Server Protocol client for Kakoune written in Rust.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license UNLICENSE COPYING MIT
%doc     README.asciidoc CHANGELOG.md
%{_bindir}/kak-lsp

%changelog
