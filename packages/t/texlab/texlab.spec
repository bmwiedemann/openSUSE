#
# spec file for package texlab
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           texlab
Version:        3.3.2
Release:        0
Summary:        Implementation of the Language Server Protocol for LaTeX 
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( Apache-2.0 OR Apache-2.0 OR MIT ) AND ( CC0-1.0 OR Artistic-2.0 ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-3-Clause AND GPL-3.0 AND GPL-3.0+ AND ISC AND MIT AND MPL-2.0 AND MPL-2.0+ AND GPL-3.0
Group:          Productivity/Publishing/TeX/Utilities
Url:            https://github.com/latex-lsp/texlab
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Cross-platform implementation of the Language Server Protocol providing rich cross-editing support for the LaTeX typesetting system. 
The server may be used with any editor that implements the Language Server Protocol.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release --offline --jobs 2

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/texlab %{buildroot}%{_bindir}/texlab

%files
%{_bindir}/texlab
%license LICENSE
%doc docs README.md CHANGELOG.md

%changelog
