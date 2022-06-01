#
# spec file for package rust-analyzer
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


Name:           rust-analyzer
Version:        2022.05.30
Release:        0
Summary:        Implementation of Language Server Protocol for the Rust programming language
License:        (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Artistic-2.0 OR CC0-1.0) AND BSD-3-Clause AND ISC AND MIT AND (MIT OR Unlicense) AND Apache-2.0 AND MIT
URL:            https://github.com/rust-lang/rust-analyzer
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
rust-analyzer is a modular compiler frontend for the Rust language. It is a part of a larger
rls-2.0 effort to create excellent IDE support for Rust

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/rust-analyzer
%license LICENSE-APACHE LICENSE-MIT
%doc README.md

%changelog
