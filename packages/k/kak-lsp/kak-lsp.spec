#
# spec file for package kak-lsp
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


Name:           kak-lsp
Version:        18.1.0
Release:        0
Summary:        Language Server Protocol client for Kakoune
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR MPL-2.0) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND MIT AND Zlib AND Unlicense
URL:            https://github.com/kakoune-lsp/kakoune-lsp
Source0:        kakoune-lsp-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}
Provides:       kakoune-lsp = %{version}

%description
kak-lsp is a Language Server Protocol client for Kakoune written in Rust.

%prep
%autosetup -a1 -n kakoune-lsp-%{version}

%build
export CARGO_HOME="$PWD/.cargo"
%{cargo_build} --all-features

%install
export CARGO_HOME="$PWD/.cargo"
%{cargo_install} --all-features
mkdir -p %{buildroot}%{_datadir}/%{name}/rc
install -Dm644 rc/lsp.kak %{buildroot}%{_datadir}/%{name}/rc/

%files
%defattr(-,root,root,-)
%license UNLICENSE COPYING MIT
%doc     README.asciidoc CHANGELOG.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/rc
%{_datadir}/%{name}/*

%{_bindir}/kak-lsp

%changelog
