#
# spec file for package wasm-pack
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


Name:           wasm-pack
#               This will be set by osc services, that will run after this.
Version:        0.10.2~0
Release:        0
Summary:        Your favorite Rust → Wasm workflow tool!
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( MIT OR Apache-2.0 AND BSD-2-Clause ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Development/Languages/Rust
URL:            https://github.com/rustwasm/wasm-pack
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
This tool seeks to be a one-stop shop for building and working with rust- generated WebAssembly that
you would like to interop with JavaScript, in the browser or with Node.js. wasm-pack helps you build
rust-generated WebAssembly packages that you could publish to the npm registry, or otherwise use
alongside any javascript packages in workflows that you already use, such as webpack.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
# find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build}

%install
# using cargo_install (only supports bindir)
%{cargo_install}

%files
%{_bindir}/wasm-pack

%changelog
