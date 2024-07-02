#
# spec file for package wasm-pack
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


Name:           wasm-pack
Version:        0.13.0~0
Release:        0
Summary:        Your favorite Rust → Wasm workflow tool!
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
Group:          Development/Languages/Rust
URL:            https://github.com/rustwasm/wasm-pack
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  cmake
ExclusiveArch:  %{rust_tier1_arches}

%description
This tool seeks to be a one-stop shop for building and working with rust- generated WebAssembly that
you would like to interop with JavaScript, in the browser or with Node.js. wasm-pack helps you build
rust-generated WebAssembly packages that you could publish to the npm registry, or otherwise use
alongside any javascript packages in workflows that you already use, such as webpack.

%prep
%autosetup -a1

%build
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
%{cargo_build}

%install
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
%{cargo_install}

%files
%{_bindir}/wasm-pack

%changelog
