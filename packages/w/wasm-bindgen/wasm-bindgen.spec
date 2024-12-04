#
# spec file for package wasm-bindgen
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


Name:           wasm-bindgen
Version:        0.2.97~0
Release:        0
Summary:        Facilitating high-level interactions between Wasm modules and JavaScript
License:        Apache-2.0 OR MIT
URL:            https://github.com/rustwasm/wasm-bindgen
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  cmake
ExclusiveArch:  %{rust_tier1_arches}

# nothing provides libldap-data = 2.4.46-150600.23.21 needed by libldap-2_4-2, (got version 2.6.8-lp156.3.3)
#!BuildIgnore: libldap-data

%description
Facilitating high-level interactions between Wasm modules and JavaScript.

Features
- Lightweight. Only pay for what you use. wasm-bindgen only generates bindings
  and glue for the JavaScript imports you actually use and Rust functionality
  that you export. For example, importing and using the document.querySelector
  method doesn't cause Node.prototype.appendChild or window.alert to be included
  in the bindings as well.
- ECMAScript modules. Just import WebAssembly modules the same way you would
  import JavaScript modules. Future compatible with WebAssembly modules and
  ECMAScript modules integration.
- Designed with the "Web IDL bindings" proposal in mind. Eventually, there
  won't be any JavaScript shims between Rust-generated wasm functions and
  native DOM methods. Because the Wasm functions are statically type checked,
  some of those native methods' dynamic type checks should become unnecessary,
  promising to unlock even-faster-than-JavaScript DOM access.

%prep
%autosetup -a1

%build
%{cargo_build} -p wasm-bindgen-cli

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/wasm-bindgen %{buildroot}%{_bindir}/wasm-bindgen

%files
%{_bindir}/wasm-bindgen

%changelog
